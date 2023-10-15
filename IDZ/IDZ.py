#Варіант 12
import pygame
from random import randrange

#Задаємо розмір квадратного вікна гри та розмір секції змійки
RES = 800
SIZE = 50

#Початкове положення змійки та яблука
x, y = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
apple = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)

dirs = {"W": True, "S": True, "A": True, "D": True} #Дозволяємо рухання для всіх клавіш

length = 1 #Довжина змійки
snake = [(x, y)]

score = 0 #Кількість набраних очок
dx, dy = 0, 0 #Напрямок руху
fps = 60
speed_count, snake_speed = 0, 10 #Відповідають за швидкість змійки

#Ініціалізуємо модулі pygame
pygame.init()
surface = pygame.display.set_mode([RES, RES]) #Створюємо робоче вікно
clock = pygame.time.Clock() #Для регулювання швидкості змійки
font_score = pygame.font.SysFont("Arial", 26, bold = True) #Налаштування для шрифту балів
font_end = pygame.font.SysFont("Arial", 66, bold = True) #Налаштування для шрифту надпису програшу
img = pygame.image.load("background-texture.png").convert() #Малюнок для заднього фону

def close_game(): #Функція для закриття гри
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

while True:
    surface.blit(img, (0, 0)) #Відображаємо фоновий малюнок
    [(pygame.draw.rect(surface, pygame.Color("green"), (i, j, SIZE - 1, SIZE - 1))) for i, j in snake] #Малюємо змійку
    pygame.draw.rect(surface, pygame.Color("red"), (*apple, SIZE, SIZE)) #Малюємо яблуко
    
    #Створюємо надпис кількості очок
    render_score = font_score.render(f"Score: {score}", 1, pygame.Color("orange"))
    surface.blit(render_score, (5, 5))
    
    #Визначаємо напрямок руху змійки
    speed_count += 1
    if not speed_count % snake_speed:
        x += dx * SIZE
        y += dy * SIZE
        snake.append((x, y))
        snake = snake[-length:]
    
    #Випадок з'їдання яблука
    if snake[-1] == apple:
        apple = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
        length += 1
        score += 1
        snake_speed -= 1
        snake_speed = max(snake_speed, 4)
        
    #Випадок програшу
    if x < 0 or x > RES - SIZE or y < 0 or y > RES - SIZE or len(snake) != len(set(snake)):
        while True:
            render_end = font_end.render("GAME OVER", 1, pygame.Color("orange"))
            surface.blit(render_end, (RES // 2 - 200, RES // 3))
            pygame.display.flip()
            close_game()
    
    pygame.display.flip() #Оновлюємо поверхню
    clock.tick(fps) #Створюємо затримку для fps
    close_game()
            
    #Визначаємо управління
    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        if dirs["W"]:
            dx, dy = 0, -1
            dirs = {"W": True, "S": False, "A": True, "D": True}
    if key[pygame.K_s]:
        if dirs["S"]:
            dx, dy = 0, 1
            dirs = {"W": False, "S": True, "A": True, "D": True}
    if key[pygame.K_a]:
        if dirs["A"]:
            dx, dy = -1, 0
            dirs = {"W": True, "S": True, "A": True, "D": False}
    if key[pygame.K_d]:
        if dirs["D"]:
            dx, dy = 1, 0
            dirs = {"W": True, "S": True, "A": False, "D": True}