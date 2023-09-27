#Варіант 9

sentence = input("Введіть речення: ")

words = sentence.split() #Розділяємо речення на слова

min_length_word = float('inf') #Присваюємо початке значення як нескінченність

#проходимося по кожному слову та шукаємо довжину найкоротшого
for word in words:
    if len(word) < min_length_word:
        min_length_word = len(word)

print(f"Довжина найкоротшого слова у реченні: {min_length_word}")
