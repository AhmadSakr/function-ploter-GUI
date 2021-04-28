# importing various libraries
import sys
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import random
import matplotlib.pyplot as plt
import numpy as np
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize

# main window
# which inherits QDialog
class Window(QDialog):

    # constructor
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        # a figure instance to plot on
        self.figure = plt.figure()

        # this is the Canvas Widget that
        # displays the 'figure'it takes the
        # 'figure' instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # Just some button connected to 'plot' method
        self.button = QPushButton('Plot')

        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Name:')
        self.equationText = QLineEdit(self)
        self.xMinText = QLineEdit(self)
        self.xMaxText = QLineEdit(self)

        self.line.move(80, 20)
        self.line.resize(200, 32)
        self.nameLabel.move(20, 20)

        # adding action to the button
        self.button.clicked.connect(self.plot)

        # creating a Vertical Box layout
        layout = QVBoxLayout()

        # adding canvas to the layout
        layout.addWidget(self.canvas)

        # adding push button to the layout
        layout.addWidget(self.button)
        layout.addWidget(self.nameLabel)
        layout.addWidget(self.line)


        # setting layout to the main window
        self.setLayout(layout)

    # action called by thte push button
    def plot(self):
        # random data
        data = [random.random() for i in range(10)]

        # clearing old figure
        self.figure.clear()

        # create an axis
        ax = self.figure.add_subplot(111)

        equ = str(input("enter t"))

        xMin = int(input("xMin"))
        xMax = int(input("xMax"))

        x = np.linspace(xMin, xMax, 100)
        equ = equ.replace("X", "x")
        equ = equ.replace("^", "**")
        y = eval(equ)


        # plot data
        ax.plot(x,y)

        # refresh canvas
        self.canvas.draw()


# driver code
if __name__ == '__main__':
    # creating apyqt5 application
    app = QApplication(sys.argv)

    # creating a window object
    main = Window()

    # showing the window
    main.show()

    # loop
    sys.exit(app.exec_())