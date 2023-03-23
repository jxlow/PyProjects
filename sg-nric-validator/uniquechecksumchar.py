checksum_S_or_T = { 0 : "J", 1 : "Z", 2 : "I", 3 : "H", 4 : "G", 5 : "F", 6 : "E", 7 : "D", 8 : "C", 9 : "B", 10 : "A" }
checksum_F_or_G = { 0 : "X", 1 : "W", 2 : "U", 3 : "T", 4 : "R", 5 : "Q", 6 : "P", 7 : "N", 8 : "M", 9 : "L", 10 : "K" }
checksum_M = { 0 : "X", 1 : "W", 2 : "U", 3 : "T", 4 : "R", 5 : "Q", 6 : "P", 7 : "N", 8 : "J", 9 : "L", 10 : "K" }

unique = []
for i,j in checksum_S_or_T.items():
    print(j)
    if j not in unique:
        unique.append(j)

for i,j in checksum_F_or_G.items():
    print(j)
    if j not in unique:
        unique.append(j)

for i,j in checksum_M.items():
    print(j)
    if j not in unique:
        unique.append(j)

print(unique)


string = ""

for i in unique:
    string += f"{i}|"

print(string)
