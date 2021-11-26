
while True:
    try:
        age = input("Введи свій вік ")
        age = int(age)
        if 0 <= age <= 100:
            break
        else:
            print("Введи будь-ласка число від 1-100")
    except ValueError:
        try:
            age = float(age)
            if 0 <= age <= 100:
                break
        except:
            print("Введи будь-ласка число")

    except:
        print("Ops. Something wrong")

print(f"Через 10 років тобі буде {age +10}.")
