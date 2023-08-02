#1 Вивести на екран назву дня тижня
number_day = int(input("Введіть цифру дня тижня від 1 до 7: "))

if number_day ==1:
    print("Понеділок")
elif number_day ==2:
    print("Вівторок")
elif number_day ==3:
    print("Середа")
elif number_day ==4:
    print("Четевер")
elif number_day ==5:
    print("Пятниця")
elif number_day ==6:
    print("Субота")
elif number_day ==7:
    print("Неділя")
else:
    print("Невірне число дeня тижня ! ")

#2 Вивести на екран назву місяця

number_day = int(input("Введіть цифру дня місяця від 1 до 12: "))

if number_day ==1:
    print("Січень")
elif number_day ==1:
    print("Лютий")
elif number_day ==2:
    print("Березень")
elif number_day ==3:
    print("Квітень")
elif number_day ==4:
    print("Травень")
elif number_day ==5:
    print("Травень")
elif number_day ==6:
    print("Червень")
elif number_day ==7:
    print("Липень")
elif number_day ==8:
    print("Серпень")
elif number_day ==9:
    print("Вересень")
elif number_day ==10:
    print("Жовтень")
elif number_day == 11:
    print("Листопад")
elif number_day ==12:
    print("Грудень")
else:
    print("Невірне число дня тижня !")

#3 Число більше, меньше, та дорівнює "0"

number = int(input("Введіть число: "))
if number > 0: print("Number is positive")
if number < 0: print("Number is negative")
elif number == 0: print("Number is equal to zero")
else:
    print()

#4 Визначити чи два числа є рівними і якщо ні вивести їх на екран у порядку зростання


number1 = int(input("Введіть перше число: "))

number2 = int(input("Введіть друге число: "))


if number1 != number2 and number1 < number2:

    print(str(number1) + " " + str(number2))

elif number1 != number2 and number1 > number2:

    print(str(number2) + " " + str(number1))

else:

    print("number1 = number2")







