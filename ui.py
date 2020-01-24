import tkinter as tk

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
reader = SimpleMFRC522()
GPIO.cleanup

#---DONE IMPORT

root = tk.Tk()
root.title('Vendors')

#---WINDOW TO CENTer
winWidth = root.winfo_reqwidth()
winwHeight = root.winfo_reqheight()
posRight = int(root.winfo_screenwidth() / 2 - winWidth / 2)
posDown = int(root.winfo_screenheight() / 2 - winwHeight / 2)
root.geometry("+{}+{}".format(posRight, posDown))

#---INITIALIZING
nameString = tk.StringVar()
courseString = tk.StringVar()
schoolIdString = tk.StringVar()
priceString = tk.StringVar()

#---BUTTON TRIGGERS
def confirm():
	id, data, = reader.read() #id, text
	
	schoolId = data.split(",")[0]
	name = data.split(",")[1]
	course = data.split(",")[2]
	amount = data.split(",")[3]	
	
	deduc = priceString.get()

	totalAmount = int(amount) - int(deduc) 
	reader.write(schoolId+","+name+","+course+","+str(totalAmount))
	
	nameString.set('------')
	courseString.set('------')
	schoolIdString.set('------')
	priceString.set('------')
	
	root.after(1500, readRfidData)

#---LABEL
tk.Label(root, text = "Name").grid(row=0,column=0, sticky = "W")
tk.Label(root, text = "Course").grid(row=2,column=0, sticky = "W")
tk.Label(root, text = "ID Number").grid(row=4,column=0, sticky = "W")
tk.Label(root, text = "Enter Price").grid(row=1,column=2, sticky = "E")
tk.Label(root, text = "Php").grid(row=2,column=3, sticky = "W")

#---TEXTFIELD
tk.Entry(root, textvariable = nameString, width = 25).grid(row=1,column=0, pady=(0,10))
tk.Entry(root, textvariable = courseString, width = 25).grid(row=3,column=0, pady=(0,10))
tk.Entry(root, textvariable = schoolIdString, width = 25).grid(row=5,column=0, pady=(0,10))
tk.Entry(root, textvariable = priceString, width = 15).grid(row=2,column=1,columnspan = 2, padx = (10,0), sticky = "E")	#price
	
#---BUTTON
tk.Button(root, text = 'Confirm', command = confirm).grid(row=3,column=1)
tk.Button(root, text = 'Exit', command = root.destroy).grid(row=3,column=2)

	
#---READER HERE
def readRfidData():
	id, data, = reader.read() #id, text
	
	schoolId = data.split(",")[0]
	name = data.split(",")[1]
	course = data.split(",")[2]
	amount = data.split(",")[3]		
	
	try:
		nameString.set(name)
		courseString.set(course)
		schoolIdString.set(schoolId)
		priceString.set('0')
		
	finally:
		GPIO.cleanup
	print(schoolId, name, course, amount)
	#reader.write(schoolId+","+name+","+course+","+str(totalamount))
	root.mainloop()

root.after(0, readRfidData)
root.mainloop()
