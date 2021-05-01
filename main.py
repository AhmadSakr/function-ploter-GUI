# libraries importing
from PyQt5.QtWidgets import QApplication
import sys
import FunctionPlotterGUI

if __name__ == '__main__':

    QTApp = QApplication(sys.argv)# create a pyqt5 application
    Window = FunctionPlotterGUI.Window() # create a window object
    Window.show()# show the window
    sys.exit(QTApp.exec_())# loop until closing the system