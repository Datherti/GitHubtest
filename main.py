n = int(input("Введіть кількість елементів у послідовності: "))
sequence = [int(x) for x in input("Введіть натуральні числа через пробіл: ").split()]

evenNumbers = [x for x in sequence if x % 2 == 0]

if len(evenNumbers) == 0:
    print("У послідовності немає парних чисел.")
else:
    print("Масив парних чисел:", evenNumbers)