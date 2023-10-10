#Варіант 12
import matplotlib.pyplot as plt
import numpy as np

#Дані про народжених дітей
months = ["Січень", "Лютий", "Березень", "Квітень", "Травень", "Червень", "Липень", "Серпень", "Вересень"]
boys_births = [1435, 1254, 1405, 1464, 1449, 1416, 1581, 1546, 1462]
girls_births = [1288, 1198, 1312, 1262, 1410, 1274, 1438, 1481, 1352]

np.array(months)
np.array(boys_births)
np.array(girls_births)

#Побудова графіку народжуваності хлопчиків та дівчат
plt.plot(months, boys_births, color="blue", label="Хлопчики", linewidth = 2)
plt.plot(months, girls_births, color="pink", label="Дівчата", linewidth = 2)
plt.xlabel("Місяць року", color = "red")
plt.ylabel("Народжуваність", color = "red")
plt.title("Динаміка народжуваності хлопчиків у м. Києві за 2019 рік")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Вибір користувачем групи для побудови стовпчастої діаграми
group = input("Введіть групу (хлопчики/дівчата): ")

#Побудова стовпчастої діаграми
if group == "хлопчики":
    plt.bar(months, boys_births, color="blue")
    plt.xlabel("Місяць року", color = "red")
    plt.ylabel("Народжуваність", color = "red")
    plt.title(f"Народжуваність хлопчиків у м. Києві за 2019 рік")
    plt.grid(axis="y")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
elif group == "дівчата":
    plt.bar(months, girls_births, color="pink")
    plt.xlabel("Місяць року", color = "red")
    plt.ylabel("Народжуваність", color = "red")
    plt.title(f"Народжуваність дівчат у м. Києві за 2019 рік")
    plt.grid(axis="y")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
else:
    print("Невірно введена група. Введіть \"хлопчики\" або \"дівчата\".")