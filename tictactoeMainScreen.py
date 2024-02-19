from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import functools
import os
import random

turn = "X"
currentBoard = [1, 2, 3, 4, 5, 6, 7, 8, 9]

X = 0
O = 0

os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"


class Ui_Form(object):
    def setupUi(self, Form):

        Form.setWindowFlag(Qt.FramelessWindowHint)
        Form.setObjectName("Form")
        Form.resize(934, 520)
        Form.setStyleSheet("background-color:black")
        self.widgetMain = QtWidgets.QWidget(Form)
        self.widgetMain.setGeometry(QtCore.QRect(30, 50, 521, 421))
        self.widgetMain.setObjectName("widgetMain")
        self.labelTitle = QtWidgets.QLabel(self.widgetMain)
        self.labelTitle.setGeometry(QtCore.QRect(60, 20, 371, 111))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelTitle.sizePolicy().hasHeightForWidth())
        self.labelTitle.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.labelTitle.setFont(font)
        self.labelTitle.setStyleSheet("color:white")
        self.labelTitle.setObjectName("labelTitle")
        self.pushButtonBot = QtWidgets.QPushButton(self.widgetMain)
        self.pushButtonBot.setGeometry(QtCore.QRect(60, 190, 331, 71))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButtonBot.setFont(font)
        self.pushButtonBot.setStyleSheet("QPushButton{\n"
                                         "    color:white;\n"
                                         "    background-color:rgb(20,20,20);\n"
                                         "    border-radius: 5px\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:pressed{\n"
                                         "    color:black;\n"
                                         "    background-color:rgb(0,0,0);\n"
                                         "    border-radius: 5px\n"
                                         "}")
        self.pushButtonBot.setObjectName("pushButtonBot")
        self.pushButtonHuman = QtWidgets.QPushButton(self.widgetMain)
        self.pushButtonHuman.setGeometry(QtCore.QRect(60, 310, 331, 71))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButtonHuman.setFont(font)
        self.pushButtonHuman.setStyleSheet("QPushButton{\n"
                                           "    color:white;\n"
                                           "    background-color:rgb(20,20,20);\n"
                                           "    border-radius: 5px\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed{\n"
                                           "    color:black;\n"
                                           "    background-color:rgb(0,0,0);\n"
                                           "    border-radius: 5px\n"
                                           "}")
        self.pushButtonHuman.setObjectName("pushButtonHuman")
        self.labelImage = QtWidgets.QLabel(Form)
        self.labelImage.setGeometry(QtCore.QRect(660, 0, 281, 611))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(18)
        self.labelImage.setFont(font)
        self.labelImage.setStyleSheet("color:white")
        self.labelImage.setText("")
        self.labelImage.setPixmap(QtGui.QPixmap("../../../Downloads/pexels-golden-jojo-2409038 (1).jpg"))
        self.labelImage.setObjectName("labelImage")

        self.labelScore = QtWidgets.QLabel(Form)
        self.labelScore.setGeometry(QtCore.QRect(760, 60, 191, 71))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(18)
        self.labelScore.setFont(font)
        self.labelScore.setStyleSheet("color:white;\n"
                                      "background-color:rgba()")
        self.labelScore.setObjectName("labelScore")
        self.labelScoreX = QtWidgets.QLabel(Form)
        self.labelScoreX.setGeometry(QtCore.QRect(700, 140, 191, 71))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(18)
        self.labelScoreX.setFont(font)
        self.labelScoreX.setStyleSheet("color:white;\n"
                                       "background-color:rgba()")
        self.labelScoreX.setAlignment(QtCore.Qt.AlignCenter)
        self.labelScoreX.setObjectName("labelScoreX")
        self.labelScoreY = QtWidgets.QLabel(Form)
        self.labelScoreY.setGeometry(QtCore.QRect(700, 200, 191, 71))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(18)
        self.labelScoreY.setFont(font)
        self.labelScoreY.setStyleSheet("color:white;\n"
                                       "background-color:rgba()")
        self.labelScoreY.setAlignment(QtCore.Qt.AlignCenter)
        self.labelScoreY.setObjectName("labelScoreY")
        self.pushButtonNewGame = QtWidgets.QPushButton(Form)
        self.pushButtonNewGame.setGeometry(QtCore.QRect(740, 410, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(18)
        self.pushButtonNewGame.setFont(font)
        self.pushButtonNewGame.setStyleSheet("QPushButton{\n"
                                             "    color:white;\n"
                                             "    background-color:rgba(20,20,20);\n"
                                             "    border-radius: 5px\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton:pressed{\n"
                                             "    color:black;\n"
                                             "    background-color:rgba(0,0,0);\n"
                                             "    border-radius: 5px\n"
                                             "}")
        self.pushButtonNewGame.setObjectName("pushButtonNewGame")
        self.widgetGame = QtWidgets.QWidget(Form)
        self.widgetGame.setGeometry(QtCore.QRect(20, 20, 611, 461))
        self.widgetGame.setObjectName("widgetGame")
        self.labeltttbg = QtWidgets.QLabel(self.widgetGame)
        self.labeltttbg.setGeometry(QtCore.QRect(20, 20, 521, 421))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(18)
        self.labeltttbg.setFont(font)
        self.labeltttbg.setStyleSheet("color:white")
        self.labeltttbg.setText("")
        self.labeltttbg.setPixmap(QtGui.QPixmap("../../../Downloads/Untitled design (11).png"))
        self.labeltttbg.setAlignment(QtCore.Qt.AlignCenter)
        self.labeltttbg.setObjectName("labeltttbg")
        self.label9 = QtWidgets.QLabel(self.widgetGame)
        self.label9.setGeometry(QtCore.QRect(350, 310, 131, 121))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(36)
        self.label9.setFont(font)
        self.label9.setStyleSheet("color:white")
        self.label9.setAlignment(QtCore.Qt.AlignCenter)
        self.label9.setObjectName("label9")
        self.label6 = QtWidgets.QLabel(self.widgetGame)
        self.label6.setGeometry(QtCore.QRect(350, 170, 121, 111))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(36)
        self.label6.setFont(font)
        self.label6.setStyleSheet("color:white")
        self.label6.setAlignment(QtCore.Qt.AlignCenter)
        self.label6.setObjectName("label6")
        self.label5 = QtWidgets.QLabel(self.widgetGame)
        self.label5.setGeometry(QtCore.QRect(220, 180, 121, 111))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(36)
        self.label5.setFont(font)
        self.label5.setStyleSheet("color:white")
        self.label5.setAlignment(QtCore.Qt.AlignCenter)
        self.label5.setObjectName("label5")
        self.label4 = QtWidgets.QLabel(self.widgetGame)
        self.label4.setGeometry(QtCore.QRect(90, 170, 121, 111))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(36)
        self.label4.setFont(font)
        self.label4.setStyleSheet("color:white")
        self.label4.setAlignment(QtCore.Qt.AlignCenter)
        self.label4.setObjectName("label4")
        self.label1 = QtWidgets.QLabel(self.widgetGame)
        self.label1.setGeometry(QtCore.QRect(80, 40, 131, 121))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(36)
        self.label1.setFont(font)
        self.label1.setStyleSheet("color:white")
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.label1.setObjectName("label1")
        self.label2 = QtWidgets.QLabel(self.widgetGame)
        self.label2.setGeometry(QtCore.QRect(220, 50, 121, 111))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(36)
        self.label2.setFont(font)
        self.label2.setStyleSheet("color:white")
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        self.label2.setObjectName("label2")
        self.label3 = QtWidgets.QLabel(self.widgetGame)
        self.label3.setGeometry(QtCore.QRect(350, 50, 121, 111))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(36)
        self.label3.setFont(font)
        self.label3.setStyleSheet("color:white")
        self.label3.setAlignment(QtCore.Qt.AlignCenter)
        self.label3.setObjectName("label3")
        self.label8 = QtWidgets.QLabel(self.widgetGame)
        self.label8.setGeometry(QtCore.QRect(220, 310, 121, 121))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(36)
        self.label8.setFont(font)
        self.label8.setStyleSheet("color:white")
        self.label8.setAlignment(QtCore.Qt.AlignCenter)
        self.label8.setObjectName("label8")
        self.label7 = QtWidgets.QLabel(self.widgetGame)
        self.label7.setGeometry(QtCore.QRect(80, 310, 121, 121))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(36)
        self.label7.setFont(font)
        self.label7.setStyleSheet("color:white")
        self.label7.setAlignment(QtCore.Qt.AlignCenter)
        self.label7.setObjectName("label7")
        self.widgetGame.raise_()
        self.labelImage.raise_()
        self.labelScore.raise_()
        self.labelScoreX.raise_()
        self.labelScoreY.raise_()
        self.pushButtonNewGame.raise_()

        self.labelCloseWindow = QtWidgets.QLabel(Form)
        self.labelCloseWindow.setGeometry(QtCore.QRect(860, 20, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(18)
        self.labelCloseWindow.setFont(font)
        self.labelCloseWindow.setStyleSheet("background-color:rgba();")
        self.labelCloseWindow.setText("")
        self.labelCloseWindow.setPixmap(QtGui.QPixmap("../../../Downloads/icons8-cross-50.png"))
        self.labelCloseWindow.setObjectName("labelImage")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButtonBot.clicked.connect(lambda: self.selectPlayer2("Bot"))
        self.pushButtonHuman.clicked.connect(lambda: self.selectPlayer2("Human"))
        self.pushButtonNewGame.clicked.connect(self.newGame)

        self.pushButtonNewGame.hide()
        self.widgetGame.hide()

        self.label1.mousePressEvent = functools.partial(self.updateBoard, label=self.label1)
        self.label2.mousePressEvent = functools.partial(self.updateBoard, label=self.label2)
        self.label3.mousePressEvent = functools.partial(self.updateBoard, label=self.label3)
        self.label4.mousePressEvent = functools.partial(self.updateBoard, label=self.label4)
        self.label5.mousePressEvent = functools.partial(self.updateBoard, label=self.label5)
        self.label6.mousePressEvent = functools.partial(self.updateBoard, label=self.label6)
        self.label7.mousePressEvent = functools.partial(self.updateBoard, label=self.label7)
        self.label8.mousePressEvent = functools.partial(self.updateBoard, label=self.label8)
        self.label9.mousePressEvent = functools.partial(self.updateBoard, label=self.label9)

        self.labelCloseWindow.mousePressEvent = functools.partial(self.closeWindow)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):

        Form.setWindowTitle("Form")
        self.labelTitle.setText("Tic Tac Toe")
        self.pushButtonBot.setText("Play against bot")
        self.pushButtonHuman.setText("Play against human")

        self.label1.setText("")
        self.label2.setText("")
        self.label3.setText("")
        self.label4.setText("")
        self.label5.setText("")
        self.label6.setText("")
        self.label7.setText("")
        self.label8.setText("")
        self.label9.setText("")

    def selectPlayer2(self, player):

        self.against = ""

        if player == "Bot":
            self.startGame()
            self.newGame()
            self.against = "Bot"

        elif player == "Human":
            self.startGame()
            self.against = "Human"

    def startGame(self):

        self.widgetMain.hide()
        self.widgetGame.show()

        self.labelScore.setText("Score ")
        self.labelScoreX.setText("X = 0")
        self.labelScoreY.setText("O = 0")

        self.pushButtonNewGame.show()
        self.pushButtonNewGame.setText("New game")

    def updateBoard(self, event, label):

        global turn, currentBoard

        if self.against == "Human":

            for x in str(label.objectName()):
                if x.isnumeric():
                    number = int(x)

            number = number - 1

            if turn == "X":
                turn = "O"

                if label.text() == "":
                    label.setText("X")

                    currentBoard[number] = "X"


            elif turn == "O":
                turn = "X"

                if label.text() == "":
                    label.setText("O")

                    currentBoard[number] = "O"

            if (
                    currentBoard[0] == currentBoard[3] == currentBoard[6] == "X" or
                    currentBoard[1] == currentBoard[4] == currentBoard[7] == "X" or
                    currentBoard[2] == currentBoard[5] == currentBoard[8] == "X" or
                    currentBoard[0] == currentBoard[1] == currentBoard[2] == "X" or
                    currentBoard[3] == currentBoard[4] == currentBoard[5] == "X" or
                    currentBoard[6] == currentBoard[7] == currentBoard[8] == "X" or
                    currentBoard[0] == currentBoard[4] == currentBoard[8] == "X" or
                    currentBoard[2] == currentBoard[4] == currentBoard[6] == "X"):

                self.playerWins("X")

            elif (
                    currentBoard[0] == currentBoard[3] == currentBoard[6] == "O" or
                    currentBoard[1] == currentBoard[4] == currentBoard[7] == "O" or
                    currentBoard[2] == currentBoard[5] == currentBoard[8] == "O" or
                    currentBoard[0] == currentBoard[1] == currentBoard[2] == "O" or
                    currentBoard[3] == currentBoard[4] == currentBoard[5] == "O" or
                    currentBoard[6] == currentBoard[7] == currentBoard[8] == "O" or
                    currentBoard[0] == currentBoard[4] == currentBoard[8] == "O" or
                    currentBoard[2] == currentBoard[4] == currentBoard[6] == "O"):

                self.playerWins("O")

            elif all(isinstance(cell, str) for cell in currentBoard):
                self.playerWins("T")


        elif self.against == "Bot":

            for x in str(label.objectName()):
                if x.isnumeric():
                    number = int(x)

            number = number - 1

            if label.text() == "":

                label.setText("X")
                currentBoard[number] = "X"

                availableSpaces = [x for x in currentBoard if isinstance(x, int)]

                try:
                    randomSpace = random.choice(availableSpaces)

                    randomSpace = randomSpace - 1
                    allLabels = [self.label1, self.label2, self.label3, self.label4, self.label5, self.label6,
                                 self.label7, self.label8, self.label9]

                    allLabels[randomSpace].setText("O")
                    currentBoard[randomSpace] = "O"

                    availableSpaces = [x for x in currentBoard if isinstance(x, int)]

                except IndexError:
                    pass

        if (
                currentBoard[0] == currentBoard[3] == currentBoard[6] == "X" or
                currentBoard[1] == currentBoard[4] == currentBoard[7] == "X" or
                currentBoard[2] == currentBoard[5] == currentBoard[8] == "X" or
                currentBoard[0] == currentBoard[1] == currentBoard[2] == "X" or
                currentBoard[3] == currentBoard[4] == currentBoard[5] == "X" or
                currentBoard[6] == currentBoard[7] == currentBoard[8] == "X" or
                currentBoard[0] == currentBoard[4] == currentBoard[8] == "X" or
                currentBoard[2] == currentBoard[4] == currentBoard[6] == "X"):

            self.playerWins("X")

        elif (
                currentBoard[0] == currentBoard[3] == currentBoard[6] == "O" or
                currentBoard[1] == currentBoard[4] == currentBoard[7] == "O" or
                currentBoard[2] == currentBoard[5] == currentBoard[8] == "O" or
                currentBoard[0] == currentBoard[1] == currentBoard[2] == "O" or
                currentBoard[3] == currentBoard[4] == currentBoard[5] == "O" or
                currentBoard[6] == currentBoard[7] == currentBoard[8] == "O" or
                currentBoard[0] == currentBoard[4] == currentBoard[8] == "O" or
                currentBoard[2] == currentBoard[4] == currentBoard[6] == "O"):

            self.playerWins("O")

        elif all(isinstance(cell, str) for cell in currentBoard):
            self.playerWins("T")

    def playerWins(self, winner):

        global X, O

        self.widgetGame.hide()
        self.widgetMain.show()

        self.pushButtonHuman.hide()
        self.pushButtonBot.hide()

        if winner == "X":

            X = X + 1
            self.labelScoreX.setText(f"X = {X}")
            self.labelTitle.setText(f"Player X wins!")

        elif winner == "O":

            O = O + 1
            self.labelScoreY.setText(f"O = {O}")
            self.labelTitle.setText(f"Player O wins!")

        elif winner == "T":
            pass
            self.labelTitle.setText(f"Draw!")

    def newGame(self):

        global currentBoard

        self.widgetMain.hide()
        self.widgetGame.show()

        currentBoard = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        self.label1.setText("")
        self.label2.setText("")
        self.label3.setText("")
        self.label4.setText("")
        self.label5.setText("")
        self.label6.setText("")
        self.label7.setText("")
        self.label8.setText("")
        self.label9.setText("")

    def closeWindow(self, event):
        app.closeAllWindows()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
