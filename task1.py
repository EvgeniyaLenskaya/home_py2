"""
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
решкой, а некоторые – гербом. Определите минимальное число
монеток, которые нужно перевернуть, чтобы все монетки были
повернуты вверх одной и той же стороной. Выведите минимальное
количество монет, которые нужно перевернуть.
"""
n = int(input("Введите количество монет: "))
a = 1
b = 0
for i in range(n):
    x = int(input("Введите цифру 1 или 0: "))
    if x == 1:
        a += 1
    else:
        b += 1    
if a > b:
    print(b)
else:
    print(a)           