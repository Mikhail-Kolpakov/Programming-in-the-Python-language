#Варіант 12

source_str = str(input("Введіть речення: \n"))

#Перевіряємо рядок на достатню довжину
while len(source_str) < 8:
    source_str = str(input("\nВведіть речення ще раз, так як воно не має достатньої довжини (8 символів): \n"))

print(f"\nПочатковий рядок: \n{source_str}\n")

sliced_str = source_str[8:] #Робимо зріз рядка

print(f"Весь рядок окрім перших восьми символів.: \n{sliced_str}")