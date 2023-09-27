#Варіант 9

numbers = str(input("Введіть чотиризначне натуральне число: "))

#Перевіряємо, чи чотирьохзначне число
while len(numbers) < 4 or len(numbers) > 4 or numbers.isdigit() == 0:
    numbers = str(input("Введіть число ще раз, так як воно не чотиризначне або це не число: "))

max_number = 0

#Проходимося по кожній цифрі у рядку та шукаємо найбільшу
for number in numbers:
    if int(number) > max_number:
        max_number = int(number)

print(f"Найбільша цифра у числі {numbers} - це {max_number}")
