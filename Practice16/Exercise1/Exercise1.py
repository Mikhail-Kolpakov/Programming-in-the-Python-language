#Варіант 12
import nltk
from nltk.corpus import stopwords
import matplotlib.pyplot as plt

#Відкриваємо файл для зчитування
with open("edgeworth-parents.txt", "r") as file:
    text = file.read()

words = nltk.word_tokenize(text) #Розділяємо текст на слова
word_count = len(words) #Визначаємо кількість слів у тексті

print(f"Кількість слів у тексті: {word_count}")

#Визначаємо 10 найбільш вживаних слів у тексті
word_freq = nltk.FreqDist(words)
top_words = word_freq.most_common(10)

#Будуємо стовпчасту діаграму для перших 10 слів
top_words_dict = dict(top_words)
plt.figure(figsize = (8, 6))
plt.bar(top_words_dict.keys(), top_words_dict.values(), color = "blue")
plt.xlabel("Слова", color = "red")
plt.ylabel("Частота", color = "red")
plt.title("10 найбільш вживаних слів (з пунктуацією та стоп-словами)")
plt.grid(axis = "y")
plt.xticks(rotation = 45)
plt.tight_layout()
plt.show()

#Видаляємо стоп-слова та пунктуацію
filtered_words = [word.lower() for word in words if word.isalpha() and word.lower() not in stopwords.words("english")]

#Рахуємо кількість вживаних слів після видалення стоп-слів та пунктуації
word_freq_filtered = nltk.FreqDist(filtered_words)
top_words_filtered = word_freq_filtered.most_common(10)

#Будуємо стовпчасту діаграму для 10 слів після видалення стоп-слів та пунктуації
top_words_filtered_dict = dict(top_words_filtered)
plt.figure(figsize = (8, 6))
plt.bar(top_words_filtered_dict.keys(), top_words_filtered_dict.values(), color = "blue")
plt.xlabel("Слова", color = "red")
plt.ylabel("Частота", color = "red")
plt.title("10 найбільш вживаних слів (після видалення стоп-слів та пунктуації)")
plt.grid(axis = "y")
plt.xticks(rotation = 45)
plt.tight_layout()
plt.show()