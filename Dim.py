# importing the required libraries 

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


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
        self.setWindowOpacity(.8)

        # setting  the geometry of window
        self.setGeometry(60, 60, 600, 400)

        # makes window black
        self.setStyleSheet("background-color:black;")
        self.showFullScreen()
        # show all the widgets
        self.show()

App = QApplication(sys.argv)

# create the instance of our Window 
window = Window()

# start the app 
sys.exit(App.exec()) 