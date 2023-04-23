import random
import string
import secrets

pwd_length = int(input("How long does it have to be?"))
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

alphabet = letters + digits + special_chars

pwd = ''
for  i in range (pwd_length):
    pwd += ''.join(secrets.choice(alphabet))

print(pwd)