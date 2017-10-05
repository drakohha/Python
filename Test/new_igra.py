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


def fun_rez(name,summa,karta,karta_2,karta_3,karta_4):
    print("\n текущие результат : ")
    for i in range(0,len(name)):
        print ("У ",name[i]," Имеется :")
        print ("сумма очков : ",summa[i])
        print ("имеющиеся карты на руках : ")
        if i==0:
            for j in range(0,len(karta)):
                print(karta[j],' ')
        if i==1:
            for j in range(0,len(karta_2)):
                print(karta_2[j],' ')
        if i==2:
            for j in range(0,len(karta_3)):
                print(karta_3[j],' ')
        if i==3:
            for j in range(0,len(karta_4)):
                print(karta_4[j],' ')
        
    
    
    
def fun_pool(name,summa,karta,karta_2,karta_3,karta_4,number_pool,num_gamer):
    if num_gamer==0:
        print("\n Крупье раздает карты : ")
        print("Вам ", name[num_gamer]," летит карта ... ")
        karta.append(koloda.pop())
        if karta[number_pool]==2:
            print("прилетел Валет(2) ")
        elif karta[number_pool]==3:
            print("Прилетела Дама(3)")
        elif karta[number_pool]==4:
            print("Прилетел король(4)")
        elif karta[number_pool]==11:
            print("Прилел туз , 1 либо 11 ")
        elif karta[number_pool]>=6 and karta[number_pool]<=10:
            print("Прилетела карта ",karta[number_pool])
        summa[num_gamer]+=(karta[number_pool])
    if num_gamer==1:
        print("\n Крупье раздает карты : ")
        print("Вам ", name[num_gamer]," летит карта ... ")
        karta_2.append(koloda.pop())
        if karta_2[number_pool]==2:
            print("прилетел Валет(2) ")
        elif karta_2[number_pool]==3:
            print("Прилетела Дама(3)")
        elif karta_2[number_pool]==4:
            print("Прилетел король(4)")
        elif karta_2[number_pool]==11:
            print("Прилел туз , 1 либо 11 ")
        elif karta_2[number_pool]>=6 and karta_2[number_pool]<=10:
            print("Прилетела карта ",karta[number_pool])
        summa[num_gamer]+=(karta_2[number_pool])

def fun_igra(game_type,kol_gamers,name,bank):
    
    global koloda
    global summa
    global number_pool
    number_pool=0
    summa=[]
    koloda = [2,3,4,6,7,8,9,10,11]*4
    shuffle(koloda)
    karta=[]
    karta_2=[]
    karta_3=[]
    karta_4=[]
    
    system='cls'
    print("Начинаеться игра! : ")
    if game_type==1:
        
        name.append('компьютер')
        bank.append(bank[0])
        while True:
            
            print("Крупье раздает карты : ")
            print("Вам ",name[0]," летит карта ...")
            karta.append(koloda.pop())
            if karta[0]==2 :
                print("прилетел Валет(2) ")
            elif karta[0]==3:
                print("Прилетела Дама(3)")
            elif karta[0]==4:
                print("Прилетел король(4)")
            elif karta[0]==11:
                print("Прилел туз , 1 либо 11 ")
            elif karta[0]>=6 and karta[0]<=10:
                print("Прилетела карта ",karta[0])
            summa.append(karta[0])
            
            
                
            
            print("Сопернику ",name[1]," летит карта ... ")
            karta_2.append(koloda.pop())
            if karta_2[0]==2 :
                print("прилетел Валет(2) ")
            elif karta_2[0]==3:
                print("Прилетела Дама(3)")
            elif karta_2[0]==4:
                print("Прилетел король(4)")
            elif karta_2[0]==11:
                print("Прилел туз , 1 либо 11 ")
            elif karta_2[0]>=6 and karta_2[0]<=10:
                print("Прилетела карта ",karta_2[0])
            summa.append(karta_2[0])

            break
        fun_rez(name,summa,karta,karta_2,karta_3,karta_4)
        number_pool+=1
            
        print("Далее : ")

        fun_pool(name,summa,karta,karta_2,karta_3,karta_4,number_pool,0)
        fun_pool(name,summa,karta,karta_2,karta_3,karta_4,number_pool,1)
        
        fun_rez(name,summa,karta,karta_2,karta_3,karta_4)
        number_pool+=1
        while True:
            if summa[0]>21:
                print("Перебор у ",name[0])
                break
            if summa[1]>21:
                print("Перебор у ",name[1])
                break

            print("Выберите действие : 1- взять еше карту 2-пасс")
            if fun_proverki(1,2)==1:
                fun_pool(name,summa,karta,karta_2,karta_3,karta_4,number_pool,0)
                fun_pool(name,summa,karta,karta_2,karta_3,karta_4,number_pool,1)
                fun_rez(name,summa,karta,karta_2,karta_3,karta_4)
                number_pool+=1
            else:
                break
                

            
            
            
    








    
def fun_accaunt(game_type,kol_gamers,name,bank):  #Создание акаунта игроков
    if game_type==1:  #Для одиночной игры
        name.append(input("Введите ваше имя! "))
        print("Введите ваш начальный банк для игрока ",name[0]," от 50 до 1000$ ")
        bank.append(fun_proverki(50,1000))
    if game_type==2 and kol_gamers==2: #для вдух игроков
        name.append(input("Введите ваше имя! "))
        print("Введите ваш начальный банк для игрока ",name[0]," от 50 до 1000$ ")
        bank.append(fun_proverki(50,1000))
        name.append(input("Введите имя второго игрока "))
        print("Введите ваш начальный банк для игрока ",name[1]," от 50 до 1000$ ")
        bank.append(fun_proverki(50,1000))
    if game_type==2 and kol_gamers==3:  #для трех игроков
        name.append(input("Введите ваше имя! "))
        print("Введите ваш начальный банк для игрока ",name[0]," от 50 до 1000$ ")
        bank.append(fun_proverki(50,1000))
        name.append(input("Введите имя второго игрока "))
        print("Введите ваш начальный банк для игрока ",name[1]," от 50 до 1000$ ")
        bank.append(fun_proverki(50,1000))
        name.append(input("Введите имя третьего игрока "))
        print("Введите ваш начальный банк для игрока ",name[2]," от 50 до 1000$ ")
        bank.append(fun_proverki(50,1000))
    if game_type==2 and kol_gamers==4:  #для четырех игроков
        name.append(input("Введите ваше имя! "))
        print("Введите ваш начальный банк для игрока ",name[0]," от 50 до 1000$ ")
        bank.append(fun_proverki(50,1000))
        name.append(input("Введите имя второго игрока "))
        print("Введите ваш начальный банк для игрока ",name[1]," от 50 до 1000$ ")
        bank.append(fun_proverki(50,1000))
        name.append(input("Введите имя третьего игрока "))
        print("Введите ваш начальный банк для игрока ",name[2]," от 50 до 1000$ ")
        bank.append(fun_proverki(50,1000))
        name.append(input("Введите имя четвертого игрока "))
        print("Введите ваш начальный банк для игрока ",name[3]," от 50 до 1000$ ")
        bank.append(fun_proverki(50,1000))
    
    



print("Правила игры : ")
print("Нужно набрать 21 очков с помошью карт ")
print("Карты ранжированы следущим образом : ")
print("6-10 соответсвтуют таким же количествам ")
print("валет - 2 очка , дама - 3 очка , король-4 очка , туз либо 1 либо 11 очков на выбор")
print("Изначально сдаеться две карта каждому игроку ")
print("каждый ход каждый игрок выбирает брать ли еше карту ")
print("Если будет перебор или недобор победит тот у ково будет ближайшее число к 21")
global name
name=[]
global bank
bank=[]




while True:
    print("\n Для выбора режима игры введите : \n 1- игра с компьютером \n 2- игра с другими игроками \n 0-выход\n ")
    game_type=fun_proverki(0,3)

    
    if game_type==0:
        break
    if game_type==1:
        system='cls'
        print("Игра с компьютером!")
        fun_accaunt(1,1,name,bank)
        fun_igra(1,1,name,bank)
    if game_type==2:
        system='cls'
        print("Игра с другими игроками : ")
        print("Введите количество игроков от 2 до 4 ")
        kol_gamers=fun_proverki(2,4)
        fun_accaunt(2,kol_gamers,name,bank)
    if game_type==3:
        system='cls'
        fun_igra(1,1)
        
