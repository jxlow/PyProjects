import random
import pyperclip

alphabets = 'abcdefghijklmnopqrstuvwxyz'
alphabets_upper = alphabets.upper()
num = '01232456789'
# special_chars = '!@#$%&'

def parts():
    all = alphabets + alphabets_upper + num
    # + special_chars
    length = 5

    password = "".join(random.sample(all, length))
    return password

final_password = parts() + '-' + parts() + '-' + parts()
print(final_password)
pyperclip.copy(final_password)