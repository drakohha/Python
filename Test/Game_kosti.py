from random import *
import os
def fun_proverki(i,j):  #функция проверки ввода в заданном диапозоне
    while True:
        try:
            n=int(input())
            if n>=i and n<=j:
                break
            else:
                print("Не верный ввод, введите число в диапозоне от ",i," до ",j)
        except ValueError:
            print("Не верный ввод, введите число в диапозоне от ",i," до ",j)
    return n

def fun_igra(game_type):  # функция игры
    while True:  # Выбор начальных пораметров
     
            if game_type==1 :
                name=input("Введите ваще имя ")
                name_2="компьютер"
            elif game_type==3:
                name=input("Введите ваще имя ")
                name_2=name+' вторая рука'
            elif game_type==2:
                name=input("Введите ваще имя ")
                name_2=input("Введите имя второго игрока")
            print("Введите начальный банк от 100 до 1000$ : ")
            bank=fun_proverki(100,1000)
            if game_type==2:
                bank_2=bank
            print("Введите  ставку для игрока ",name," от 100 до 500$ : ")
            stavka=fun_proverki(100,500)
            os.system('clear')
            print ("Правила просты : выбрости кости суммой больше чем соперник! Вперед!")
            while True: # Бросок костей и их сравнивание
                print("Введите цифру 1 чтобы бросить кости!")
                brosok=fun_proverki(1,1)
                if brosok==1:
                    kubik_1=randint(1,6)
                    print("первоя кость прокатилась по столу и выдала : ",kubik_1)
                    kubik_2=randint(1,6)
                    print("Вторая кость перевернулась и показала :",kubik_2)
                    summa=kubik_1+kubik_2
                    print("Общая сумма у ",name, " получилась :",summa)
                    print("Теперь очередь Соперника !")
                    kubik_3=randint(1,6)
                    print("первоя кость прокатилась по столу и выдала : ",kubik_3)
                    kubik_4=randint(1,6)
                    print("Вторая кость перевернулась и показала :",kubik_4)
                    summa_2=kubik_3+kubik_4
                    print("Общая сумма у ",name_2," получилась :",summa_2)
                    if summa>summa_2: # Если игрок выигрывает
                        bank=bank+stavka
                        print("Вы выйграли! банк ",name," составляет : ",bank)
                        if game_type==2:
                            bank_2=bank_2-stavka
                            print("у вашего противника ",name_2," банк составляет :",bank_2)
                        print("Продолжить такую рискованую игру или остановиться?")
                        print("1- продолжить! 2- закончить! 3-изменить ставку")
                        flag_igru=fun_proverki(1,3)
                        os.system('clear')
                        if(flag_igru==1):  # Продолжить ли игру!
                            continue
                        elif flag_igru==3:  #Изменить ставку
                            print("Введите новую ставку : ")
                            stavka=fun_proverki(100,500)
                        else:
                            break
                    elif summa==summa_2:
                        print("Ничья ! Вы остались при своих")
                        print("Продолжить такую рискованую игру или остановиться?")
                        print("1- продолжить! 2- закончить! 3-изменить ставку")
                        flag_igru=fun_proverki(1,3)
                        os.system('clear')
                        if(flag_igru==1):  # Продолжить ли игру!
                            continue
                        elif flag_igru==3:#Изменить ставку
                            print("Введите новую ставку : ")
                            stavka=fun_proverki(100,500)
                        else:
                            break
                        
                    else:  #Если игрок проигрывет!
                        bank=bank-stavka
                        print("Вы проиграли!  банк ",name," составляет : ", bank)
                        if game_type==2:
                            bank_2=bank_2+stavka
                            print("у вашего противника ",name_2," банк составляет :",bank_2)
                        
                        if bank<0:  #Если кончилься банк
                            print("У ",name," не осталось денег , игра закончена")
                            break
                        if game_type==2:
                            if bank_2<0: #Если кончилься банк
                                print("У ",name_2," не осталось денег , игра закончена")
                                break
                        else:  # Продолжить ли игру
                            print("Продолжить такую рискованую игру или остановиться?")
                        print("1- продолжить! 2- закончить! 3-изменить ставку")
                        flag_igru=fun_proverki(1,3)
                        os.system('clear')
                        if(flag_igru==1):  # Продолжить ли игру!
                            continue
                        elif flag_igru==3:#Изменить ставку
                            print("Введите новую ставку : ")
                            stavka=fun_proverki(100,500)
                        else:
                            break
            break
    

i=0
j=0
game_type=0
print("Добро пожаловать в игру кости ! \n")         
while True:   #цикл начала игры и ее повторения до выхода из игры
    print("Выберите тип игры : \n 1-игра против компьютера   \n 2- игра против другова игрока \n 3- игра сам с сабой О_о\n 0- выход из игры ")
    game_type=fun_proverki(0,3)
    if game_type==0: #Выход из игры
        break
    if game_type==1: # Игра против компьютера
       os.system('clear')
       print("Игра против компьютера")
       fun_igra(1)
    if game_type==2: # Игра против другого игрока
        os.system('clear')
        print('Игра против другово игрока!')
        fun_igra(2)
    if game_type==3: # Игра сам с сабой О_о
        os.system('clear')
        print("Игра сам с сабой О_о ")
        fun_igra(3)
