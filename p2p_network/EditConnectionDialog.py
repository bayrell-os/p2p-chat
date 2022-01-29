# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/drive/d/files/Projects/bayrell/p2p-network/p2p_network/EditConnectionDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EditConnectionDialog(object):
    def setupUi(self, EditConnectionDialog):
        EditConnectionDialog.setObjectName("EditConnectionDialog")
        EditConnectionDialog.resize(405, 479)
        self.buttonBox = QtWidgets.QDialogButtonBox(EditConnectionDialog)
        self.buttonBox.setGeometry(QtCore.QRect(0, 430, 381, 41))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.userNameEdit = QtWidgets.QLineEdit(EditConnectionDialog)
        self.userNameEdit.setGeometry(QtCore.QRect(10, 30, 381, 31))
        self.userNameEdit.setObjectName("userNameEdit")
        self.connectionNameEdit = QtWidgets.QLineEdit(EditConnectionDialog)
        self.connectionNameEdit.setGeometry(QtCore.QRect(10, 90, 381, 31))
        self.connectionNameEdit.setObjectName("connectionNameEdit")
        self.clientPortEdit = QtWidgets.QLineEdit(EditConnectionDialog)
        self.clientPortEdit.setGeometry(QtCore.QRect(10, 150, 381, 31))
        self.clientPortEdit.setObjectName("clientPortEdit")
        self.secretKeyEdit = QtWidgets.QLineEdit(EditConnectionDialog)
        self.secretKeyEdit.setGeometry(QtCore.QRect(10, 210, 381, 31))
        self.secretKeyEdit.setObjectName("secretKeyEdit")
        self.connectStringEdit = QtWidgets.QLineEdit(EditConnectionDialog)
        self.connectStringEdit.setGeometry(QtCore.QRect(10, 270, 381, 31))
        self.connectStringEdit.setObjectName("connectStringEdit")
        self.enableRelay = QtWidgets.QCheckBox(EditConnectionDialog)
        self.enableRelay.setGeometry(QtCore.QRect(10, 310, 381, 21))
        self.enableRelay.setObjectName("enableRelay")
        self.localIpEdit = QtWidgets.QLineEdit(EditConnectionDialog)
        self.localIpEdit.setGeometry(QtCore.QRect(10, 360, 381, 31))
        self.localIpEdit.setObjectName("localIpEdit")
        self.label_1 = QtWidgets.QLabel(EditConnectionDialog)
        self.label_1.setGeometry(QtCore.QRect(10, 190, 151, 17))
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(EditConnectionDialog)
        self.label_2.setGeometry(QtCore.QRect(10, 250, 371, 17))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(EditConnectionDialog)
        self.label_4.setGeometry(QtCore.QRect(10, 70, 151, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(EditConnectionDialog)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 151, 17))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(EditConnectionDialog)
        self.label_6.setGeometry(QtCore.QRect(10, 130, 151, 17))
        self.label_6.setObjectName("label_6")
        self.label_3 = QtWidgets.QLabel(EditConnectionDialog)
        self.label_3.setGeometry(QtCore.QRect(10, 340, 371, 17))
        self.label_3.setObjectName("label_3")
        self.autoStartPeerVPN = QtWidgets.QCheckBox(EditConnectionDialog)
        self.autoStartPeerVPN.setGeometry(QtCore.QRect(10, 400, 381, 21))
        self.autoStartPeerVPN.setObjectName("autoStartPeerVPN")
        self.vpnVersion = QtWidgets.QComboBox(EditConnectionDialog)
        self.vpnVersion.setGeometry(QtCore.QRect(200, 395, 90, 31))
        self.vpnVersion.setObjectName("vpnVersion")
        self.vpnVersion.addItem("")
        self.vpnVersion.addItem("")

        self.retranslateUi(EditConnectionDialog)
        self.buttonBox.accepted.connect(EditConnectionDialog.accept) # type: ignore
        self.buttonBox.rejected.connect(EditConnectionDialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(EditConnectionDialog)

    def retranslateUi(self, EditConnectionDialog):
        _translate = QtCore.QCoreApplication.translate
        EditConnectionDialog.setWindowTitle(_translate("EditConnectionDialog", "Edit connection"))
        self.clientPortEdit.setText(_translate("EditConnectionDialog", "33002"))
        self.enableRelay.setText(_translate("EditConnectionDialog", "Enable relay for this computer"))
        self.localIpEdit.setText(_translate("EditConnectionDialog", "10.5.0.1"))
        self.label_1.setText(_translate("EditConnectionDialog", "Secret Key"))
        self.label_2.setText(_translate("EditConnectionDialog", "Clients (example: 127.0.0.1:33002;127.0.0.2:33002)"))
        self.label_4.setText(_translate("EditConnectionDialog", "Network name"))
        self.label_5.setText(_translate("EditConnectionDialog", "Your user name"))
        self.label_6.setText(_translate("EditConnectionDialog", "Network port"))
        self.label_3.setText(_translate("EditConnectionDialog", "Local IP (Must be 10.5.*.*)"))
        self.autoStartPeerVPN.setText(_translate("EditConnectionDialog", "Autostart PeerVPN"))
        self.vpnVersion.setItemText(0, _translate("EditConnectionDialog", "32bit"))
        self.vpnVersion.setItemText(1, _translate("EditConnectionDialog", "64bit"))
