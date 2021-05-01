# libraries importing
from PyQt5 import QtCore
from PIL import Image
import numpy as np
import FunctionPlotterGUI

def test_hello(qtbot):
    widget = FunctionPlotterGUI.Window()
    widget.error_message_window_display_state = 0
    widget.saveImagePath = "plottedImage(GUI).png"

    qtbot.addWidget(widget)

    qtbot.keyClicks(widget.equationText, 'x^3')

    qtbot.keyClicks(widget.xMinText, '-5')

    qtbot.keyClicks(widget.xMaxText, '5')

    qtbot.mouseClick(widget.plotButton, QtCore.Qt.LeftButton)

    plotedImageTest = Image.open('plottedImage(GUI).png')
    plotedImageRefernce = Image.open('plotedImageReference.png')
    # compute the sum of the squared differences as an image similarity metric
    sum_sq_diff = np.sum(
        (np.asarray(plotedImageTest).astype('float') - np.asarray(plotedImageRefernce).astype('float')) ** 2)
    assert sum_sq_diff == 0