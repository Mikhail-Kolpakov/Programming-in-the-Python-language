#Варіант 12

word = str(input("Введіть слово: "))

#Перевіряємо, чи починається слово з великої літери
if word[0].isupper():
    print("Слово починається з великої літери")
else:
    print("Слово не починається з великої літери")