from os import *
from random import *
print("Игра '21' \n")
def fun_proverki(i,j):
    while True:
        try:
            n=int(input())
            if n>=i and n<=j:
                break
            else:
                print("Неверный ввод , введите в диапозоне от ",i," до ",j)
        except ValueError:
            print("Неверный ввод , введите в диапозоне от ",i," до ",j)
    return n

def fun_igra(game_type,kol_gamers):
    system='cls'
    global summa
    global summa_2
    summa=0
    summa_2=0
    print("Начинаеться игра! : ")
    if game_type==1:
        name_2='компьютер'
        bank_2=bank
        while True:
            print("Крупье раздает карты : ")
            print("Вам ",name," летит карта ...")
            karta_1=randint(2,14)
            if karta_1>=2 and karta_1<=10:
                print("прилетела " ,karta_1)
            elif karta_1==11:
                print("Прилетел Валет(2)")
                karta_1=2
            elif karta_1==12:
                print("Прилетела Дама(3)")
                karta_1=3
            elif karta_1==13:
                print("Прилетел король(4)")
                karta_1=4
            elif karta_1==14:
                print("Прилел туз , 1 либо 11 ")
                karta_1=1
            summa=summa+karta_1
            print("Сопернику ",name_2," летит карта ... ")
            karta_2=randint(2,14)
            if karta_2>=2 and karta_2<=10:
                print("прилетела " ,karta_1)
            elif karta_2==11:
                print("Прилетел Валет(2)")
                karta_2=2
            elif karta_2==12:
                print("Прилетела Дама(3)")
                karta_2=3
            elif karta_2==13:
                print("Прилетел король(4)")
                karta_2=4
            elif karta_2==14:
                print("Прилел туз , 1 либо 11 ")
                karta_2=1
            summa_2=summa_2+karta_2
            print("\n текущие результат : ")
            print ("У ",name," набралось очков : ",summa)
            print("У ",name_2," набралось очков : ",summa_2)
            if summa<21 and summa_2<21:
                print("Взять еше карту? 1-да , 2-нет")
                flag_igra=fun_proverki(1,2)
                if flag_igra==1:
                    continue
                else:
                    break
            if summa==21 or summa_2==21:
                print("У нас есть победитель!!!")
                break
            if summa>21 or summa_2>21:
                print("У одного из игроков перебор!!!")
                break

        print("Игра закончена текуший результат : ")
        if (21-summa)< (21-summa_2):
            print("Победил ",name," с результатом в ",summa," очков")
            print("Его банк теперь составляет : ",bank," !!!")
        if (21-summa)> (21-summa_2):
            print("Победил ",name_2," с результатом в ",summa_2," очков")
            print("Его банк теперь составляет : ",bank_2," !!!")
        if (21-summa)==(21-summa_2):
            print("Ничья!!!")








    
def fun_accaunt(game_type,kol_gamers):
    if game_type==1:
        global name
        global bank
        name=input("Введите ваше имя! ")
        print("Введите ваш начальный банк для игрока ",name," от 50 до 1000$ ")
        bank=fun_proverki(50,1000)
        return name,bank
    if game_type==2 and kol_gamers==2:
        global name_2
        global bank_2
        name=input("Введите ваше имя! ")
        print("Введите ваш начальный банк для игрока ",name," от 50 до 1000$ ")
        bank=fun_proverki(50,1000)
        name_2=input("Введите имя второго игрока ")
        print("Введите ваш начальный банк для игрока ",name_2," от 50 до 1000$ ")
        bank_2=fun_proverki(50,1000)
        return name,name_2,bank,bank_2
    if game_type==2 and kol_gamers==3:
        global name_3
        global bank_3
    
        name=input("Введите ваше имя! ")
        print("Введите ваш начальный банк для игрока ",name," от 50 до 1000$ ")
        bank=fun_proverki(50,1000)
        name_2=input("Введите имя второго игрока ")
        print("Введите ваш начальный банк для игрока ",name_2," от 50 до 1000$ ")
        bank_2=fun_proverki(50,1000)
        name_3=input("Введите имя третьего игрока ")
        print("Введите ваш начальный банк для игрока ",name_3," от 50 до 1000$ ")
        bank_3=fun_proverki(50,1000)
        return name,name_2,name_3,bank,bank_2,bank_3
    if game_type==2 and kol_gamers==4:
        global name_4
        global bank_4
        name=input("Введите ваше имя! ")
        print("Введите ваш начальный банк для игрока ",name," от 50 до 1000$ ")
        bank=fun_proverki(50,1000)
        name_2=input("Введите имя второго игрока ")
        print("Введите ваш начальный банк для игрока ",name_2," от 50 до 1000$ ")
        bank_2=fun_proverki(50,1000)
        name_3=input("Введите имя третьего игрока ")
        print("Введите ваш начальный банк для игрока ",name_3," от 50 до 1000$ ")
        bank_3=fun_proverki(50,1000)
        name_4=input("Введите имя четвертого игрока ")
        print("Введите ваш начальный банк для игрока ",name_4," от 50 до 1000$ ")
        bank_4=fun_proverki(50,1000)
        return name,name_2,name_3,name_4,bank,bank_2,bank_3,bank_4
    
    



print("Правила игры : ")
print("Нужно набрать 21 очков с помошью карт ")
print("Карты ранжированы следущим образом : ")
print("2-10 соответсвтуют таким же количествам ")
print("валет - 2 очка , дама - 3 очка , король-4 очка , туз 1 либо 11 очков на выбор")
print("Изначально сдаеться одна карта каждому игроку ")
print("каждый ход каждый игрок выбирает брать ли еше карту ")
print("Если будет перебор или недобор победит тот у ково будет ближайшее число к 21")


while True:
    print("\n Для выбора режима игры введите : \n 1- игра с компьютером \n 2- игра с другими игроками \n 0-выход\n ")
    game_type=fun_proverki(0,2)

    
    if game_type==0:
        break
    if game_type==1:
        system='cls'
        print("Игра с компьютером!")
        fun_accaunt(1,1)
        fun_igra(1,1)
    if game_type==2:
        system='cls'
        print("Игра с другими игроками : ")
        print("Введите количество игроков от 2 до 4 ")
        kol_gamers=fun_proverki(2,4)
        fun_accaunt(2,kol_gamers)
        
