students_scores = [1, 21, 19, 6, 5]

# плохой вариант: не сработеает, если мы не знаем сколько элементов 
# в списке; каждый раз должны написать, что делаем; 
print(students_scores[0])
print(students_scores[1])
print(students_scores[2])
print(students_scores[3])
print(students_scores[4])

# правильный вариант
for score in students_scores:
    print(score)

# выполняет тело цикла для каждого элемента цикла

# цикл for может итерировать по:
# - спискам;
# – строкам;
# – словарям и т.д.

text = 'Алло, гараж!'

for letter in text:
    print(letter)