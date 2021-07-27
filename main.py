################################################################################
##
## BY: WANDERSON M.PIMENTA
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
################################################################################

import sys


from PyQt5.QtWidgets import *
from PyQt5 import uic

from LoadingWindow import *

## ==> YOUR APPLICATION WINDOW
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()#调用父类的构造函数
        uic.loadUi(r'main.ui', self)
        ## ==> SET VALUES TO DEF progressBarValue
        def setValue(self, slider, labelPercentage, progressBarName, color):

            # GET SLIDER VALUE
            value = slider.value()

            # CONVERT VALUE TO INT
            sliderValue = int(value)

            # HTML TEXT PERCENTAGE
            htmlText = """<p align="center"><span style=" font-size:50pt;">{VALUE}</span><span style=" font-size:40pt; vertical-align:super;">%</span></p>"""
            labelPercentage.setText(htmlText.replace("{VALUE}", str(sliderValue)))

            # CALL DEF progressBarValue
            self.progressBarValue(sliderValue, progressBarName, color)

        ## ==> APPLY VALUES TO PROGREESBAR
        self.sliderCPU.valueChanged.connect(lambda: setValue(self, self.sliderCPU, self.labelPercentageCPU, self.circularProgressCPU, "rgba(85, 170, 255, 255)"))
        self.sliderGPU.valueChanged.connect(lambda: setValue(self, self.sliderGPU, self.labelPercentageGPU, self.circularProgressGPU, "rgba(85, 255, 127, 255)"))
        self.sliderRAM.valueChanged.connect(lambda: setValue(self, self.sliderRAM, self.labelPercentageRAM, self.circularProgressRAM, "rgba(255, 0, 127, 255)"))

        ## ==> DEF START VALUES
        self.sliderCPU.setValue(25)
        self.sliderGPU.setValue(65)
        self.sliderRAM.setValue(45)


    ## DEF PROGRESS BAR VALUE
    ########################################################################
    def progressBarValue(self, value, widget, color):

        # PROGRESSBAR STYLESHEET BASE
        styleSheet = """
        QFrame{
        	border-radius: 110px;
        	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 0, 127, 0), stop:{STOP_2} {COLOR});
        }
        """

        # GET PROGRESS BAR VALUE, CONVERT TO FLOAT AND INVERT VALUES
        # stop works of 1.000 to 0.000
        progress = (100 - value) / 100.0

        # GET NEW VALUES
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        # FIX MAX VALUE
        if value == 100:
            stop_1 = "1.000"
            stop_2 = "1.000"

        # SET VALUES TO NEW STYLESHEET
        newStylesheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2).replace("{COLOR}", color)

        # APPLY STYLESHEET WITH NEW VALUES
        widget.setStyleSheet(newStylesheet)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    lw = LoadingWindow(delayTime=20, mainWindow=window)
    sys.exit(app.exec_())
