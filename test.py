
from Tkinter import *
from tkMessageBox import *
import time
import sqlite3
import random

x=Tk()
#root.configure(bg="pink")
x.title("AVANT BILLING SOFTWARE")
Label(x,text="AVANT MEDICARE ",relief='ridge',font='times 20 bold',bd=20).grid(row=0,column=3)
Label(x,text="39, SHASHTRI NAGAR, VARANASI-221 004, UTTAR PRADESH").grid(row=1,column=0,columnspan=5)
Label(x,text='----------------------------------------------------------------------').grid(row=2,column=0,columnspan=5)
con=sqlite3.Connection('med')
cur=con.cursor()
cur.execute("create table if not exists med(batchno varchar(5) primary key,med varchar(20),price varchar(5),exp date)")
cur.execute("insert into med values('12-66','Pentamox-CV',80.50,'17-DEC-2020')")
a=[('12-67','Finemox-AV',55.65,'14-JUL-2020'),('12-68','NK-Para',65.55,'14-MAR-2020'),('12-69','Ibuprofane',105.50,'14-JAN-2020'),('12-70','Pantakind-DSR',122.65,'14-FEB-2020'),
   ('12-71','OFLAKEM',66.85,'14-APR-2020'),('12-72','NORAGYL',66.85,'18-DEC-2020'),('12-73','METROGYL',35.00,'14-OCT-2020')]
cur.executemany("insert into med values(?,?,?,?)",a)
                                       
cur.execute('Select * from med') 
print cur.fetchall()
def clock():
    t=time.strftime('%Y-%m-%d \n%H:%M:%S',time.localtime())
    if t!='':
        Label(x,text=t,font='times 10').grid(row=0,column=4)
    x.after(100,clock)
#Label.grid(row=0,column=4)
clock()
Label(x,text="USERNAME",relief='solid').grid(row=3,column=2,padx=10,pady=10)
e1=Entry(x)
e1.grid(row=3,column=3)
Label(x,text="PASSWORD",relief='solid').grid(row=4,column=2,padx=10,pady=10)
e2=Entry(x,show='*')
e2.grid(row=4,column=3)
c=0
#tp1=FloatVar()


tp1=0.0
tp2=0.0
tp3=0.0
tp4=0.0
tp5=0.0
tp6=0.0
fp=0.0
e3=''
#print type(tp1)
#y1=FloatVar()
#l1=''
#l2=''
#l3=''

def login():
    if((e1.get())=="1" and (e2.get())=='11'):
        showinfo('Welcome',"Your Entry is Successful")
        x.destroy()
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        root=Tk()
        root.title("SALES INVOICE")
        root.geometry("1600x800+0+0")
        Label(root,text="AVANT MEDICARE \n SALES INVOICE",font='times 20 bold').grid(row=0,columnspan=3)
        Label(root,text="39, SHASHTRI NAGAR, VARANASI-221 004, UTTAR PRADESH").grid(row=1,column=0,columnspan=5)
        Label(root,text='----------------------------------------------------------------------').grid(row=2,column=0,columnspan=5)

        def clock1():
            
            
            
            t=time.strftime('%Y-%m-%d \n%H:%M:%S',time.localtime())
            if t!='':
                
                
                Label(root,text=t,font='times 10').grid(row=0,column=4)
            root.after(100,clock1)
        clock1()
        

        f1=Frame(root,relief="ridge",bg="gray",bd='10',padx=10,pady=10,width=800)
        f1.grid(row=3,column=0)

        f2=Frame(root,relief="ridge",bg="linen",bd='10',padx=10,pady=10)
        f2.grid(row=3,column=1,columnspan=2)

        f3=Frame(root,relief="ridge",bg="azure",bd='10')
        f3.grid(row=4,column=0,columnspan=2)
        

       # f3=Frame(root,relief="ridge",width='800',height='1400',bg="pink")
        Label(f1,text="Customer Details",relief='ridge',font='times 15 bold').grid(row=0,columnspan=5)
        Label(f1,text="Cutomer Name",font='times 15').grid(row=1,column=0,padx=5,pady=5)
        global e3
        e3=Entry(f1)
        e3.grid(row=1,column=1,columnspan=2)
        Label(f1,text="Customer Mobile",font='times 15').grid(row=2,column=0,padx=5,pady=5)
        e4=Entry(f1)
        e4.grid(row=2,column=1,columnspan=2)
        Label(f1,text="Gender",font='times 15').grid(row=3,column=0,padx=3,pady=5)
        vr=IntVar()
        Radiobutton(f1,text="MALE",variable=vr,value=1).grid(row=3,column=1,padx=2,pady=5)
        Radiobutton(f1,text="FEMALE",variable=vr,value=2).grid(row=3,column=2,padx=2,pady=5)
        Label(f1,text="Customer's Doctor Name",font='times 15').grid(row=4,column=0,padx=5,pady=5)
        e5=Entry(f1)
        e5.grid(row=4,column=1,columnspan=2)

       # Label(root,text="------------------------------------------------------------------------------").grid(row=4,columnspan=5)
        #
        
        def enter():
            Label(f3,text="BILL No.",font="times 15").grid(row=0,column=0)
            Label(f3,text=random.randint(0,55)).grid(row=0,column=1)
            global tp1
            global tp2
            global tp3
            global tp4
            global tp5
            global tp6

            if (e10.get())=="":
                showerror("Error","Enter valid Quantity")
            else:
                
                
            

                x=list(cur.execute("select * from med"))
                flag=-1
                for i in x:
                    if(i[0]==e6.get()):
                        flag=i
                if(flag==-1):
                    showerror("No entry","No such entry exist \n Enter a valid BatchNo.")

                else:    
                    global c
                    c=c+1
                    if c==1:
                        Label(f3,text="*",font="times 15").grid(row=2,column=0)
                        Label(f3,font="times 15").grid(row=2,column=5)

                    
                        #y1=cur.fetchall()
                    
                        bno=e6.get()
                        cur.execute("select med from med where batchno=?",(e6.get(),))
                        y1=cur.fetchall()
                        
                        l1=Label(f2,text=str(y1[0][0]),font="times 15",width=20).grid(row=3,column=1)
                        cur.execute("select med from med where batchno=?",(e6.get(),))
                        Label(f3,text=str(y1[0][0]),font="times 15").grid(row=2,column=2)

                        cur.execute("Select price from med where batchno=?",(e6.get(),))
                        y2=cur.fetchall()
                        l2=Label(f2,text="Rs."+str(y2[0][0]),font="times 15",width=20).grid(row=4,column=1)
                        cur.execute("Select price from med where batchno=?",(e6.get(),))
                        Label(f3,text="Rs."+str(y2[0][0]),font="times 15").grid(row=2,column=3)

                    
                        cur.execute("Select exp from med where batchno=?",(e6.get(),))
                        y3=cur.fetchall()
                        l3=Label(f2,text=str(y3[0][0]),font="times 15",width=20).grid(row=5,column=1)
                        cur.execute("Select exp from med where batchno=?",(e6.get(),))
                        Label(f3,text=str(y3[0][0]),font="times 15").grid(row=2,column=4)



                        Label(f3,font="times 15",text=e6.get()).grid(row=2,column=1)
                        Label(f3,font="times 15",text=e10.get()).grid(row=2,column=5)

                        #l2=IntVar()
                        cur.execute("select price from med where batchno=?",(e6.get(),))

                        y=cur.fetchone()

                        x1=list()
                        x1.append(y[0].encode('utf-8'))
                        print x1[0]
                        y1=x1[0]


                        qty1=int(e10.get())

                        tp1=tp1+(float(y1)*(qty1))
                        print tp1
                        
                        Label(f3,text="Rs"+str(tp1),font="times 15").grid(row=2,column=6)
                        
                            
                        

                    elif c==2:
                        Label(f3,text="*",font="times 15").grid(row=3,column=0)
                        Label(f3,font="times 15").grid(row=3,column=5)
                        bno=e6.get()
                        cur.execute("select med from med where batchno=?",(e6.get(),))
                        z1=cur.fetchall()
                        l1=Label(f2,text=str(z1[0][0]),font="times 15",width=20).grid(row=3,column=1)
                        cur.execute("select med from med where batchno=?",(e6.get(),))
                        Label(f3,text=str(z1[0][0]),font="times 15").grid(row=3,column=2)

                        cur.execute("Select price from med where batchno=?",(e6.get(),))
                        z2=cur.fetchall()
                        l2=Label(f2,text="Rs."+str(z2[0][0]),font="times 15",width=20).grid(row=4,column=1)
                        cur.execute("Select price from med where batchno=?",(e6.get(),))
                        Label(f3,text="Rs."+str(z2[0][0]),font="times 15").grid(row=3,column=3)

                        cur.execute("Select exp from med where batchno=?",(e6.get(),))
                        z3=cur.fetchall()
                        l3=Label(f2,text=str(z3[0][0]),font="times 15",width=20).grid(row=5,column=1)
                        cur.execute("Select exp from med where batchno=?",(e6.get(),))
                        Label(f3,text=str(z3[0][0]),font="times 15").grid(row=3,column=4)

                        Label(f3,font="times 15",text=e6.get()).grid(row=3,column=1)
                        Label(f3,font="times 15",text=e10.get()).grid(row=3,column=5)


                        cur.execute("select price from med where batchno=?",(e6.get(),))

                        y=cur.fetchone()

                        x2=list()
                        x2.append(y[0].encode('utf-8'))
                        print x2[0]
                        y2=x2[0]


                        qty2=int(e10.get())

                        tp2=tp2+(float(y2)*(qty2))
                        print tp2
                        
                        Label(f3,text="Rs."+str(tp2),font="times 15").grid(row=3,column=6)

                    elif c==3:
                        Label(f3,text="*",font="times 15").grid(row=4,column=0)
                        Label(f3,font="times 15").grid(row=4,column=5)

                        bno=e6.get()
                        
                        cur.execute("select med from med where batchno=?",(e6.get(),))
                        p1=cur.fetchall()
                        #l1=Label(f2,text='',font="times 15",width=20).grid(row=3,column=1)
                        l1=Label(f2,text=str(p1[0][0]),font="times 15",width=20).grid(row=3,column=1)
                        cur.execute("select med from med where batchno=?",(e6.get(),))
                        p1=cur.fetchall()
                        Label(f3,text=str(p1[0][0]),font="times 15").grid(row=4,column=2)

                        cur.execute("Select price from med where batchno=?",(e6.get(),))
                        p2=cur.fetchall()
                        #l2=Label(f2,text='',font="times 15",width=20).grid(row=4,column=1)
                        l2=Label(f2,text="Rs."+str(p2[0][0]),font="times 15",width=20).grid(row=4,column=1)
                        cur.execute("Select price from med where batchno=?",(e6.get(),))
                        p2=cur.fetchall()
                        Label(f3,text="Rs."+str(p2[0][0]),font="times 15").grid(row=4,column=3)

                        cur.execute("Select exp from med where batchno=?",(e6.get(),))
                        p3=cur.fetchall()
                        l3=Label(f2,text=str(p3[0][0]),font="times 15",width=20).grid(row=5,column=1)
                        cur.execute("Select exp from med where batchno=?",(e6.get(),))
                        p3=cur.fetchall()
                        Label(f3,text=str(p3[0][0]),font="times 15").grid(row=4,column=4)

                        Label(f3,text=e6.get(),font="times 15").grid(row=4,column=1)
                        Label(f3,font="times 15",text=e10.get()).grid(row=4,column=5)

                        cur.execute("select price from med where batchno=?",(e6.get(),))

                        y=cur.fetchone()

                        x3=list()
                        x3.append(y[0].encode('utf-8'))
                        print x3[0]
                        y3=x3[0]


                        qty3=int(e10.get())

                        tp3=tp3+(float(y3)*(qty3))
                        print tp3
                        
                        Label(f3,text="Rs."+str(tp3),font="times 15").grid(row=4,column=6)


                    elif c==4:
                        Label(f3,text="*",font="times 15").grid(row=5,column=0)
                        Label(f3,font="times 15").grid(row=5,column=5)

                        bno=e6.get()
                        cur.execute("select med from med where batchno=?",(e6.get(),))
                        q1=cur.fetchall()
                        l1=Label(f2,text=str(q1[0][0]),font="times 15",width=20).grid(row=3,column=1)
                        cur.execute("select med from med where batchno=?",(e6.get(),))
                        Label(f3,text=str(q1[0][0]),font="times 15").grid(row=5,column=2)

                        cur.execute("Select price from med where batchno=?",(e6.get(),))
                        q2=cur.fetchall()
                        l2=Label(f2,text="Rs."+str(q2[0][0]),font="times 15",width=20).grid(row=4,column=1)
                        
                        cur.execute("Select price from med where batchno=?",(e6.get(),))
                        Label(f3,text="Rs."+str(q2[0][0]),font="times 15").grid(row=5,column=3)

                        cur.execute("Select exp from med where batchno=?",(e6.get(),))
                        q3=cur.fetchall()
                        l3=Label(f2,text=str(q3[0][0]),font="times 15",width=20).grid(row=5,column=1)
                        cur.execute("Select exp from med where batchno=?",(e6.get(),))
                        Label(f3,text=str(q3[0][0]),font="times 15").grid(row=5,column=4)

                        Label(f3,font="times 15",text=e6.get()).grid(row=5,column=1)
                        Label(f3,font="times 15",text=e10.get()).grid(row=5,column=5)

                        cur.execute("select price from med where batchno=?",(e6.get(),))

                        y=cur.fetchone()

                        x4=list()
                        x4.append(y[0].encode('utf-8'))
                        print x4[0]
                        y4=x4[0]


                        qty4=int(e10.get())

                        tp4=tp4+(float(y4)*(qty4))
                        print tp4
                        
                        Label(f3,text="Rs."+str(tp4),font="times 15").grid(row=5,column=6)



                    elif c==5:
                        Label(f3,text="*",font="times 15").grid(row=6,column=0)
                        Label(f3,font="times 15").grid(row=6,column=5)

                        bno=e6.get()
                        cur.execute("select med from med where batchno=?",(e6.get(),))
                        r1=cur.fetchall()
                        l1=Label(f2,text=str(r1[0][0]),font="times 15",width=20).grid(row=3,column=1)
                        cur.execute("select med from med where batchno=?",(e6.get(),))
                        Label(f3,text=str(r1[0][0]),font="times 15").grid(row=6,column=2)

                        cur.execute("Select price from med where batchno=?",(e6.get(),))
                        r2=cur.fetchall()
                        l2=Label(f2,text="Rs."+str(r2[0][0]),font="times 15",width=20).grid(row=4,column=1)
                        cur.execute("Select price from med where batchno=?",(e6.get(),))
                        Label(f3,text="Rs."+str(r2[0][0]),font="times 15").grid(row=6,column=3)

                        cur.execute("Select exp from med where batchno=?",(e6.get(),))
                        r3=cur.fetchall()
                        l3=Label(f2,text=str(r3[0][0]),font="times 15",width=20).grid(row=5,column=1)
                        cur.execute("Select exp from med where batchno=?",(e6.get(),))
                        Label(f3,text=str(r3[0][0]),font="times 15").grid(row=6,column=4)

                        Label(f3,font="times 15",text=e6.get()).grid(row=6,column=1)
                        Label(f3,font="times 15",text=e10.get()).grid(row=6,column=5)


                        cur.execute("select price from med where batchno=?",(e6.get(),))

                        y=cur.fetchone()

                        x5=list()
                        x5.append(y[0].encode('utf-8'))
                        print x5[0]
                        y5=x5[0]


                        qty5=int(e10.get())

                        tp5=tp5+(float(y5)*(qty5))
                        print tp5
                        
                        Label(f3,text="Rs."+str(tp5),font="times 15").grid(row=6,column=6)


                    elif c==6:
                        Label(f3,text="*",font="times 15").grid(row=7,column=0)
                        ##q2=Entry(f3,font="times 15").grid(row=7,column=5)

                        

                        
                        bno=e6.get()
                        cur.execute("select med from med where batchno=?",(e6.get(),))
                        s1=cur.fetchall()
                        Label(f2,text=str(s1[0][0]),font="times 15",width=20).grid(row=3,column=1)
                        cur.execute("select med from med where batchno=?",(e6.get(),))
                        Label(f3,text=str(s1[0][0]),font="times 15").grid(row=7,column=2)

                        cur.execute("Select price from med where batchno=?",(e6.get(),))
                        s2=cur.fetchall()
                        Label(f2,text="Rs."+str(s2[0][0]),font="times 15",width=20).grid(row=4,column=1)
                        cur.execute("Select price from med where batchno=?",(e6.get(),))
                        Label(f3,text="Rs."+str(s2[0][0]),font="times 15").grid(row=7,column=3)

                        cur.execute("Select exp from med where batchno=?",(e6.get(),))
                        s3=cur.fetchall()
                        Label(f2,text=str(s3[0][0]),font="times 15",width=20).grid(row=5,column=1)
                        cur.execute("Select exp from med where batchno=?",(e6.get(),))
                        Label(f3,text=str(s3[0][0]),font="times 15").grid(row=7,column=4)

                        Label(f3,font="times 15",text=e6.get()).grid(row=7,column=1)
                        Label(f3,font="times 15",text=e10.get()).grid(row=7,column=5)


                        cur.execute("select price from med where batchno=?",(e6.get(),))

                        y=cur.fetchone()

                        x6=list()
                        x6.append(y[0].encode('utf-8'))
                        print x6[0]
                        y6=x6[0]


                        qty6=int(e10.get())

                        tp6=tp6+(float(y6)*(qty6))
                        print tp6
                        
                        Label(f3,text="Rs."+str(tp6),font="times 15").grid(row=7,column=6)
                    else:
                        showerror('Warning.....','Your Bill is full..Enter in a New Bill')

                


          
                
              
          
                
            
        Label(f2,text="Product Details",relief='ridge',font='times 15 bold').grid(row=0,columnspan=5)
        Label(f2,text="Batch No",font='times 15').grid(row=1,column=0,padx=5,pady=5)
        e6=Entry(f2)
        e6.grid(row=1,column=1)
        Label(f2,text=" Quantity",font='times 15').grid(row=2,column=0,padx=5,pady=5)
        e10=Entry(f2)
        e10.grid(row=2,column=1)
        
        Label(f2,text="Medicine Name",font='times 15').grid(row=3,column=0,padx=5,pady=5)
        #e7=Entry(f2)
        #e7.grid(row=2,column=1)
        Label(f2,text=" Price",font='times 15').grid(row=4,column=0,padx=5,pady=5)
        #e8=Entry(f2)
        #e8.grid(row=3,column=1)
        
        Label(f2,text=" Expiry",font='times 15').grid(row=5,column=0,padx=5,pady=5)
        #e9=Entry(f2)
        #e9.grid(row=4,column=1)
       # Label(f2,text=" Quantity",font='times 15').grid(row=5,column=0,padx=5,pady=5)
        #e10=Entry(f2)
        #e10.grid(row=5,column=1)
        
        

        def add():
  
            #e6.delete(0,END)
           # e7.delete(0,END)
            #e8.delete(0,END)
            #e9.delete(0,END)
            e10.delete(0,END)
            e6.delete(0,END)
            Label(f2,text="",font="times 15",width=20).grid(row=3,column=1)
            Label(f2,text="",font="times 15",width=20).grid(row=4,column=1)
            Label(f2,text="",font="times 15",width=20).grid(row=5,column=1)
            

            
            
        Button(f2,text="NEW",command=add).grid(row=6,column=0)
        Button(f2,text="ENTER",command=enter).grid(row=6,column=1)


        #FRAME #---------------------------------------------------------------------------------------------------------------------------------------
        #c=1
        #def newbill():


            
        #Label(f3,text="Bill No:",font="arial 14").grid(row=0,column=0)
        #Label(f3, textvariable=var,font="arial 14").grid(row=0,column=1)
        #var.set(c)
            #Label(f3, textvariable=c,font="times 15").grid(row=0,column=1)
            
            #Label(f3,text="Bill No:",font="arial 14").grid(row=0,column=0)


        Label(f3,text="*",font="times 15").grid(row=1,column=0)
        Label(f3,text="Batch No",font='times 15').grid(row=1,column=1)
        Label(f3,text="Medicine Name",font='times 15').grid(row=1,column=2)
        Label(f3,text="Price",font='times 15').grid(row=1,column=3)
        Label(f3,text="Expiry",font='times 15').grid(row=1,column=4)
        Label(f3,text="Quantity",font='times 15').grid(row=1,column=5)
        Label(f3,text="Total Price",font="times 15").grid(row=1,column=6)


        
        #-----------------------------------------------------------------------------CLACULATE TOTAL-----------------------------------------------------------------------------------
        def calc(x=0):
            disc=0.0
            global tp1
            global tp2
            global tp3
            global tp4
            global tp5
            global tp6
            global fp
            tp=tp1+tp2+tp3+tp4+tp5+tp6+x
            Label(f3,font="arial 14",text='Rs'+str(tp)).grid(row=9,column=7)

            gst=(0.12*tp)
            Label(f3,font="arial 14",text='Rs'+str(gst)).grid(row=10,column=7)
            if (tp+gst)>800:
                disc=0.03*(tp+gst)
            elif (tp+gst)>1500:
                disc=0.07*(tp+gst)
            elif (tp+gst)>2000:
                disc=0.1*(tp+gst)

            Label(f3,font="arial 14",text="Rs"+str(disc)).grid(row=11,column=7)

            fp=(tp+gst)-disc
            Label(f3,font="arial 14",text="Rs"+ str(fp)).grid(row=12,column=7)

            
        #m1=Entry(f3,font="times 15").grid(row=2,column=2)
       # p1=Entry(f3,font="times 15").grid(row=2,column=3)
       # ex1=Entry(f3,font="times 15").grid(row=2,column=4)
        


        
        #b2=Entry(f3,font="times 15").grid(row=3,column=1)
        #m2=Entry(f3,font="times 15").grid(row=3,column=2)
        #p2=Entry(f3,font="times 15").grid(row=3,column=3)
        #ex2=Entry(f3,font="times 15").grid(row=3,column=4)
        


        
        ##m3=Entry(f3,font="times 15").grid(row=4,column=2)
        #p3=Entry(f3,font="times 15").grid(row=4,column=3)
        #e#x3=Entry(f3,font="times 15").grid(row=4,column=4)
        

      #  Label(f3,text="*",font="times 15").grid(row=5,column=0)
      #  b4=Entry(f3,font="times 15").grid(row=5,column=1)
      #  m4=Entry(f3,font="times 15").grid(row=5,column=2)
      #  p4=Entry(f3,font="times 15").grid(row=5,column=3)
       # ex4=Entry(f3,font="times 15").grid(row=5,column=4)
      #  q4=Entry(f3,font="times 15").grid(row=5,column=5)

       # Label(f3,text="*",font="times 15").grid(row=6,column=0)
       # b5=Entry(f3,font="times 15").grid(row=6,column=1)
       # m5=Entry(f3,font="times 15").grid(row=6,column=2)
        #p5=Entry(f3,font="times 15").grid(row=6,column=3)
        #ex5=Entry(f3,font="times 15").grid(row=6,column=4)
        #q5=Entry(f3,font="times 15").grid(row=6,column=5)

        #Label(f3,text="*",font="times 15").grid(row=7,column=0)
        #b6=Entry(f3,font="times 15").grid(row=7,column=1)
        #m6=Entry(f3,font="times 15").grid(row=7,column=2)
        #p6=Entry(f3,font="times 15").grid(row=7,column=3)
       # ex6=Entry(f3,font="times 15").grid(row=7,column=4)
        #q6=Entry(f3,font="times 15").grid(row=7,column=5)
       # b1.grid(row=2,

        Label(f3,font="times 15",text="Total Price").grid(row=9,column=4)
        #Entry(f3,font="arial 14").grid(row=9,column=7)
        Label(f3,font="times 15",text="GST @ 12%").grid(row=10,column=4)
        #Entry(f3,font="arial 14").grid(row=10,column=7)
        Label(f3,font="times 15",text="Discount").grid(row=11,column=4)
        #Entry(f3,font="arial 14").grid(row=11,column=7)
        Label(f3,font="times 15",text="To pay Rs.").grid(row=12,column=4)
        #Entry(f3,font="arial 14").grid(row=12,column=7)

        def close():
            root.destroy()



        def pbill():
            global e3
            global fp
            showinfo("THanks for Visiting",(e3.get())+"You have to pay"+fp)

#        def pbill():
 #           global fp
  #          showinfo("Thanks for visiting",e3.get()+"You have to pay \n Thanks for visiting"+fp)

        v2=IntVar()
        Checkbutton(f3,text="Home Delivery @ 200",variable=v2,onvalue=200).grid(row=9,column=1)


        Button(f3,text="Print Bill",font="arial 14 bold").grid(row=8,column=1)
        Button(f3,text="EXIT",font="arial 14 bold",command=close).grid(row=8,column=2)
        Button(f3,text="Calculate Total",font="arial 14 bold",command=lambda:calc(int(v2.get()))).grid(row=8,column=3)
        
    else:
        showerror('!!!INVALID ATTEMPT','Enter a valid ID and PASSWORD')
def exit():
    
    x.destroy()
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++MEDICAL DATABASE++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


Button(x,text="LOGIN",command=login).grid(row=5,column=2,padx=5,pady=5)
Button(x,text="EXIT",command=exit).grid(row=5,column=3,padx=5,pady=5)
x.mainloop()

