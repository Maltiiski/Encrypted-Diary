import base64
import os
import sys
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

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