# importing various libraries
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout, QGridLayout, QFormLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np
import sys
from PIL import Image

from PyQt5.QtWidgets import QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton,QMessageBox

class Window(QDialog):

    # constructor
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        # a figure instance to plot on
        self.figure = plt.figure()

        self.canvas = FigureCanvas(self.figure)
        self.canvas.setMinimumSize(400,400)
        self.plotButton = QPushButton('Plot')

        self.equationLabel = QLabel('enter the equation')
        self.xMinLabel = QLabel('enter xMin')
        self.xMaxLabel = QLabel('enter xMax')

        self.equationText = QLineEdit(self)
        self.xMinText = QLineEdit(self)
        self.xMaxText = QLineEdit(self)



        self.plotButton.clicked.connect(self.plot)

        # creating a Vertical Box layout
        layout = QGridLayout()
        layout2 = QVBoxLayout()

        # adding components to the layout
        layout.addWidget(self.canvas,0,0,1,6)
        layout.addWidget(self.plotButton,1,0)
        layout.addWidget(self.equationLabel,1,1)
        layout.addWidget(self.equationText,1,3,1,3)
        layout.addWidget(self.xMinLabel,2,0)
        layout.addWidget(self.xMinText,2,1,1,2)
        layout.addWidget(self.xMaxLabel,2,3)
        layout.addWidget(self.xMaxText,2,4,1,2)


        self.setLayout(layout)

    def plot(self):
        self.figure.clear()

        ax = self.figure.add_subplot(111)

        if  str(self.xMinText.text()) == str(""):
            self.msg = QMessageBox()
            self.msg.setWindowTitle("xMin error massage")
            self.msg.setText("empty xMin text")
            self.msg.setIcon(QMessageBox.Critical)
            x = self.msg.exec_()

        else:
            try:
                xMin = float(self.xMinText.text())
            except:
                print("wrong xMin")
                self.msg = QMessageBox()
                self.msg.setWindowTitle("minimum x value error")
                self.msg.setText("wrong value")
                self.msg.setIcon(QMessageBox.Critical)
                x = self.msg.exec_()



        if  str(self.xMaxText.text()) == str(""):
            self.msg = QMessageBox()
            self.msg.setWindowTitle("xMax error massage")
            self.msg.setText("empty xMax text")
            self.msg.setIcon(QMessageBox.Critical)
            x = self.msg.exec_()
        else:
            try:
                xMax = float(self.xMaxText.text())
            except:
                print("wrong xMax")
                self.msg = QMessageBox()
                self.msg.setWindowTitle("maximum x value error")
                self.msg.setText("wrong value")
                self.msg.setIcon(QMessageBox.Critical)
                x = self.msg.exec_()



        if  self.equationText.text() == str(""):
            self.msg = QMessageBox()
            self.msg.setWindowTitle("equation error massage")
            self.msg.setText("empty equation")
            self.msg.setIcon(QMessageBox.Critical)
            x = self.msg.exec_()
        else:
            try:
                equ = str(self.equationText.text())
                x = np.linspace(xMin, xMax, 100)
                equ = equ.replace("X", "x")
                equ = equ.replace("^", "**")
                y = eval(equ)

                ax.plot(x, y)

            except:
                self.msg = QMessageBox()
                self.msg.setWindowTitle("equation error massage")
                self.msg.setText("wrong operation")
                self.msg.setIcon(QMessageBox.Critical)
                x = self.msg.exec_()


        self.canvas.draw()

if __name__ == '__main__':
    # creating a pyqt5 application
    app = QApplication(sys.argv)

    # creating a window object
    main = Window()

    # showing the window
    main.show()

    # loop
    sys.exit(app.exec_())