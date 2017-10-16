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


def fun_rez(data):
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


def fun_bank(data):
    for i in range(0,len(name)):
        print("У игрока ",name[i]," банк составляет : ",bank[i])

        if bank[i]<=0:
            print("у игрока ",name[i]," закончились деньги !!! конец игре!!")
            flag=22
            break
        
    

            
def fun_clear(data):
    temp=''
    stavka[0]=0
    
    for i in range(0,len(name)):
        summa[i]=0
        na_rukah[i]=[]
        flag_rezult[i]=1
        number_pool[i]=0
    keys=['Валет','Дама','Король','Туз']*4
    koloda = [2,3,4,6,7,8,9,10,k,k,k,k]*4
    shuffle(koloda)
    flag=0
    return data
    
    
def fun_mozg_ii(data,kol_gamers):
    temp_ii=0
    print(kol_gamers)
    while True:
        for i in range(0,kol_gamers):
            if summa[i]>21:
                print("У игрока ",name[i]," перебор, он проиграл!!!")
                temp_ii=i
                flag_rezult[i]=0
                for i in range(0,kol_gamers):
                    if i!=temp_ii:
                        bank[i]+=stavka[0]//(kol_gamers-1)
                    else:
                        bank[i]-=stavka[0]
                break
            elif summa[i]==21 and na_rukah[i].issuperset('Туз')!=True:
                print("У игрока ",name[i]," победа!!!!")
                flag_rezult[i]=33
                temp_ii=i
                for i in range(0,kol_gamers):
                    if i!=temp_ii:
                        bank[i]-=stavka[0]
                    else:
                        bank[i]+=stavka[0]
                break
            elif na_rukah[i]==['Туз',10] or na_rukah[i]==['Туз','Дама'] or na_rukah[i]==['Туз','Валет'] or na_rukah[i]==['Туз','Король']:
                print("У игрока ",name[i]," БлекДжек он победил!!!")
                temp_ii=i
                flag_rezult[i]=33
                for i in range(0,kol_gamers):
                    if i!=temp_ii:
                        bank[i]-=stavka[0]
                    else:
                        bank[i]+=stavka[0]
                break
            elif game_type==1 and i==1:
                if summa[1]<=16:
                    flag_rezult[1]=10
                else:
                    flag_rezult[1]=0
            else:
                print("Игра идет дальше...")
                continue
        break
            
                    




    
def fun_pool(data,num_gamer):
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
    

def fun_igra(data):
    system('cls')
    print("Начинаеться игра! : ")
    if game_type==1:
        
        kol_gamers=2
        
        name[1]='Диллер'
        bank[1]=2000
        
        while True:
            #print(koloda)
           # print(na_rukah)
           # print(keys)
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
            while True:
                #print(flag_rezult)
                if flag_rezult[0]==0 or flag_rezult[0]==33 or flag_rezult[1]==33:
                    break
                print("Выберите действие : 1- взять еше карту 2-пасс")
                if fun_proverki(1,2)==1:
                    fun_pool(data,0)
                    number_pool[0]+=1
                    fun_rez(data)
                    fun_mozg_ii(data,kol_gamers)
                    
                else:
                    while flag_rezult[1]!=0:    
                        fun_mozg_ii(data,kol_gamers)
                        if flag_rezult[1]==10:
                            fun_pool(data,1)
                            number_pool[1]+=1
                            fun_rez(data)
                            fun_mozg_ii(data,kol_gamers)
                        else:
                            print("Дилер пассует")
                            if summa[0]>summa[1]:
                                bank[0]+=stavka[0]
                                bank[1]-=stavka[0]
                                print("Побеждает игрок ",name[0])
                            elif summa[0]==summa[1]:
                                print("Ничья")
                            else :
                                bank[1]+=stavka[0]
                                bank[0]-=stavka[0]
                                print("Побеждает игрок ",name[1])
                            break
                    
                
                if flag_rezult[1]==0:
                    break
                if flag_rezult[1]==10:
                    fun_pool(data,1)
                    number_pool[1]+=1
                    fun_rez(data)
                    fun_mozg_ii(data,kol_gamers)
                else:
                    print("Дилер пассует!!")
                    
                

                
            
            
            #очистка
            fun_clear(data)
            fun_bank(data)
            print("Играть еше? 1-да 2-нет")
            if fun_proverki(1,2)==1:
                fun_clear(data)
                continue
            else:
                break

            
            
    if game_type==2:
        flag_id=[0,0,0,0]
        flag_de=0
        system('cls')
        print("В процессе разработке :)")
        while True:
            print("Введите ставку  от 50 до 200")
            stavka[0]=fun_proverki(50,200)
            for i in range (0,2):    
                fun_pool(data,i)
                number_pool[i]+=1
            fun_rez(data)
            print("Далее : ")
            for i in range (0,2):    
                fun_pool(data,i)
                number_pool[i]+=1
            fun_rez(data)
            
            while flag_de!=1:
                if flag==22:
                    break
                for i in range(0,kol_gamers):
                    if flag_id[0]==1 and flag_id[1]==1 and kol_gamers==2:
                        if summa[0]>summa[1]:
                            print("У игрока ",name[0]," победа!")
                            bank[0]+=stavka[0]
                            bank[1]-=stavka[0]
                        else:
                            print("У игрока ",name[1]," победа!")
                            bank[1]+=stavka[0]
                            bank[0]-=stavka[0]
                            
                        flag_de=1
                        break
                    if flag_id[i]==1:
                        continue
                    print(name[i]," Выберите действие : 1- взять еше карту 2-пасс")
                    if fun_proverki(1,2)==1:
                        fun_pool(data,i)
                        number_pool[i]+=1
                        fun_rez(data)
                    else:
                        print("Тогда ход за следущим игроком")
                        flag_id[i]=1
                for i in range(0,kol_gamers+1):
                    if summa[i]>21:
                        print("У игрока ",name[i], " перебор")
                        bank[i]-=stavka[0]
                        flag_de=1
                        break
                    elif summa[i]==21:
                        print("У игрока ",name[i]," победа!")
                        bank[i]+=stavka[0]
                        flag_de=1
                        break
                    else:
                        continue
                
                
            fun_bank(bank)




            flag_de=0
            flag_id=[0,0,0,0]
            print("Играть еше? 1-да 2-нет")
            if fun_proverki(1,2)==1:
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
data=[keys,name,summa,bank,flag,flag_rezult,na_rukah,game_type,kol_gamers,karta,temp,k,kol_kar,number_pool,stavka,koloda]

while True:
    system('cls')
    print("\n Для выбора режима игры введите : \n 1- игра одному \n 2- игра с другими игроками \n 0-выход\n ")
    game_type=fun_proverki(0,3)

    
    if game_type==0:
        break
    if game_type==1:
        system('cls')
        
        print("Игра проив Дилера!")
        fun_accaunt(data)
        fun_igra(data)
    if game_type==2:
        system('cls')
        print("Игра с другими игроками : ")
        print("Введите количество игроков от 2 до 4 ")
        kol_gamers=fun_proverki(2,4)
        fun_accaunt(data)
        fun_igra(data)
    
        

#Дополнительные правила#
#
#На своих боксах игроку разрешается не только брать карты, но также пользоваться дополнительными возможностями.
#Сплит (Split) – имея на боксе две карты одного номинала (в некоторых казино даже одного достоинства, то есть, дама и король), игрок может разделить их на два бокса, поставив еще одну ставку того же размера. После этого будет производиться дополнительный набор карт на каждый из новых боксов. Если на один из новых боксов придет карта того же номинала, сплит можно сделать еще раз. Количество возможных сплитов с одного бокса варьируется, но обычно не превышает трех. При сплите тузов, как правило, раздается лишь одна карта, после чего игра переходит на следующий бокс. Если вновь приходит туз, можно сделать еще сплит. Туз и любая карта в десять очков полученные в результате сплита, не считаются блэкджеком и рассматриваются как двадцать одно очко (это означает, что они проиграют, если блэкджек будет у крупье).#
#Дабл (Double) – получив первые две карты, игрок имеет право сделать дабл. Для этого он должен удвоить свою первоначальную ставку. После этого ему раздается еще одна карта на этот бокс и дилер переходит к следующему игроку или открывает свои карты.#
