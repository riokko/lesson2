

user_phrase = input()
user_phrase = user_phrase.replace("=","")


if "+" in user_phrase:
    user_phrase = user_phrase.split("+")
    calculation = float(user_phrase[0]) + float(user_phrase[1])

if "-" in user_phrase:
    user_phrase = user_phrase.split("-")
    print(user_phrase)
    calculation = float(user_phrase[0]) - float(user_phrase[1])

if "/" in user_phrase:
    user_phrase = user_phrase.split("/")
    calculation = round(float(user_phrase[0]) / float(user_phrase[1]), 2)

if "*" in user_phrase:
    calculation = float(user_phrase[0]) * float(user_phrase[1])


print(calculation)