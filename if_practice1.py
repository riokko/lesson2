age = int(input("Введите возраст: "))

def user_doing(age):
    if age < 7:
        return "Вы должны быть в детском саду."
    elif age < 17:
        return "Вы должны учиться в школе."
    elif age < 22:
        return "Вы должны получать высшее образование."
    elif age <= 65:
        return "Вы должны работать."
    else:
        return "Вам пора на пенсию"

should_do = user_doing(age)
print(should_do)