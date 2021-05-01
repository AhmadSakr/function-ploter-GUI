# function-ploter-GUI
### a simply function ploter GUI which can do the following:
1. take an arbitrary equation from user with minimum and maximum x values (supported operatons: + - * / ^) and simply plot it
2. has resizable GUI components (GridLayout)
3. has logic testing codes (pytest) and GUI tesing codes (pytest-qt)
4. display error messages in case of entering any inappropriate inputs:
* display error message if xminText, xmaxText or equationText is empty
* display error message if xminText or xmaxText is not a number
* display error message if equationText is not written properly 
* display error message if any other error happened

### how to use it:
1. install python libiraries using pip command (pip install libName) (in python terminal) written in libiraries version text file
2. to run qtbot(pytest-qt) you must have python 3.6+
3. you must set the PYTEST_QT_API environment variable to pyqt5
4. simply open python main file and run it and the window will be displayed 
5. enter the equation you want to plot in a textLine next to "enter the equation"
6. enter the minimun value of x in a textLine next to "enter xMin"
7. enter the maximum value of x in a textLine next to "enter xMax"
8. then click on plot to plot the entered equation with xMin and xMax values
9. to run testing codes:
* run testFunctionLogic.py to test all functions of FunctionPlotterGUI.py
* run testGUI.py to test GUI of FunctionPlotterGUI.py (qtbot simulates GUI clicks and text input)
