# list // generator
import datetime

stat = datetime.datetime.now()


# ll = [i for i in range(2 * 10 ** 7)]
# print(ll)


def gen():
    for i in range(2 * 10 ** 7):
        yield i


gg = (item for item in range(2 * 10 ** 7))

rez = None
for i in gen():
    if i > 100 and i % 2 == 1:
        rez = i
        break
print(f"YES {rez}")

finish = datetime.datetime.now()

print(f'Time processing {((finish - stat).microseconds) / 10 ** 6}s.')

str_date = str(stat)
print(str_date)
print(stat.strftime("%w -- %a -- %A"))
print(stat.strftime("%m -- %b -- %B"))

# Monday 11 of November. The year is 2021
ss = stat.strftime("%A %d of %B. The year is %Y.")
print(ss)
days = {
    0: "понеділок",
    1: "Вівторок",
    2: "Середа",
    3: "Четвер",
    4: "П'ятниця",
    5: "Субота",
    6: "неділя"
}
ss2 = f"{days[stat.weekday()]} {stat.day} {stat.month}. Рік зараз {stat.year}."

print(ss2)
