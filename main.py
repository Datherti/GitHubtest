import math

def func(x, l):
    if math.cos(x) == 0 or h == 0:
        print("Помилка: ctg(x) невизначений або крок h дорівнює 0.")
        return None

    result = 1 / math.tan(x) + l
    return result

a = float(input("Введіть початкове значення a: "))
b = float(input("Введіть кінцеве значення b: "))
h = float(input("Введіть крок h: "))
l = float(input("Введіть значення константи l: "))

if a == 0 or b == 0 or h == 0:
    print("Значення a, b або h не можуть дорівнювати 0.")
else:
    print("\nЗначення аргументу\tЗначення функції F(x)")

    x = a
    while x <= b:
        result = func(x, l)
        if result is not None:
            print(f"{round(x, 2)}\t\t\t\t{round(result, 4)}")
        x += h
