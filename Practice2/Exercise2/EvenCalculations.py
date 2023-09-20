def even_numbers(x, y): #Функція для розрахунку суми всіх парних чисел на проміжку від x до y
    sum = 0;
    for i in range(x, y + 1):
        if i % 2 == 0:
            sum += i
    return sum