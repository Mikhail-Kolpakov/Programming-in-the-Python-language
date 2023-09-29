#Варіант 12

rows, columns = 7, 7 #Вказуємо кількість рядків та стовпців

array = [[0 for _ in range(columns)] for _ in range(rows)] #Створюємо пустий двовимірний масив

#Заповнюємо масив значеннями згідно з умовою
for i in range(rows):
    for j in range(columns):
        array[i][j] = i - 6 + j

#Виводимо значення двовимірного масиву до консолі
for i in range(rows):
    for j in range(columns):
        print(array[i][j], end = "\t")
    print()
