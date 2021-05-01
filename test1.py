
import pytest
import main

from PyQt5.QtWidgets import QDialog, QApplication
from PySide2 import QtCore

from PyQt5.QtWidgets import QDialog, QApplication, QGridLayout,QLabel, QLineEdit, QPushButton,QMessageBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np
import sys

QTApp = QApplication(sys.argv)# create a pyqt5 application
testWindow = main.Window() # create a window object
#testWindow.show()

def test_equation_xmin_xmax_evaluate():
    x,y= testWindow.equation_xmin_xmax_evaluate("x^2",-5,5,10)
    i = np.linspace(-5,5,10)
    j = i**2
    assert set(i) == set(x)
    assert set(j) == set(y)
def test_validate_equation():
    validatedEquation = testWindow.validate_equation("X^2")
    assert validatedEquation == "x**2"
def test_display_error_message():
    errMsgTitle,errMsgTest =testWindow.display_error_message("errorMessageTitle","errorMessageText")
    assert errMsgTitle =="errorMessageTitle"
    assert errMsgTest =="errorMessageText"
#sys.exit(QTApp.exec_())
