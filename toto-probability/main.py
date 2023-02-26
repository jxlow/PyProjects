import random

winning_numbers = [2,5,19,24,34,44]

system = 6

number_list = []
for number in range(50):
    if number != 0:
        number_list.append(number)

count = 1

while True:
    quickpick = sorted(random.sample(number_list, system))
    print(f"Attempt #{count:,} - {quickpick}")
    if set(winning_numbers).issubset(quickpick) == True:
        print(f"Attempt #{count:,} - {quickpick} - Congratulations!")
        break
    else:
        count += 1
        continue