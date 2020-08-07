import tkinter

class simpleapp_tk(tkinter.Tk):
    def __init__(self,parent):
        tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()
        self.entryVariable = tkinter.StringVar()
        self.entry = tkinter.Entry(self,textvariable = self.entryVariable)
0
        self.entry.grid(column = 0, row = 0, sticky = 'EW')

        button = tkinter.Button(self,text=u"Click me !", command = self.onButtonClick())
        button.grid(column = 1,row=0)
        label = tkinter.Label(self,textvariable= self.labelVariable,anchor='w',fg="white",bg="blue")
        label.grid(column=0, row=1, columnspan=2,sticky= 'EW')
        self.labelVariable.set("Hello world !")
        self.grid_columnconfigure(0,weight=1)
        self.entry.bind("<Return>", self.onPressEnter()) 
    def onButtonClick(self):
        print("Yeah , well thats TRUE if you want it to be")
    def onPressEnter(self):
        print("Well, i was just kidding dude")

        
if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('GUI coding')
    app.mainloop()
