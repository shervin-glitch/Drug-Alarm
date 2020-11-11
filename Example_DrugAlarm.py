from tkinter import *
from threading import Thread
import time

master=Tk()
master.title("Drug Alarm")
master.resizable(0 , 0)
master.geometry("265x100")
master["bg"]="Light Blue"

sv_result=StringVar()
lbl01=Label(master, textvariable = sv_result , font = ("Courier" , 9 , "bold") , bg = "tomato" , relief = RAISED , borderwidth = 2)
lbl01.grid(row = 0 , column = 0)
lbl01.config(width = 5)

sv_result02=StringVar()
lbl02=Label(master , textvariable = sv_result02 , font = ("Courier" , 9 , "bold") , bg = "tomato" , relief = RAISED , borderwidth = 2)
lbl02.grid(row = 0 , column = 1)
lbl02.config(width = 5)

sv_num01=StringVar()
en01=Entry(master, textvariable= sv_num01 , justify = "center" , borderwidth = 2)
en01.grid(row = 1 , column = 0)

sv_num02=StringVar()
en02=Entry(master, textvariable= sv_num02 , justify = "center" , borderwidth = 2)
en02.grid(row = 1 , column = 1)


def timer01(t):
        num01=int(sv_num01.get())
        while num01>0:
            num01-=1
            time.sleep(1)
            sv_result.set(num01)

Thread01=Thread(target = timer01 , args =(0 ,))


def callback():
    Thread01.start()

btn01=Button(master , text = "Start" , command = callback , bg = "Green" , relief = RAISED , borderwidth = 3)
btn01.grid(row = 2 , column = 0)
btn01.config(width = 8)

def timer02(t):
        num02=int(sv_num02.get())
        while num02>0:
            num02-=1
            time.sleep(1)
            sv_result02.set(num02)

Thread02=Thread(target = timer02, args = (0 ,))


def callback02():
    Thread02.start()

btn02=Button(master , text ="Start" , command = callback02 , bg = "Yellow" , relief = RAISED , borderwidth = 3)
btn02.grid(row = 2 , column = 1)
btn02.config(width = 8)


def exit():
    master.destroy()

btn_exit=Button(master , text ="Exit" , command = exit ,bg = "Red" , relief = RAISED , borderwidth = 3)
btn_exit.place(x = 90 , y = 70)
btn_exit.config(width = 8)

master.mainloop()