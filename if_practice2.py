def comparison(str1, str2):
    if type(str1) is str:
        if type(str2) is not str:
            return 0
    elif type(str1) is not str:
            return 0
    if str1 == str2:
        return 1
    if str1 != str2:
        if len(str1) > len(str2):
            return 2
        elif str(str2) == 'learn':
            return 3

print("В обоих параметрах — не строки: {}".format(comparison(5, 18)))
print("В первом параметре не строка, во втором — строка: {}".format(comparison(45, "53")))
print("В первом параметре строка, во втором — не строка: {}".format(comparison("45", 53)))
print("Если строки одинаковые: {}".format(comparison("привет", "привет")))
print("Если строки разные, но первая длинее: {}".format(comparison("Hello", "Hi")))
print("Если строки разные, и вторая 'learn': {}".format(comparison('hi', 'learn')))