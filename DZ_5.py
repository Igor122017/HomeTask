# 5 Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между 
# ними в 2D пространстве.

# Пример: -  
#  A (7,-5); B (1,-1) -> 7,21

x_coo1 = float(input("Введите первое число X = "))
y_coo1 = float(input("Введите первое число Y = "))
x_coo2 = float(input("Введите второе число X = "))
y_coo2 = float(input("Введите второе число Y = "))

def lens(x1, y1, x2, y2):
    res = round(((x2 - x1) ** 2 + ((y2 - y1)) ** 2) ** 0.5, 2)
    return res

result = lens(x_coo1, y_coo1, x_coo2, y_coo2)

print(f' -> {result}')