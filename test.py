from Tkinter import *

root = Tk() #Makes the window GUI will be displayed on
root.wm_title("Window Title") #Makes title that will appear on topleft
root.config(background = "#FFFFFF") #Sets background color to white

#Put Widgets here

leftFrame = Frame(root, width=200, height=600)
leftFrame.grid(row=0, column=0, padx=10, pady=2)

##firstLabel = Label(leftFrame, text="This is  my first label")
##firstLabel.grid(row=0, column=0, padx=2, pady=2)

##imageEx = PhotoImage(file = 'IMG_0000.pgm')
##Label(leftFrame, image=imageEx).grid(row=0, column=0, padx=10, pady=2)

def A():
    print("Hello, how are you?")
def B():
    print("I'm doing very well Dave")
def C():
    print("...")
def D():
    print("I'm afraid I can't do that Dave")
    
newButton = Button(leftFrame, text="Hello HAL", command=A)
newButton.grid(row=0, column=0, padx=10, pady=2)
newButton = Button(leftFrame, text="I'm doing well, yourself?", command=B)
newButton.grid(row=5, column=0, padx=10, pady=2)
newButton = Button(leftFrame, text="Did you lock the podbay doors HAL?", command=C)
newButton.grid(row=10, column=0, padx=10, pady=2)
newButton = Button(leftFrame, text="Open the podbay doors HAL", command=D)
newButton.grid(row=15, column=0, padx=10, pady=2)


root.mainloop() #Start monitoring and updating the GUI. Nothing below here runs.
