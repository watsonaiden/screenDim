# importing the required libraries 

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from tkinter import *


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        #keeps the window on top level even when user clicks
        QMainWindow.__init__(self, None, Qt.WindowStaysOnTopHint)

        #makes mouse events pass through window
        self.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        # removes frame
        self.setWindowFlag(Qt.FramelessWindowHint)

        #removes from taskbar
        self.setWindowFlag(Qt.Tool)

        # makes window semi transparent
        self.setWindowOpacity(0)

        # makes window black
        self.setStyleSheet("background-color:black;")
        self.showFullScreen()
        # show all the widgets
        self.show()

    def changeBrightess(self, brightness):
        self.setWindowOpacity(brightness)

def addslider(master):
    w = tkinter.Scale(master, from_=0, to=100, orient=tkinter.HORIZONTAL)
    w.pack()
    return w


def sel():
   selection = "Value = " + str(var.get())
   label.config(text = selection)


def sliderChange(event):
    brightness = scale.get()/100
    window.changeBrightess(brightness)

layer = QApplication(sys.argv)
root = Tk()
var = DoubleVar()
scale = Scale( root, variable = var,orient=HORIZONTAL, command = sliderChange)
scale.pack(anchor=CENTER)

label = Label(root)
label.pack()
window = Window()
# start the app
root.mainloop()
sys.exit(layer.exec())
