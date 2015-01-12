# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created: Mon Jan 12 18:35:54 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(431, 331)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton_rollback = QtGui.QPushButton(Dialog)
        self.pushButton_rollback.setEnabled(False)
        self.pushButton_rollback.setObjectName(_fromUtf8("pushButton_rollback"))
        self.gridLayout.addWidget(self.pushButton_rollback, 5, 1, 1, 1)
        self.pushButton_create = QtGui.QPushButton(Dialog)
        self.pushButton_create.setEnabled(False)
        self.pushButton_create.setObjectName(_fromUtf8("pushButton_create"))
        self.gridLayout.addWidget(self.pushButton_create, 3, 0, 1, 2)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 6, 0, 1, 2)
        self.label_layers = QtGui.QLabel(Dialog)
        self.label_layers.setObjectName(_fromUtf8("label_layers"))
        self.gridLayout.addWidget(self.label_layers, 0, 0, 1, 2)
        self.pushButton_commit = QtGui.QPushButton(Dialog)
        self.pushButton_commit.setEnabled(False)
        self.pushButton_commit.setObjectName(_fromUtf8("pushButton_commit"))
        self.gridLayout.addWidget(self.pushButton_commit, 5, 0, 1, 1)
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lineEdit_sql = QtGui.QLineEdit(self.widget)
        self.lineEdit_sql.setEnabled(False)
        self.lineEdit_sql.setObjectName(_fromUtf8("lineEdit_sql"))
        self.horizontalLayout.addWidget(self.lineEdit_sql)
        self.pushButton_sql = QtGui.QPushButton(self.widget)
        self.pushButton_sql.setEnabled(False)
        self.pushButton_sql.setObjectName(_fromUtf8("pushButton_sql"))
        self.horizontalLayout.addWidget(self.pushButton_sql)
        self.gridLayout.addWidget(self.widget, 4, 0, 1, 2)
        self.listWidget_layers = QtGui.QListWidget(Dialog)
        self.listWidget_layers.setProperty("showDropIndicator", False)
        self.listWidget_layers.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.listWidget_layers.setObjectName(_fromUtf8("listWidget_layers"))
        self.gridLayout.addWidget(self.listWidget_layers, 1, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Transaction Test", None))
        self.pushButton_rollback.setText(_translate("Dialog", "Rollback transaction", None))
        self.pushButton_create.setText(_translate("Dialog", "Create transaction", None))
        self.label_layers.setText(_translate("Dialog", "Select transaction layers:", None))
        self.pushButton_commit.setText(_translate("Dialog", "Commit transaction", None))
        self.pushButton_sql.setText(_translate("Dialog", "Execute SQL", None))

