import random
import string

upperCase_letters = string.ascii_letters.upper()
lowerCase_letters = string.ascii_letters.lower()
digits = string.digits
specialCharacters = string.punctuation

upper, lower, nums, special = True, True, True, True   # optional parameters for the password generator

all = ""

if upper:
    all += upperCase_letters
if lower:
    all += lowerCase_letters
if nums:
    all += digits
if special:
    all += specialCharacters

length = 21
amount = 10

for x in range(amount):
    password = "".join(random.sample(all, length))
    print(password)


