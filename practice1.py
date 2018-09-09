age = int(input("Введите возраст: "))

def user_doing(age):
    if age < 7:
        print("Вы должны быть в детском саду.")
    elif age < 17:
        print("Вы должны учиться в школе.")
    elif age < 22:
        print("Вы должны получать высшее образование.")
    elif age <= 65:
        print("Вы должны работать.")
    else:
        print("Вам пора на пенсию")

user_doing(age)
print(age)