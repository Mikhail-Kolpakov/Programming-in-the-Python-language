#Варіант 12

length = int(input("Введіть довжину масиву: ")) #Вводимо довжину масиву

array = [] #Створюємо пустий масив

#Заповнюємо масив значеннями з клавіатури
for i in range(length):
    element = int(input(f"Введіть значення для елементу з індексом [{i}]: "))
    array.append(element)

negative_values = [x for x in array if x < 0] #Знаходимо всі від'ємні елементи в масиві

#Виводимо результат у зворотному порядку до консолі
print("\nВід'ємні елементи у зворотному порядку: ")
for value in reversed(negative_values):
    print(value)
