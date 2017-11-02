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

class Critter():   #класс питомца
    rabota=0
    sutost=5
    nastroenie=3
    flag_hinsi=1
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return self.name
    def kormlenie(self,x):  #функция кормления
        self.sutost+=x
    def radost(self,x):   #функция поднятия настроения
        self.nastroenie+=x
    def pahat(self,x):   #функция работы питомца от настроения
        if self.nastroenie<=10:
            self.rabota+=x-3
            self.kormlenie(-6)
            self.radost(-1)
        elif self.nastroenie >10:
            self.rabota+=x
            self.kormlenie(-3)
            self.radost(-1)
            
            
    def __call__(self):   #функция будет отвечать за состояние питомца
        #print(self.name)
        if self.sutost<=10 and self.sutost>0:
            print("Животинка очень голодная срочно покормите!!")
        elif self.sutost<=0:
            print("Животинка умерла от голода!!")
            self.flag_hinsi=0
        if self.nastroenie<=10 and self.nastroenie>0:
            print("Животинка не в настроении... работать будет плохо !")
        elif self.nastroenie<=0:
            print("Животнка была в сильной дипресии и самоубилась ")
            self.flag_hinsi=0







def fun_vzaim(criter,tek):   #функция игры (создание выбор животинки)
    flag_de=10
    while True:
        system('clr') 
        print("Меню взаимодействия : 1-кормить 2- поднять настроение 3-послать животинку работать 0-выйти")
        print("0- выход")
        print("Текущий результат : ")
        print("Имя животинки = ",criter[tek].name)
        print("Уровень сытости = ",criter[tek].sutost)
        print("Уровень настроения = ",criter[tek].nastroenie)
        print("Сделаная работа = ",criter[tek].rabota ,"%")
        criter[tek]()
        if criter[tek].flag_hinsi==0:
            print("Конец игры!")
            #criter.pop(tek)
            break
        
        flag_de=fun_proverki(0,3)
        if flag_de==1:
            criter[tek].kormlenie(5)
        elif flag_de==2:
            criter[tek].radost(1)
        elif flag_de==0:
            break
        elif flag_de==3:
            criter[tek].pahat(5)
        if criter[tek].rabota>=100:
            print("Животинка закончила за вас всю работу!!!")
            print("Вы победили!!")
            break

def fun_igra():  #функция работы с питомцем 
    print("Вы начали новую игру!!")
    index=0
    flag_menu=10
    global criter
    criter=[]
    while True:   #проверка на наличие сдохшей животинки
        if index>0:
            if criter[index-1].flag_hinsi==0:
                criter.pop(index-1)
                index-=1
        system('clr')        
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
            for i in range(0,index):
                print("доступны :" , criter[i].name, " под номером : ",i)
            if index >0:
                tek=fun_proverki(0,index)
            else :
                print("Нету созданых животинок")
            
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
