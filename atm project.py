# Atm Project Created by Gurharsh >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


from playsound import playsound # 1.2.2 for stable and error 
import os
from gtts import gTTS
from tkinter import *
from PIL import ImageTk,Image
import mysql.connector as con
from tkinter import messagebox
import time
atmsys=Tk()
atmsys.geometry("350x400") #width * height
atmsys.maxsize(350,400)
atmsys.minsize(350,400)
atmsys.title("Atm System")
atmsys.iconbitmap("atm icon.ico")
# atm logo frame start
atmlogofr=Frame(atmsys,height=52,width=152,borderwidth=0,relief="sunken",bg="#364aef")
atmlogofr.place(x="100")
# atm logo frame end

# for logo image start
logoopen=Image.open("atm.png") #load img
imgresize=logoopen.resize((150,50)) # for resize img(w*h)
logo=ImageTk.PhotoImage(imgresize) # cover the image with imageTk
logoimg=Label(atmlogofr,image=logo).pack()
# for logo image end

# atm First Window For Digit frame start
atmdigitw1=Frame(atmsys,width=350,height=200,bg="#364aef",border=0.2,relief="sunken")
atmdigitw1.place(y=80)
middlelb=Label(atmdigitw1,text="Please Enter Number Between 10 to 99  \nFor Example : 25",foreground="#4060c6",font=("Arial",13,"bold"),padx=30)
middlelb.place(x=0)
# atm First Window For Digit frame end

# atm txt frame entry
numberoutput=IntVar(value=25)
numbercheck=Entry(atmdigitw1,font=("Arial","13"),textvariable=numberoutput)
numbercheck.place(x=90,y=80)
# atm txt frame entry


# Functions -------------------------------------------------------------------------------------
def yesfun():
    sound=playsound("click.mp3")
    # print(numberoutput.get())
    num=numberoutput.get()
    print(type(num))

    print(num)
    if(num>9 and num<100):
        print("Login Success")
        yesbtn.after(100,yesbtn.place_forget)
        yesbtn.after(100,nobtn.place_forget)
        atmdigitw1.after(2000,atmdigitw1.place_forget)
        # -------Error ------------------------------------------------------------------------------------------------------------
        # middlelb2.after(3000,middlelb2)
        # Frame Second Window Start --------------------------------------------------------------------
        chooseoptionfr=Frame(atmsys,width=350,height=200,bg="#364aef",border="2",relief="sunken")
        chooseoptionfr.place(y=80)
        a="Welcome to Sbi"
        middlelb=Label(chooseoptionfr,text=a,foreground="#4060c6",font=("Arial",13,"bold"),padx=110,pady=10)
        middlelb.place(x=0)
        middlelb2=Label(chooseoptionfr,text="Please Wait for Some Time",foreground="#4060c6",font=("Arial",13,"bold"),padx=70,pady=10)
        middlelb2.place(x=0)
        middlelb.after(2000,middlelb2.place_forget) # here it help to forget label( please wait to hide) and show Welcome to sbi 
        
        def bankfun():
            print("hello")
            sound=playsound("click.mp3")
            accountbtn.after(100,accountbtn.place_forget)
            accountbtn.after(100,atmbtn.place_forget)
            time.sleep(1)
            # Frame Second Window Start --------------------------------------------------------------------
            chooseoptionfr=Frame(atmsys,width=350,height=200,bg="#364aef",border="2",relief="sunken")
            chooseoptionfr.place(y=80)
            a="Enter Your Account Number "
            middlelb=Label(chooseoptionfr,text=a,foreground="#4060c6",font=("Arial",13,"bold"),padx=70,pady=10)
            middlelb.place(x=0)
            accountnumber=Entry(chooseoptionfr,font=("Arial","13"))
            accountnumber.place(x=90,y=80)
            accountnumber.delete(0,END)



            def accountcheckfun():
                # bank account deposit code
            # Backend Code ------------------------------------------------------------------------------------------------------------------------------
                sound=playsound("click.mp3")
                conn=con.connect(host="localhost",username="root",password="root",database="atmdb")
                accountnum=accountnumber.get()
                if(conn):
                    print("Connection Success")
                else:                    
                    print("Connection not Establish")
                cur=conn.cursor(buffered=True)
                cur.execute("select accountnumber from atm_details where accountnumber='"+accountnum+"'")
                verifydata=cur.fetchall()
                conn.commit()
                accountverify=[]
                for verifying in verifydata:
                    for c in verifying:
                        accountverify.append(c)
                if(accountnum in accountverify):
                    print("Account verify")
                
                    cur.execute("Select name from atm_details where accountnumber='"+accountnum+"' ")
                    name=cur.fetchall()
                    for check in name:

                        for x in check:
                            print(x)
                            nameshow=x


                            
                    accountdetailsfr=Frame(atmsys,width=350,height=200,bg="#364aef",border="2",relief="sunken")
                    accountdetailsfr.place(y=80)
                    a="Enter Deposit Amount "
                    middlelb=Label(accountdetailsfr,text=a,foreground="#4060c6",font=("Arial",13,"bold"),padx=100,pady=10)
                    middlelb.place(x=0)
                    a="Welcome "+nameshow
                    middlelbwelcome=Label(accountdetailsfr,text=a,foreground="#4060c6",font=("Arial",13,"bold"),padx=100,pady=10)
                    middlelbwelcome.place(x="0")
                    
                    middlelb.after(7000,middlelbwelcome.place_forget)
                    
                    
                    namespeak=gTTS(text=a,lang="en",slow=False)
                    namespeak.save("name.mp3")
                    namespeakplay=playsound("name.mp3")
                    os.remove("name.mp3")
                        # time.sleep(3)
                        # os.remove("name.mp3")
                    accountamount=Entry(accountdetailsfr,font=("Arial","13")) # hide for seconds amount entry
                    accountamount.after(3000,accountamount.place)
                    accountamount.place(x=90,y=80)
                    accountamount.delete(0,END)
                    # moneylist=[100,200,300,]
                    moneylist=[100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000,
                    2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000, 3100, 3200, 3300, 3400, 3500, 3600, 3700, 3800, 3900, 4000, 
                    4100, 4200, 4300, 4400, 4500, 4600, 4700, 4800, 4900, 5000, 5100, 5200, 5300, 5400, 5500, 5600, 5700, 5800, 5900, 6000,
                    6100, 6200, 6300, 6400, 6500, 6600, 6700, 6800, 6900, 7000, 7100, 7200, 7300, 7400, 7500, 7600, 7700, 7800, 7900, 8000,
                    8100, 8200, 8300, 8400, 8500, 8600, 8700, 8800, 8900, 9000, 9100, 9200, 9300, 9400, 9500, 9600, 9700, 9800, 9900, 10000,
                    10100, 10200, 10300, 10400, 10500, 10600, 10700, 10800, 10900, 11000, 11100, 11200, 11300, 11400, 11500, 11600, 11700,
                    11800, 11900, 12000, 12100, 12200, 12300, 12400, 12500, 12600, 12700, 12800, 12900, 13000, 13100, 13200, 13300, 13400,
                    13500, 13600, 13700, 13800, 13900, 14000, 14100, 14200, 14300, 14400, 14500, 14600, 14700, 14800, 14900, 15000, 15100,
                    15200, 15300, 15400, 15500, 15600, 15700, 15800, 15900, 16000, 16100, 16200, 16300, 16400, 16500, 16600, 16700,16800,
                    16900, 17000, 17100, 17200, 17300, 17400, 17500, 17600, 17700, 17800, 17900, 18000, 18100, 18200, 18300, 18400, 18500,
                    18600, 18700, 18800, 18900, 19000, 19100, 19200, 19300, 19400, 19500, 19600, 19700, 19800, 19900, 20000, 20100, 20200,
                    20300, 20400, 20500, 20600, 20700, 20800, 20900, 21000, 21100, 21200, 21300, 21400, 21500, 21600, 21700, 21800, 21900,
                    22000, 22100, 22200, 22300, 22400, 22500, 22600, 22700, 22800, 22900, 23000, 23100, 23200, 23300, 23400, 23500, 23600,
                    23700, 23800, 23900, 24000, 24100, 24200, 24300, 24400, 24500, 24600, 24700, 24800, 24900, 25000]
                    def successfullmsg():
                        sound=playsound("click.mp3")
                        if(accountamount.get()!="" and int(accountamount.get())<=25000 and int(accountamount.get()) in moneylist):

                            cur.execute("select balance from atm_details where accountnumber='"+accountnum+"'")
                            accountamountcheck=int(accountamount.get())
                            result=cur.fetchall()
                            data=[accountamountcheck]
                            for balance in result:
                                for c in balance:
                                    data.append(int(c))
                                    total=sum(data)
                                    print(total)
                                    cur.execute("update atm_details set balance='"+str(total)+"' where accountnumber='"+accountnum+"';")
                                    conn.commit()
                                    reenterbtn.place_forget()
                                    yesbtn.place_forget()
                                    accountamount.place_forget()
                                    successmsglb=Label(accountdetailsfr,text="Transaction Successful",foreground="#4060c6",font=("Arial",13,"bold"),padx=100,pady=50)
                                    successmsglb.place(x="-20")
                                    balancelbmsg=Label(accountdetailsfr,text="    Your Available Balance is "+str(total),foreground="#4060c6",font=("Arial",13,"bold"),padx=100,pady=10)
                                    balancelbmsg.place(x="-70",y=80)
                                    pleasewaitmsg=Label(accountdetailsfr,text="Please Wait . . . . .",foreground="#4060c6",font=("Arial",13,"bold"),padx=110,pady=50)
                                    pleasewaitmsg.place(x=0)
                                    pleasewaitmsg.after(4000,pleasewaitmsg.place_forget)
                                    notecounter=playsound("note.mp3")
                                    detail="Transaction Successful, Your Available Balance is "+str(total)
                                    detailspeak=gTTS(text=detail,lang="en",slow=False)
                                    detailspeak.save("detailspeak.mp3")
                                    speak=playsound("detailspeak.mp3")
                                    os.remove("detailspeak.mp3")
                                    atmsys.after(5000,atmsys.destroy)
                                
                                
                                    
                                    
                        else:
                            sound=playsound("Wrong alert.mp3")
                            print("Please Enter Valid Notes")
                            accountamount.delete(0,END)
                            notvalidmsg=Label(accountdetailsfr,text="Please Enter Valid Notes",foreground="#4060c6",font=("Arial",13,"bold"),padx=80,pady=10)
                            notvalidmsg.place(x=0)
                            notvalidmsg.after(3000,notvalidmsg.place_forget)
                    def reenteramountfun():
                        sound=playsound("click.mp3")
                        accountamount.delete(0,END)
                    yesbtn.config(text="Confirm",command=successfullmsg,padx=10)
                    reenterbtn.config(command=reenteramountfun)
                                
                            


                else:
                    sound=playsound("Wrong alert.mp3")
                    accountnumber.delete(0,END)
                    print("Account not found")
                    a="  Account not found "
                    speakengine=gTTS(text=a,lang="en",slow=False)
                    speakengine.save("noaccount.mp3")
                    play=playsound("noaccount.mp3")
                    os.remove("noaccount.mp3")
                    middlelb=Label(chooseoptionfr,text=a,foreground="#4060c6",font=("Arial",13,"bold"),padx=70,pady=10)
                    middlelb.place(x=0)
                    middlelb.after(4000,middlelb.place_forget)
  
               
            def reenterfun():
                sound=playsound("click.mp3")
                accountnumber.delete(0,END)
            yesbtn.place(x=265,y=280)
            yesbtn.config(text="Confirm",command=accountcheckfun,padx=10)
            yesbtn.after(3000,yesbtn.place)
            # confirmbtn.place(x=265,y=280)
            reenterbtn=Button(text="Re-enter",command=reenterfun)
            reenterbtn.place(x=265,y=340)
            # Button.config(confirmbtn,bg="#00A2DA",font=("Arial,13"),padx=0)
            Button.config(reenterbtn,bg="#00A2DA",font=("Arial,13"),padx=0)
# bankaccount deposit code close
        accountbtn=Button(text="Bank Account",command=bankfun)
        accountbtn.place(x=0,y=280)
# atm code -------------------------------------------------------------
        def atmfun():
            print("Atm check")
            sound=playsound("click.mp3")
            accountbtn.after(100,accountbtn.place_forget)
            accountbtn.after(100,atmbtn.place_forget)
            time.sleep(1)
            # Frame Second Window Start --------------------------------------------------------------------
            chooseoptionfr=Frame(atmsys,width=350,height=200,bg="#364aef",border="2",relief="sunken")
            chooseoptionfr.place(y=80)
            a="Enter Your Card Number "
            middlelb=Label(chooseoptionfr,text=a,foreground="#4060c6",font=("Arial",13,"bold"),padx=80,pady=10)
            middlelb.place(x=0)
            accountnumber=Entry(chooseoptionfr,font=("Arial","13"))
            accountnumber.place(x=90,y=80)
            accountnumber.delete(0,END)
            def atmcardcheck():
                # atmcard check code start ---------------------------------------------------------------------------------------
                sound=playsound("click.mp3")
                conn=con.connect(host="localhost",username="root",password="root",database="atmdb")
                cardnumber=accountnumber.get()
                print(type(cardnumber))
                print(cardnumber)
                
                if(conn):
                    print("Connection Success")
                else:                    
                    print("Connection not Establish")
                cur=conn.cursor(buffered=True)
                cur.execute("select cardnumber from atm_details where cardnumber='"+cardnumber+"'")
                verifydata=cur.fetchall()
                conn.commit()
                cardverify=[]
                for verifycard in verifydata:
                        for check in verifycard:
                            cardverify.append(check)
                            print(cardverify)
                if(cardnumber in cardverify):
                    print("Card Verify")
                    cur.execute("Select name from atm_details where cardnumber='"+cardnumber+"' ")
                    name=cur.fetchall()
                    for check in name:

                        for x in check:
                            print(x)
                            nameshow=x
                    accountdetailsfr=Frame(atmsys,width=350,height=200,bg="#364aef",border="2",relief="sunken")
                    accountdetailsfr.place(y=80)
                    a="Enter You Pin "
                    middlelb=Label(accountdetailsfr,text=a,foreground="#4060c6",font=("Arial",13,"bold"),padx=120,pady=10)
                    middlelb.place(x=0)
                    a="Welcome "+nameshow
                    middlelbwelcome=Label(accountdetailsfr,text=a,foreground="#4060c6",font=("Arial",13,"bold"),padx=100,pady=10)
                    middlelbwelcome.place(x="0")
                    
                    middlelb.after(7000,middlelbwelcome.place_forget)
                    
                    
                    namespeak=gTTS(text=a,lang="en",slow=False)
                    namespeak.save("name.mp3")
                    namespeakplay=playsound("name.mp3")
                    os.remove("name.mp3")
                    atmpin=StringVar()
                    atmpintxt=Entry(accountdetailsfr,font=("Arial","13"),textvariable=atmpin,show="*") # hide for seconds amount entry
                    atmpintxt.after(3000,atmpintxt.place)
                    atmpintxt.place(x=90,y=80)
                    atmpintxt.delete(0,END)
                    def atmpinfun():
                            atmpinoutput=atmpin.get()
                            print("atmpinfun is working")
                            conn=con.connect(host="localhost",username="root",password="root",database="atmdb")
                            cur=conn.cursor(buffered=True)
                            cur.execute("select atmpin from atm_details where cardnumber='"+cardnumber+"'  ")
                            result=cur.fetchall()
                            conn.commit()
                            atmpinchecklist=[]
                            print(type(atmpinoutput))
                            print(atmpinoutput)
                            for check in result:
                                for pin in check:
                                    atmpinchecklist.append(pin)
                                print(atmpinchecklist)
                            if(atmpinoutput in atmpinchecklist):
                                print("Correct Pin")
                                atmoptionsfr=Frame(atmsys,width=350,height=200,bg="#364aef",border="2",relief="sunken")
                                atmoptionsfr.place(y=80)
                                yesbtn.place_forget()
                                reenterbtn.place_forget()
                                chooseoptionfr.place_forget()
                                # Functions code  for atm option start 
                                #  Desposit Function code start 
                                def despositfun():  
                                    print("Deposit option")
                                    sound=playsound("click.mp3")
                                    atmoptionsfr.after(1000,atmoptionsfr.place_forget)
                                    # new frame from deposit ==================================================================
                                    depositfr=Frame(atmsys,width=350,height=320,bg="#364aef",border="2",relief="sunken")
                                    depositfr.place(y=80)
                                    # new frame from deposit end ==================================================================
                                    middlelb=Label(depositfr,text=" Enter Deposit Amount ",foreground="#4060c6",font=("Arial",13,"bold"),padx=80,pady=10)
                                    middlelb.place(x=0)
                                    amount=Entry(depositfr,font=("Arial","13"))
                                    amount.place(x=90,y=80)
                                    amount.delete(0,END)
                                    def confirmfun():
                                        if(amount.get()!=""):
                                            amountnum=int(amount.get())
                                            print("Confirm Click")
                                            playsound("click.mp3")
                                            conn=con.connect(host="localhost",username="root",password="root",
                                                        database="atmdb" )

                                            cur=conn.cursor(buffered=True)
                                            cur.execute("select balance from atm_details where cardnumber='"+cardnumber+"'")
                                            depositcheck=cur.fetchall()
                                            conn.commit()
                                            balance=[amountnum]
                                            print(balance)
                                            for check in depositcheck:
                                                for bal in check:
                                                    balance.append(int(bal))
                                                    updatebal=sum(balance)
                                                    print("In loop : ",updatebal)
                                                    moneylist=[100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000,
                                                    2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000, 3100, 3200, 3300, 3400, 3500, 3600, 3700, 3800, 3900, 4000, 
                                                    4100, 4200, 4300, 4400, 4500, 4600, 4700, 4800, 4900, 5000, 5100, 5200, 5300, 5400, 5500, 5600, 5700, 5800, 5900, 6000,
                                                    6100, 6200, 6300, 6400, 6500, 6600, 6700, 6800, 6900, 7000, 7100, 7200, 7300, 7400, 7500, 7600, 7700, 7800, 7900, 8000,
                                                    8100, 8200, 8300, 8400, 8500, 8600, 8700, 8800, 8900, 9000, 9100, 9200, 9300, 9400, 9500, 9600, 9700, 9800, 9900, 10000,
                                                    10100, 10200, 10300, 10400, 10500, 10600, 10700, 10800, 10900, 11000, 11100, 11200, 11300, 11400, 11500, 11600, 11700,
                                                    11800, 11900, 12000, 12100, 12200, 12300, 12400, 12500, 12600, 12700, 12800, 12900, 13000, 13100, 13200, 13300, 13400,
                                                    13500, 13600, 13700, 13800, 13900, 14000, 14100, 14200, 14300, 14400, 14500, 14600, 14700, 14800, 14900, 15000, 15100,
                                                    15200, 15300, 15400, 15500, 15600, 15700, 15800, 15900, 16000, 16100, 16200, 16300, 16400, 16500, 16600, 16700,16800,
                                                    16900, 17000, 17100, 17200, 17300, 17400, 17500, 17600, 17700, 17800, 17900, 18000, 18100, 18200, 18300, 18400, 18500,
                                                    18600, 18700, 18800, 18900, 19000, 19100, 19200, 19300, 19400, 19500, 19600, 19700, 19800, 19900, 20000, 20100, 20200,
                                                    20300, 20400, 20500, 20600, 20700, 20800, 20900, 21000, 21100, 21200, 21300, 21400, 21500, 21600, 21700, 21800, 21900,
                                                    22000, 22100, 22200, 22300, 22400, 22500, 22600, 22700, 22800, 22900, 23000, 23100, 23200, 23300, 23400, 23500, 23600,
                                                    23700, 23800, 23900, 24000, 24100, 24200, 24300, 24400, 24500, 24600, 24700, 24800, 24900, 25000]
                                            if(amountnum in balance and amountnum in moneylist ):
                                                print(updatebal)
                                                cur.execute("update atm_details set balance='"+str(updatebal)+"' where cardnumber='"+cardnumber+"';")
                                                conn.commit()
                                                confirmbtn.place_forget()
                                                amount.place_forget()
                                                clearbtn.place_forget()
                                                successlb=Label(depositfr,text=" Transaction Successful\n\n Your Available balance is {}".format(updatebal),foreground="#4060c6",font=("Arial",13,"bold"),padx=60,pady=10)
                                                successlb.place(x=0)
                                                speak=" Transaction Successful Your Available balance is "+str(updatebal)
                                                speakengine=gTTS(text=speak,lang="en",slow=False)
                                                counter=playsound("note.mp3")
                                                speakengine.save("deposit.mp3")
                                                play=playsound("deposit.mp3")
                                                os.remove("deposit.mp3")
                                                atmsys.after(5000,atmsys.destroy)
                                            else:
                                                noteerrorlb=Label(depositfr,text="Please Enter Valid Notes",foreground="#4060c6",font=("Arial",13,"bold"),padx=90,pady=10)
                                                noteerrorlb.place(x=0)
                                                sound=playsound("wrong alert.mp3")
                                                print("Please Enter Valid Amount")
                                                amount.delete(0,END)
                                                noteerrorlb.after(4000,noteerrorlb.place_forget)
                                        else:
                                            emptylb=Label(depositfr,text="Deposit Machine is Empty",foreground="#4060c6",font=("Arial",13,"bold"),padx=90,pady=10)
                                            emptylb.place(x=0)
                                            emptylb.after(4000,emptylb.place_forget)
                                            sound=playsound("wrong alert.mp3")
                                    confirmbtn=Button(depositfr,text="Confirm",command=confirmfun,bg="#00A2DA",font=("Arial,13"),padx=5)
                                    confirmbtn.place(x=260,y=200)
                                    def clearfun():
                                        playsound("click.mp3")
                                        amount.delete(0,END)

                                    clearbtn=Button(depositfr,text="Clear",command=clearfun,bg="#00A2DA",font=("Arial,13"),padx=15)
                                    clearbtn.place(x=260,y=250)
                                #  Desposit Function code start 
                                
                                # ===================Check Balance Function Code  Start ===========================
                                def checkbalancefun():
                                     print("Balance Check")
                                     sound=playsound("click.mp3")
                                     atmoptionsfr.after(1000,atmoptionsfr.place_forget)
                                     checkbalancefr=Frame(atmsys,width=350,height=320,bg="#364aef",border="2",relief="sunken")
                                     checkbalancefr.place(y=80)
                                     conn=con.connect(host="localhost",username="root",password="root",
                                                          database="atmdb" )
                                         
                                     cur=conn.cursor(buffered=True)
                                     cur.execute("select balance from atm_details where cardnumber='"+cardnumber+"'")
                                     balance=cur.fetchall()
                                     conn.commit()
                                     for check in balance: # for rows 
                                          for checkbalance in check:
                                              print(checkbalance)
                                              
                                     balancelb=Label(checkbalancefr,text=" Your Avaialble Balance is\n\n Rs. {}".format(checkbalance),foreground="#4060c6",font=("Arial",13,"bold"),padx=80,pady=10)
                                     balancelb.place(x=0)
                                     speak="Your Avaialble Balance is Rs"+str(checkbalance)
                                     speakengine=gTTS(text=speak,lang="en",slow=False)
                                     speakengine.save("checkbal.mp3")
                                     play=playsound("checkbal.mp3")
                                     os.remove("checkbal.mp3")
                                     atmsys.after(5000,atmsys.destroy)

                                # ===================Check Balance Function Code End =============================  

                                # ===================Withdrawal  Function Code Start =============================  
                                def withdrawnfun():
                                     print("Withdrawn Function")
                                     sound=playsound("click.mp3")
                                     atmoptionsfr.after(1000,atmoptionsfr.place_forget)
                                     # new frame from deposit ==================================================================
                                     withdrawnfr=Frame(atmsys,width=350,height=320,bg="#364aef",border="2",relief="sunken")
                                     withdrawnfr.place(y=80)
                                     # new frame from deposit end ==================================================================
                                     middlelb=Label(withdrawnfr,text=" Enter Withdrawal Amount ",foreground="#4060c6",font=("Arial",13,"bold"),padx=80,pady=10)
                                     middlelb.place(x=0)
                                     amount=Entry(withdrawnfr,font=("Arial","13"))
                                     amount.place(x=90,y=80)
                                     amount.delete(0,END)
                                     def confirmfun():
                                         if(amount.get()!=""):
                                             amountnum=int(amount.get())
                                             print("Confirm Click")
                                             playsound("click.mp3")
                                             conn=con.connect(host="localhost",username="root",password="root",
                                                         database="atmdb" )
                                             cur=conn.cursor(buffered=True)
                                             cur.execute("select balance from atm_details where cardnumber='"+cardnumber+"'")
                                             depositcheck=cur.fetchall()
                                             conn.commit()
                                             balance=amountnum
                                             print(balance)
                                             moneylist=[100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000,
                                             2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000, 3100, 3200, 3300, 3400, 3500, 3600, 3700, 3800, 3900, 4000, 
                                             4100, 4200, 4300, 4400, 4500, 4600, 4700, 4800, 4900, 5000, 5100, 5200, 5300, 5400, 5500, 5600, 5700, 5800, 5900, 6000,
                                             6100, 6200, 6300, 6400, 6500, 6600, 6700, 6800, 6900, 7000, 7100, 7200, 7300, 7400, 7500, 7600, 7700, 7800, 7900, 8000,
                                             8100, 8200, 8300, 8400, 8500, 8600, 8700, 8800, 8900, 9000, 9100, 9200, 9300, 9400, 9500, 9600, 9700, 9800, 9900, 10000,
                                             10100, 10200, 10300, 10400, 10500, 10600, 10700, 10800, 10900, 11000, 11100, 11200, 11300, 11400, 11500, 11600, 11700,
                                             11800, 11900, 12000, 12100, 12200, 12300, 12400, 12500, 12600, 12700, 12800, 12900, 13000, 13100, 13200, 13300, 13400,
                                             13500, 13600, 13700, 13800, 13900, 14000, 14100, 14200, 14300, 14400, 14500, 14600, 14700, 14800, 14900, 15000, 15100,
                                             15200, 15300, 15400, 15500, 15600, 15700, 15800, 15900, 16000, 16100, 16200, 16300, 16400, 16500, 16600, 16700,16800,
                                             16900, 17000, 17100, 17200, 17300, 17400, 17500, 17600, 17700, 17800, 17900, 18000, 18100, 18200, 18300, 18400, 18500,
                                             18600, 18700, 18800, 18900, 19000, 19100, 19200, 19300, 19400, 19500, 19600, 19700, 19800, 19900, 20000, 20100, 20200,
                                             20300, 20400, 20500, 20600, 20700, 20800, 20900, 21000, 21100, 21200, 21300, 21400, 21500, 21600, 21700, 21800, 21900,
                                             22000, 22100, 22200, 22300, 22400, 22500, 22600, 22700, 22800, 22900, 23000, 23100, 23200, 23300, 23400, 23500, 23600,
                                             23700, 23800, 23900, 24000, 24100, 24200, 24300, 24400, 24500, 24600, 24700, 24800, 24900, 25000]
                                             for check in depositcheck:
                                                 for checkbal in check:
                                                     if(checkbal>=balance and balance in moneylist):
                                                         availbal=checkbal-balance
                                                         updatebal=availbal
                                                         print("In loop : ",updatebal)
                                                         print(updatebal)
                                                         cur.execute("update atm_details set balance='"+str(updatebal)+"' where cardnumber='"+cardnumber+"';")
                                                         conn.commit()
                                                         confirmbtn.place_forget()
                                                         amount.place_forget()
                                                         clearbtn.place_forget()
                                                         successlb=Label(withdrawnfr,text=" Transaction Successful\n\n Your Available balance is Rs. {}        ".format(updatebal),foreground="#4060c6",font=("Arial",13,"bold"),padx=30,pady=10)
                                                         successlb.place(x=0)
                                                         speak=" Transaction Successful Your Available balance is Rs"+str(updatebal)
                                                         from gtts import gTTS
                                                         speakengine=gTTS(text=speak,lang="en",slow=False)
                                                         cashsound=playsound("note.mp3")
                                                         speakengine.save("withdraw.mp3")
                                                         play=playsound("withdraw.mp3")
                                                         os.remove("withdraw.mp3")

                                                         atmsys.after(5000,atmsys.destroy)
                                                     elif(balance>checkbal and balance in moneylist):
                                                          validbalance=Label(withdrawnfr,text=" Your Available balance is Rs. {}\nEnter Lower Amount than Your Balance".format(checkbal),foreground="#4060c6",font=("Arial",13,"bold"),padx=30,pady=10)
                                                          validbalance.place(x=0)
                                                          validbalance.after(4000,validbalance.place_forget)
                                                          play=playsound("Wrong alert.mp3")
                                                     else:
                                                         validamountlb=Label(withdrawnfr,text=" Please Enter Valid Withdrawal Amount",foreground="#4060c6",font=("Arial",13,"bold"),padx=30,pady=10)
                                                         validamountlb.place(x=0)
                                                         validamountlb.after(4000,validamountlb.place_forget)
                                                         sound=playsound("wrong alert.mp3")
                                                         print("Please Enter Valid Withdrawal Amount")
                                                         amount.delete(0,END)
                                         else:
                                             withdrawalamountlb=Label(withdrawnfr,text=" Please Enter  Withdrawal Amount ",foreground="#4060c6",font=("Arial",13,"bold"),padx=20,pady=10)
                                             withdrawalamountlb.place(x=0)
                                             withdrawalamountlb.after(3000,withdrawalamountlb.place_forget)
                                             sound=playsound("wrong alert.mp3")
                                     confirmbtn=Button(withdrawnfr,text="Confirm",command=confirmfun,bg="#00A2DA",font=("Arial,13"),padx=5)
                                     confirmbtn.place(x=260,y=200)
                                     def clearfun():
                                         playsound("click.mp3")
                                         amount.delete(0,END)
                                     clearbtn=Button(withdrawnfr,text="Clear",command=clearfun,bg="#00A2DA",font=("Arial,13"),padx=15)
                                     clearbtn.place(x=260,y=250) 
                                # ===================Withdrawal  Function Code End =============================  
                                # Change Pin Code Start Here ================================================
                                def pinchangefun():
                                     print("Pin Change Function")
                                     sound=playsound("click.mp3")
                                     atmoptionsfr.after(1000,atmoptionsfr.place_forget)
                                     # new frame from deposit ==================================================================
                                     pinchangefr=Frame(atmsys,width=350,height=320,bg="#364aef",border="2",relief="sunken")
                                     pinchangefr.place(y=80)
                                     # new frame from deposit end ==================================================================
                                     middlelb=Label(pinchangefr,text=" Enter Your New Pin ",foreground="#4060c6",font=("Arial",13,"bold"),padx=100,pady=10)
                                     middlelb.place(x=0)
                                     atmpin=Entry(pinchangefr,font=("Arial","13"),show="*")
                                     atmpin.place(x=90,y=80)
                                     def confirmfun():
                                           print("Confirm Click")
                                           pin=atmpin.get()
                                           atmpin.delete(0,END)
                                           if(pin!=""):    
                                                 print("Entered Atm ",pin)
                                                 conn=con.connect(host="localhost",username="root",password="root",database="atmdb" )
                                                 cur=conn.cursor(buffered=True)
                                                 cur.execute("update atm_details set atmpin='"+str(pin)+"' where cardnumber='"+cardnumber+"'")
                                                 conn.commit()  
                                                 txt=" \nYour Pin is Updated Successfully\n "
                                                 atmpinupdatelb=Label(pinchangefr,text=txt,foreground="#4060c6",font=("Arial",13,"bold"),padx=60,pady=10)
                                                 atmpinupdatelb.place(x=0)
                                                 atmpin.after(1000,atmpin.place_forget)
                                                 confirmbtn.after(1000,confirmbtn.place_forget)
                                                 clearbtn.after(1000,clearbtn.place_forget)
                                                 speakengine=gTTS(text=txt,lang="en",slow=False)
                                                 speakengine.save("pinupdate.mp3")
                                                 play=playsound("pinupdate.mp3")
                                                 os.remove("pinupdate.mp3")
                                                 atmsys.after(4000,atmsys.destroy)
                                           else:
                                                 sound=playsound("wrong alert.mp3")
                                                 txt="Please Enter Your Pin"
                                                 atmpinerrorlb=Label(pinchangefr,text=txt,foreground="#4060c6",font=("Arial",13,"bold"),padx=100,pady=10)
                                                 atmpinerrorlb.place(x=0)
                                                 atmpinerrorlb.after(1000,atmpinerrorlb.place_forget)
                                     def clearfun():
                                         playsound("click.mp3")
                                         atmpin.delete(0,END)
                                     clearbtn=Button(pinchangefr,text="Clear",command=clearfun,bg="#00A2DA",font=("Arial,13"),padx=15)
                                     clearbtn.place(x=260,y=250)
                                     confirmbtn=Button(pinchangefr,text="Confirm",command=confirmfun,bg="#00A2DA",font=("Arial,13"),padx=5)
                                     confirmbtn.place(x=260,y=200)
                                # Change Pin Code Start Here ================================================
                                
                                #  Money Transfer Function  Start ====================================================================================================
                                def moneytransferfun():
                                    print("Money Transfer Function")
                                    sound=playsound("click.mp3")
                                    atmoptionsfr.after(1000,atmoptionsfr.place_forget)
                                    # new frame from deposit ==================================================================
                                    moneytransferfr=Frame(atmsys,width=350,height=320,bg="#364aef",border="2",relief="sunken")
                                    moneytransferfr.place(y=80)
                                    # new frame from deposit end ==================================================================
                                    middlelb=Label(moneytransferfr,text=" Enter Account Number ",foreground="#4060c6",font=("Arial",13,"bold"),padx=90,pady=10)
                                    middlelb.place(x=0)
                                    accounttxt=Entry(moneytransferfr,font=("Arial","13"))
                                    accounttxt.place(x=90,y=80)
                                    def confirmfun():
                                          print("Confirm Click")
                                          account=accounttxt.get()
                                          accounttxt.delete(0,END)
                                          if(account!=""):    
                                             print("Entered Account Number ",account)
                                             conn=con.connect(host="localhost",username="root",password="root",database="atmdb" )
                                             cur=conn.cursor(buffered=True)
                                             cur.execute("select accountnumber from atm_details where accountnumber='"+account+"'")
                                             accountnumber=cur.fetchall()
                                             conn.commit()
                                             accountnum=[]
                                             for check in accountnumber:
                                                 for accountcheck in check:
                                                     accountnum.append(accountcheck)
                                             print(accountnum)
                                             if(account in accountnum):
                                                 print("Account Found")
                                                 sound=playsound("click.mp3")
                                                 cur.execute("select name from atm_details where accountnumber='"+account+"'")
                                                 nameshow=cur.fetchall()
                                                 conn.commit()
                                                 for name in nameshow:
                                                     for checkname in name:
                                                        accountholdername=checkname
                                
                                                 print("Name ",accountholdername)
                                                 txt=" Account Holder Name "+accountholdername
                                                 accountholder=gTTS(text=txt,lang="en",slow=False)
                                                 accountholder.save("accountholdername.mp3")
                                                 speakname=playsound("accountholdername.mp3")
                                                 middlelb.place_forget()
                                                 accounttxt.place_forget()
                                                 accountamountlb=Label(moneytransferfr,text="Enter Transfer Amount",foreground="#4060c6",font=("Arial",13,"bold"),padx=90,pady=10)
                                                 accountamountlb.place(x=0)
                                                 accountholderlb=Label(moneytransferfr,text=txt,foreground="#4060c6",font=("Arial",13,"bold"),padx=60,pady=10)
                                                 accountholderlb.place(x=0)
                                                 accountholderlb.after(4000,accountholderlb.place_forget)
                                                 transferamounttxt=Entry(moneytransferfr,font=("Arial","13"))
                                                 transferamounttxt.place(x=90,y=80)
                                                 os.remove("accountholdername.mp3")
                                                 def amountcheckfun():
                                                     playsound("click.mp3")
                                                     transferamount=int(transferamounttxt.get())
                                                     print("Amount Check function in Money Transfer",transferamount)
                                                     cur.execute("select balance from atm_details where cardnumber='"+cardnumber+"'")
                                                     balance=cur.fetchall()
                                                     conn.commit()
                                                     if(transferamount>100):
                                                         for check in balance:
                                                             for bal in check:
                                                                 updatebal=bal-transferamount
                                                         print(updatebal)
                                                         if(updatebal>=0):
                                                             print("Money Transfer")
                                                             cur.execute("update atm_details set balance='"+str(updatebal)+"' where cardnumber='"+cardnumber+"'")
                                                             conn.commit()
                                                             cur.execute("select balance from atm_details where accountnumber ='"+account+"'")
                                                             accountuserbal=cur.fetchall()
                                                             conn.commit()
                                                             for balcheck in accountuserbal:
                                                                 for bal in balcheck:
                                                                     transferupdate=bal+transferamount
                                                                     print("Account Data Details",transferupdate)
                                                             cur.execute("update atm_details set balance='"+str(transferupdate)+"' where accountnumber='"+account+"'")
                                                             conn.commit()
                                                             cur.execute("select balance from atm_details where cardnumber='"+cardnumber+"' ")
                                                             newbal=cur.fetchall()
                                                             conn.commit()
                                                            #  for resolve same account problem
                                                             for againcheck in newbal:
                                                                 for checking in againcheck:
                                                                     print("Available Bal check",checking)
                                                            #  for resolve same account problem
                                                             accountbalerror=Label(moneytransferfr,text="Money Transfer Successfully\n Your Available Balance is Rs {}".format(checking),foreground="#4060c6",font=("Arial",13,"bold"),padx=50,pady=10)
                                                             accountbalerror.place(x=0)
                                                             transfersound=playsound("transfer sound.mp3")
                                                             txtspeak="Money Transfer Successfully\n Your Available Balance is Rs "+str(checking)
                                                             speakbal=gTTS(text=txtspeak,lang="en",slow=False)
                                                             speakbal.save("moneytransfer.mp3")
                                                             speakbalplay=playsound("moneytransfer.mp3")
                                                             os.remove("moneytransfer.mp3")
                                                             confirmbtn.place_forget()
                                                             clearbtn.place_forget()
                                                             transferamounttxt.place_forget()
                                                             atmsys.after(5000,atmsys.destroy)
                                                         else:
                                                             accountbalerror=Label(moneytransferfr,text="Your Balance is Low \n Your Account Balance Rs. {} ".format(bal),foreground="#4060c6",font=("Arial",13,"bold"),padx=50,pady=10)
                                                             accountbalerror.place(x=0)
                                                             accountbalerror.after(4000,accountbalerror.place_forget)
                                                             transferamounttxt.delete(0,END)
                                                             playsound("Wrong alert.mp3")
                                                             print("Your balance is lower than entered Amount")
                                                     else:
                                                             amounttxterror=Label(moneytransferfr,text="Please Enter Amount More Than\n Rs.100",foreground="#4060c6",font=("Arial",13,"bold"),padx=60,pady=12)
                                                             amounttxterror.place(x=0)
                                                             amounttxterror.after(4000,amounttxterror.place_forget)
                                                             transferamounttxt.delete(0,END)
                                                             playsound("Wrong alert.mp3")
                                                             print("Please Enter Valid Input")
                                                 def cleartransferamount():
                                                     transferamounttxt.delete(0,END)
                                                     playsound("click.mp3")
                                                 confirmbtn.config(command=amountcheckfun)
                                                 clearbtn.config(command=cleartransferamount)
                                
                                
                                             else:
                                                 playsound("click.mp3")
                                                 noaccount=playsound("Wrong alert.mp3")
                                                 print("No Account Found")       
                                                 txt="No Account Found"
                                                 speakengine=gTTS(text=txt,lang="en",slow=False)
                                                 speakengine.save("noaccount.mp3")
                                                 playnoaccount=playsound("noaccount.mp3")
                                                 os.remove("noaccount.mp3")
                                                 accounterrorlb=Label(moneytransferfr,text=txt,foreground="#4060c6",font=("Arial",13,"bold"),padx=100,pady=10)
                                                 accounterrorlb.place(x=0)
                                                 accounterrorlb.after(1000,accounterrorlb.place_forget)
                                          else:
                                             sound=playsound("wrong alert.mp3")
                                             txt="Please Enter Account Number"
                                             accounterrorlb=Label(moneytransferfr,text=txt,foreground="#4060c6",font=("Arial",13,"bold"),padx=50,pady=10)
                                             accounterrorlb.place(x=0)
                                             accounterrorlb.after(1000,accounterrorlb.place_forget)
                                    def clearfun():
                                        playsound("click.mp3")
                                        accounttxt.delete(0,END)
                                    clearbtn=Button(moneytransferfr,text="Clear",command=clearfun,bg="#00A2DA",font=("Arial,13"),padx=15)
                                    clearbtn.place(x=260,y=250)
                                    confirmbtn=Button(moneytransferfr,text="Confirm",command=confirmfun,bg="#00A2DA",font=("Arial,13"),padx=5)
                                    confirmbtn.place(x=260,y=200)
                                #  Money Transfer Function  End  ====================================================================================================

                                # Functions code  for atm option end 

                                # Frame code for atm options start  
                                atmoptionsfr=Frame(atmsys,width=350,height=320,bg="#364aef",border="2",relief="sunken")
                                atmoptionsfr.place(y=80)
                                #  Left Side -----------------------------------------------------
                                middlelb=Label(atmoptionsfr,text=" Please choose Option ",foreground="#4060c6",font=("Arial",13,"bold"),padx=90,pady=10)
                                middlelb.place(x=0)
                                depositbtn=Button(atmoptionsfr,command=despositfun,text="Deposit",bg="#00A2DA",font=("Arial,13"),padx=25)
                                depositbtn.place(x=0,y=60)
                                withdrawnbtn=Button(atmoptionsfr,text="Withdrawn",command=withdrawnfun,bg="#00A2DA",font=("Arial,13"),padx=12)
                                withdrawnbtn.place(x=0,y=110)
                                transferbtn=Button(atmoptionsfr,text="Transfer",command=moneytransferfun,bg="#00A2DA",font=("Arial,13"),padx=22)
                                transferbtn.place(x=0,y=160)
                                #  Left Side End -----------------------------------------------------
                                
                                # ---------------------------Right Side
                                checkbalancebtn=Button(atmoptionsfr,text="Check Balance",command=checkbalancefun,bg="#00A2DA",font=("Arial,13"),padx=5)
                                checkbalancebtn.place(x=200,y=60)
                                changepinbtn=Button(atmoptionsfr,text="Pin Change",command=pinchangefun,bg="#00A2DA",font=("Arial,13"),padx=20)
                                changepinbtn.place(x=200,y=110)
                                # ----------------------------Right Side End
                               
                                # Frame code for atm options end
                                    
                            else:
                               print(" You Entered Wrong Pin")
                               playsound("Wrong alert.mp3")
                               atmpintxt.delete(0,END)
                               a="You Entered Wrong Pin"
                               wrongpinlb=Label(accountdetailsfr,text=a,foreground="#4060c6",font=("Arial",13,"bold"),padx=100,pady=10)
                               wrongpinlb.place(x=0)
                               wrongpinlb.after(3000,wrongpinlb.place_forget)
                        
                    yesbtn.config(text="Confirm",command=atmpinfun,padx=10)
                    def atmpinclear():
                        sound=playsound("click.mp3")
                        atmpintxt.delete(0,END)
                    reenterbtn.config(text="Clear",command=atmpinclear,padx=20)

                else:
                    print("Card Not Found")                
                    playsound("Wrong alert.mp3")
                    speaken=gTTS(text="Card Not Found",lang="en",slow=False)
                    speaken.save("nocard.mp3")
                    nocard=playsound("nocard.mp3")
                    middlelb=Label(chooseoptionfr,text="   Card Not Found",foreground="#4060c6",font=("Arial",13,"bold"),padx=100,pady=10)
                    middlelb.place(x=0)
                    middlelb.after(4000,middlelb.place_forget)
                    accountnumber.delete(0,END)
                    os.remove("nocard.mp3")
  
                
                # atmcard check code End ---------------------------------------------------------------------------------------
            def reenterfun():
                sound=playsound("click.mp3")
                accountnumber.delete(0,END)
            yesbtn.place(x=265,y=280)
            yesbtn.config(text="Confirm",command=atmcardcheck,padx=10)
            yesbtn.after(3000,yesbtn.place)
            # confirmbtn.place(x=265,y=280)
            reenterbtn=Button(text="Re-enter",command=reenterfun)
            reenterbtn.place(x=265,y=340)
            # Button.config(confirmbtn,bg="#00A2DA",font=("Arial,13"),padx=0)
            Button.config(reenterbtn,bg="#00A2DA",font=("Arial,13"),padx=0)
            

            
# atm code end--------------------------------------------------------------
 


        Button.config(accountbtn,bg="#00A2DA",font=("Arial,13"),padx=0)
        atmbtn=Button(text="Atm card",command=atmfun)
        atmbtn.place(x=0,y=340)
        Button.config(atmbtn,bg="#00A2DA",font=("Arial,13"),padx=20)

# Frame Second Window End --------------------------------------------------------------------
    else:
        sound=playsound("Wrong alert.mp3")
        numbercheck.delete(0,END)
        lbmsg=Label(text="Please Enter Right Digit",font=("Arial",12,"bold"),bg="#fefffe",fg="red")
        lbmsg.place(x=90,y=200)
        lbmsg.after(3000,lbmsg.place_forget)
        yesbtn.config(command=yesfun)

def nofun():
    sound=playsound("click.mp3")
    atmsys.destroy()

# atm yes no button start
yesbtn=Button(text="Yes",command=yesfun)
yesbtn.place(x=265,y=280)
nobtn=Button(text="No",command=nofun)
nobtn.place(x=265,y=340)
# accountbtn.place(x=0,y=280)


# atm yes no button end

# Functions -------------------------------------------------------------------------------------

atmsys.config(bg="#364aef")
Button.config(yesbtn,bg="#00A2DA",font=("Arial,13"),padx=25)
Button.config(nobtn,bg="#00A2DA",font=("Arial,13"),padx=25)
atmsys.mainloop()

# Atm Project Created by Gurharsh >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>