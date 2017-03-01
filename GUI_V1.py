from Tkinter import *

root = Tk() #Makes the window GUI will be displayed on
root.wm_title("Fahrenheit 162 - GUI V1") #Makes title that will appear on topleft
root.config(background = "#FFFFFF") #Sets background color to white

##w,h = root.winfo_screenwidth(),root.winfo_screenheight()
##root.overrideredirect(1)
##root.geometry("%dx%d+0+0" % (w,h))





#Put Widgets here
frame1 = Frame(root, width=200, height=600)
frame1.grid(row=0, column=0, padx=10, pady=2)

# Pressing button1 will run our prototype executable file
import os
def A():
    os.system('/home/pi/prototype/prototype')
button1 = Button(frame1, text = "Click Me", command=A)
button1.grid(row=0,column=0,padx=10,pady=2)

# Define a function to close window
def close(event=None):
    root.destroy()

button2 = Button(frame1, text = "Exit Program", command=close)
button2.grid(row=0,column=5,padx=10,pady=2)

label1 = Label(frame1,text="Put yo thang herrr").grid(row=5,column=0)
input1 = Entry(frame1)
input1.grid(row=7,column=0)

def show():
    x = input1.get()
    x*5
button3 = Button(frame1,text="Show me the money",command=show)
button3.grid(row=10,column=0,padx=10,pady=2)




root.mainloop() #Start monitoring and updating the GUI. Nothing below here runs.
