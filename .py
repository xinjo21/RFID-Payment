import tkinter as tk
import random
import time

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
reader = SimpleMFRC522()

root = tk.Tk()
root.title('Vendors')
root.resizable(0,0)

nameString = tk.StringVar()
courseString = tk.StringVar()
schoolIdString = tk.StringVar()

class Ven:
    def __init__(tempId, tempName, tempCourse):
        tk.Label(root, text = "Name", width = 10).grid(row=0,column=0, sticky = 'SW')
        tk.Label(root, text = "Course", width = 10).grid(row=2,column=0, sticky = 'SW')
        tk.Label(root, text = "ID Number", width = 10).grid(row=4,column=0, sticky = 'SW')

        nameTF = tk.Entry(root, textvariable = tempName, width = 25).grid(row=1,column=0)
        courseTF = tk.Entry(root, textvariable = tempCourse, width = 25).grid(row=3,column=0)
        idNumTF = tk.Entry(root, textvariable = tempId, width = 25).grid(row=5,column=0)
        
    def setData():
        
        while True:
            temp = id
            id, data = reader.read() #id, text
            schoolId = data.split(",")[0]
            name = data.split(",")[1].replace("\"","")
            course = data.split(",")[2].replace("\"","")
            if id == temp:
                break
            
            nameString.set(tempName)
            courseString.set(tempCourse)
            schoolIdString.set(tempId)
    
    def draw():
        root.after(50, ven.setData())

ven = Ven(schoolId, name, course)
ven.draw()
root.mainloop()
