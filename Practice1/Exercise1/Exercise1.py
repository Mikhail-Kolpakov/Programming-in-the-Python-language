#Варіант 12

a = float(input("Введіть значення для змінної A: "))

#Перевіряємо змінну B на коректність
while (a < 1 or a > 100):
    a = float(input("\nНе коректне значення\nВведіть A ще раз: "))

b = float(input("Введіть значення для змінної B: "))

#Перевіряємо змінну A на коректність
while (b < 1 or b > 100):
    b = float(input("\nНе коректне значення\nВведіть B ще раз: "))

#Робимо обчислення в залежності від значень A та B
if a < b:
    print("\nA < B")
    x = b / a + 1
elif a == b:
    print("\nA = B")
    x = 25
else:
    print("\nA > B")
    x = (a ** 3 - 5) / b

print(f"\nПісля обчислень X = {format(x, '.2f')}")