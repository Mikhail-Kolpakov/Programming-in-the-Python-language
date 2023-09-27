#Варіант 12

sentence = str(input("Введіть речення: \n"))

words = sentence.split() #Розділяємо речення на слова

sorted_words = []

#Сортуємо слова за довжиною в порядку неспадання
while words:
    shortest_word = words[0]
    for word in words:
        if len(word) <= len(shortest_word):
            shortest_word = word;
    sorted_words.append(shortest_word)
    words.remove(shortest_word)

print("\nСлова у порядку неспадання довжини: ")
for word in sorted_words:
    print(word)