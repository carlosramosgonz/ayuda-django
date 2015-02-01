# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'directorydialog.ui'
#
# Created: Fri Jan 30 14:33:53 2015
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DirectoryDialog(object):
    def setupUi(self, DirectoryDialog):
        DirectoryDialog.setObjectName("DirectoryDialog")
        DirectoryDialog.resize(543, 130)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DirectoryDialog.sizePolicy().hasHeightForWidth())
        DirectoryDialog.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(DirectoryDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(DirectoryDialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.directoryEdit = QtWidgets.QLineEdit(DirectoryDialog)
        self.directoryEdit.setObjectName("directoryEdit")
        self.horizontalLayout.addWidget(self.directoryEdit)
        self.openButton = QtWidgets.QPushButton(DirectoryDialog)
        self.openButton.setObjectName("openButton")
        self.horizontalLayout.addWidget(self.openButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(DirectoryDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(DirectoryDialog)
        self.buttonBox.accepted.connect(DirectoryDialog.accept)
        self.buttonBox.rejected.connect(DirectoryDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(DirectoryDialog)

    def retranslateUi(self, DirectoryDialog):
        _translate = QtCore.QCoreApplication.translate
        DirectoryDialog.setWindowTitle(_translate("DirectoryDialog", "Abrir"))
        self.label.setText(_translate("DirectoryDialog", "Seleccione el directorio donde se encuentra la documentación de Django:"))
        self.openButton.setText(_translate("DirectoryDialog", "Abrir..."))

