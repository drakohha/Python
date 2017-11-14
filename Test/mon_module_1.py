from tkinter import *
from mon_class_1 import *
global kol_player
global index
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
def next_enter(event):
    buffer=text_3.get('1.0', END)
    human[0].name=buffer
    text_3.delete('1.0', END)
    but_10.destroy()
def next_enter_2(event):
    buffer=text_3.get('1.0', END)
    human[1].name=buffer
    text_3.delete('1.0', END)
    win.destroy()
    
    
def clear():
    # Удаление предыдущего окна, чтобы окна не наслаивались одно на другое
    if win.winfo_children():
        win.winfo_children()[0].destroy()
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
    text_2=Text(frame_10,font="Verdana 12",wrap=WORD,width=20,height=10,)
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



class Zamer_gr():
    model_razmer_x=0
    model_razmer_y=0
    def __init__(self,model_razmer_x=None,model_razmer_y=None):
        self.model_razmer_x=model_razmer_x
        self.model_razmer_y=model_razmer_y
    #def __str__(self):
       # return(self.model_razmer_x,self.model_razmer_y)
    def razmer_gr_x(self,x):
        self.model_razmer_x=x
    def razmer_gr_y(self,y):
        self.model_razmer_y=y    


class Player():
    def __init__(self,name=None,money=None,bordplase=None,koloda=None):
        self.name=name
        self.money=money
        self.bordplase=bordplase
        self.koloda=koloda
    def __str__(self):
        return(self.name)
class Hod():
    def __init__(self,player_name=None,case=None):
        self.player_name=player_name
        self.case=case
    def case_1(self,x):
        self.case=x
        if self.case==1:
            text_1.delete('1.0', END)
            text_1.insert(1.0,'Текущий ход \n выбирете действие : \n' )
            text_1.insert(3.0,'1 ')
            text_1.insert(3.1,' бросить кубики \n')
            text_1.insert(4.0,'2 ')
            text_1.insert(4.1,' Торговать с другими игроками \n')
            list_1=["1-бросить кубики","2-торговать"]
            for i in list_1:
                lbox_1.insert(END,i)



def game_hod(event):
    pool=Hod()
    pool.name=human[0]
    pool.case_1(1)
    
def razmer_t(event):
    
    
    if frame_0["width"]<=500:
        tek.razmer_gr_x(1)
    elif frame_0["width"]>500 and frame_0["width"]<=1000:
        tek.razmer_gr_x(2)
    elif frame_0["width"]>1000:
        tek.razmer_gr_x(3)
    if frame_0["height"]<=500:
        tek.razmer_gr_y(1)
    elif frame_0["height"]>500 and frame_0["height"]<=1000:
        tek.razmer_gr_y(2)
    elif frame_0["height"]>1000:
        tek.razmer_gr_y(3)
    #print(tek.model_razmer_x,tek.model_razmer_y) 
    element_razmer(tek)

def ReSize(event):
    razmer_x=''
    razmer_y=''
    flag=0
   # print(root.geometry())
   # print(type(root.geometry()))
    for i in range(0,len(root.geometry())):
        if root.geometry()[i]!='x' and flag!=1:
            razmer_x+=root.geometry()[i]
        else:
            flag=1
        if flag==1:
            if root.geometry()[i]!='x' and root.geometry()[i]!='+':
                razmer_y+=root.geometry()[i]
            elif root.geometry()[i]=='+':
                break
    #print(razmer_x,razmer_y)
    if tek.model_razmer_x!=1 and int(razmer_x)<=500:
        
        frame_0["width"]=razmer_x
    elif tek.model_razmer_x!=2 and int(razmer_x)>500 and int(razmer_x)<=1000:
        frame_0["width"]=razmer_x
    elif tek.model_razmer_x!=3 and int(razmer_x)>1000 :
        frame_0["width"]=razmer_x
    if tek.model_razmer_y!=1 and int(razmer_y)<=500:
        frame_0["height"]=razmer_y
    elif tek.model_razmer_y!=2 and int(razmer_y)>500 and int(razmer_y)<=1000:
        frame_0["height"]=razmer_y
    elif tek.model_razmer_y!=3 and int(razmer_y)>1000 :
        frame_0["height"]=razmer_y
    
        


    
    

def element_razmer(tek):
    for i in range(0,11):
        frame[i]["width"]=tek.model_razmer_x*5
        frame[i]["height"]=tek.model_razmer_y*2
        but[i]["width"]=tek.model_razmer_x*5
        but[i]["height"]=tek.model_razmer_y*2
        
    for i in range(0,10):
        frame_2[i]["width"]=tek.model_razmer_x*5
        frame_2[i]["height"]=tek.model_razmer_y*2
        but_2[i]["width"]=tek.model_razmer_x*5
        but_2[i]["height"]=tek.model_razmer_y*2
    for i in range(0,10):
        frame_3[i]["width"]=tek.model_razmer_x*5
        frame_3[i]["height"]=tek.model_razmer_y*2
        but_3[i]["width"]=tek.model_razmer_x*5
        but_3[i]["height"]=tek.model_razmer_y*2
    for i in range(0,9):
        frame_4[i]["width"]=tek.model_razmer_x*5
        frame_4[i]["height"]=tek.model_razmer_y*2
        but_4[i]["width"]=tek.model_razmer_x*5
        but_4[i]["height"]=tek.model_razmer_y*2
    frame_5["width"]=tek.model_razmer_x*8
    frame_5["height"]=tek.model_razmer_y*2
    frame_6["width"]=tek.model_razmer_x*8
    frame_6["height"]=tek.model_razmer_y*2
    but_5["width"]=tek.model_razmer_x*8
    but_5["height"]=tek.model_razmer_y*2
    but_6["width"]=tek.model_razmer_x*8
    but_6["height"]=tek.model_razmer_y*2
    text_1["width"]=tek.model_razmer_x*7
    text_1["height"]=tek.model_razmer_y*7
    lbox_1["width"]=tek.model_razmer_x*5
    lbox_1["height"]=tek.model_razmer_y*4

root=Tk()


MB = Menu(root)
MN = Menu(MB)
MN.add_command(label=u"Выбор игроков", command=gotomenu1)
MN.add_command(label=u"Второе окно", command=gotomenu2)
MB.add_cascade(label=u"Меню", menu=MN)
root.config(menu=MB)


root.focus_force()




tek=Zamer_gr()
tek.razmer_gr_x(1)
tek.razmer_gr_y(1)
root["width"]=500
root["height"]=500

root.title('Монополия')

frame_0=Frame(root,bg='green',bd=5,width=500,height=500)
frame_0.grid(row=0,column=0)


root.bind('<Configure>',ReSize)
frame_0.bind('<Configure>',razmer_t)
frame=[]
but=[]
for i in range(0,11):
    frame.append(0)
    but.append(0)
    frame[i]=Frame(frame_0,bg='black',bd=2,width=tek.model_razmer_x*2,height=tek.model_razmer_y*2)
    but[i]=Button(frame[i],bg='red',font='arial 8',width=tek.model_razmer_x*2,height=tek.model_razmer_y*2)
    frame[i].grid(row=i,column=0)
    but[i].grid(row=i,column=0)
frame_2=[]
but_2=[]
for i in range(0,10):
    frame_2.append(0)
    but_2.append(0)
    frame_2[i]=Frame(frame_0,bg='black',bd=2,width=tek.model_razmer_x*2,height=tek.model_razmer_y*2)
    but_2[i]=Button(frame_2[i],bg='red',font='arial 8',width=tek.model_razmer_x*2,height=tek.model_razmer_y*2)
    frame_2[i].grid(row=0,column=i+1)
    but_2[i].grid(row=0,column=i+1)
    
frame_3=[]
but_3=[]
for i in range(0,10):
    frame_3.append(0)
    but_3.append(0)
    frame_3[i]=Frame(frame_0,bg='black',bd=2,width=tek.model_razmer_x*2,height=tek.model_razmer_y*2)
    but_3[i]=Button(frame_3[i],bg='red',font='arial 8',width=tek.model_razmer_x*2,height=tek.model_razmer_y*2)
    frame_3[i].grid(row=i+1,column=10)
    but_3[i].grid(row=i+1,column=10)
    
frame_4=[]
but_4=[]
for i in range(0,9):
    frame_4.append(0)
    but_4.append(0)
    frame_4[i]=Frame(frame_0,bg='black',bd=2,width=tek.model_razmer_x*2,height=tek.model_razmer_y*2)
    but_4[i]=Button(frame_4[i],bg='red',font='arial 8',width=tek.model_razmer_x*2,height=tek.model_razmer_y*2)
    frame_4[i].grid(row=10,column=i+1)
    but_4[i].grid(row=10,column=i+1)




frame_5=Frame(frame_0,bg='black',bd=2,width=tek.model_razmer_x*4,height=tek.model_razmer_y*2)
but_5=Button(frame_5,bg='red',font='arial 8',width=tek.model_razmer_x*4,height=tek.model_razmer_y*2)
but_5["text"]="Карта"
frame_5.grid(row=3, column=3, columnspan=2)
but_5.grid(row=3,column=3, columnspan=2)

frame_6=Frame(frame_0,bg='black',bd=2,width=tek.model_razmer_x*4,height=tek.model_razmer_y*2)
but_6=Button(frame_6,bg='red',font='arial 12',width=tek.model_razmer_x*4,height=tek.model_razmer_y*2)
but_6["text"]="Ход"
frame_6.grid(row=6, column=6,columnspan=2)
but_6.grid(row=6,column=6,columnspan=2)



text_1=Text(frame_0,font="Verdana 12",wrap=WORD,width=tek.model_razmer_x*7,height=tek.model_razmer_y*7)
text_1.grid(row=3,column=4,columnspan=3,rowspan=3)

lbox_1=Listbox(frame_0,height=tek.model_razmer_y*4,width=tek.model_razmer_x*2,selectmode =SINGLE)
lbox_1.grid(row=3,column=7,rowspan=3)

#but_7=Button(frame[0],bg='blue',font='arial 2',width=tek.model_razmer_x,height=tek.model_razmer_y)
#but_7.grid(row=0,column=0)
#but_8=Button(frame[0],bg='light blue',font='arial 2',width=tek.model_razmer_x,height=tek.model_razmer_y*2)
#but_8.grid(row=0,column=0)





#main

text_1.insert(1.0,'Игра монополия!!!! \n')
text_1.insert(2.0,'Для начала игры нажмите кнопку ход')

but_6.bind("<Button-1>",game_hod)

root.mainloop()
