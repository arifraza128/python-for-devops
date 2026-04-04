import json
import os
from crypto_utils import encrypt_data, decrypt_data

FILE = "secrets.json"

def load_secrets():
    if not os.path.exists(FILE):
        return {}
    with open(FILE, "r") as f:
        return json.load(f)

def save_secrets(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_secret(name, value):
    secrets = load_secrets()
    secrets[name] = encrypt_data(value)
    save_secrets(secrets)
    print("Secret stored securely!")

def get_secret(name):
    secrets = load_secrets()
    if name not in secrets:
        print(" Secret not found")
        return
    decrypted = decrypt_data(secrets[name])
    print(f"{name} = {decrypted}")
