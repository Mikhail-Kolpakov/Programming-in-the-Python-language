# Варіант 12

#Створення файлу TF15_2.txt з різними рядками
with open("TF15_1.txt", 'w') as file:
    file.write("майор шабаш\n")
    file.write("радар яблуко трактор\n")
    file.write("насіння\n")
    file.write("трикутник шалаш\n")
    file.write("абоба\n")
    file.write("гітара привіт\n")
    file.write("кабак\n")
    file.write("ротор наган музика\n")
    file.write("дах\n")
    print("Слова були успішно додані да файлу TF15_1.txt")

#Знаходження та запис всіх симетричних слів з файлу TF15_1.txt у файл TF15_2.txt
with open("TF15_1.txt", 'r') as input_file, open("TF15_2.txt", 'w') as output_file:
    symmetric_words_list = [] #Список для зберігання симетричних слів

    for line in input_file:
        words = line.split()
        symmetric_words = [word for word in words if word == word[::-1]] #Перевіряємо слово на симетричність
        symmetric_words_list.extend(symmetric_words) #Додавання симетричних слів до списку

    symmetric_line = ' '.join(symmetric_words_list) #Об'єднання симетричних слів через пробіли
    output_file.write(symmetric_line)
    print("\nСиметричні слова були успішно додані до файлу TF15_2.txt")

#Друк кожного слова з файлу TF15_2.txt в окремому рядку
print("\nСиметричні слова з файлу TF15_2.txt: ")
with open("TF15_2.txt", 'r') as file:
    for line in file:
        words = line.split()
        for word in words:
            print(word)
