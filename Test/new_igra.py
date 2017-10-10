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


def fun_rez(name,summa,karta):
    system('cls')
    print("\n текущие результат : ")
    for i in range(0,len(name)):
        print ("У ",name[i]," Имеется :")
        print ("сумма очков : ",summa[i])
        print ("имеющиеся карты на руках : ")
        if i==0:
            for j in range(0,len(karta[0])):
                print(karta[0][j])
            
        if i==1:
            for j in range(0,len(karta[1])):
                print(karta[1][j])
            
        if i==2:
            for j in range(0,len(karta[2])):
                print(karta[2][j])
            
        if i==3:
            for j in range(0,len(karta[3])):
                print(karta[3][j])
            
        
    
    
    
def fun_pool(name,summa,karta,number_pool,num_gamer):
    if num_gamer==0:
        print("\n Крупье раздает карты : ")
        print("Вам ", name[num_gamer]," летит карта ... ")
        karta[0].append(koloda.pop())
        #
        #print(number_pool[0])
        #print(type(number_pool[0]))
        #print(type(karta[0][number_pool[0]]))
        #
        if karta[0][number_pool[0]]==2:
            print("прилетел Валет(2) ")
        elif karta[0][number_pool[0]]==3:
            print("Прилетела Дама(3)")
        elif karta[0][number_pool[0]]==4:
            print("Прилетел король(4)")
        elif karta[0][number_pool[0]]==11:
            print("Прилел туз , 1 либо 11 ")
        elif karta[0][number_pool[0]]>=6 and karta[0][number_pool[0]]<=10:
            print("Прилетела карта ",karta[0][number_pool[0]])
        summa[num_gamer]+=(karta[0][number_pool[0]])
    if num_gamer==1:
        print("\n Крупье раздает карты : ")
        print("Вам ", name[num_gamer]," летит карта ... ")
        karta[1].append(koloda.pop())
        if karta[1][number_pool[1]]==2:
            print("прилетел Валет(2) ")
        elif karta[1][number_pool[1]]==3:
            print("Прилетела Дама(3)")
        elif karta[1][number_pool[1]]==4:
            print("Прилетел король(4)")
        elif karta[1][number_pool[1]]==11:
            print("Прилел туз , 1 либо 11 ")
        elif karta[1][number_pool[1]]>=6 and karta[1][number_pool[1]]<=10:
            print("Прилетела карта ",karta[1][number_pool[1]])
        summa[num_gamer]+=(karta[1][number_pool[1]])
    if num_gamer==2:
        print("\n Крупье раздает карты : ")
        print("Вам ", name[num_gamer]," летит карта ... ")
        karta[2].append(koloda.pop())
        if karta[2][number_pool[2]]==2:
            print("прилетел Валет(2) ")
        elif karta[2][number_pool[2]]==3:
            print("Прилетела Дама(3)")
        elif karta[2][number_pool[2]]==4:
            print("Прилетел король(4)")
        elif karta[2][number_pool[2]]==11:
            print("Прилел туз , 1 либо 11 ")
        elif karta[2][number_pool[2]]>=6 and karta[2][number_pool[2]]<=10:
            print("Прилетела карта ",karta[2][number_pool[2]])
        summa[num_gamer]+=(karta[2][number_pool[2]])
    input("Нажмите любую клавишу чтобы продолжить ...")    
    

def fun_igra(game_type,kol_gamers,name,bank):
    
    global koloda
    global summa
    global number_pool
    global stavka
    stavka=[0,0]
    number_pool=[0,0]
    #print(type(number_pool[0]))
    summa=[0,0,0,0]
    koloda = [2,3,4,6,7,8,9,10,11]*4
    shuffle(koloda)
    flag=0
    karta=[[],[],[],[]]
    
    
    system('cls')
    print("Начинаеться игра! : ")
    if game_type==1:
        name[1]='компьютер'
        bank[1]=2000
        
        while True:
            print("Введите ставку  от 50 до 200")
            stavka[0]=fun_proverki(50,200)
            fun_pool(name,summa,karta,number_pool,0)
            fun_pool(name,summa,karta,number_pool,1)
            fun_rez(name,summa,karta)
            number_pool[0]+=1
            number_pool[1]+=1
            
            print("Далее : ")
            fun_pool(name,summa,karta,number_pool,0)
            fun_pool(name,summa,karta,number_pool,1)
            fun_rez(name,summa,karta)
            number_pool[0]+=1
            number_pool[1]+=1
            while True:
                if flag==1:
                    #мозг ии  думает:
                    if summa[1]<=17:
                        fun_pool(name,summa,karta,number_pool,1)
                        number_pool[1]+=1
                    elif summa[0]>21:
                        print("Компьютер пассует")
                    else:
                        fun_rez(name,summa,karta)
                        if summa[0]<=21 and summa[0] > summa[1]:
                             print("Победил ",name[0])
                        elif summa[1]<=21 and summa[1] > summa[0]:
                             print("Победил ",name[1])
                        break
                    
                if summa[0]>21:
                    print("Перебор у ",name[0])
                    print("Победил ",name[1])
                    bank[1]+=stavka[0]
                    bank[0]-=stavka[0]
                    break
                if summa[1]>21:
                    print("Перебор у ",name[1])
                    print("Победил ",name[0])
                    bank[0]+=stavka[0]
                    bank[1]-=stavka[0]
                    break
                if summa[0]==21:
                    print("Победил ",name[0])
                    bank[0]+=stavka[0]
                    bank[1]-=stavka[0]
                    break
                if summa[1]==21:
                    print("Победил ",name[1])
                    bank[1]+=stavka[0]
                    bank[0]-=stavka[0]
                    break
                print("Выберите действие : 1- взять еше карту 2-пасс")
        
                if fun_proverki(1,2)==1:
                    fun_pool(name,summa,karta,number_pool,0)
                    number_pool[0]+=1
                    #мозг ии  думает:
                    if summa[1]<=17:
                        fun_pool(name,summa,karta,number_pool,1)
                        number_pool[1]+=1
                    elif summa[0]>21:
                        print("Компьютер пассует")
                    fun_rez(name,summa,karta)
                    
                else:
                    flag=1
                    #мозг ии  думает:
                    if summa[1]<=17:
                        fun_pool(name,summa,karta,number_pool,1)
                        number_pool[1]+=1
                    elif summa[0]>21:
                        print("Компьютер пассует")
                    else:
                        fun_rez(name,summa,karta)
                        if summa[0]<=21 and summa[0] > summa[1]:
                            print("Победил ",name[0])
                            bank[0]+=stavka[0]
                            bank[1]-=stavka[0]
                        elif summa[1]<=21 and summa[1] > summa[0]:
                            print("Победил ",name[1])
                            bank[1]+=stavka[0]
                            bank[0]-=stavka[0]
                        break
                

                
            
            
            #очистка
            summa[0]=0
            summa[1]=0
            karta[0]=[]
            karta[1]=[]
            number_pool[0]=0
            number_pool[1]=0
            flag=0
            for i in range(0,len(name)):
                print("У игрока ",name[i]," банк составляет : ",bank[i])

            if bank[0]<=0:
                print("у игрока ",name[0]," закончились деньги !!! конец игре!!")
                break
            if bank[1]<=0:
                print("у игрока ",name[1]," закончились деньги !!! конец игре!!")
                break
            print("Играть еше? 1-да 2-нет")
            if fun_proverki(1,2)==1:
                koloda = [2,3,4,6,7,8,9,10,11]*4
                continue
            else:
                break

            
            
    if game_type==2:
        print("В процессе разработке :)")
    








    
def fun_accaunt(game_type,kol_gamers,name,bank):  #Создание акаунта игроков
    name[0]=(input("Введите ваше имя! "))
    print("Введите ваш начальный банк для игрока ",name[0]," от 50 до 1000$ ")
    bank[0]=(fun_proverki(50,1000))
    if game_type==2 and kol_gamers==2: #для вдух игроков
        name[1]=(input("Введите имя второго игрока "))
        print("Введите ваш начальный банк для игрока ",name[1]," от 50 до 1000$ ")
        bank[1]=(fun_proverki(50,1000))
    if game_type==2 and kol_gamers==3:  #для трех игроков
        name[1]=(input("Введите имя второго игрока "))
        print("Введите ваш начальный банк для игрока ",name[1]," от 50 до 1000$ ")
        bank[1]=(fun_proverki(50,1000))
        name.append(input("Введите имя третьего игрока "))
        print("Введите ваш начальный банк для игрока ",name[2]," от 50 до 1000$ ")
        bank.append(fun_proverki(50,1000))
    if game_type==2 and kol_gamers==4:  #для четырех игроков
        name[1]=(input("Введите имя второго игрока "))
        print("Введите ваш начальный банк для игрока ",name[1]," от 50 до 1000$ ")
        bank[1]=(fun_proverki(50,1000))
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
name=['','']
global bank
bank=[0,0]




while True:
    system('cls')
    print("\n Для выбора режима игры введите : \n 1- игра с компьютером \n 2- игра с другими игроками \n 0-выход\n ")
    game_type=fun_proverki(0,3)

    
    if game_type==0:
        break
    if game_type==1:
        system('cls')
        
        print("Игра с компьютером!")
        fun_accaunt(1,1,name,bank)
        fun_igra(1,1,name,bank)
    if game_type==2:
        system('cls')
        print("Игра с другими игроками : ")
        print("Введите количество игроков от 2 до 4 ")
        kol_gamers=fun_proverki(2,4)
        fun_accaunt(2,kol_gamers,name,bank)
    
        
