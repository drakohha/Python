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
            print(na_rukah[i])
            
        if i==1:
            
            print(na_rukah[i])
            
        if i==2:
            
            print(na_rukah[i])
            
        if i==3:
            
            print(na_rukah[i])
            
        
    
    
    
def fun_pool(name,summa,karta,number_pool,num_gamer):
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
    

def fun_igra(game_type,kol_gamers,name,bank):
    
    global koloda
    global summa
    global number_pool
    global stavka
    global k
    global keys
    global kol_kar
    global temp
    global na_rukah
    na_rukah=[[],[],[],[]]
    temp=''
    stavka=[0,0]
    number_pool=[0,0]
    #print(type(number_pool[0]))
    summa=[0,0,0,0]
    kol_kar={'Валет':10,'Дама':10,'Король':10,'Туз':11}
    k='k'
    keys=['Валет','Дама','Король','Туз']
    
    koloda = [2,3,4,6,7,8,9,10,k,k,k,k]*4
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
            for i in range(0,2):
                fun_pool(name,summa,karta,number_pool,i)
                number_pool[i]+=1
            fun_rez(name,summa,karta)
            print("Далее : ")
            for i in range(0,2):
                fun_pool(name,summa,karta,number_pool,i)
                number_pool[i]+=1
            fun_rez(name,summa,karta)
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
                koloda = [2,3,4,6,7,8,9,10,k,k,k,k]*4
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
                fun_pool(name,summa,karta,number_pool,i)
                number_pool[i]+=1
            fun_rez(name,summa,karta)
            print("Далее : ")
            for i in range (0,2):    
                fun_pool(name,summa,karta,number_pool,i)
                number_pool[i]+=1
            fun_rez(name,summa,karta)
            
            while flag_de!=1:
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
                        fun_pool(name,summa,karta,number_pool,i)
                        number_pool[i]+=1
                        fun_rez(name,summa,karta)
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
                
                
            for i in range(0,len(name)):
                print("У игрока ",name[i]," банк составляет : ",bank[i])

            if bank[0]<=0:
                print("у игрока ",name[0]," закончились деньги !!! конец игре!!")
                break
            if bank[1]<=0:
                print("у игрока ",name[1]," закончились деньги !!! конец игре!!")
                break




            flag_de=0
            flag_id=[0,0,0,0]
            print("Играть еше? 1-да 2-нет")
            if fun_proverki(1,2)==1:
                koloda = [2,3,4,6,7,8,9,10,11]*4
                for i in range(0,kol_gamers):
                    summa[i]=0
                    karta[i]=[]
                    number_pool[i]=0
                continue
            else:
                break
    








    
def fun_accaunt(game_type,kol_gamers,name,bank):  #Создание акаунта игроков
    name[0]=(input("Введите ваше имя! "))
    print("Введите ваш начальный банк для игрока ",name[0]," от 50 до 1000$ ")
    bank[0]=(fun_proverki(50,1000))
    if game_type==2: #для вдух игроков
        for i in range(1,kol_gamers):
            
            name[i]=(input("Введите имя второго игрока "))
            print("Введите ваш начальный банк для игрока ",name[i]," от 50 до 1000$ ")
            bank[i]=(fun_proverki(50,1000))
            if kol_gamers>2:
                name.append('')
                bank.append(0)
            
print("Игра блэкджек!!!!")
print("Правила игры : ")
print("Нужно набрать 21 очков с помошью карт ")
print("Карты ранжированы следущим образом : ")
print("2-10 соответсвтуют таким же количествам ")
print("валет,дама,король -10 очков , туз либо 1 либо 11 очков на выбор")
print("Изначально сдаеться две карта каждому игроку ")
print("каждый ход каждый игрок выбирает брать ли еше карту ")
print("Если будет перебор игрок проиграет если недобор победит тот у ково будет ближайшее число к 21")
global name
name=['','']
global bank
bank=[0,0]




while True:
    system('cls')
    print("\n Для выбора режима игры введите : \n 1- игра одному \n 2- игра с другими игроками \n 0-выход\n ")
    game_type=fun_proverki(0,3)

    
    if game_type==0:
        break
    if game_type==1:
        system('cls')
        
        print("Игра проив Дилера!")
        fun_accaunt(1,1,name,bank)
        fun_igra(1,1,name,bank)
    if game_type==2:
        system('cls')
        print("Игра с другими игроками : ")
        print("Введите количество игроков от 2 до 4 ")
        kol_gamers=fun_proverki(2,4)
        fun_accaunt(2,kol_gamers,name,bank)
        fun_igra(2,kol_gamers,name,bank)
    
        
#правила игры блэк джек
#Достоинство карт
#Карты от двойки до десятки имеют достоинство, совпадающее с их номиналом. Достоинство валета, дамы и короля равно десяти очкам. Туз может давать одно или одиннадцать очков. Этот выбор делается в пользу игрока.
#
#Например, если на боксе туз и четверка, объявляется, что у игрока пять или пятнадцать очков. Если ему придет шестерка, он получит двадцать одно очко (в некоторых казино в такой ситуации игра автоматически переходит на следующий бокс, а в некоторых объявляется одиннадцать или двадцать одно и игрок сам делает выбор, брать ли еще карту). Однако, если он получит семерку, будет считаться, что у него двенадцать очков, но не двадцать два.#
#
#Количество игроков
#Количество игроков ограничивается количеством боксов (полей для ставок) на игровом столе. В традиционном варианте их семь. Однако это не означает, что игроки могут делать совместные ставки на один бокс. Главное, чтобы их сумма не превышала максимальный размер ставок, разрешенный для этого стола.#
#Количество ставок
#Во многих казино запрещено играть на один бокс, поэтому игрок должен делать не менее двух ставок. Максимальное количество ставок для одного игрока определяется каждым казино, однако обычно оно ограничивается лишь количеством боксов на столе.
#Ход игры
#Дилер тщательно перемешивает все колоды, отделяет часть карт (от пятой до третьей) с помощью специальной пластиковой карты и вставляет их все в «башмак». В процессе игры он достает из него карты по одной и раздает их игрокам и себе. Вышедшие из игры карты помещаются в специальный отбойник и находятся там, пока из «башмака» не выйдет пластиковая карта. Раздача, в течение которой это произошло, объявляется последней и по ее окончанию все карты снова перемешиваются.
#Подготовив карты к игре, дилер предлагает игрокам сделать ставки, после чего прекращает их прием и начинает раздавать карты. В базовом варианте игры он раздает всем игрокам и себе по две карты Одну из своих карт он открывает. В нашей стране получил распространение вариант правил, по которым дилер раздает себе лишь одну открытую карту, а остальные набирает себе после всех игроков. 
#Если на каком-то боксе образуется блэкджек, а открытая карта дилера исключает возможность такой же комбинации у него (то есть, это карта от двойки до девятки), он сразу оплачивает блэкджек и забирает карты в отбойник. Если у дилера открыт туз или карта достоинством в десять очков, блэкджек не оплачивается до тех пор, пока не придет время сравнивать комбинации. Если у крупье открыт туз, по правилам некоторых казино он предлагает игроку, у которого блэкджек, так называемые «равные деньги». Это означает, что он сразу оплачивает блэкджек 1:1 и забирает карты.
#Игроки, оценивая силу своих карт и принимая во внимание достоинство открытой карты крупье, принимают решение, брать ли еще карту или останавливаться на той сумме очков, которая уже есть на боксе. На бокс можно набирать любое количество карт при условии, что сумма очков не превышает двадцати одного. 
#Набор карт происходит строго по очереди. Первый бокс находится по левую руку от дилера. После того, как на всех боксах было принято окончательное решение, дилер вскрывает свою вторую карту, при необходимости добирает карты и сравнивает полученную комбинацию с картами игроков. Дилер берет себе карты строго в соответствии с правилами: он обязан брать еще карту, если у него шестнадцать или меньше очков и останавливаться, если у него семнадцать и больше очков.
#Игрок не имеет права касаться своих карт, все операции с ними производит дилер.
#Выигравшие боксы оплачиваются 1:1, блэкджек оплачивается 3:2 (в некоторых казино блэкджек из карт одной масти оплачивается 2:1).
#
#
#Дополнительные правила#
#
#На своих боксах игроку разрешается не только брать карты, но также пользоваться дополнительными возможностями.
#Сплит (Split) – имея на боксе две карты одного номинала (в некоторых казино даже одного достоинства, то есть, дама и король), игрок может разделить их на два бокса, поставив еще одну ставку того же размера. После этого будет производиться дополнительный набор карт на каждый из новых боксов. Если на один из новых боксов придет карта того же номинала, сплит можно сделать еще раз. Количество возможных сплитов с одного бокса варьируется, но обычно не превышает трех. При сплите тузов, как правило, раздается лишь одна карта, после чего игра переходит на следующий бокс. Если вновь приходит туз, можно сделать еще сплит. Туз и любая карта в десять очков полученные в результате сплита, не считаются блэкджеком и рассматриваются как двадцать одно очко (это означает, что они проиграют, если блэкджек будет у крупье).#
#
#Дабл (Double) – получив первые две карты, игрок имеет право сделать дабл. Для этого он должен удвоить свою первоначальную ставку. После этого ему раздается еще одна карта на этот бокс и дилер переходит к следующему игроку или открывает свои карты.#
#
#Трипл (Triple) – это правило действует далеко не во всех казино и позволяет игроку сделать после дабла на боксе еще одну ставку, равную первоначальной и получить дополнительную карту.
#
#Сарренда (Surrender) – получив первые две карты, игрок имеет право отказаться от продолжения игры на этом боксе, отдав половину первоначальной ставки. Следует отметить, что это правило почти во всех казино не действует, если у дилера открыт туз. Более того, оно нередко отменяется, если у дилера открыта карта достоинством в десять очков.#
#
#Страховка (Insurance) – если у дилера открыт туз, он предлагает игрокам застраховаться от блэкджека. Размер страховки равен половине первоначальной ставки и она оплачивается в размере 2:1, если у дилера будет блэкджек.#
