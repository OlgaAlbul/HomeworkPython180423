# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

n = int(input('Введите количество элементов первого множества: '))
m = int(input('Введите количество элементов второго множества: '))
a = []
import random
for i in range(n):
    a.append(random.randint(1,150))
print(a)
b = []
for i in range(m):
    b.append(random.randint(1,150))
print(b)

a = set(a)
b = set(b)
if n>m: 
    q = a.union(b)
else:
    q = b.union(a)

print(q)
q = list(q)
q2 = sorted(q)
print(q2)
