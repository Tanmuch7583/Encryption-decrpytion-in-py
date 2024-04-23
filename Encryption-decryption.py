import random
import string

chars =list(' ' + string.ascii_letters + string.punctuation + string.digits)

key = chars.copy()

random.shuffle(key)

print(f"chars: {chars}")
print(f"Key: {key}")

#Encrypt-----------------------------------

plain_text = input("Enter your Message here: ")
cipher_text = " "

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"Original Message: {plain_text}")
print(f"Encrypted Message: {cipher_text}")


#Decrypt--------------------------------------
cipher_text = input("Enter your Message here: ")
plain_text = " "

for letter in cipher_text:
    index = key.index(letter)
    plain_text  += chars[index]

print(f"Original Message: {plain_text}")