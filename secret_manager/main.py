import sys
from crypto_utils import generate_key
from storage import add_secret, get_secret

def init():
    try:
        open("key.key", "rb")
    except FileNotFoundError:
        generate_key()
        print("Encryption key generated!")

def main():
    init()

    if len(sys.argv) < 3:
        print("Usage:")
        print("  python main.py add <name> <value>")
        print("  python main.py get <name>")
        return

    command = sys.argv[1]

    if command == "add":
        name = sys.argv[2]
        value = sys.argv[3]
        add_secret(name, value)

    elif command == "get":
        name = sys.argv[2]
        get_secret(name)

    else:
        print("Invalid command")

if __name__ == "__main__":
    main()
