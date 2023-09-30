#Варіант 12

word = input("Введіть слово з латинських літер: ") #Вводимо слово латинськими літерами

unique_letters = set() #Створюємо пусту множину для збереження перших входжень літер
result = []

#Перебираємо кожен символ у слові
for char in word:
    if char not in unique_letters: #Якщо символ ще не зустрічався, додаємо його до множини
        unique_letters.add(char)
        result.append(char)

print(f"\nПерші входження літер у тексті: \n{result}")