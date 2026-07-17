import hashlib

with open("hashes.txt", "r") as file:
    hashes = [line.strip() for line in file]

with open("wordlist.txt.py", "r") as file:
    words = [line.strip() for line in file]

for target_hash in hashes:
    found = False

    for word in words:
        guess_hash = hashlib.sha256(word.encode()).hexdigest()

        if guess_hash == target_hash:
            print(f"Match found: {word}")
            found = True
            break

    if not found:
        print("No match")

print(words)