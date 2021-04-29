# libraries importing
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout, QGridLayout, QFormLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np
import sys
from PIL import Image

from PyQt5.QtWidgets import QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton,QMessageBox
from PyQt5 import QtCore, QtGui
class Window(QDialog):

    # constructor
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        # a figure instance to plot on
        self.figure = plt.figure()
        self.figure
        self.test_image = QtGui.QImage()
        self.test_image.load('1.png')
        self.test_image.save('x.png')

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

        self.error_messages_handling()
        try:
            x, y = self.equation_xmin_xmax_evaluate(self.equationText.text(), self.xMinText.text(), self.xMaxText.text(), 100)
            ax.plot(x, y)
        except:
            self.display_error_message("equation error massage", "wrong operation")

        self.canvas.draw()
        plt.savefig('foo.png')


    def display_error_message(self,errorWindowTitleText,errorWindowText):
        self.msg = QMessageBox()
        self.msg.setWindowTitle(str(errorWindowTitleText))
        self.msg.setText(str(errorWindowText))
        self.msg.setIcon(QMessageBox.Critical)
        x = self.msg.exec_()
    def error_messages_handling(self):
        print('')
        if  str(self.xMinText.text()) == str(""):
            self.display_error_message("xMin error massage", "empty xMin text")

        else:
            try:
                xMin = float(self.xMinText.text())
            except:
                self.display_error_message("minimum x value error", "wrong value")

        if  str(self.xMaxText.text()) == str(""):
            self.display_error_message("xMax error massage", "empty xMax text")
        else:
            try:
                xMax = float(self.xMaxText.text())
            except:
                self.display_error_message("maximum x value error", "wrong value")

        if  self.equationText.text() == str(""):
            self.display_error_message("equation error massage", "empty equation")

    def equation_xmin_xmax_evaluate(self, equation_text, xMin_text, xMax_text, no_of_points):

        x = np.linspace(float(xMin_text), float(xMax_text), int(no_of_points))

        equ = self.validate_equation(equation_text)
        y = eval(equ)
        return x,y
    def validate_equation(self,equation_text_to_be_validated):
        equation_text_to_be_validated = str(equation_text_to_be_validated)
        equation_text_to_be_validated = equation_text_to_be_validated.replace("X", "x")
        equation_text_to_be_validated = equation_text_to_be_validated.replace("^", "**")
        validated_equation = equation_text_to_be_validated
        return validated_equation
if __name__ == '__main__':
    # creating a pyqt5 application
    app = QApplication(sys.argv)

    # creating a window object
    main = Window()

    # showing the window
    main.show()

    # loop
    sys.exit(app.exec_())