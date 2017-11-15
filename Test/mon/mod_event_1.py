from tkinter import *
from random import *
from configure import *
from mod_class_1 import *
from mod_win_1 import *
from mod_resize_1 import *

global kol_player
global index
global pl_index
global kubiki
global text_1
pl_index=0








class Hod():
    pl_index_2=0
    case_index=1
    case_index_2=1
    def __init__(self,player_name=None,case=None,pl_index_2=0,case_index=1):
        self.player_name=player_name
        self.case=case
        self.pl_index_2=pl_index_2
        self.case_index=case_index
    def case_1(self,x):
        self.case=x
        if self.case==1:
            #text_1.delete('1.0', END)
            #text_1.insert(1.0,'Текущий ход \n выбирете действие : \n' )
            #fun_print()
            text_1.insert(3.0,'1 ')
            text_1.insert(3.1,' бросить кубики \n')
            text_1.insert(4.0,'2 ')
            text_1.insert(4.1,' Торговать с другими игроками \n')
            list_1=["1-бросить кубики","2-торговать"]
            for i in list_1:
                lbox_1.insert(END,i)
        if self.case==2:
            #text_1.delete('1.0', END)
            #text_1.insert(1.0,'Текущий ход \n выбирете действие : \n' )
            text_1.insert(3.0,'1 ')
            text_1.insert(3.1,' бросить кубики \n')
            text_1.insert(4.0,'2 ')
            text_1.insert(4.1,' Торговать с другими игроками \n')
            text_1.insert(5.0,'2 ')
            text_1.insert(5.1,' Купить данную собственность \n')
            list_1=["1-бросить кубики","2-торговать","3-Купить"]
            for i in list_1:
                lbox_1.insert(END,i)
            
    def case_2(self,x):
        self.case=x
        if self.case==0:
            kubiki=randint(1,12)
            text_1.delete('1.0',END)
            text_1.insert(1.0,' вы бросили кубики на \n')
            text_1.insert(2.0,kubiki)
            human[pool.pl_index_2].bordplase+=kubiki
            if human[pool.pl_index_2].bordplase>40:
                human[pool.pl_index_2].bordplase-=40
            pool.case_3(human[pool.pl_index_2].bordplase)
        if self.case==2:
            print("вы чтото купили !!!")
            text_1.delete('1.0', END)
            lbox_1.delete(0,END)
            if pool.pl_index_2==0:
                pool.case_index=1
            elif pool.pl_index_2==1:
                pool.case_index_2=1
            pool.case_1(1)
    def case_3(self,x):
        self.case=x
        if self.case>=0 and self.case<=12:
            print("сроботоло событие...")
            lbox_1.delete(0,END)
            if pool.pl_index_2==0:
                pool.case_index=2
                pool.pl_index_2=1
            elif pool.pl_index_2==1:
                pool.case_index_2=2
                pool.pl_index_2=0
        if self.case>12:
            print("сроботоло событие...")
            lbox_1.delete(0,END)
            if pool.pl_index_2==0:
                pool.case_index=2
                pool.pl_index_2=1
            elif pool.pl_index_2==1:
                pool.case_index_2=2
                pool.pl_index_2=0



    
        
        
        
    





def game_hod(event):
    text_1.delete('1.0',END)
    pool.name=human[pool.pl_index_2].name
    text_1.insert(1.0,'ход игрока \n')
    text_1.insert(2.0,human[pool.pl_index_2].name)
    print(pool.case_index)
    if pool.pl_index_2==0:
        pool.case_1(pool.case_index)
    elif pool.pl_index_2==1:
        pool.case_1(pool.case_index_2)
       

def game_in(event):
    x= lbox_1.curselection()
    pool.case_2(int(x[0]))
  

def gotomenu1():
    u"""Построение кнопки первого меню"""
    #clear()
    global win
    global text_3
    global text_2
    win = Toplevel(root,relief=SUNKEN,bd=10,bg="lightblue")
    win.title("Выбор игроков")
    win.minsize(width=400,height=200)
    win.focus
    frame_10=Frame(win,width=20,height=10,bd=2)
    frame_10.grid(row=0,column=0)
    text_2=Text(frame_10,font="Verdana 12",wrap=WORD,width=20,height=10)
    text_2.grid(row=0,column=0,rowspan=2)
    text_2.insert(1.0,'Введите количество игроков')
    text_3=Text(frame_10,bd=2,width=10,font="Verdana 12",wrap=WORD,height=10)
    text_3.grid(row=0,column=1,pady=0)
    but_10=Button(frame_10,font='arial 8',text='Подтвердить',width=10,height=5)
    but_10.grid(row=1,column=1)
    win.focus_force()
    but_10.bind("<Button-1>",next_pass)
def gotomenu2():
    global win
    global text_3
    global text_2
    global index
    global but_10
    global but_11
    index=0
    u"""Построение кнопки второго меню"""
    #clear()
    win = Toplevel(root,relief=SUNKEN,bd=10,bg="lightblue")
    win.title("Выбор имени игроков")
    win.minsize(width=400,height=200)
    win.focus
    frame_10=Frame(win,width=20,height=10,bd=2)
    frame_10.grid(row=0,column=0)
    text_2=Text(frame_10,font="Verdana 12",wrap=WORD,width=20,height=10,)
    text_2.grid(row=0,column=0,rowspan=2)
    text_2.insert(1.0,'Введите имя первого игрока')
    text_3=Text(frame_10,bd=2,width=10,font="Verdana 12",wrap=WORD,height=10)
    text_3.grid(row=0,column=1,pady=0)
    but_10=Button(frame_10,font='arial 8',text='Подтвердить',width=10,height=5)
    but_10.grid(row=1,column=1)
    win.focus_force()
    but_10.bind("<Button-1>",next_enter)
    but_11=Button(frame_10,font='arial 8',text='Подтвердить',width=10,height=5)
    but_11.grid(row=2,column=1)
    but_11.bind("<Button-1>",next_enter_2)

def next_enter(event):
    buffer=text_3.get('1.0', END)
    human[0].name=buffer
    human[0].money=500
    human[0].bordplase=0
    human[0].koloda=['none']
    text_3.delete('1.0', END)
    text_2.delete('1.0',END)
    text_2.insert(1.0,'Введите имя второго игрока')
    but_10.destroy()
def next_enter_2(event):
    buffer=text_3.get('1.0', END)
    human[1].name=buffer
    human[1].money=500
    human[1].bordplase=0
    human[1].koloda=['none']
    text_3.delete('1.0', END)
    win.destroy()
    

def clear():
    # Удаление предыдущего окна, чтобы окна не наслаивались одно на другое
    if win.winfo_children():
        win.winfo_children()[0].destroy()

def tek_pos():
    global win
    win = Toplevel(root,relief=SUNKEN,bd=10,bg="lightblue")
    win.title("Текущий счет")
    win.minsize(width=400,height=200)
    win.focus
    frame_10=Frame(win,width=20,height=10,bd=2)
    frame_10.grid(row=0,column=0)
    text_ifo_1=Text(frame_10,font="Verdana 12",wrap=WORD,width=30,height=30)
    text_ifo_1.grid(row=0,column=0)
    text_ifo_1.insert(1.0,'Имя - ')
    text_ifo_1.insert(2.0,human[0].name)
    text_ifo_1.insert(3.0,'количество денег : ')
    text_ifo_1.insert(4.0,human[0].money)
    text_ifo_1.insert(5.0,'\nпозиция на доске : ')
    text_ifo_1.insert(6.0,human[0].bordplase)
    text_ifo_1.insert(7.0,'\nВ наличии карты : ')
    text_ifo_1.insert(8.0,human[0].koloda)
    text_ifo_2=Text(frame_10,font="Verdana 12",wrap=WORD,width=30,height=30)
    text_ifo_2.grid(row=0,column=2)
    text_ifo_2.insert(1.0,'Имя - ')
    text_ifo_2.insert(2.0,human[1].name)
    text_ifo_2.insert(3.0,'количество денег : ')
    text_ifo_2.insert(4.0,human[1].money)
    text_ifo_2.insert(5.0,'\nпозиция на доске : ')
    text_ifo_2.insert(6.0,human[1].bordplase)
    text_ifo_2.insert(7.0,'\nВ наличии карты : ')
    text_ifo_2.insert(8.0,human[1].koloda)


def next_pass(event):
    global human
    global kol_player
    human=[]
    win.focus_force()
    kol_player=text_3.get('1.0', END)
    
    for i in range(0,int(kol_player)):
        human.append(0)
        human[i]=Player()
    #print("Проверка работы евента")
    win.destroy()
    #clear()
    gotomenu2()  








root.bind('<Configure>',ReSize)
frame_0.bind('<Configure>',razmer_t)

but_6.bind("<Button-1>",game_hod)
but_7.bind("<Button-1>",game_in)

MN.add_command(label=u"Выбор игроков", command=gotomenu1)
MN.add_command(label=u"Второе окно", command=gotomenu2)
MN_2.add_command(label=u"Просмотр счета", command=tek_pos)


#main

pool=Hod()


root.mainloop()



