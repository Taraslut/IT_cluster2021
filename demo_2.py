# open & read file
# create list of list
# [['hello', "world"], ['I\'m', "ALIVE"]]

import json

dd = json.loads('{"a": 12, "hello":"world"}')

rez = []
# IO -- file-rw, DB-crud, HTTP/HTTPS -- req/res
with open("sample.txt") as f:
    for line in f:
        # str.slit()
        words = line.split()
        rez.append(words)

print(rez)
