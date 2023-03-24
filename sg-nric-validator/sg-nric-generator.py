import random

first_char = ["S", "T", "F", "G", "M"]
checksum_S_or_T = { 0 : "J", 1 : "Z", 2 : "I", 3 : "H", 4 : "G", 5 : "F", 6 : "E", 7 : "D", 8 : "C", 9 : "B", 10 : "A" }
checksum_F_or_G = { 0 : "X", 1 : "W", 2 : "U", 3 : "T", 4 : "R", 5 : "Q", 6 : "P", 7 : "N", 8 : "M", 9 : "L", 10 : "K" }
checksum_M = { 0 : "X", 1 : "W", 2 : "U", 3 : "T", 4 : "R", 5 : "Q", 6 : "P", 7 : "N", 8 : "J", 9 : "L", 10 : "K" }

nric_list = []
frequency = 100
for _ in range(frequency):

    generator_nric = random.randint(1, 9999999)
    nric_fin = str(generator_nric).zfill(7)

    # multiply accordingly by weight
    numbers = nric_fin
    digit_1 = int(numbers[0]) * 2
    digit_2 = int(numbers[1]) * 7
    digit_3 = int(numbers[2]) * 6
    digit_4 = int(numbers[3]) * 5
    digit_5 = int(numbers[4]) * 4
    digit_6 = int(numbers[5]) * 3
    digit_7 = int(numbers[6]) * 2

    # sum of all product in previous step
    total = digit_1 + digit_2 + digit_3 + digit_4 + digit_5 + digit_6 + digit_7

    # divide by 11
    r_11 = total % 11

    # lookup checksum character
    checksum_char = checksum_S_or_T[r_11]

    final = f"S{nric_fin}{checksum_char}"

    # print(final)
    nric_list.append(final)

print(nric_list)