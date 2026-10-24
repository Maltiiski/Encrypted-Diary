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

def new_file(title, content):
    counter = 0
    while True:
        suffix = "" if counter == 0 else f"_{counter}"
        file_path = Decr_f / f"{title}{suffix}.txt"
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

def encrypt_file(title, content):
    counter = 0
    while True:
        suffix = "" if counter == 0 else f"_{counter}"
        file_path = Encr_f / f"{title}{suffix}.txt"
        try:
            with file_path.open("xb") as f:
                f.write(content)
            return file_path
        except FileExistsError:
            counter += 1

while True:
    log = input("New[N] | Encrypt[E] | Decrypt[D] | Delete[X] | Quit[Q] ").lower().strip()
    match log:
        case 'n':
            safe_log = safe_logging()
            if not safe_log:
                continue

            file_path = new_file(safe_log, "Your diary starts here...")
            print(f"Created: {file_path}")

            # === Seperator, I couldn't read shi
        case 'e':
            safe_log = safe_logging()
            if not safe_log:
                continue

            file_path = Decr_f / f"{safe_log}.txt"
            if not file_path:
                print("File not found.")
                continue

            raw_data = file_path.read_text(encoding="utf-8")
            pro_data = fer.encrypt(raw_data.encode())

            encf_path = encrypt_file(safe_log, pro_data)
            file_path.unlink(missing_ok=True)
            print(f"{safe_log}.txt has been encrypted.")

            # === Seperator, I couldn't read shi
        case 'd':
            safe_log = safe_logging()
            if not safe_log:
                continue
            
            file_path = Encr_f / f"{safe_log}.txt"
            if not file_path:
                print("File not found.")
                continue

            raw_data = file_path.read_bytes()
            pro_data = fer.decrypt(raw_data)

            decf_path = new_file(safe_log, pro_data)
            file_path.unlink(missing_ok=True)
            print(f"{safe_log}.txt has been decrypted.")

            # === Seperator, I couldn't read shi
        case 'x':
            log = input("Encrypted Files[E] | Decrypted Files[D]").lower().strip()
            if log == "e":

            elif log == "d":
                
            else:
                print("Invalid option.")
        case 'q':
            sys.exit()
        case _:
            print("Invalid option.")
