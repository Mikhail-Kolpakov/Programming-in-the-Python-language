#Варіант 12

#Словник, що характеризує ціну автомобіля то його вік
cars = {
    "Car1": {"вартість": 15000, "вік": 5},
    "Car2": {"вартість": 20000, "вік": 8},
    "Car3": {"вартість": 18000, "вік": 3},
    "Car4": {"вартість": 22000, "вік": 7},
    "Car5": {"вартість": 16000, "вік": 4},
    "Car6": {"вартість": 25000, "вік": 9},
    "Car7": {"вартість": 17000, "вік": 2},
    "Car8": {"вартість": 23000, "вік": 6},
    "Car9": {"вартість": 19000, "вік": 1},
    "Car10": {"вартість": 21000, "вік": 10}
}

def display_cars(): #Функція для виводу всіх автомобілів з словника до консолі
    print()
    for key in cars:
        print(f"{key}: {cars[key]}")

def add_car(): #Функція для додавання нового автомобіля до словника
    print("\nДодавання нового автомобіля: ")
    car_name = input("Введіть назву автомобіля: ")
    cost = int(input("Введіть вартість автомобіля: "))
    age = int(input("Введіть вік автомобіля: "))
    cars[car_name] = {"вартість": cost, "вік": age}
    print(f"\nАвтомобіль {car_name} було додано до словника")

def remove_car(): #Функція для видалення автомобіля зі словника
    print("\nВидалення автомобіля: ")
    car_name = input("Введіть назву автомобіля для видалення: ")
    if car_name in cars:
        del cars[car_name]
        print(f"\nАвтомобіль {car_name} було видалено зі словника")
    else:
        print(f"\nАвтомобіль {car_name} не було знайдено у словнику")

def display_sorted_cars(): #Функція для перегляду вмісту словника за відсортованими ключами
    sorted_keys = sorted(cars.keys())
    for key in sorted_keys:
        info = cars[key]
        print(f"{key}: {info}")

def average_cost_of_old_cars(): #Функція для обчислення середньої вартості автомобілів старших 6-ти років
    total_cost = 0
    count = 0
    for car, info in cars.items():
        if info["вік"] > 6:
            total_cost += info["вартість"]
            count += 1
    if count > 0:
        average_cost = total_cost / count
        print(f"\nСередня вартість автомобілів старших 6-ти років: {average_cost:.2f}")
    else:
        print("\nНемає жодного автомобіля старшого 6-ти років у словнику")

while(True): #Головний цикл програми
    print("\nМеню: ")
    print("1. Вивести всі автомобілі на екран")
    print("2. Додати новий автомобіль до словника")
    print("3. Видалити автомобіль зі словника")
    print("4. Переглянути відсортований словник")
    print("5. Вивести середню вартість всіх автомобілів старших 6-ти років")
    print("6. Вийти з програми")

    choice = input("\nОберіть опцію (1/2/3/4/5): ")

    if choice == "1":
        display_cars()
    elif choice == "2":
        add_car()
    elif choice == "3":
        remove_car()
    elif choice == "4":
        display_sorted_cars()
    elif choice == "5":
        average_cost_of_old_cars()
    elif choice == "6":
        print("\nВи вийшли з програми")
        break
    else:
        print("\nНевірний вибір, спробуйте ще раз")