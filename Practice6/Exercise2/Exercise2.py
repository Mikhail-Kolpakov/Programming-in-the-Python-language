#Варіант 12

start_list = input("Заповніть список значеннями через пробіл: ").split() #Вводимо список розділений пробілами

if len(start_list) < 2: #Перевірка наявності достатньої кількості елементів у списку
    print("Список занадто короткий")
else:
    all_valid = True

    for item in start_list: #Перевірка коректності введених значень
        if not item.isdigit():
            print("\nПомилка: введені значення повинні бути цілими числами")
            all_valid = False
            break

    if all_valid:
        new_list = [int(item) for item in start_list] #Перетворення введених значень в цілі числа

        #Знаходимо максимальний і мінімальний елементи та їхні індекси
        max_value = max(new_list)
        min_value = min(new_list)
        max_index = new_list.index(max_value)
        min_index = new_list.index(min_value)

        print(f"\nМаксимальний елемент списка: {max_value}")
        print(f"Мінімальний елемент списку: {min_value}")

        new_list[max_index], new_list[min_index] = new_list[min_index], new_list[max_index] #Міняємо місцями максимальний та мінімальний елемент

        print(f"\nСписок після заміни місцями максимального та мінімального елементів: \n{new_list}")