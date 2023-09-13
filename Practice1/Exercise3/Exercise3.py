#Варіант 12(2)

n = 5

#Будуємо пірамідку
for i in range(n, 0, -1):
    for j in range(n - i):
        print(" ", end=" ")
    for k in range(i, 0, -1):
        print(k, end=" ")
    print()