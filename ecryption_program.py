# Python Ecryption Program
import string
import random

chars = list(string.ascii_letters + string.digits + string.punctuation + " ")
key = chars.copy()

random.shuffle(key)

# print(f"chars: {chars}")
# print(f"key  : {key}")
while True:
    print("Hint: q to exit!")
    method = input("Choose a method(Encrypt or Decrypt): ").lower()
    # Encrypt
    if method == "encrypt":
        plain_text = input("Enter a message to encrypt: ")
        cipher_text = ""

        for l in plain_text:
            cipher_text += key[chars.index(l)]

        print(f"Encrypted message: {cipher_text}")
        print(f"Original message : {plain_text}")

    # Decrypt
    elif method == "decrypt":
        cipher_text = input("Enter a message to Decrypt: ")
        plain_text = ""

        for l in cipher_text:
            plain_text += chars[key.index(l)]

        print(f"Encrypted message: {cipher_text}")
        print(f"Original message : {plain_text}")
    elif method == "q":
        break
    else:
        print("Error: Invalid Input!")
