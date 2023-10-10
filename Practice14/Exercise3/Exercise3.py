#Варіант 12
import matplotlib.pyplot as plt
import numpy as np

#Вікові категорії та відсотки для кожної категорії
age_categories = ["0", "5-9", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40-44", "45-49", "50-54", "55-59", "60-64", "65-69", "70-74", "75-79", "80-84"]
percentages = [2.7, 2.9, 2.3, 2.2, 2.8, 3.8, 4.2, 3.9, 3.5, 3.1, 3.3, 3.1, 3.0, 2.0, 1.2, 1.2, 0.7]

np.array(age_categories)
np.array(percentages)

# Побудова кругової діаграми
plt.figure(figsize=(10, 10))
plt.pie(percentages, labels = age_categories, autopct='%1.1f%%', startangle = 140)
plt.legend(title="Вікові категорії", loc="upper right")
plt.title("Вікова статистика чоловічого населення України (2017 р.)")

plt.show() #Відображення кругової діаграми