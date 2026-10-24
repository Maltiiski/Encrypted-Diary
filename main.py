import base64
import os
import sys
import re
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from pathlib import Path

def load_key():
    with open("salt.key", "rb") as f:
        salt = f.read()

        master_pw = input("What is the master password? ").encode()

        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=600_000,
        )

        key = base64.urlsafe_b64decode(kdf.derive(master_pw))
        return key

fer = Fernet(load_key())

Encr_f = Path("Encr")
Encr_f.mkdir(parents=True, exist_ok=True)

Decr_f = Path("Decr")
Decr_f.mkdir(parents=True, exist_ok=True)

def new_file(folder, title, content):
    counter = 0
    while True:
        suffix = "" if counter == 0 else f"_{counter}"
        file_path = folder / f"{title}{suffix}.txt"
        try:
            with file_path.open("x", encoding="utf-8") as f:
                f.write(content)
            return file_path
        except FileExistsError:
            counter += 1

def safe_logging():
    log = input("Title: ")
    safe_log = re.sub(r"[^\w\- ]", "_", log.strip()).strip()

    if not safe_log:
        print("Invalid title")
        return
    return safe_log

def encrypt_file(data):
    pass

while True:
    log = input("New[N] | Encrypt[E] | Decrypt[D] | Delete[X] | Quit[Q] ").lower().strip()
    match log:
        case 'n':
            safe_log = safe_logging()
            if not safe_log:
                continue

            file_path = new_file(Encr_f, safe_log, "Your diary starts here...")
            print(f"Created: {file_path}")
        case 'e':
            safe_log = safe_logging()
            if not safe_log:
                continue

            file_path = Decr_f / f"{safe_log}.txt"
            if not file_path:
                print("File not found.")
                continue

            data = file_path.read_text(encoding="utf-8")

            
        case 'd':
            pass
        case 'x':
            pass
        case 'q':
            sys.exit()
        case _:
            print("Invalid option.")
