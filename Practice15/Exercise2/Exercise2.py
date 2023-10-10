#Варіант 12
import pandas as pd

data = pd.read_csv("comptagevelo20162.csv")

#Конвертуємо стовпець "Date" у формат дати з рядка у форматі "%d/%m/%Y" та додаємо стовпець місяця
data["Date"] = pd.to_datetime(data["Date"], format = "%d/%m/%Y")
data["Month"] = data["Date"].dt.month

#Групуємо дані за місяцем, обчислюємо суму для певних велодоріжок та знаходимо місяць, у якому велодоріжка була найпопулярнішою
sum_per_bike_paths  = data.groupby("Month")[["Berri1", "Boyer", "Brébeuf", "CSC (Côte Sainte-Catherine)", "Maisonneuve_2", "Maisonneuve_3", "Notre-Dame", "Parc", "PierDup", "Pont_Jacques_Cartier", "Rachel / Hôtel de Ville", "Rachel / Papineau", "René-Lévesque", "Saint-Antoine", "Saint-Urbain", "Totem_Laurier", "University", "Viger"]].sum()
most_popular_months_per_bike_paths = sum_per_bike_paths.idxmax()

print(f"Список велодоріжок та найпопулярніші місяці для них: \n{most_popular_months_per_bike_paths}")

#Обчислюємо загальну популярність велодоріжок у кожному місяці, знаходимо найпопулярніший місяць загалом
sum_total = data.groupby("Month")[["Berri1", "Boyer", "Brébeuf", "CSC (Côte Sainte-Catherine)", "Maisonneuve_2", "Maisonneuve_3", "Notre-Dame", "Parc", "PierDup", "Pont_Jacques_Cartier", "Rachel / Hôtel de Ville", "Rachel / Papineau", "René-Lévesque", "Saint-Antoine", "Saint-Urbain", "Totem_Laurier", "University", "Viger"]].sum().sum(axis=1)
most_popular_month_in_total = sum_total.idxmax()

print(f"\nНайпопулярніший місяць у велосипедистів: {most_popular_month_in_total}")