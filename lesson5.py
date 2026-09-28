try:
        a = int(input("Введите целое число: "))
except ValueError:
     print("Это не число")
else:
    if ((a % 2) == 0) and (a > 0):
        print("Положительное четное число")
    elif ((a % 2) == 0) and (a < 0):
        print("Отрицательное четное число")
    elif ((a % 2) != 0) and (a > 0):
        print("Положительное нечетное число")
    elif ((a % 2) != 0) and (a < 0):
        print("Отрицательное нечетное число")
    elif a == 0:
        print("Нулевое число")