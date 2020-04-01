import sys
from PyQt5 import QtCore, QtGui, uic

qtCreatorFile = "main.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class myownGUI(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)


        #button
        self.Do_button.clicked.connect(self.action)

        #slider
        self.SLIDER.valueChanged[int].connect(self.SLIDER_update)

        #"global" variable init. by callback
        self.SLIDER_update()


    #The button callback
    def action(self):
        print ("DOING ACTION!")
        print (self.Slider)
        #trying to display the image in the Image_label
        image = QtGui.QImage(QtGui.QImageReader(":/images/test.png").read())
        self.Image_label.setPixmap(QtGui.QPixmap(image))
        #self.Image_label.show() #unuseful command?


    #Slider update callback
    def SLIDER_update(self):
        self.Slider= self.SLIDER.value()
        if (self.Slider % 2 == 0): #even 
            self.Slider = self.Slider + 1
        self.Slider_label.setText(str(self.Slider))

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = myownGUI()
    window.show()
    sys.exit(app.exec_())