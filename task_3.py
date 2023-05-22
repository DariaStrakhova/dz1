#Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
#Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
#Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
#Пример:
#385916 -> yes
#123456 -> no

i = int(input('Введите номер билетa: '))

if i > 1000000 or i <= 99999:

    print("Ошибка. Номер билета содержит 6 цифры")
else:
    print("Правда что билет счастливый?")

a = i // 100000
b = i // 10000 % 10
c = i // 1000 % 10
d = i // 100 % 10
e = i // 10 % 10
f = i % 10

sum1 = a+b+c
sum2 = d+e+f

if sum1==sum2:
    print("yes")
else:
    print("no")
 




