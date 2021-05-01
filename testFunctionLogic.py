
from PyQt5.QtWidgets import QApplication
import numpy as np
import sys
from PIL import Image
import FunctionPlotterGUI

QTApp = QApplication(sys.argv)# create a pyqt5 application
testWindow = FunctionPlotterGUI.Window() # create a window object
testWindow.error_message_window_display_state =0
#testWindow.show()
#sys.exit(QTApp.exec_())
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
def test_plot():
    plotedImageTest = testWindow.plot("x^3",-5,5,100,"plottedImage(logic).png")
    plotedImageRefernce = Image.open('plotedImageReference.png')
    #compute the sum of the squared differences as an image similarity metric
    sum_sq_diff = np.sum((np.asarray(plotedImageTest).astype('float') - np.asarray(plotedImageRefernce).astype('float')) ** 2)
    assert sum_sq_diff == 0



