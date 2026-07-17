import hashlib

passwords = [
    "password"
    "purple123"
    "network2026"
    "SuperStrong!987"
]

with open("hashes.txt", "w") as file:
    for password in passwords:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        file.write(hashed_password + "\n")

        print(f"Password: {password}")
        print(f"Hashed Password: {hashed_password}")
        print("-" * 40)

print("passwords hashed successfully!")