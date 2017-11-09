from tkinter import *



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
    print(tek.model_razmer_x,tek.model_razmer_y) 
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

root=Tk()

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




frame_5=Frame(frame_0,bg='black',bd=2,width=tek.model_razmer_x*2,height=tek.model_razmer_y*2)
but_5=Button(frame_5,bg='red',font='arial 8',width=tek.model_razmer_x*2,height=tek.model_razmer_y*2)
frame_5.grid(row=3, column=3)
but_5.grid(row=3,column=3)

frame_6=Frame(frame_0,bg='black',bd=2,width=tek.model_razmer_x*2,height=tek.model_razmer_y*2)
but_6=Button(frame_6,bg='red',font='arial 8',width=tek.model_razmer_x*2,height=tek.model_razmer_y*2)
frame_6.grid(row=6, column=6)
but_6.grid(row=6,column=6)



root.mainloop()
