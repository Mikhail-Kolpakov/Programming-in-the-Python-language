#Варіант 12
import json

def load_data(): #Функція для завантаження даних з JSON файлу
    try:
        with open("cars.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("\nПомилка: файл cars.json не знайдено")
    except:
        data = []

    return data

def save_data(data): #Функція для збереження даних у JSON файл
    try:
        with open("cars.json", "w") as file:
            json.dump(data, file)
    except FileNotFoundError:
        print("\nПомилка: файл cars.json не знайдено")
    except Exception as e:
        print(f"\nПомилка при збереженні даних: {e}")

def display_json(): #Функція для виведення вмісту JSON файлу на екран
    data = load_data()

    if data:
        print()
        print(json.dumps(data, indent = 4))
    else:
        print("\nJSON файл порожній")

def add_car(): #Функція для додавання нового запису у JSON файл
    data = load_data()
    model = input("\nВведіть модель автомобіля: ")
    price = int(input("Введіть вартість автомобіля $: "))
    age = int(input("Введіть вік автомобіля: "))
    car = {'model': model, 'price': price, 'age': age}
    data.append(car)
    save_data(data)
    print("\nАвтомобіль було успішно додано до JSON файлу")

def delete_car(index): #Функція для видалення запису з JSON файлу за індексом
    data = load_data()
    if 0 <= index < len(data):
        deleted_car = data.pop(index)
        save_data(data)
        print(f"\nАвтомобіль {deleted_car['model']} був видалений з JSON файлу")
    else:
        print("\nНеправильний індекс. Видалення не виконано")

def find_car_by_age(): #Функція для пошуку автомобілів за віком
    data = load_data()
    max_age = 6
    cars = [car for car in data if car['age'] > max_age]

    if cars:
        print("\nАвтомобілі старші 6-ти років: ")
        print(json.dumps(cars, indent = 4))
    else:
        print("\nАвтомобілів, які старші 6-ти років, не знайдено")

def average_price_of_old_cars(): #Функція для обчислення середньої вартості автомобілів старше 6 років
    data = load_data()
    max_age = 6
    old_cars = [car for car in data if car['age'] > max_age]

    if old_cars:
        total_price = sum(car['price'] for car in old_cars)
        average_price = total_price / len(old_cars)
        print(f"\nСередня вартість автомобілів старше 6-ти років: {average_price:.2f}")
    else:
        print("\nАвтомобілів, які старші 6-ти років, не знайдено")

while True: #Головний цикл програми
    print("\nМеню: ")
    print("1. Вивести JSON файл")
    print("2. Додати новий запис")
    print("3. Видалити запис ")
    print("4. Знайти автомобілі старші 6-ти років")
    print("5. Середня вартість автомобілів старших 6-ти років")
    print("6. Вийти з програми")

    choice = input("Виберіть опцію (1/2/3/4/5/6): ")

    if choice == "1":
        display_json()
    elif choice == "2":
        add_car()
    elif choice == "3":
        index = int(input("\nВведіть індекс запису для видалення: "))
        delete_car(index)
    elif choice == "4":
        find_car_by_age()
    elif choice == "5":
        average_price_of_old_cars()
    elif choice == "6":
        print("\nВи вийшли з програми")
        break
    else:
        print("Введена неправильна опція, спробуйте ще раз")