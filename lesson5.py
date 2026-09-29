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

# Второе задание

word = input("Введите слово: ")
vowels = "aeiou"

vowels_count = 0
consonants_count = 0

for letter in word:
    if letter in vowels:
        vowels_count += 1
    else:
        consonants_count += 1

print("Гласных:", {vowels_count})
print("Согласных:", {consonants_count})

for vowel in vowels:
    count = word.count(vowel)

    if count > 0:
        print(vowel, ":", count)
    else:
        print(vowel, ":", False)


#Третья задача

X = int(input("Минимальная сумма: "))
A = int(input("Деньги Майкла: "))
B = int(input("Деньги Ивана: "))

if A >= X and B >= X:
    print(2)

elif A >= X:
    print("Mike")

elif B >= X:
    print("Ivan")

elif A + B >= X:
    print(1)

else:
    print(0)