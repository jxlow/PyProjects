import re

first_char = ["S", "T", "F", "G", "M"]
checksum_S_or_T = { 0 : "J", 1 : "Z", 2 : "I", 3 : "H", 4 : "G", 5 : "F", 6 : "E", 7 : "D", 8 : "C", 9 : "B", 10 : "A" }
checksum_F_or_G = { 0 : "X", 1 : "W", 2 : "U", 3 : "T", 4 : "R", 5 : "Q", 6 : "P", 7 : "N", 8 : "M", 9 : "L", 10 : "K" }
checksum_M = { 0 : "X", 1 : "W", 2 : "U", 3 : "T", 4 : "R", 5 : "Q", 6 : "P", 7 : "N", 8 : "J", 9 : "L", 10 : "K" }

nric_fin_regex_pattern = r'^[G|S|T|F|M]\d{7}[J|Z|I|H|G|F|E|D|C|B|A|X|W|U|T|R|Q|P|N|M|L|K]$'

user_input = input("Enter NRIC/FIN: ")
nric_fin = user_input.upper()

if not re.match(nric_fin_regex_pattern, nric_fin) :
    print("Invalid input; exiting script - please try again.")
    quit()

else:
    print(f"Valid input: {nric_fin}")

# multiply accordingly by weight
numbers = nric_fin[1:8]
digit_1 = int(numbers[0]) * 2
digit_2 = int(numbers[1]) * 7
digit_3 = int(numbers[2]) * 6
digit_4 = int(numbers[3]) * 5
digit_5 = int(numbers[4]) * 4
digit_6 = int(numbers[5]) * 3
digit_7 = int(numbers[6]) * 2

# sum of all product in previous step
total = digit_1 + digit_2 + digit_3 + digit_4 + digit_5 + digit_6 + digit_7

# offset
if nric_fin[0] == "T" or nric_fin[0] == "G" :
    total += 4

if nric_fin[0] == "M":
    total += 3

# divide by 11
r_11 = total % 11

# lookup checksum character
if nric_fin[0] == "S" or nric_fin[0] == "T" :
    checksum_char = checksum_S_or_T[r_11]
    print(f"Checksum character is: {checksum_char}")
    
if nric_fin[0] == "F" or nric_fin[0] == "G" :
    checksum_char = checksum_F_or_G[r_11]
    print(f"Checksum character is: {checksum_char}")

if nric_fin[0] == "M":
    checksum_char = checksum_M[r_11]
    print(f"Checksum character is: {checksum_char}")


if checksum_char == nric_fin[-1]:
    print("Checksum pass")
else :
    print("Checksum fail")