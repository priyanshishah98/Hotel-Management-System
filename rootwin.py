from tkinter import *
from PIL import ImageTk, Image

import destination

class MainClass():
    def __init__(self, master):
        self.master = master
        self.master.title("Travel Agency")
        self.master.geometry('1366x768')
        self.background_image = ImageTk.PhotoImage(Image.open("mini.jpg"))
        self.background_label = Label(self.master, image=self.background_image)
        # background_label.place(x=10, y=10, relwidth=1, relheight=1)
        self.background_label.pack(side="bottom", fill="both", expand="yes")

        self.button_1 = Button(self.master, text="Destination", fg="Purple", bg="black", width=25, font=('arial', 20),command=callsignup)
        self.button_1.place(x=470, y=350)

        self.DisL = Label(self.master, text="Latest reviews. Lowest prices.", bg="sky blue", fg="white", width=25,
                          font=('arial', 25))
        self.DisL.place(x=450, y=100)
        # self.DisL.pack(fill=X)





def callsignup():
    destination.start()

def main():
    root = Tk()
    myGUIProj = MainClass(root)
    root.mainloop()

if __name__ == "__main__":
    main()