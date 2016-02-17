
from Tkinter import *
from string import *
from tkMessageBox import *
from time import sleep

def callback():
    if askokcancel("Quit","Do you really wish to quit?"):
        try:
            for i in h.find_withtag('all'):
                h.delete(i)
        except:
            for i in first.h.find_withtag('all'):
                first.h.delete(i)
        global wrong_quit
        wrong_quit=1
        root.quit()
        root.destroy()

def open_save():
    try:
        f = open("save.txt","r")
        jindu = f.readlines()
        for i in range(len(jindu)):
            jindu[i]=eval(jindu[i])
        f.close
    except:
        f = open("save.txt","w")
        for i in range(4):
            f.write("0\n")
        f.close
        f = open("save.txt","r")
        jindu = f.readlines()
        for i in range(len(jindu)):
            jindu[i]=eval(jindu[i])
        f.close
    return jindu

def open_levels(series,now):
    FangGe=[[(-1,1),(1,-1)],[(2,0),(-2,0),(0,2),(0,-2),(2,-2),(-2,2)],[(2,0),(0,0),(-2,-2),(-2,0),(0,2),(0,-2),(2,-2),(-2,2)],[(2,2),(0,0),(-2,-2),(0,2),(0,-2),(2,-2),(-2,2)],[(2,2),(2,0),(0,2),(0,-2),(-2,0),(-2,2)],[(-1,5),(-3,5),(-3,1),(-3,-1),(-3,-5),(1,-1),(3,-3),(1,-5)],[(2,2),(0,0),(-2,-2),(2,0),(2,4),(2,-4),(2,-2),(-2,2)],[(0,0),(2,2),(-2,0),(-2,-2),(0,-2)],[(0,0),(2,2),(-2,0),(2,0),(-2,2),(0,2),(0,-2),(2,-2),(-2,-2)],[(0,0),(2,0),(-2,0),(-2,2),(0,2),(2,-2),(-2,-2)],[(-3,4),(-1,4),(1,4),(3,4),(-3,2),(-1,2),(1,2),(3,2), (-3,0),(-1,0),(1,0),(3,0),(-3,-2),(-1,-2),(1,-2),(3,-2),(-3,-4),(-1,-4),(1,-4),(3,-4)],[(-3,3), (-1,3), (1,3), (3,3), (-3,1), (-1,1), (1,1), (3,1), (-3,-1), (-1,-1), (1,-1), (3,-1), (-3,-3), (-1,-3), (1,-3), (3,-3)],[(-3,2), (-1,2), (1,2), (3,2), (-3,0), (-1,0), (1,0), (3,0), (-3,-2), (-1,-2), (1,-2), (3,-2)],[(-3,2), (-1,2), (1,2), (3,2), (-3,0), (-1,0), (1,0), (3,0), (-3,-2), (-1,-2), (1,-2), (3,-2)],[(-2,4), (-2,2), (-2,0), (-2,-2), (-2,-4), (0,4), (0,2), (0,0), (0,-2), (0,-4), (2,4), (2,2), (2,0), (2,-2), (2,-4)],[(-3,4), (-1,4), (1,4), (3,4), (-3,2), (-1,2), (1,2), (-1,0), (1,0), (3,0), (-3,-2), (-1,-2), (1,-2), (3,-2), (-3,-4), (1,-4), (3,-4)],[(-3,4), (-1,4), (1,4), (3,4), (-1,2), (1,2), (3,2), (-1,0), (1,0), (-3,-2), (-1,-2), (1,-2), (3,-2), (-3,-4), (-1,-4), (3,-4)],[(-3,4), (-1,4), (1,4), (3,4), (-3,2), (-1,2), (1,2), (3,2), (-3,0), (-1,0), (1,0), (3,0), (-3,-2), (-1,-2), (1,-2), (3,-2), (-3,-4), (-1,-4), (1,-4), (3,-4)], [(-3,4), (-1,4), (1,4), (3,4), (-3,2), (-1,2), (1,2), (3,2), (-3,0), (-1,0), (1,0), (3,0), (-3,-2), (-1,-2), (1,-2), (3,-2), (-3,-4), (-1,-4), (1,-4), (3,-4)],[(-3,3), (-1,3), (1,3), (3,3), (-3,1), (-1,1), (1,1), (3,1), (-3,-1), (-1,-1), (1,-1), (3,-1), (-3,-3), (-1,-3), (1,-3), (3,-3)] ,[(-3,3),(-1,3),(1,3),(-3,1),(1,1),(3,1),(-3,-1),(1,-1),(-1,-3),(1,-3)],[(-2,2),(0,2),(2,2),(2,0),(2,-2),(0,-2),(-2,-2),(-2,0)],[(-3,4),(-1,4),(1,4),(-3,2),(-1,2),(1,2),(3,2),(-3,0),(-1,0),(1,0),(3,0),(-3,-2),(1,-2),(3,-2),(-1,-4),(1,-4),(3,-4)] ,[(-3,4),(-1,4),(1,4),(-3,2),(-1,2),(1,2),(3,2),(-1,0),(1,0),(3,0),(-3,-2),(-1,-2),(1,-2),(3,-2),(-3,-4),(-1,-4),(1,-4)],[(-1,5),(1,5),(3,5),(-3,3),(-1,3),(1,3),(3,3),(-3,1),(-1,1),(1,1),(3,1),(-3,-1),(-1,-1),(1,-1),(3,-1),(-3,-3),(-1,-3),(1,-3),(3,-3),(-3,-5),(-1,-5),(1,-5),(3,-5)],[(-3,5),(-1,5),(1,5),(3,5),(-3,3),(-1,3),(3,3),(-1,1),(3,1),(-3,-1),(-1,-1),(1,-1),(3,-1),(-3,-3),(-1,-3),(1,-3),(3,-3),(-3,-5),(-1,-5),(1,-5)],[(-3,4),(-1,4),(1,4),(3,4),(-3,2),(-1,2),(1,2),(3,2),(-3,0),(-1,0),(1,0),(3,0),(-3,-2),(-1,-2),(1,-2),(3,-2),(-3,-4),(-1,-4),(1,-4),(3,-4)],[(-3,5),(-1,5),(1,5),(-1,3),(1,3),(3,3),(-3,1),(-1,1),(1,1),(3,1),(-3,-1),(-1,-1),(3,-1),(-3,-3),(-1,-3),(1,-3),(3,-3),(-3,-5),(-1,-5),(3,-5)],[(-3,3),(-1,3),(1,3),(-3,-1),(-1,-1),(1,-1),(3,-1),(-3,-3),(1,-3),(3,-3),(-3,1),(-1,1),(1,1),(3,1)],[(-3,3),(-1,3),(1,3),(-3,1),(-1,1),(1,1),(3,1),(-3,-1),(-1,-1),(1,-1),(3,-1),(-3,-3),(-1,-3),(1,-3),(3,-3),(1,-5),(3,-5)],[(-1,-1),(-1,-3),(-3,-3),(-3,-1),(3,-3),(3,-1),(1,-1),(1,-3),(-3,3),(-3,1),(-1,3),(-1,1),(3,1),(1,3),(1,1),(3,3)],[(-1,-1),(-1,-3),(-3,-1),(3,-3),(3,-1),(1,-1),(1,-3),(-3,1),(-1,3),(-1,1),(1,1)] ,[(-1,-1),(-1,-3),(-3,-1),(-3,-3),(-3,-5),(-5,-1),(-5,-3),(-5,-5),(-1,1),(-3,1),(-3,3),(-5,1),(-5,3),(3,1),(3,3),(1,1),(1,3),(1,-1),(1,-3),(1,-5),(3,-1),(3,-3),(3,-5)],[(-1,-3),(-1,-5),(-3,-1),(-3,-3),(-1,3),(-1,1),(-1,5),(-3,1),(-3,3),(3,1),(3,3),(1,5),(1,-1),(1,-3),(1,-5),(3,-1),(3,-3)],[(-1,-3),(-1,-5),(-3,-3),(-1,3),(-1,1),(-3,1),(-3,5),(3,1),(3,5),(1,3),(1,5),(1,-1),(1,-5),(3,-1),(3,-3)],[(-1,-3),(-1,-5),(-3,-3),(-3,-1),(-1,3),(-1,1),(-3,1),(-3,3),(3,1),(3,5),(1,3),(1,5),(1,1),(1,-1),(1,-5),(1,-3),(3,-1),(3,-3),(3,-5)],[(-1,-1),(-1,-3),(-1,-5),(-3,-3),(-3,-5),(-1,5),(-1,3),(-1,1),(-3,1),(-3,3),(-3,5),(3,1),(3,3),(1,3),(1,5),(1,-1),(1,-3),(1,-5),(3,-1),(3,-3)],[(-1,-1),(-1,-3),(-1,-5),(-3,-1),(-3,-3),(-3,-5),(-1,3),(-1,1),(-3,1),(-3,3),(1,3),(1,1),(1,-1),(1,-3),(1,-5)],[(-1,-1),(-1,-3),(-1,-5),(-3,-1),(-3,-3),(-3,-5),(-5,-1),(-5,-3),(-1,3),(-1,1),(-3,1),(-3,3),(-5,1),(3,1),(1,1),(1,3),(1,-3),(1,-5),(3,-1),(3,-3)], [(-1,-1),(-1,-3),(-1,-5),(-3,-1),(-3,-3),(-3,-5),(-1,3),(-1,1),(-3,1),(-3,3),(3,1),(1,3),(1,-1),(1,-3),(1,-5),(3,-1),(3,-3),(3,-5)]]
    QiDian=[[[(-3,4),(1,-1)]],[[(-2,-3),(1,1)]],[[(2,3),(-1,-1)]],[[(-3,0),(1,-1)]],[[(-2,-3),(1,1,)]],[[(3,4),(-1,-1)]],[[(0,-5),(1,1)]],[[(-3,2),(1,-1)]],[[(3,-2),(-1,1)]],[[(0,-3),(-1,1)]],[[(-4,0),(1,-1)]],[[(1,4),(-1,-1)]],[[(-1,3),(1,-1)]],[[(3,3),(-1,-1)]],[[(1,4),(-1,-1)]],[[(-4,0),(1,-1)]],[[(-4,0),(1,-1)]] ,[[(-3,3),(1,-1)]],[[(-4,2),(1,-1)]],[[(-4,1),(1,-1)],[(3,2),(-1,-1)]],   [[(-3,-4),(1,1)]],[[(0,3),(1,-1)]],[[(-1,-1),(-1,-1)]],[[(-4,0),(1,-1)]],[[(-4,5),(1,-1)]],[[(1,0),(-1,1)]],[[(-4,4),(1,-1)]],[[(3,6),(-1,-1)]] ,  [[(0,-3),(-1,1)]], [[(0,-5),(-1,1)]],[[(4,-3),(-1,1)]],[[(4,-3),(-1,1)]],[[(-6,-1),(1,-1)]], [[(4,-5),(-1,1)]], [[(1,6),(1,-1)]], [[(0,3),(1,-1)]], [[(-2,5),(1,-1)]],[[(-1,-2),(1,1)]], [[(1,0),(-1,-1)]], [[(2,-1),(-1,1)]]]
    ZhongDian=[[(1,4)],[(-1,0)],[(0,-3)],[(3,0)],[(2,-3)],[(1,4)],[(0,1),(0,3),(0,5),(0,-1),(0,-3)],[(2,-3)],[(-3,0)],[(-3,0)],[(-1,1)],[(-1,0),(1,0),(-1,-2),(1,-2)],[(0,0), (0,2), (2,0), (-2,0), (0,-2)],[(0,0), (2,0), (-2,0)],[(0,5)], [(0,0), (0,2), (0,-2)],[(0,0), (0,2), (0,-2)],[(1,-1),(-4,2)],[(-2,2),(-2,-2),(2,0)],[(1,0),(4,-1),(-1,0),(-3,-2)] , [(0,-3)] ,[(-1,2)],[(-2,2)] ,[(-3,1),(-2,-2),(0,2),(1,-1)], [(4,-3)],[(-1,-4)],[(-1,-3)],[(-1,-2),(-1,-4)],[(-3,0),(2,1)],[(0,3),(2,-1)],[(-2,1),(0,-1),(-1,0),(1,-2)],[(-2,1),(0,-1),(-1,0),(1,-2)],[(-4,1),(2,-1)], [(-2,3)], [(1,-6)], [(0,-1),(2,-3)], [(-1,-4),(2,3)], [(-4,3),(-3,-6),(2,-5)], [(0,1),(-2,1)], [(-1,-3),(-3,-5)]]
    ZhuanKuai=[[[(1,-1),1]],[[(2,-2),1],[(-2,2),1]],[[(2,-2),1],[(-2,2),1]],[[(0,0),1],[(2,2),1],[(-2,-2),1]],[[(0,-2),1],[(2,2),1],[(-2,2),1]],[[(-1,5),1],[(-3,1),1],[(1,-1),1],[(-3,-5),1]],[[(0,0),1],[(2,2),1],[(-2,-2),1],[(2,-2),1],[(-2,2),1]],[[(0,0),2],[(0,-2),2]],[[(2,0),2],[(-2,-2),2],[(-2,2),2],[(0,2),1],[(0,-2),1]],[[(-2,-2),1],[(-2,2),1],[(2,2),1]],[[(-3,4),1], [(3,4),1], [(3,-4),1], [(-3,-4),1],[(-1,0),2]],[[(3,3),1],[(-3,3),1],[(3,-3),1],[(-3,-3),1]],[[(-3,2),1], [(3,2),1], [(-3,-2),1], [(3,-2),1]],[[(-3,2),1], [(3,2),1], [(-3,-2),1], [(3,-2),1]],[[(-2,4),1], [(2,-4),1], [(2,4),1], [(-2,-4),1]],[[(-3,4),1], [(3,4),1], [(3,-4),1], [(-3,-4),1]],[[(-3,4),1], [(3,4),1], [(3,-4),1], [(-3,-4),1]],[[(-3,4),1], [(3,4),1], [(3,-4),1], [(-3,-4),1],[(3,0),2],[(-3,0),1]],[[(-3,4),1], [(3,4),1], [(3,-4),1], [(-3,-4),1]],[[(3,3),1], [(-3,3),1], [(3,-3),1], [(-3,-3),1]],[[(-1,3),1],[(-3,1),1],[(1,-3),1]],[[(-2,2),1],[(2,0),1],[(0,-2),1],[(-2,-2),1]], [[(3,2),1],[(-3,0),1],[(1,-2),1],[(3,-4),1]],[[(1,2),1],[(-1,0),1],[(3,-2),1]],[[(1,5),1],[(-1,1),1],[(3,1),1],[(1,-1),2],[(-1,-5),1]],[[(-1,5),1],[(3,5),1],[(1,-3),1],[(3,-3),1]],[[(-3,2),1],[(1,2),1],[(-1,0),1],[(1,0),1],[(3,-2),1],[(-1,-4),1]],[[(3,1),1],[(-3,-5),1],[(3,-5),1]],[[(-3,3),1],[(1,3),1],[(1,-1),1],[(-3,-3),1],[(3,-3),1]],[[(-3,3),1],[(-1,1),1],[(3,1),1],[(1,-3),1],[(3,-5),1]],[[(3,-1),1],[(1,3),1]],[[(3,-1),1],[(1,-3),1],[(-1,-3),1],[(-1,-1),1],[(-3,-1),1]],[[(-1,-1),1],[(-5,-5),1],[(3,3),1],[(3,-5),1],[(-5,3),1]], [[(-1,-5),1],[(1,-5),1],[(-3,-3),1],[(3,-1),1],[(3,3),1]], [[(-1,1),1],[(-1,3),1],[(-3,1),1],[(1,3),1],[(1,-1),1],[(3,1),1],[(3,-1),1],[(-1,-3),1],[(-1,-5),1],[(-3,-3),1]], [[(-3,3),1],[(-1,-5),1]], [[(-1,-1),1],[(-3,1),1],[(1,-5),1],[(1,5),1]], [[(-1,-5),1],[(-3,-3),1],[(1,3),1]], [[(-1,-1),1],[(-3,-5),1],[(-5,-3),1],[(1,-5),1],[(3,-3),1]], [[(-1,-3),1],[(-3,-5),1],[(-3,1),1],[(-1,3),1],[(3,1),1],[(3,-3),2],[(3,-5),2]]]
    return FangGe[series*10+now],QiDian[series*10+now],ZhongDian[series*10+now],ZhuanKuai[series*10+now]

class firstwindow:
    def __init__(self,j):
        self.jd = j
        global root
        self.root = root
        self.root.title("Lazors")
        self.h = Canvas(self.root,width=600,height=600,bg='black')
        self.h.pack()
        self.back_img = PhotoImage(file='back_pic.gif')
        self.bg = self.h.create_image(300,300,image=self.back_img)
        self.flag = 0
    def clear(self):
        self.h.delete(self.name)
        self.start.place_forget()
        self.root.quit()
    def clear2(self):
        for i in range(4):
            self.h.delete(self.id_e[i])
            self.h.delete(self.id_j[i])
            self.selection[i].place_forget()
            self.h.delete(self.id_t,self.bg)
        self.root.quit()
    def first_(self):
        self.name = self.h.create_text(300,250,text = "Lazors",fill = 'Red',font = ("Times",100,"italic"))
        self.start = Button(self.h,text = "Start Game",font = ("Helvetica",30,"italic"),command = self.clear)
        self.start.place(x = 300,y = 400,anchor = CENTER)
        self.root.mainloop()
    def giveback1(self):
        self.flag = 0
        self.clear2()
        self.root.quit()
    def giveback2(self):
        self.flag = 1
        self.clear2()
        self.root.quit()
    def giveback3(self):
        self.flag = 2
        self.clear2()
        self.root.quit()
    def giveback4(self):
        self.flag = 3
        self.clear2()
        self.root.quit()
    def next_(self):
        self.selection = []
        self.id_e = []
        self.id_j = []
        self.id_t = self.h.create_text(300,100,text = "Level Choose",font = ("Times","50","italic"),fill = 'Red')
        for i in range(4):
            self.id_e.append(self.h.create_rectangle(200,180+i*100,550,i*100+210,fill='Ivory'))
            self.id_j.append(self.h.create_rectangle(200,i*100+180,200+350*(float(self.jd[i])/10),i*100+210,fill='Orange',outline=''))
        self.selection.append(Button(self.h,text="Series 1",font=("Helvetica",30,"italic"),command=self.giveback1))
        self.selection.append(Button(self.h,text="Series 2",font=("Helvetica",30,"italic"),command=self.giveback2))
        self.selection.append(Button(self.h,text="Series 3",font=("Helvetica",30,"italic"),command=self.giveback3))
        self.selection.append(Button(self.h,text="Series 4",font=("Helvetica",30,"italic"),command=self.giveback4))
        for i in range(4):
            self.selection[i].place(relx=0.25/3,rely=0.295+i*0.167)
        self.root.mainloop()
    def run(self):
        self.first_()
        self.next_()
        self.close()
        return self.flag
    def close(self):
        self.h.pack_forget()
        self.root.quit()

def start():
    jindu = open_save()
    global first
    first = firstwindow(jindu)
    number_s = first.run()
    now = jindu[number_s]
    if now == 10:
        now = 0
    fg,qd,zd,zk = open_levels(number_s,now)
    return number_s,now,fg,qd,zd,zk

def Progress(series,now):
    jindu = open_save()
    if jindu[series]<10:
        jindu[series]=jindu[series]+1
    now = now+1
    f = open("save.txt","w")
    for i in range(4):
        f.write("%d\n"%(jindu[i]))
    f.close
    if now == 10:
        now = 0
        series = series+1
    else:
        series = series
    if series == 4:
        series = 0
    fg,qd,zd,zk = open_levels(series,now)
    return series,now,fg,qd,zd,zk

def converter(x):
    a = (450 + 50 * x[0],450 + 50 * x[1])
    return a


class brick:
    def __init__(self, position, type):
        self.position = position
        self.LunRd = (401 + 50 * position[0],401 + 50 * position[1])+(499 + 50 * position[0],499 + 50 * position[1])
        self.type = type
        self.count = 0
    def create(self,list):
        self.group = list
        BC2= '#%02x%02x%02x'%(40,40,40)
        if self.type == 1:
            self.tag = h.create_rectangle(self.LunRd,fill = 'ivory', outline = '',width = 4)
        if self.type == 2:
            self.tag = h.create_rectangle(self.LunRd,fill = BC2, outline = '',width = 4)
        def inchange(event):
            h.itemconfig(self.tag, outline = 'gold')
        def outchange(event):
            if self.count%2 == 0:
                h.itemconfig(self.tag, outline = '')
        def count(event):
            for i in self.group:
                i.count = 0
            self.count = self.count + 1
            for i in self.group:
                if i.count == 0:
                    h.itemconfig(i.tag,outline = '')
        h.tag_bind(self.tag, '<Enter>',inchange)
        h.tag_bind(self.tag,'<Leave>',outchange)
        h.tag_bind(self.tag,'<1>',count)
    def move(self, a ):
        h.move(self.tag,50 *(a[0]-self.position[0]),50 *(a[1]-self.position[1]))
        self.position = (a[0],a[1])
        self.count = self.count + 1

class ZhongDian:
    def __init__(self,xy):
        self.xy = xy
        self.status = 0
    def create(self):
        h.create_oval(440+50*self.xy[0],440+50 *self.xy[1],460 + 50 *self.xy[0],460 + 50 *self.xy[1], outline = 'black',fill='',tags='#out')
        h.create_oval(443+50*self.xy[0],443+50 *self.xy[1],457 + 50 *self.xy[0],457 + 50 *self.xy[1], outline = 'black',fill='',tags='#mid')
        h.create_oval(446+50*self.xy[0],446+50 *self.xy[1],454 + 50 *self.xy[0],454 + 50 *self.xy[1], outline = 'black',fill='',tags='#in')

class QiDian:
    def __init__(self,xy,victor):
        self.victor = victor
        self.x = xy[0]
        self.y = xy[1]
    def create(self):
        self.tag = h.create_oval(445+50*self.x,445 + 50 * self.y , 455+50*self.x,455 + 50 * self.y,outline = '',fill = 'red')

class FangGe:
    def __init__(self,xy,zklist,zdlist,lilist):
        self.center = xy
        self.status = 0
        self.show = 1
        self.nw = (xy[0] * 50 + 405,xy[1] * 50 + 495)
        self.se = (xy[0] *50 +495 , xy[1] * 50 +405)
        self.monitor = zklist
        self.zd = zdlist
        self.li = lilist
    def create(self):
        def wash(event):
            for i in self.zd:
                i.status = 0
            for i in self.monitor:
                if i.count % 2 == 1:
                    i.move(self.center)
            for i in self.li:
                i.Lines(self.zd)
            if JudgeEnd(self.zd)==True:
                for i in ['#in','#mid','#out']:
                    for j in h.find_withtag(i):
                        h.itemconfig(j,fill='Red')
                        h.update()
                    sleep (0.3)
                for i in h.find_withtag('all'):
                    h.delete(i)
                            
                root.quit()
                
        def inchange(event):
            h.itemconfig(self.tag, outline = 'blue')
        def outchange(event):
            h.itemconfig(self.tag,outline = '')
        FGC = '#%02x%02x%02x'%(110,110,110)
        self.tag = h.create_rectangle(self.nw,self.se, fill=FGC, outline = '')
        wash('<1>')
        h.tag_bind(self.tag,'<1>',wash)
        h.tag_bind(self.tag,'<Enter>',inchange)
        h.tag_bind(self.tag,'<Leave>',outchange)



class light:
    def __init__(self,xy, ab,zklist):
        self.startX = xy[0]
        self.startY = xy[1]
        self.a = ab[0]
        self.b = ab[1]
        self.monitor = zklist
    def Lines(self,zdlist):
        for i in h.find_withtag('#light'):
            h.delete(i)
        x,y,a,b=self.startX,self.startY,self.a,self.b
        signal=0
        while signal == 0:
            
            if self.aLine(x,y,a,b,zdlist)!=False:
                x,y,a,b=self.aLine(x,y,a,b,zdlist)
                if abs(x)== 9 or abs(y)== 9:
                    signal=1
            else:
                signal=1
    def aLine(self,x,y,a,b,zdlist):
        flag=0
        for i in zdlist:
            if i.xy == (x , y):
                i.status = 1
        for i in self.monitor:
            if (x + a, y) == i.position:
                if i.type==2:
                    return False
                else:
                    flag = 1
            elif (x, y + b) == i.position:
                if i.type==2:
                    return False
                else:
                    flag = 2
 
        if flag==1:
            return x,y,-a,b
        elif flag==2:
            return x,y,a,-b
        else:
            h.create_line(converter((x,y)),converter((x+a,y+b)) , fill = 'red',tag='#light')
            return x+a,y+b,a,b

def gameStart(fg,qd,zd,zk):
    zdlist = []
    for i in zd:
        zdlist = zdlist + [ZhongDian(i)]
    qdlist = []
    lilist = []
    zklist = []
    for i in zk:
        zklist = zklist + [brick(i[0], i [1])]
    for i in qd:
        qdlist = qdlist + [QiDian(i[0],i[1 ])]
        lilist = lilist + [light(i[0],i[1],zklist)]
    fglist = []
    n = 0
    for i in fg:
        fglist = fglist + [FangGe(i,zklist,zdlist,lilist)]
        fglist[n].create()
        n = n + 1
    for i in zdlist:
        i.create()
    for i in qdlist:
        i.create()
    for i in zklist:
        i.create(zklist)
    root.mainloop()
    return fglist , qdlist , zdlist , zklist, lilist


def JudgeEnd(zdlist):
    for i in zdlist:
        if i.status == 0:
            return False
    return True


root = Tk()
root.protocol("WM_DELETE_WINDOW", callback)

def main():
    try:
        BGC = '#%02x%02x%02x'%(120,120,120)
        series,nowlevel,fg,qd,zd,zk=start()
        global h
        h=Canvas(root,width=900,height=900,bg=BGC)
        h.pack()
        global wrong_quit
        wrong_quit=0
        while True:
            try:
                gameStart(fg,qd,zd,zk)
            except:
                print "Goodbye"
                break
            if wrong_quit==0:
                series,nowlevel,fg,qd,zd,zk = Progress(series,nowlevel)
    except:
        print "Goodbye"
        quit

main()
