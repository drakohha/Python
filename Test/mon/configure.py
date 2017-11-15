from tkinter import *
from mod_class_1 import *


    




root=Tk()
tek=Zamer_gr()
tek.razmer_gr_x(1)
tek.razmer_gr_y(1)

MB = Menu(root)
MN = Menu(MB)
MN_2 = Menu(MB)

MB.add_cascade(label=u"Меню", menu=MN)
MB.add_cascade(label=u"Счет", menu=MN_2)
root.config(menu=MB)


root.focus_force()

root["width"]=500
root["height"]=500

root.title('Монополия')

frame_0=Frame(root,bg='green',bd=5,width=500,height=500)
frame_0.grid(row=0,column=0)



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


frame_5=Frame(frame_0,bg='black',bd=2,width=tek.model_razmer_x*2,height=tek.model_razmer_y*2)
but_5=Button(frame_5,bg='red',font='arial 8',width=tek.model_razmer_x*2,height=tek.model_razmer_y*2)
but_5["text"]="Карта"
frame_5.grid(row=3, column=3)
but_5.grid(row=3,column=3)

frame_6=Frame(frame_0,bg='black',bd=2,width=tek.model_razmer_x*2,height=tek.model_razmer_y*2)
but_6=Button(frame_6,bg='red',font='arial 12',width=tek.model_razmer_x*2,height=tek.model_razmer_y*2)
but_6["text"]="Ход"
frame_6.grid(row=6, column=6)
but_6.grid(row=6,column=6)



text_1=Text(frame_0,font="Verdana 12",wrap=WORD,width=tek.model_razmer_x*8,height=tek.model_razmer_y*8)
text_1.grid(row=3,column=4,columnspan=3,rowspan=3)

lbox_1=Listbox(frame_0,height=tek.model_razmer_y*6,width=tek.model_razmer_x*4,selectmode =SINGLE)
lbox_1.grid(row=3,column=7,rowspan=2,columnspan=2)

but_7=Button(frame_0,bg='red',font='arial 12',width=tek.model_razmer_x*10,height=tek.model_razmer_y*2)
but_7["text"]="подтвердить"
but_7.grid(row=5,column=7,columnspan=2)


