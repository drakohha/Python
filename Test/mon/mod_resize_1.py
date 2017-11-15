from configure import *
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
    frame_5["width"]=tek.model_razmer_x*5
    frame_5["height"]=tek.model_razmer_y*2
    frame_6["width"]=tek.model_razmer_x*5
    frame_6["height"]=tek.model_razmer_y*2
    but_5["width"]=tek.model_razmer_x*5
    but_5["height"]=tek.model_razmer_y*2
    but_6["width"]=tek.model_razmer_x*5
    but_6["height"]=tek.model_razmer_y*2
    text_1["width"]=tek.model_razmer_x*12
    text_1["height"]=tek.model_razmer_y*8
    lbox_1["width"]=tek.model_razmer_x*10
    lbox_1["height"]=tek.model_razmer_y*6
