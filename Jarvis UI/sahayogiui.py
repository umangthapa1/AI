from PyQt5 import QtCore, QtGui, QtWidgets
import main

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1146, 641)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../Downloads/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet("background-color: bacl\n"
        "")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 140, 361, 311))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../../Downloads/R.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(680, 360, 461, 271))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../../Downloads/cyberpunk-retro-futuristic-hud-animation-for-live-streaming-display-overlay-and-copy-space-in-neon-light-color-free-video.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(340, 10, 551, 91))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../../../Downloads/text-1706882966116 (1).png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 510, 51, 41))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("../../../Downloads/discord-logo-2-1.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(86, 502, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setStyleSheet("color: white\n"
        "")
        self.label_5.setTextFormat(QtCore.Qt.RichText)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(10, 560, 71, 61))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("../../../Downloads/R (1).png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(86, 562, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: white\n"
        "")
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(710, 160, 361, 171))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("../../../Downloads/e8c5b61a18d49c20c48f0fe6d4839def4a96d970r1-444-250_00.gif"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(340, 220, 371, 301))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("../../../Downloads/R (1).gif"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.terminalOutputBox = QtWidgets.QPlainTextEdit(Dialog)
        self.terminalOutputBox.setGeometry(QtCore.QRect(730, 440, 361, 101))
        self.terminalOutputBox.setStyleSheet("color: rgb(19, 192, 235)")
        self.terminalOutputBox.setObjectName("terminalOutputBox")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "S.A.H.A.Y.G.U"))
        self.label_5.setText(_translate("Dialog", "dsc.gg/coders-hub"))
        self.label_7.setText(_translate("Dialog", "github.com/umangthapa1"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())