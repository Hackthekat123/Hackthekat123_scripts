import hashlib
import argparse

def crack_password(wordlist_path, salt, target_hash):
    try:
        with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                pw = line.strip()
                h = hashlib.sha256((salt + pw).encode()).hexdigest()
                if h == target_hash:
                    print(f"[+] Password found: {pw}")
                    return
        print("[-] Password not found in wordlist.")
    except FileNotFoundError:
        print(f"[-] Wordlist file not found: {wordlist_path}")

def main():
    parser = argparse.ArgumentParser(description="SHA-256 Password Cracker with Salt")
    parser.add_argument("-w", "--wordlist", required=True, help="Path to the wordlist file")
    parser.add_argument("-s", "--salt", required=True, help="Salt string to prepend to the password")
    parser.add_argument("-t", "--target", required=True, help="Target SHA-256 hash to crack")

    args = parser.parse_args()
    crack_password(args.wordlist, args.salt, args.target)

if __name__ == "__main__":
    main()