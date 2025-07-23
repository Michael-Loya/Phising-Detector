import hashlib

def generate_wordlist():
    words = [
        "123456",
        "password",
        "admin",
        "letmein",
        "pass",         # <--- target word
        "qwerty",
        "12345678",
        "welcome",
        "ninja",
        "abc123"
    ]
    with open("wordlist.txt", "w") as file:
        for word in words:
            file.write(word + "\n")
    print("✅ wordlist.txt generated.")

def crack_hash(target_hash):
    try:
        with open("wordlist.txt", "r") as wordlist:
            for word in wordlist:
                word = word.strip()
                hashed_word = hashlib.md5(word.encode("utf-8")).hexdigest()
                print(f"Trying: {word} -> {hashed_word}")
                if hashed_word == target_hash:
                    print(f"\n✅ Password found: {word}")
                    return
            print("\n❌ Password not found in wordlist.")
    except FileNotFoundError:
        print("🚫 wordlist.txt not found in the directory.")

if __name__ == "__main__":
    generate_wordlist()
    crack_hash("1a1dc91c907325c3a1a3f0e6b4b7d8e2")
