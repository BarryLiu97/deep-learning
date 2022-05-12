# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_win.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(522, 559)
        MainWindow.setMinimumSize(QtCore.QSize(522, 559))
        MainWindow.setMaximumSize(QtCore.QSize(522, 559))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self._num_canvas = Canvas(self.centralwidget)
        self._num_canvas.setMinimumSize(QtCore.QSize(500, 500))
        self._num_canvas.setMaximumSize(QtCore.QSize(500, 500))
        self._num_canvas.setStyleSheet("background-color: rgb(255, 255, 255);")
        self._num_canvas.setText("")
        self._num_canvas.setObjectName("_num_canvas")
        self.verticalLayout.addWidget(self._num_canvas)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self._num_mode_btn = QtWidgets.QPushButton(self.centralwidget)
        self._num_mode_btn.setMinimumSize(QtCore.QSize(120, 28))
        self._num_mode_btn.setMaximumSize(QtCore.QSize(120, 28))
        self._num_mode_btn.setObjectName("_num_mode_btn")
        self.horizontalLayout.addWidget(self._num_mode_btn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self._num_le = QtWidgets.QLineEdit(self.centralwidget)
        self._num_le.setMinimumSize(QtCore.QSize(200, 28))
        self._num_le.setMaximumSize(QtCore.QSize(200, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        self._num_le.setFont(font)
        self._num_le.setText("")
        self._num_le.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self._num_le.setObjectName("_num_le")
        self.horizontalLayout.addWidget(self._num_le)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self._run_btn = QtWidgets.QPushButton(self.centralwidget)
        self._run_btn.setMinimumSize(QtCore.QSize(90, 28))
        self._run_btn.setMaximumSize(QtCore.QSize(90, 28))
        self._run_btn.setObjectName("_run_btn")
        self.horizontalLayout.addWidget(self._run_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self._num_mode_btn.setText(_translate("MainWindow", "Single number"))
        self._run_btn.setText(_translate("MainWindow", "Run"))

from MNIST.gui.canvas import Canvas

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

