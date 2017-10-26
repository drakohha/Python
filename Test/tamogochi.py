from os import *
from random import *

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

class Critter():
    rabota=0
    sutost=5
    nastroenie=3
    flag_hinsi=1
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return self.name
    def kormlenie(self,x):
        self.sutost+=x
    def radost(self,x):
        self.nastroenie+=x
    def pahat(self,x):
        self.rabota+=x
    def __call__(self):
        #print(self.name)
        if self.sutost<=10 and self.sutost>0:
            print("Животинка очень голодная срочно покормите!!")
        elif self.sutost<=0:
            print("Животинка умерла от голода!!")
            self.flag_hinsi=0







def fun_vzaim(criter,tek):
    flag_de=10
    while True:
        print("Меню взаимодействия : 1-кормить 2- поднять настроение 3-послать животинку работать 0-выйти")
        print("Текущий результат : ")
        print("Имя животинки = ",criter[tek].name)
        print("Уровень сытости = ",criter[tek].sutost)
        criter[tek]()
        print("Уровень настроения = ",criter[tek].nastroenie)
        if criter[tek].nastroenie<=10 and criter[tek].nastroenie>0:
            print("Животинка не в настроении... работать будет плохо !")
        elif criter[tek].nastroenie<=0:
            print("Животнка была в сильной дипресии и самоубилась ")
            print("Конец игры!")
            break
        
        flag_de=fun_proverki(0,3)
        if flag_de==1:
            criter[tek].kormlenie(5)
        elif flag_de==2:
            criter[tek].radost(1)
        elif flag_de==0:
            break
        elif flag_de==3:
            criter[tek].kormlenie(-4)
            criter[tek].radost(-1)
            criter[tek].pahat(5)
        if criter[tek].rabota>=30:
            print("Животинка закончила за вас всю работу!!!")
            print("Вы победили!!")
            break

def fun_igra():
    print("Вы начали новую игру!!")
    index=0
    flag_menu=10
    global criter
    criter=[]
    while True:
        print("Выберете действие : ")
        print("1- Родить новую животного")
        print("2-Выбрать текущию животного")
        print("3-Взаимодействовать с текущей животным")
        flag_menu=fun_proverki(0,3)
        if flag_menu==1:
            print("Введите имя животного")
            criter.append(0)
            criter[index]=Critter(input())
            index+=1
        elif flag_menu==0:
            break
        elif flag_menu==2:
            print("Выберите одного из доступных животных : (0-4)")
            print("доступны :" , criter[0].name)
            tek=fun_proverki(0,4)
            
        elif flag_menu==3:
            print("Модуль взаимодействия с выбраной животинкой")
            fun_vzaim(criter,tek)
    
        
    

#main
print("Игра тамагочи!!! Жри! Воруй! Уибавай!....")
print("В смысле расти животинку и заботься о его нуждах!")

while True:
    print("Меню действий")
    print("1- начать игру \n 2- выход")
    flag_menu=fun_proverki(1,2)
    if flag_menu==1:
        fun_igra()
        
    else:
        break
