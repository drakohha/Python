from os import *
from random import *
print("Игра '21' \n")
def fun_proverki(i,j):  #Проверка на правельность ввода
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


def fun_rez(data):   # Ввывод текущего результата суммы очков и карт на руках
    system('cls')
    
    print("\n текущие результат : ")
    for i in range(0,len(name)):
        print ("У ",name[i]," Имеется :")
        print ("сумма очков : ",summa[i])
        print ("имеющиеся карты на руках : ")
        if i==0:
            print(na_rukah[i])
            
        if i==1:
            
            print(na_rukah[i])
            
        if i==2:
            
            print(na_rukah[i])
            
        if i==3:
            
            print(na_rukah[i])


def fun_bank(data):   # Проверка на остаток средств в банке и показ результата
    for i in range(0,len(name)):
        print("У игрока ",name[i]," банк составляет : ",bank[i])

        if bank[i]<=0:
            print("у игрока ",name[i]," закончились деньги !!! конец игре!!")
            flag=22
            break
    return data
        
    

            
def fun_clear(data):  #очистка игровых параметров перед каждой игрой пополнение карт
    temp=''
    stavka[0]=0
    index_t=[]
    for i in range(0,len(name)):
        summa[i]=0
        karta[i]=[]
        na_rukah[i]=[]
        flag_rezult[i]=1
        number_pool[i]=0
    keys=['Валет','Дама','Король','Туз']*4
    koloda = [2,3,4,6,7,8,9,10,k,k,k,k]*4
    shuffle(koloda)
    flag=0
    return data
    
    
def fun_mozg_ii(data,kol_gamers):  #Интилект игры 
    temp_ii=0
    
    
    while True: 
        for i in range(0,kol_gamers): # цикл обхода всех игроков
            # проверка на выбор туза за 1 очко или 11
            if summa[i]>21  and na_rukah[i].count('Туз')==True and index_t.count('Туз')!=True :
                print("Игрок ",name[i]," выбирает значение Туза за 1 очко")
                summa[i]-=10
                index_t.append('Туз')
                fun_rez(data)
                continue
            #Проверка на перебор у игрока    
            elif summa[i]>21:
                print("У игрока ",name[i]," перебор, он проиграл!!!")
                temp_ii=i
                flag_rezult[i]=32
                for i in range(0,kol_gamers):
                    if i!=temp_ii:
                        bank[i]+=stavka[0]
                    else:
                        bank[i]-=stavka[0]
                break
            #Проверка на победу у игрока
            elif summa[i]==21 and na_rukah[i].count('Туз')!=1:
                print("У игрока ",name[i]," победа!!!!")
                flag_rezult[i]=33
                temp_ii=i
                for i in range(0,kol_gamers):
                    if i!=temp_ii:
                        bank[i]-=stavka[0]
                    else:
                        bank[i]+=stavka[0]
                break
            #Проверка на блэкджек
            elif summa[i]==21 and (na_rukah[i].count('Туз')and na_rukah[i].count(10) or na_rukah[i].count('Туз')and na_rukah[i].count('Валет') or na_rukah[i].count('Туз')and na_rukah[i].count('Дама') or na_rukah[i].count('Туз')and na_rukah[i].count('Король')):
                print("У игрока ",name[i]," БлекДжек он победил!!!")
                temp_ii=i
                flag_rezult[i]=33
                for i in range(0,kol_gamers):
                    if i!=temp_ii:
                        bank[i]-=stavka[0]
                    else:
                        bank[i]+=stavka[0]
                break
            elif summa[i]==21 :
                print("У игрока ",name[i]," победа!!!!")
                flag_rezult[i]=33
                temp_ii=i
                for i in range(0,kol_gamers):
                    if i!=temp_ii:
                        bank[i]-=stavka[0]
                    else:
                        bank[i]+=stavka[0]
                break
            #Проверка для ии дилера брать ли карту
            elif game_type==1 and i==1:
                if summa[1]<=16:
                    flag_rezult[1]=10
                else:
                    flag_rezult[1]=0
            else:
                print("Игра идет дальше...")
                continue
        break
            
                    




    
def fun_pool(data,num_gamer):  #функция раздачи карт
    temp=0
    
    print("\n Крупье раздает карты : ")
    print("Вам ", name[num_gamer]," летит карта ... ")
    karta[num_gamer].append(koloda.pop())
    
    if karta[num_gamer][number_pool[num_gamer]]=='k':
        temp=keys.pop()
        karta[num_gamer][number_pool[num_gamer]]=int(kol_kar[temp])
    if temp=='Валет':
        print("прилетел Валет(10) ")
        na_rukah[num_gamer].append(temp)
    elif temp=='Дама':
        print("Прилетела Дама(10)")
        na_rukah[num_gamer].append(temp)
    elif temp=='Король':
        print("Прилетел король(10)")
        na_rukah[num_gamer].append(temp)
    elif temp=='Туз':
        print("Прилел туз , 1 либо 11 ")
        na_rukah[num_gamer].append(temp)
    elif karta[num_gamer][number_pool[num_gamer]]>=2 and karta[num_gamer][number_pool[num_gamer]]<=10:
        print("Прилетела карта ",karta[num_gamer][number_pool[num_gamer]])
        na_rukah[num_gamer].append(karta[num_gamer][number_pool[num_gamer]])
    summa[num_gamer]+=(karta[num_gamer][number_pool[num_gamer]])
    
    input("Нажмите любую клавишу чтобы продолжить ...")    
    

def fun_igra(data,kol_gamers):  #функция игры
    flag=0
    system('cls')
    print("Начинаеться игра! : ")
    if game_type==1:  #игра для одного игрока
        
        kol_gamers=2
        
        name[1]='Диллер'
        bank[1]=2000
        
        while True: #повторение игры до конца банка или выхода
            
            if flag==22:
                break
            print("Введите ставку  от 50 до 200")
            stavka[0]=fun_proverki(50,200)
            for i in range(0,2):
                fun_pool(data,i)
                number_pool[i]+=1
            fun_rez(data)
            fun_mozg_ii(data,kol_gamers)
            print("Далее : ")
            for i in range(0,2):
                fun_pool(data,i)
                number_pool[i]+=1
            fun_rez(data)
            fun_mozg_ii(data,kol_gamers)
            
            while True: # повторени взятие карт 
                
                if flag_rezult[0]==33 or flag_rezult[1]==33 or flag_rezult[0]==32 or flag_rezult[1]==32:
                    break
                print("Выберите действие : 1- взять еше карту 2-пасс")
                if fun_proverki(1,2)==1:
                    fun_pool(data,0)
                    number_pool[0]+=1
                    fun_rez(data)
                    fun_mozg_ii(data,kol_gamers)
                    if flag_rezult[0]==32 or flag_rezult[0]==33 :
                        break
                else:
                    while True:    #при пассе игрока Дилеер решает продолжать ли игру
                        fun_mozg_ii(data,kol_gamers)
                        if flag_rezult[1]==10:
                            fun_pool(data,1)
                            number_pool[1]+=1
                            fun_rez(data)
                            fun_mozg_ii(data,kol_gamers)
                            if flag_rezult[1]==0 or flag_rezult[1]==33 or flag_rezult[1]==32:
                                break
                        else: # если у всех недобор
                            
                            if summa[0]>summa[1]:
                                bank[0]+=stavka[0]
                                bank[1]-=stavka[0]
                                print("Побеждает игрок ",name[0])
                                flag_rezult[0]=33
                            elif summa[0]==summa[1]:
                                print("Ничья")
                                flag_rezult[0]=33
                            else :
                                bank[1]+=stavka[0]
                                bank[0]-=stavka[0]
                                print("Побеждает игрок ",name[1])
                                flag_rezult[0]=33
                            break
                    
                
                
                if flag_rezult[1]==10:
                    fun_pool(data,1)
                    number_pool[1]+=1
                    fun_rez(data)
                    fun_mozg_ii(data,kol_gamers)
                    if flag_rezult[1]==0 or flag_rezult[1]==33 or flag_rezult[1]==32:
                        break
                else:
                    print("Дилер пассует!!")
                    
                

                
            
            
            #очистка
            fun_clear(data)
            fun_bank(data)
            if flag==22:
                break
            print("Играть еше? 1-да 2-нет")
            if fun_proverki(1,2)==1:
                fun_clear(data)
                continue
            else:
                break

            
            
    if game_type==2: #игра для нескольких игроков
        flag_id=[0,0,0,0]
        flag_de=0
        flag=0
        index=0
        system('cls')
        flag_rezult=[1,1,1,1]
        while True:  #цикл повторения игры
            print("Введите ставку  от 50 до 200")
            flag_de=0
            stavka[0]=fun_proverki(50,200)
            for i in range (0,2):    
                fun_pool(data,i)
                number_pool[i]+=1
            fun_rez(data)
            fun_mozg_ii(data,kol_gamers)
            print("Далее : ")
            for i in range (0,2):    
                fun_pool(data,i)
                number_pool[i]+=1
            fun_rez(data)
            fun_mozg_ii(data,kol_gamers)
            for i in range (0,kol_gamers): #провера на блэклжек
                if flag_rezult[i]==33 or flag_rezult[i]==32:
                    print(flag_rezult[i])
                    flag_de=1
                    break
            while flag_de!=1: #повторение ходов
                if flag==22:
                    break
                for i in range(0,kol_gamers): #проверка если все сделали пасс
                    if flag_id[i]==2:
                        index+=1
                     
                if index==kol_gamers:
                    break
                for i in range(0,kol_gamers): #поочередный ход игроков
                    
                    if flag_rezult[i]==0 or flag_rezult[i]==33 or flag_de==1:
                        flag=1
                        
                        break
                    if flag_id[0]==2 and flag_id[1]==2:
                        
                        flag_de=1
                        break
                    elif flag_id[0]==2 and flag_id[1]==2 and flag_id[2]==2:
                        flag_de=1
                        break
                    elif flag_id[0]==2 and flag_id[1]==2 and flag_id[2]==2 and flag_id[3]==2:
                        flag_de=1
                        break
                    print(name[i]," Выберите действие : 1- взять еше карту 2-пасс")
                    if fun_proverki(1,2)==1:
                        fun_pool(data,i)
                        number_pool[i]+=1
                        fun_rez(data)
                        fun_mozg_ii(data,kol_gamers)
                        if flag_rezult[i]==0 or flag_rezult[i]==33 or flag_rezult[i]==32:
                            flag=1
                            flag_de=1
                            break
                    else:
                        print("Тогда ход за следущим игроком")
                        flag_id[i]=2
            if summa[0]<21 and summa[1]<21:
                if summa[0]>summa[1]:
                    bank[0]+=stavka[0]
                    bank[1]-=stavka[0]
                    print("Побеждает игрок ",name[0])
                    flag_rezult[0]=33
                elif summa[0]==summa[1]:
                    print("Ничья")
                    flag_rezult[0]=33
                else :
                    bank[1]+=stavka[0]
                    bank[0]-=stavka[0]
                    print("Побеждает игрок ",name[1])
                    flag_rezult[0]=33
                  
            fun_bank(bank)
            if flag==22:
                break




            flag_de=0
            for i in range(0,kol_gamers):
                flag_id[i]=0
                flag_rezult[i]=1
            print("Играть еше? 1-да 2-нет")
            if fun_proverki(1,2)==1:
                flag_de=0
        
                fun_clear(data)
                continue
            else:
                break
    








    
def fun_accaunt(data):  #Создание акаунта игроков
    name[0]=(input("Введите ваше имя! "))
    print("Введите ваш начальный банк для игрока ",name[0]," от 50 до 1000$ ")
    bank[0]=(fun_proverki(50,1000))
    if game_type==2: #для нескольких игроков
        for i in range(1,kol_gamers):
            
            name[i]=(input("Введите имя второго игрока "))
            print("Введите ваш начальный банк для игрока ",name[i]," от 50 до 1000$ ")
            bank[i]=(fun_proverki(50,1000))
            if kol_gamers>2:
                name.append('')
                bank.append(0)
                flag_rezult.append(0)
            
print("Игра блэкджек!!!!")
print("Правила игры : ")
print("Нужно набрать 21 очков с помошью карт ")
print("Карты ранжированы следущим образом : ")
print("2-10 соответсвтуют таким же количествам ")
print("валет,дама,король -10 очков , туз либо 1 либо 11 очков на выбор")
print("Изначально сдаеться две карта каждому игроку ")
print("каждый ход каждый игрок выбирает брать ли еше карту ")
print("Если будет перебор игрок проиграет если недобор победит тот у ково будет ближайшее число к 21")
print("Блекджек когда туз + 10 очкоф сразу победа")
#тело игры создание переменных
global name
name=['','']
global bank
bank=[0,0]
global flag_rezult
global game_type
global flag
global summa
global na_rukah
global data
global kol_gamers
global koloda
global number_pool
global stavka
global k
global keys
global kol_kar
global temp
global karta
global index_t
index_t=[]
kol_kar={'Валет':10,'Дама':10,'Король':10,'Туз':11}
k='k'
karta=[[],[],[],[]]
flag_rezult=[1,1]
na_rukah=[[],[],[],[]]
temp=''
stavka=[0,0]
number_pool=[0,0]
summa=[0,0,0,0]
keys=['Валет','Дама','Король','Туз']*4
koloda = [2,3,4,6,7,8,9,10,k,k,k,k]*4
shuffle(koloda)
flag=0
number_pool=[0,0,0,0]
flag=0
kol_gamers=0
game_type=0
data=[keys,name,summa,index_t,bank,flag,flag_rezult,na_rukah,game_type,kol_gamers,karta,temp,k,kol_kar,number_pool,stavka,koloda]

while True: # цикл выбора режима игры
    system('cls')
    print("\n Для выбора режима игры введите : \n 1- игра одному \n 2- игра с другими игроками \n 0-выход\n ")
    game_type=fun_proverki(0,3)

    
    if game_type==0:
        break
    if game_type==1:
        system('cls')
        
        print("Игра проив Дилера!")
        fun_accaunt(data)
        fun_igra(data,kol_gamers)
    if game_type==2:
        system('cls')
        print("Игра с другими игроками : ")
        print("Введите количество игроков от 2 до 4 ")
        kol_gamers=fun_proverki(2,4)
        fun_accaunt(data)
        fun_igra(data,kol_gamers)
    
        

