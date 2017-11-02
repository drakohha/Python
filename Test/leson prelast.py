from tkinter import *
fr_razmer_1=5
fr_razmer_2=5
root=Tk()
def printer(event):
    print("Будущая инфо")
def razmer(event):
    root.geometry("150x150")
def razmer_2(event):
    root.geometry("250x250")
def razmer_3(event):
    root.geometry("350x350")
def razmerf_1(event):
    fr_razmer_1=text_1.get()
    frame_3["width"]=fr_razmer_1
     
   
def razmerf_2(event):
    fr_razmer_2=text_2.get()
    frame_3["height"]=fr_razmer_2
#root.minsize(width=500,height=500)
#root.maxsize(width=500,height=500)
root.geometry("1000x500")
root.title("Новое окошко")

frame_1=Frame(root,width=50,height=50,bg="light blue",bd=10)
frame_1.grid(row=0,column=0)
frame_2=Frame(root,width=100,height=100,bg="red",bd=10)
frame_2.grid(row=0,column=1)
bt_1=Button(frame_1)
bt_1["text"]="размер 1"
bt_1.font="arial 18"
bt_1["bg"]="light blue"
bt_1.bind("<Button-1>",razmer)
bt_1.grid(sticky = 'w')
bt_2=Button(frame_1)
bt_2["text"]="размер 2"
bt_2.font="arial 18"
bt_2["bg"]="light blue"
bt_2.bind("<Button-1>",razmer_2)
bt_2.grid(row=0,column=1)
bt_3=Button(frame_1)
bt_3["text"]="размер 3"
bt_3.font="arial 18"
bt_3["bg"]="light blue"
bt_3.bind("<Button-1>",razmer_3)
bt_3.grid(row=0,column=2)
text_1=Entry(frame_2,width=20,font="arial 8")
text_1.grid(row=0,column=0,sticky = 'w')
text_2=Entry(frame_2,width=20,font="arial 8")
text_2.grid(row=1,column=0,sticky = 'w')
frame_3=Frame(root,width=100,height=100,bg="blue",bd=10)
frame_3.grid(row=0,column=2)

text_1.bind('<Return>',razmerf_1)
text_2.bind('<Return>',razmerf_2)
root.mainloop()
