# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат.

x = int(input("Введите х = "))
y = int(input("Введите y = "))
z = int(input("Введите z = "))

a = not (x or y or z)
b = not x and not y and not z

if a == b:
    print("Истинно!")
else:
    print("Ложно!")