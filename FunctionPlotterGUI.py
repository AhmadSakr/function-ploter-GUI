# libraries importing
from PyQt5.QtWidgets import QGridLayout,QLabel, QLineEdit, QPushButton,QMessageBox, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

class Window(QWidget):#main window which inherits from QWidget
    error_message_window_display_state = 1#determine Whether error message window will be displayed or not
    saveImagePath="plottedImage(logic).png"
    # constructor
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        self.figure = plt.figure()# a figure instance to plot on

        self.canvas = FigureCanvas(self.figure)# a canvas widget that displays the figure

        self.canvas.setMinimumSize(400,400)#set canvas minimum size to 400*400 to be fully seen
        #creating some UI components
        self.plotButton = QPushButton('Plot')#create QPushButton named plotButton
        self.equationLabel = QLabel('enter the equation')#create QLabel named equationLabel
        self.xMinLabel = QLabel('enter xMin')#create QLabel named xMinLabel
        self.xMaxLabel = QLabel('enter xMax')#create QLabel named xMaxLabel
        self.equationText = QLineEdit(self)#create QLineEdit named equationText
        self.xMinText = QLineEdit(self)#create QLineEdit named xMinText
        self.xMaxText = QLineEdit(self)#create QLineEdit named xMaxText
        self.plotButton.clicked.connect(lambda :self.plot(self.equationText.text(),self.xMinText.text(),self.xMaxText.text(),100,self.saveImagePath))#perfrom plot function on click

        layout = QGridLayout()# creating a QGridLayout

        # adding components to the layout
        layout.addWidget(self.canvas,0,0,1,6)#adding canvas starting from (0,0) with 6*1 dimensions
        layout.addWidget(self.plotButton,1,0)#adding plotButton starting from (1,0) with 1*1 dimensions
        layout.addWidget(self.equationLabel,1,1)#adding equationLabel starting from (1,1) with 1*1 dimensions
        layout.addWidget(self.equationText,1,2,1,4)#adding equationText starting from (1,2) with 4*1 dimensions
        layout.addWidget(self.xMinLabel,2,0)#adding xMinLabel starting from (2,0) with  1*1 dimensions
        layout.addWidget(self.xMinText,2,1,1,2)#adding xMinText starting from (2,1) with 2*1 dimensions
        layout.addWidget(self.xMaxLabel,2,3)#adding xMaxLabel starting from (2,3) with 3*1 dimensions
        layout.addWidget(self.xMaxText,2,4,1,2)#adding xMaxText starting from (2,4) with 2*1 dimensions

        self.setLayout(layout)#setting the layout to the main window

    def plot(self, equation_text, xMin_text, xMax_text, no_of_points, saveImagePathValue):#plot function which is performed on clicking on the plot button

        self.figure.clear()#to clear old figures

        axis = self.figure.add_subplot(111)#creating axis in figure with 1 no of rows 1 no of cols and index 1

        if str(self.xMinText.text()) == str(""):  # check if the xMinText is empty
            self.display_error_message("xMin error massage", "empty xMin text")  # display error message with "xMin error massage" as a title and "empty xMin text" as a text
        else:
            try:
                xMin = float(self.xMinText.text())  # try to get xMin value from xMinText
            except:
                self.display_error_message("minimum x value error", "wrong value")  # display error message with "minimum x value error" as a title and "wrong value" as a text
        if str(self.xMaxText.text()) == str(""):  # check if the xMaxText is empty
            self.display_error_message("xMax error massage", "empty xMax text")  # display error message with "xMax error massage" as a title and "empty xMax text" as a text
        else:
            try:
                xMax = float(self.xMaxText.text())  # try to get xMax value from xMaxText
            except:
                self.display_error_message("maximum x value error", "wrong value")  # display error message with "maximum x value error" as a title and "wrong value" as a text
        if self.equationText.text() == str(""):  # check if the equationText is empty
            self.display_error_message("equation error massage", "empty equation")  # display error message with "equation error massage" as a title and "empty equation" as a text
        else:
            try:#call the function to get x and y values needed to plot
                x, y = self.equation_xmin_xmax_evaluate(equation_text, xMin_text, xMax_text, no_of_points)
                axis.plot(x, y)#plot the equation
                self.canvas.draw()# refresh canvas
                plt.savefig(str(saveImagePathValue))#save current plotted figure to be tested
                plotedImage = Image.open(str(saveImagePathValue))#get current plotted figure to be tested
                return plotedImage#return plotedImage
            except:
                self.display_error_message("equation error massage", "wrong operation")#display error message if any other error happended

    def display_error_message(self,errorWindowTitleText,errorWindowText):#diplay error messages
        self.msg = QMessageBox()#create QMessageBox
        self.msg.setWindowTitle(str(errorWindowTitleText))#create QMessageBox title
        self.msg.setText(str(errorWindowText))#create QMessageBox text
        self.msg.setIcon(QMessageBox.Critical)#set the severity level of the message
        if(self.error_message_window_display_state == 1):#determine Whether error message window will be displayed or not
            x = self.msg.exec_()#exceute error message display
        errorMessageTitle = self.msg.windowTitle()#get the title of error messege for testing
        errorMessageText = self.msg.text()#get the text of error messege for testing
        return errorMessageTitle, errorMessageText#return their values for testing purposes

    # evaluate the values of x and y, and validate equation string
    def equation_xmin_xmax_evaluate(self, equation_text, xMin_text, xMax_text, no_of_points):#get x , y and no of points values needed to plot
        x = np.linspace(float(xMin_text), float(xMax_text), int(no_of_points))#get start, end and no of points of x
        equ = self.validate_equation(equation_text)#call validate_equation function
        y = eval(equ)#return the result evaluated from the equ string
        return x,y#return values of x and y
    def validate_equation(self,equation_text_to_be_validated):# validated the entered equation
        equation_text_to_be_validated = equation_text_to_be_validated.replace("X", "x")#replace any uppercase X by lowercase x
        equation_text_to_be_validated = equation_text_to_be_validated.replace("^", "**")#replace any ^ by ** to perform power operation proprly
        validated_equation = equation_text_to_be_validated
        return validated_equation#return the validated_equation

