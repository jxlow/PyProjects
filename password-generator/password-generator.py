import random
import pyperclip

def char() :
    characterlist = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    range = len(characterlist)
    random_number = random.randrange(0,range)
    x = characterlist[random_number]
    return x

password = ""
for _ in range(15) :
    password += char()
    
finalpassword = password[:5] + '-' + password[5:10]+ '-' + password[10:]
print(finalpassword)
print('Copied to clipboard')
pyperclip.copy(finalpassword)