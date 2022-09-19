# 1 - Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]
def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            num = int(input(inputText))
            if num < 0:
                num *= -1
            is_OK = True
        except ValueError:
            print("это не число, повторите попытку")
    return num

def Mnojiteli(n):
    ls = []
    delitel = 2
    while delitel * delitel <= n:
        if n % delitel == 0:
            ls.append(delitel)
            n //= delitel
        else:
            delitel += 1
    if n > 1:
        ls.append(n)
    return ls

number = InputNumbers('Введите натуральное число: ')
print(Mnojiteli(number))