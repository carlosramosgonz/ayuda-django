# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanaayuda.ui'
#
# Created: Thu Jan 29 13:40:05 2015
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!
#

# Copyright (C) 2015 Carlos Ramos González, <carlos+git@carlosramos.me>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(966, 661)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.contentsTab = QtWidgets.QWidget()
        self.contentsTab.setObjectName("contentsTab")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.contentsTab)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.contentsTreeWidget = QtWidgets.QTreeWidget(self.contentsTab)
        self.contentsTreeWidget.setObjectName("contentsTreeWidget")
        self.contentsTreeWidget.headerItem().setText(0, "1")
        self.horizontalLayout_3.addWidget(self.contentsTreeWidget)
        self.tabWidget.addTab(self.contentsTab, "")
        self.indexTab = QtWidgets.QWidget()
        self.indexTab.setObjectName("indexTab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.indexTab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.indexSearchEdit = QtWidgets.QLineEdit(self.indexTab)
        self.indexSearchEdit.setObjectName("indexSearchEdit")
        self.verticalLayout.addWidget(self.indexSearchEdit)
        self.listView = QtWidgets.QListView(self.indexTab)
        self.listView.setObjectName("listView")
        self.verticalLayout.addWidget(self.listView)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.tabWidget.addTab(self.indexTab, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        self.webView = QtWebKitWidgets.QWebView(self.centralwidget)
        self.webView.setUrl(QtCore.QUrl("about:blank"))
        self.webView.setObjectName("webView")
        self.horizontalLayout.addWidget(self.webView)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 966, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ayuda Django"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.contentsTab), _translate("MainWindow", "Contenido"))
        self.indexSearchEdit.setPlaceholderText(_translate("MainWindow", "Buscar..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.indexTab), _translate("MainWindow", "Índice"))

from PyQt5 import QtWebKitWidgets
