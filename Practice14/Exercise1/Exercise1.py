#Варіант 12
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 8, 400)  #x=[0...8] з 400 точками для гладкості графіку
y = 5 * np.sin(10 * x) * np.sin(3 * x) / (x**x) #Обчислюємо значення функції Y(x) для кожного x

plt.plot(x, y, label="Y(x)=5*sin(10*x)*sin(3*x)/(x^x)", color="blue", linewidth = 2)  #Задаємо колір та товщину лінії

#Додаємо осі та позначки на них
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)

#Підписуємо осі
plt.xlabel("x", color="blue")
plt.ylabel("y", color="blue")

plt.title("Графік функції Y(x)") #Додаємо назву графіка

plt.legend(loc="upper right") #Додаємо легенду

#Відображаємо графік на екрані
plt.grid(True)
plt.show()