#Игра, "Угадай число"
print("игра : Угадай число\n")
from random import *
print("я загадал число от 1 до 100!\n")
print('Угадай, что это за число\n')
ehe=1
kol_p=0
var=0
kol_p2=0
stavka=0
bank=1000
while ehe!=0:  #цикл повторения игры
    
    number = randrange(1,101)
    print(number)
    while True:  #Проверка на правельность ввода !
        try:
            
            kol_p2=int(input('За сколько попыток вы хотите угодать число? (количество может быть от 1 до 10) : '))
            if kol_p2>0 and kol_p2<11 :
                break
            else:
                print('Число не в диапозоне от 1 до 10, введите заного: ')
        except ValueError:
                print('Число не в диапозоне от 1 до 10, введите заного: ')

    while True: #Проверка на правельность ввода !
        try:
            stavka=int(input('Сколько $ вы хотите поставить на свою ставку (количество может быть от 1 до 1000)?: '))
            if stavka>0 and stavka<1001:
                break
            else:
                print('Число не в диапозоне от 1 до 1000, введите заного: ')

        except ValueError:
                print('Число не в диапозоне от 1 до 1000, введите заного: ')
    print("Ваш банк составляет : ",bank," текущая ставка : ",stavka, " за ",kol_p2,"попыток!")
    while True: # Цикл угадывания числа
        while True: #Проверка на правельность ввода !
            try:
                var=int(input('Ваше число: '))
                if var>0 and var<101 and type(var)==int:
                    break
                else:
                    print('Число не в диапозоне от 1 до 100, введите заного: ')
            except ValueError:
                print('Число не в диапозоне от 1 до 100, введите заного: ')
                
        
        if var>number:
            print("Нээ, мое число меньше!")
            kol_p+=1
        elif var<number:
            print("Нээ, мое число больше!")
            kol_p+=1
        else:
            print("Да, мое число это", number)
            kol_p+=1
            break
    if kol_p<=kol_p2:
        bank=bank+stavka
        print('Вы выйграли свою ставку ваш банк пополнен и составляет: ',bank)
    else:
        bank=bank-stavka
        print('Вы проиграли свою ставку ваш банк уменьшен : ',bank)
    print('Ок. это было круто!, Вы справелись за',kol_p,'попыток!')
    if bank >0:
        ehe=int(input('Хотите сыграть еше? : 1- Да, 0-Нет: '))
    else:
        print('у вас кончелись деньги вы больше не можете играть !')
        ehe=0
    kol_p=0
