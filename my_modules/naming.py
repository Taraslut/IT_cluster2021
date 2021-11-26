days = ['Monday', "Thursday", 'Wednesday', "Thursday", "Friday", "Saturday", 'Sunday']
names = ['Ivan', "Petro", "Jon", "Sem", "Bob", "Richard"]


# for n, day in enumerate(days, start=1):
#     print(n, day, sep=" => ")

def add(one, other):
    return one + other


print(__name__)

if __name__ == '__main__':
    for n, (name, day) in enumerate(zip(names, days), start=1):
        print(f"{n} =>>>   For {day} the person {name} is no duty.")
