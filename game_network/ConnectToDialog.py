# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/drive/d/files/Projects/bayrell/p2p-chat/p2p_chat/ConnectToDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ConnectToDialog(object):
    def setupUi(self, ConnectToDialog):
        ConnectToDialog.setObjectName("ConnectToDialog")
        ConnectToDialog.resize(400, 123)
        self.verticalLayoutWidget = QtWidgets.QWidget(ConnectToDialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 381, 111))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.verticalLayoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(ConnectToDialog)
        self.buttonBox.accepted.connect(ConnectToDialog.accept) # type: ignore
        self.buttonBox.rejected.connect(ConnectToDialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(ConnectToDialog)

    def retranslateUi(self, ConnectToDialog):
        _translate = QtCore.QCoreApplication.translate
        ConnectToDialog.setWindowTitle(_translate("ConnectToDialog", "Dialog"))
        self.label.setText(_translate("ConnectToDialog", "Connect to server"))