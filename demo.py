# open & read file
# create list of list
# [['hello', "world"], ['I\'m', "ALIVE"]]

f = open("sample.txt")
rez = []

for line in f:
    # str.slit()
    words = line.split()
    rez.append(words)

f.close()

print(rez)
