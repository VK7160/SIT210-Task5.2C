from tkinter import*
import tkinter.font
from gpiozero import LED
import RPi.GPIO 
RPi.GPIO.setmode(RPi.GPIO.BCM)

#Hardware
led1=LED(3)
led2=LED(5)
led3=LED(8)

# GUI Definitions
win =Tk()
win.title("LED TOGGLER")
myFont=tkinter.font.Font(family='Helvitica', size=12, weight="bold")

#Event Functions 
def ledToggle1():
	if led1.is_lit:
		led1.off()
		ledButton1["text"]="Turn Red Led On"
	else:
		led1.on()
		ledButton1["text"]="Turn Red Led Off"
def ledToggle2():
	if led2.is_lit:
		led2.off()
		ledButton2["text"]="Turn Yellow Led On"
	else:
		led2.on()
		ledButton2["text"]="Turn Yellow Led Off"	
def ledToggle3():
	if led3.is_lit:
		led3.off()
		ledButton3["text"]="Turn Green Led On"
	else:
		led3.on()
		ledButton3["text"]="Turn Green Led Off"	
		

# Menu Widgets
ledButton1= Button(win,text="Turn Red Led On",font=myFont, command =ledToggle1, bg='bisque2',height=2,width=24)
ledButton1.grid(row=0,column=1)

ledButton2= Button(win,text="Turn Yellow Led On",font=myFont, command =ledToggle2, bg='bisque2',height=2,width=24)
ledButton2.grid(row=1,column=1)

ledButton3= Button(win,text="Turn Green Led On",font=myFont, command =ledToggle3, bg='bisque2',height=2,width=24)
ledButton3.grid(row=2,column=1)

exitButton= Button(win,text="Exit",font=myFont, command =exit, bg='red',height=2,width=6)
exitButton.grid(row=3,column=1)



