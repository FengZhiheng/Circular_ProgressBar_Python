
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QColor

class LoadingWindow(QMainWindow):
    counter = 0
    jumper = 10
    def __init__(self, delayTime = 10, mainWindow = None):
        super(LoadingWindow, self).__init__()#调用父类的构造函数
        uic.loadUi(r'splash_screen.ui', self)
        self.mainWindow = mainWindow
        ## ==> SET INITIAL PROGRESS BAR TO (0) ZERO
        self.progressBarValue(0)

        ## ==> REMOVE STANDARD TITLE BAR
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) # Remove title bar
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground) # Set background to transparent

        ## ==> APPLY DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 120))
        self.circularBg.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(delayTime)
        self.show()

        ## DEF TO LOANDING
    ########################################################################
    def progress (self):
        # global counter
        # global jumper
        value = self.counter

        # HTML TEXT PERCENTAGE
        htmlText = """<p><span style=" font-size:58pt;">{VALUE}</span><span style=" font-size:48pt; vertical-align:super;">%</span></p>"""

        # REPLACE VALUE
        newHtml = htmlText.replace("{VALUE}", str(self.jumper))

        if(value > self.jumper):
            # APPLY NEW PERCENTAGE TEXT
            self.labelPercentage.setText(newHtml)
            self.jumper += 10

        # SET VALUE TO PROGRESS BAR
        # fix max value error if > than 100
        if value >= 100: value = 1.000
        self.progressBarValue(value)

        # CLOSE SPLASH SCREE AND OPEN APP
        if self.counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            # self.main = MainWindow()
            if self.mainWindow is not None:
                self.mainWindow.show()
            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        self.counter += 0.5

    ## DEF PROGRESS BAR VALUE
    ########################################################################
    def progressBarValue(self, value):

        # PROGRESSBAR STYLESHEET BASE
        styleSheet = """
        QFrame{
        	border-radius: 150px;
        	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 0, 127, 0), stop:{STOP_2} rgba(85, 170, 255, 255));
        }
        """

        # GET PROGRESS BAR VALUE, CONVERT TO FLOAT AND INVERT VALUES
        # stop works of 1.000 to 0.000
        progress = (100 - value) / 100.0

        # GET NEW VALUES
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        # SET VALUES TO NEW STYLESHEET
        newStylesheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)

        # APPLY STYLESHEET WITH NEW VALUES
        self.circularProgress.setStyleSheet(newStylesheet)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    lw = LoadingWindow(10)
    sys.exit(app.exec_())

