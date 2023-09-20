#Варіант 12
import math

def expression(x): #Функція для розрахунку виразу z
    z = (1 - 2 * math.pow(math.sin(x), 2)) / (1 + pow(math.sin(x), 2))
    return z

def even_numbers(x, y): #Функція для розрахунку суми всіх парних чисел на проміжку від x до y
    sum = 0;
    for i in range(x, y + 1):
        if i % 2 == 0:
            sum += i
    return sum

x = int(input("Введіть значення x: "));

print(f"Значення z = {format(expression(x), '.2f')}")

x = int(input("\nВведіть від якого числа (x) знаходити суму парних чисел: "))
y = int(input("Введіть до якого числа (y) знаходити суму парних чисел: "))

while x > y:
    x = int(input("\ny не може бути менше x, введіть ще раз від якого числа (x) знаходити суму парних чисел: "))
    y = int(input("Введіть до якого числа (y) знаходити суму парних чисел: "))

print(f"Сума парних чисел в {x} до {y} = {even_numbers(x, y)}")