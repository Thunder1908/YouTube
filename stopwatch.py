import functools

import pygame
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, Qt


class Ui_Form(QtWidgets.QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(821, 523)
        Form.setStyleSheet("background-color:black")
        self.labelImage = QtWidgets.QLabel(Form)
        self.labelImage.setGeometry(QtCore.QRect(560, 0, 381, 671))
        self.labelImage.setText("")
        self.labelImage.setPixmap(QtGui.QPixmap("../../../Downloads/pexels-golden-jojo-2409038 (1).jpg"))
        self.labelImage.setObjectName("labelImage")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(360, 540, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:white; \n"
                                   "\n"
                                   "border-radius:5px")
        self.label_7.setObjectName("label_7")
        self.labelAlarms = QtWidgets.QLabel(Form)
        self.labelAlarms.setGeometry(QtCore.QRect(590, 50, 191, 71))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(18)
        self.labelAlarms.setFont(font)
        self.labelAlarms.setStyleSheet("color:white;\n"
                                       "background-color:rgba(20,20,20,0)")
        self.labelAlarms.setObjectName("labelAlarms")
        self.labelTimer = QtWidgets.QLabel(Form)
        self.labelTimer.setGeometry(QtCore.QRect(590, 140, 191, 71))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(18)
        self.labelTimer.setFont(font)
        self.labelTimer.setStyleSheet("color:white;\n"
                                      "background-color:rgba(20,20,20,0)")
        self.labelTimer.setObjectName("labelTimer")
        self.labelStopwatch = QtWidgets.QLabel(Form)
        self.labelStopwatch.setGeometry(QtCore.QRect(590, 230, 191, 71))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(18)
        self.labelStopwatch.setFont(font)
        self.labelStopwatch.setStyleSheet("color:white;\n"
                                          "background-color:rgba(20,20,20,0)")
        self.labelStopwatch.setObjectName("labelStopwatch")
        self.labelSettings = QtWidgets.QLabel(Form)
        self.labelSettings.setGeometry(QtCore.QRect(40, 40, 61, 61))
        self.labelSettings.setStyleSheet("border-radius:30px;\n"
                                         "background-color:rgba(20,20,20,0)")
        self.labelSettings.setText("")
        self.labelSettings.setPixmap(QtGui.QPixmap("../../../Downloads/icons8-settings-32.png"))
        self.labelSettings.setObjectName("labelSettings")
        self.labelReminders = QtWidgets.QLabel(Form)
        self.labelReminders.setGeometry(QtCore.QRect(590, 320, 191, 71))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(18)
        self.labelReminders.setFont(font)
        self.labelReminders.setStyleSheet("color:white;\n"
                                          "background-color:rgba(20,20,20,0)")
        self.labelReminders.setObjectName("labelReminders")
        self.widgetStopwatch = QtWidgets.QWidget(Form)
        self.widgetStopwatch.setGeometry(QtCore.QRect(60, 50, 471, 441))
        self.widgetStopwatch.setObjectName("widgetStopwatch")
        self.labelStopwatchStartbutton = QtWidgets.QLabel(self.widgetStopwatch)
        self.labelStopwatchStartbutton.setGeometry(QtCore.QRect(190, 280, 101, 101))
        self.labelStopwatchStartbutton.setStyleSheet("border-radius:10px;\n"
                                                     "\n"
                                                     "background-color: rgb(52, 98, 63);")
        self.labelStopwatchStartbutton.setText("")
        self.labelStopwatchStartbutton.setPixmap(QtGui.QPixmap("../../../Downloads/icons8-play-50.png"))
        self.labelStopwatchStartbutton.setAlignment(QtCore.Qt.AlignCenter)
        self.labelStopwatchStartbutton.setObjectName("labelStopwatchStartbutton")
        self.labelStopwatchClockHours = QtWidgets.QLabel(self.widgetStopwatch)
        self.labelStopwatchClockHours.setGeometry(QtCore.QRect(70, 80, 101, 151))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(72)
        self.labelStopwatchClockHours.setFont(font)
        self.labelStopwatchClockHours.setStyleSheet("color:white")
        self.labelStopwatchClockHours.setObjectName("labelStopwatchClockHours")
        self.labelStopwatchClockMinutes = QtWidgets.QLabel(self.widgetStopwatch)
        self.labelStopwatchClockMinutes.setGeometry(QtCore.QRect(200, 80, 101, 151))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(72)
        self.labelStopwatchClockMinutes.setFont(font)
        self.labelStopwatchClockMinutes.setStyleSheet("color:white")
        self.labelStopwatchClockMinutes.setObjectName("labelStopwatchClockMinutes")
        self.labelStopwatchClockSeconds = QtWidgets.QLabel(self.widgetStopwatch)
        self.labelStopwatchClockSeconds.setGeometry(QtCore.QRect(330, 80, 101, 151))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(72)
        self.labelStopwatchClockSeconds.setFont(font)
        self.labelStopwatchClockSeconds.setStyleSheet("color:white")
        self.labelStopwatchClockSeconds.setObjectName("labelStopwatchClockSeconds")
        self.labelStopwatchcolon1 = QtWidgets.QLabel(self.widgetStopwatch)
        self.labelStopwatchcolon1.setGeometry(QtCore.QRect(170, 120, 20, 61))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(48)
        self.labelStopwatchcolon1.setFont(font)
        self.labelStopwatchcolon1.setStyleSheet("color:white")
        self.labelStopwatchcolon1.setObjectName("labelStopwatchcolon1")
        self.labelStopwatchcolon2 = QtWidgets.QLabel(self.widgetStopwatch)
        self.labelStopwatchcolon2.setGeometry(QtCore.QRect(300, 120, 20, 61))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(48)
        self.labelStopwatchcolon2.setFont(font)
        self.labelStopwatchcolon2.setStyleSheet("color:white")
        self.labelStopwatchcolon2.setObjectName("labelStopwatchcolon2")
        self.widgetStopwatch.raise_()
        self.labelImage.raise_()
        self.label_7.raise_()
        self.labelAlarms.raise_()
        self.labelTimer.raise_()
        self.labelStopwatch.raise_()
        self.labelSettings.raise_()
        self.labelReminders.raise_()

        self.labelStopwatchPausebutton = QtWidgets.QLabel(self.widgetStopwatch)
        self.labelStopwatchPausebutton.setGeometry(QtCore.QRect(190, 280, 101, 101))
        self.labelStopwatchPausebutton.setStyleSheet("border-radius:10px;\n"
                                                     "\n"
                                                     "background-color: rgb(52, 98, 63);")
        self.labelStopwatchPausebutton.setText("")
        self.labelStopwatchPausebutton.setPixmap(QtGui.QPixmap("../../../Downloads/icons8-pause-50"))
        self.labelStopwatchPausebutton.setAlignment(QtCore.Qt.AlignCenter)

        self.labelStopwatchPausebutton.hide()

        self.labelStopwatchResetbutton = QtWidgets.QLabel(self.widgetStopwatch)
        self.labelStopwatchResetbutton.setGeometry(QtCore.QRect(90, 300, 61, 61))
        self.labelStopwatchResetbutton.setStyleSheet("border-radius:10px;\n"
                                                     "\n"
                                                     "background-color: rgb(20,20,20);")
        self.labelStopwatchResetbutton.setText("")
        self.labelStopwatchResetbutton.setPixmap(QtGui.QPixmap("../../../Downloads/icons8-reset-30 (1)"))
        self.labelStopwatchResetbutton.setAlignment(QtCore.Qt.AlignCenter)

        self.labelStopwatchPausebutton.mousePressEvent = functools.partial(self.pauseStopwatch)
        self.labelStopwatchStartbutton.mousePressEvent = functools.partial(self.startStopwatch)
        self.labelStopwatchResetbutton.mousePressEvent = functools.partial(self.resetStopwatch)

        self.labelStopwatchResetbutton.hide()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_7.setText(_translate("Form", "<html><head/><body><p align=\"center\">Hours</p></body></html>"))
        self.labelAlarms.setText(_translate("Form", "<html><head/><body><p align=\"center\">Alarms</p></body></html>"))
        self.labelTimer.setText(_translate("Form", "<html><head/><body><p align=\"center\">Timer</p></body></html>"))
        self.labelStopwatch.setText(
            _translate("Form", "<html><head/><body><p align=\"center\">Stopwatch</p></body></html>"))
        self.labelReminders.setText(
            _translate("Form", "<html><head/><body><p align=\"center\">Reminders</p></body></html>"))
        self.labelStopwatchClockHours.setText(_translate("Form", "00"))
        self.labelStopwatchClockMinutes.setText(_translate("Form", "00"))
        self.labelStopwatchClockSeconds.setText(_translate("Form", "00"))
        self.labelStopwatchcolon1.setText(_translate("Form", ":"))
        self.labelStopwatchcolon2.setText(_translate("Form", ":"))

    def startStopwatch(self, event):
        # Changing the icon from play to pause

        self.labelStopwatchPausebutton.show()
        self.labelStopwatchStartbutton.hide()
        self.labelStopwatchResetbutton.hide()

        self.timerStopwatch = QTimer(self)
        self.timerStopwatch.timeout.connect(self.showTime)
        self.timerStopwatch.start(1000)

        pass

    def showTime(self):

        stopwatchTimeSeconds = int(self.labelStopwatchClockSeconds.text())
        stopwatchTimeMinutes = int(self.labelStopwatchClockMinutes.text())
        stopwatchTimeHours = int(self.labelStopwatchClockHours.text())

        newtimeSeconds = stopwatchTimeSeconds + 1

        self.labelStopwatchClockSeconds.setText(f"{newtimeSeconds}")
        print(newtimeSeconds)

        if len(str(newtimeSeconds)) < 2:
            self.labelStopwatchClockSeconds.setText(f"0{newtimeSeconds}")

        else:
            self.labelStopwatchClockSeconds.setText(f"{newtimeSeconds}")

        if newtimeSeconds == 60:

            self.labelStopwatchClockSeconds.setText("00")
            newtimeMinutes = stopwatchTimeMinutes + 1

            if len(str(newtimeMinutes)) < 2:
                self.labelStopwatchClockMinutes.setText(f"0{newtimeMinutes}")

            else:
                self.labelStopwatchClockMinutes.setText(f"{newtimeMinutes}")

            if newtimeMinutes == 60:

                self.labelStopwatchClockMinutes.setText("00")
                newtimeHours = stopwatchTimeHours + 1

                if len(str(newtimeHours)) < 2:
                    self.labelStopwatchClockHours.setText(f"0{newtimeHours}")

                else:
                    self.labelStopwatchClockHours.setText(f"{newtimeHours}")

    def pauseStopwatch(self, event):

        self.labelStopwatchPausebutton.hide()
        self.labelStopwatchStartbutton.show()
        self.labelStopwatchResetbutton.show()
        self.timerStopwatch.stop()

    def resetStopwatch(self,event):

        self.pauseStopwatch(None)

        self.labelStopwatchClockSeconds.setText("00")
        self.labelStopwatchClockMinutes.setText("00")
        self.labelStopwatchClockHours.setText("00")



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
