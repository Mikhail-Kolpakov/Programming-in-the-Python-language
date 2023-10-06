#Варіант 12
import csv

def find_min_max(data): #Функція для знаходження найнижчого та найвищого значень показника
    min_value = float(data[0]["percent"])
    max_value = float(data[0]["percent"])
    min_age = data[0]["percent"]
    max_age = data[0]["percent"]

    for row in data:
            if row["percent"]:
                value = float(row["percent"])
                age = row["age"]
                if value < min_value:
                    min_value = value
                    min_age = age
                if value > max_value:
                    max_value = value
                    max_age = age

    return min_value, max_value, min_age, max_age

try:
    #Зчитування даних з вхідного .csv файлу
    with open("age_statistics_of_men_of_Ukraine.csv", "r", newline = "", encoding = "utf-8") as input_file:
        reader = csv.DictReader(input_file)
        data = list(reader)

        #Виведення вмісту .csv файлу на екран
        print("Вікова статистика чоловічого населення України(2017 р.): ")
        for row in data:
            print(row)

        #Знаходження найнижчого та найвищого значень показника та вік при якому вони існують
        min_value, max_value, min_age, max_age = find_min_max(data)

        #Запис результатів у новий .csv файл
        with open("results.csv", "w", newline = '', encoding = "utf-8") as results_file:
            columns = ["age", "percent"]
            writer = csv.DictWriter(results_file, fieldnames = columns)
            writer.writeheader()

            writer.writerow({"age": min_age, "percent": min_value})
            writer.writerow({"age": max_age, "percent": max_value})

            print(f"\nНайнижче значення при віці {min_age} - {min_value}%")
            print(f"Найвище значення при віці {max_age} - {max_value}%")

except FileNotFoundError:
    print("Помилка: файл не знайдено")
except Exception as e:
    print(f"Помилка: {e}")