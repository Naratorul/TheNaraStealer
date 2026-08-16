```markdown
# Naratorul Stealer – Build & Deployment Tool

**Naratorul** is a modular, evasive information stealer designed for authorized penetration testing, red-team exercises, and academic research. It extracts credentials, cookies, Discord tokens, crypto wallets, gaming sessions, and more – then exfiltrates the data via Discord webhooks.

**WARNING**: This tool is intended solely for ethical security testing in controlled environments. Do not use against any system without explicit written permission. Unauthorized use is illegal and violates the Computer Fraud and Abuse Act (CFAA) and similar laws worldwide.

---

## Features

- Discord-only exfiltration – all Telegram code removed for simplicity.
- Anti-sandbox and anti-debug – 90-second initial delay, VM detection.
- AES-256-CBC encrypted payload – static signatures bypassed.
- Reflective loading – payload decrypted and executed in memory.
- Customizable – prompt for webhook, archive password, and output EXE name.
- Icon embedding – use a `icon.png` to brand your EXE.
- Clean build process – interactive prompts, no hard-coded secrets.

---

## Project Structure

```
├── process.py              # The stealer source (rebranded to "Naratorul")
├── config.json             # Configuration (webhook, module toggles)
├── build_evasive.py        # Main build script (interactive)
├── loader_template.py      # Decryption stub (separate file)
├── run.bat                 # One-click build and cleanup
├── requirements.txt        # Python dependencies
├── sigthief.py             # Optional – clone digital certificates
├── rar.exe / rarreg.key    # Optional – create password-protected RAR archives
├── icon.png                # Optional – custom EXE icon
└── README.md               # This file
```

---

## Requirements

- Python 3.8+ (tested on Python 3.10)
- Dependencies (install via `pip install -r requirements.txt`):
  - `pyaes`
  - `urllib3`
  - `pyinstaller`

Additional optional tools (already included in most Blank Grabber bundles):
- `rar.exe` / `rarreg.key` – for RAR archive creation (falls back to ZIP if missing)
- `sigthief.py` – to clone a digital signature from a legitimate system executable

---

## Installation and Setup

1. Clone or download this repository.
2. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

3. (Optional) If you want to clone a certificate for your EXE, ensure `sigthief.py` is present in the same folder.
4. Place your icon (if any) as `icon.png` in the root folder – it will be automatically embedded.

---

## Configuration

The main settings are stored in `config.json`. You can edit it manually or let the build script update it interactively.

- `settings.c2` – `[0, "webhook_url"]` – Discord webhook URL.  
  If the webhook is empty, the build script will prompt you to enter it.
- `settings.archivePassword` – default password for the archive (can be changed during build).
- `settings.*` – various toggles for features (e.g., `captureCookies`, `startup`, `melt`).
- `modules.*` – enable/disable specific data stealing modules.

---

## Building the EXE

Run the build script (interactive):

```
python build_evasive.py
```

or simply double-click `run.bat` (Windows) – it will:

1. Prompt you for:
   - Discord webhook (if not already in `config.json`)
   - Archive password (or use default)
   - Desired output EXE name (e.g., `SystemHelper`)
2. Obfuscate and encrypt `process.py`.
3. Generate `loader-o.py` (the decryption stub).
4. Build a single standalone `.exe` with PyInstaller.
5. (Optional) Clone a certificate using `sigthief.py`.
6. Move the final EXE to the current folder and clean up temporary files.

The final output is a self-contained `.exe` – no extra files needed on the target.

---

## Usage on Target

- Double-click the EXE.
- It will:
  - Sleep for 90 seconds (evades sandbox timeouts).
  - Check for VM artifacts and debuggers – exits if detected.
  - Decrypt and run the stealer payload.
  - Collect browser data, Discord tokens, wallets, etc.
  - Pack everything into an archive.
  - Send the archive to your configured Discord webhook.

---

## Legal and Ethical Disclaimer

This software is provided for educational and research purposes only.  
By using this tool, you agree that you have obtained explicit written permission from the owner of any system you test. The author assumes no responsibility for misuse. Unauthorized access to computer systems is a crime in most jurisdictions. Use this knowledge to strengthen defenses, not to compromise them.

---

## Credits

- Original concept derived from open-source Blank Grabber.
- Rebranded and hardened for research purposes.

---

## Contact

For questions or suggestions (research-related only), please reach out via the repository issue tracker.
```
