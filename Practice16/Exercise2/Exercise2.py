#Варіант 12
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
import string

#Зчитування тексту з файлу
with open("input.txt", "r") as file:
    input_text = file.read()

words = word_tokenize(input_text)

#Ініціалізація лексичних аналізаторів для стеммінгу та лемматизації
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

words = [word.lower() for word in words if word.isalpha()] #Видалення пунктуації та перетворення на нижній регістр
words = [stemmer.stem(word) for word in words] #Стеммінг
words = [lemmatizer.lemmatize(word) for word in words] #Лемматизація

#Видалення стоп-слів
stop_words = set(stopwords.words("english"))
words = [word for word in words if word not in stop_words]

processed_text = " ".join(words) #Повернення обробленого тексту у вигляді рядка

#Запис обробленого тексту в інший файл
with open("output.txt", "w") as file:
    file.write(processed_text)

print("Оброблений текст збережено в файлі \"output.txt\".")