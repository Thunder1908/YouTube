import functools
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QTimer
import pygame
from mutagen import File
from mutagen.mp3 import MP3
import re

pygame.init()
pygame.mixer.init()


class Ui_Form(QtWidgets.QWidget):
    def setupUi(self, Form):

        Form.setObjectName("Form")
        Form.resize(1031, 565)
        Form.setStyleSheet("background-color:black")
        Form.setWindowFlag(Qt.FramelessWindowHint)

        self.labelSongName = QtWidgets.QLabel(Form)
        self.labelSongName.setGeometry(QtCore.QRect(670, 40, 361, 111))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(36)
        self.labelSongName.setFont(font)
        self.labelSongName.setStyleSheet("color:white;background-color:rgba(0,0,0,0)")
        self.labelSongName.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSongName.setObjectName("labelSongName")
        self.horizontalSliderMusic = QtWidgets.QSlider(Form)
        self.horizontalSliderMusic.setGeometry(QtCore.QRect(720, 450, 271, 22))
        self.horizontalSliderMusic.setStyleSheet("background-color:rgba(0,0,0,0)")
        self.horizontalSliderMusic.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderMusic.setObjectName("horizontalSliderMusic")
        self.labelPlayPause = QtWidgets.QLabel(Form)
        self.labelPlayPause.setGeometry(QtCore.QRect(830, 480, 61, 61))
        self.labelPlayPause.setStyleSheet("background-color:rgba(0,0,0,0)")
        self.labelPlayPause.setText("")
        self.labelPlayPause.setPixmap(QtGui.QPixmap("../../../Downloads/icons8-play-24.png"))
        self.labelPlayPause.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPlayPause.setObjectName("labelPlayPause")
        self.labelNextSong = QtWidgets.QLabel(Form)
        self.labelNextSong.setGeometry(QtCore.QRect(900, 480, 51, 61))
        self.labelNextSong.setStyleSheet("background-color:rgba(0,0,0,0)")
        self.labelNextSong.setText("")
        self.labelNextSong.setPixmap(QtGui.QPixmap("../../../Downloads/icons8-end-30.png"))
        self.labelNextSong.setAlignment(QtCore.Qt.AlignCenter)
        self.labelNextSong.setObjectName("labelNextSong")
        self.labelPreviousSong = QtWidgets.QLabel(Form)
        self.labelPreviousSong.setGeometry(QtCore.QRect(780, 480, 41, 61))
        self.labelPreviousSong.setStyleSheet("background-color:rgba(0,0,0,0)")
        self.labelPreviousSong.setText("")
        self.labelPreviousSong.setPixmap(QtGui.QPixmap("../../../Downloads/icons8-end-30 - Copy.png"))
        self.labelPreviousSong.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPreviousSong.setObjectName("labelPreviousSong")
        self.widgetMusicList = QtWidgets.QWidget(Form)
        self.widgetMusicList.setGeometry(QtCore.QRect(30, 30, 611, 561))
        self.widgetMusicList.setObjectName("widgetMusicList")
        self.listWidgetPlaying = QtWidgets.QListWidget(self.widgetMusicList)
        self.listWidgetPlaying.setGeometry(QtCore.QRect(10, 100, 561, 341))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(16)
        self.listWidgetPlaying.setFont(font)
        self.listWidgetPlaying.setStyleSheet("background-color:rgb(20,20,20);\n"
                                             "border-radius:5px;\n"
                                             "color:white")

        self.listWidgetPlaying.setSpacing(5)
        self.listWidgetPlaying.setItemAlignment(Qt.AlignHCenter)
        self.listWidgetPlaying.setObjectName("listWidgetPlaying")
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setKerning(True)
        item.setFont(font)
        self.listWidgetPlaying.addItem(item)

        self.listWidgetPlaying.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidgetPlaying.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.labelBackground = QtWidgets.QLabel(Form)
        self.labelBackground.setGeometry(QtCore.QRect(670, -20, 461, 641))
        self.labelBackground.setText("")
        self.labelBackground.setPixmap(QtGui.QPixmap("../../../Downloads/pexels-golden-jojo-2409038 (1).jpg"))
        self.labelBackground.setObjectName("labelBackground")
        self.labelSongArtist = QtWidgets.QLabel(Form)
        self.labelSongArtist.setGeometry(QtCore.QRect(670, 130, 361, 71))
        self.labelSongArtist.setAlignment(Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(16)
        self.labelSongArtist.setFont(font)
        self.labelSongArtist.setStyleSheet("color:white;\n"
                                           "background-color:rgba(0,0,0,0)")
        self.labelSongArtist.setObjectName("labelSongArtist")
        self.labelBackground.raise_()
        self.widgetMusicList.raise_()
        self.labelSongName.raise_()
        self.horizontalSliderMusic.raise_()
        self.labelPlayPause.raise_()
        self.labelNextSong.raise_()
        self.labelPreviousSong.raise_()
        self.labelSongArtist.raise_()

        self.lineEditSearch = QtWidgets.QLineEdit(self.widgetMusicList)
        self.lineEditSearch.setStyleSheet("color:white;\n"
                                          "background-color:rgb(10,10,10);\n"
                                          "border-radius: 5px")
        self.lineEditSearch.setGeometry(10, 30, 441, 31)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(14)
        self.lineEditSearch.setFont(font)

        self.songPlayingEvent = 1
        self.searchForSongs()

        self.listWidgetPlaying.itemClicked.connect(self.playNewSong)
        self.labelPlayPause.mousePressEvent = functools.partial(self.playPause)
        self.lineEditSearch.textEdited.connect(self.filterSongs)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.labelSongName.setText(_translate("Form", "Heathens"))
        __sortingEnabled = self.listWidgetPlaying.isSortingEnabled()
        self.listWidgetPlaying.setSortingEnabled(False)
        item = self.listWidgetPlaying.item(1)
        item.setText(_translate("Form", "Heathens - Twenty one Pilots"))
        self.listWidgetPlaying.setSortingEnabled(__sortingEnabled)
        self.labelSongArtist.setText(_translate("Form", "Twenty one Pilots"))

    def searchForSongs(self):

        a = os.listdir(r"C:\Users\Thunder 1908\Songs")
        print(type(a))

        self.allSongsList = []

        for x in a:
            if x.endswith(".mp3"):
                self.allSongsList.append(x)

                x = re.sub("\(.*?\)", "()", x)
                print(x)

                x = x.replace(".mp3", "")
                x = x.replace("()", "")
                x = x.rstrip()

                item = QtWidgets.QListWidgetItem()
                item.setText(x)
                self.listWidgetPlaying.addItem(item)

    def playNewSong(self):

        self.resetELements()
        self.selectedSong = self.listWidgetPlaying.currentItem().text()

        metaData = dict(File(fr"C:\Users\Thunder 1908\Songs\{self.selectedSong}.mp3", easy=True))

        title = str(metaData.get("title"))
        title = title[2:-2]

        artist = str(metaData.get("artist"))
        artist = artist[2:-2]

        self.labelSongName.setText(title)
        self.labelSongArtist.setText(artist)

        self.labelPlayPause.setPixmap(QtGui.QPixmap("../../../Downloads/icons8-pause-30.png"))

        pygame.mixer_music.load(rf"C:\Users\Thunder 1908\Songs\{self.selectedSong}.mp3")
        pygame.mixer_music.play()

    def resetELements(self):
        self.horizontalSliderMusic.setSliderPosition(0)
        self.selectedSong = self.listWidgetPlaying.currentItem().text()

        songLength = MP3(rf"C:\Users\Thunder 1908\Songs\{self.selectedSong}.mp3")
        songLength = songLength.info.length
        songLength = songLength

        self.songLength = int(songLength)

        try:
            self.timer.stop()
        except:
            pass

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateSlider)
        self.timer.start(self.songLength * 10)

    def playPause(self, event):

        if self.songPlayingEvent == 1:
            self.songPlayingEvent = 0

            self.labelPlayPause.setPixmap(QtGui.QPixmap("../../../Downloads/icons8-play-24.png"))
            self.timer.stop()

            pygame.mixer_music.pause()

        elif self.songPlayingEvent == 0:
            self.songPlayingEvent = 1

            self.timer.start()
            self.labelPlayPause.setPixmap(QtGui.QPixmap("../../../Downloads/icons8-pause-30.png"))

            pygame.mixer_music.unpause()

    def updateSlider(self):

        a = self.horizontalSliderMusic.sliderPosition()
        self.horizontalSliderMusic.setSliderPosition(a + 1)

        print(a)

    def filterSongs(self):

        self.listWidgetPlaying.clear()

        songName = self.lineEditSearch.text()
        print(songName)

        for x in self.allSongsList:
            if songName in x:
                x = re.sub("\(.*?\)", "()", x)
                print(x)

                x = x.replace(".mp3", "")
                x = x.replace("()", "")

                item = QtWidgets.QListWidgetItem()
                item.setText(x)
                self.listWidgetPlaying.addItem(item)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
