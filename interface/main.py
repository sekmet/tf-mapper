# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../assets/interface\main.ui'
#
# Created: Thu Feb 28 14:32:18 2013
#      by: PyQt4 UI code generator 4.9.6
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(745, 783)
        self.uiComponentCentralWidget = QtGui.QWidget(MainWindow)
        self.uiComponentCentralWidget.setObjectName(_fromUtf8("uiComponentCentralWidget"))
        self.gridLayout = QtGui.QGridLayout(self.uiComponentCentralWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.uiComponentViewingFrame = QtGui.QFrame(self.uiComponentCentralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiComponentViewingFrame.sizePolicy().hasHeightForWidth())
        self.uiComponentViewingFrame.setSizePolicy(sizePolicy)
        self.uiComponentViewingFrame.setMinimumSize(QtCore.QSize(250, 250))
        self.uiComponentViewingFrame.setFrameShape(QtGui.QFrame.Box)
        self.uiComponentViewingFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.uiComponentViewingFrame.setMidLineWidth(1)
        self.uiComponentViewingFrame.setObjectName(_fromUtf8("uiComponentViewingFrame"))
        self.gridLayout.addWidget(self.uiComponentViewingFrame, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.uiComponentCentralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 745, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuView = QtGui.QMenu(self.menuBar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        MainWindow.setMenuBar(self.menuBar)
        self.uiComponentToolsPanel = QtGui.QDockWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiComponentToolsPanel.sizePolicy().hasHeightForWidth())
        self.uiComponentToolsPanel.setSizePolicy(sizePolicy)
        self.uiComponentToolsPanel.setMinimumSize(QtCore.QSize(250, 400))
        self.uiComponentToolsPanel.setMaximumSize(QtCore.QSize(250, 400))
        self.uiComponentToolsPanel.setFeatures(QtGui.QDockWidget.AllDockWidgetFeatures)
        self.uiComponentToolsPanel.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.uiComponentToolsPanel.setObjectName(_fromUtf8("uiComponentToolsPanel"))
        self.uiComponentToolsPanelContentWidget = QtGui.QWidget()
        self.uiComponentToolsPanelContentWidget.setObjectName(_fromUtf8("uiComponentToolsPanelContentWidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.uiComponentToolsPanelContentWidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.compassButtonsGridLayout = QtGui.QGridLayout()
        self.compassButtonsGridLayout.setObjectName(_fromUtf8("compassButtonsGridLayout"))
        self.compassN = QtGui.QToolButton(self.uiComponentToolsPanelContentWidget)
        self.compassN.setMinimumSize(QtCore.QSize(30, 30))
        self.compassN.setMaximumSize(QtCore.QSize(30, 30))
        self.compassN.setObjectName(_fromUtf8("compassN"))
        self.compassButtons = QtGui.QButtonGroup(MainWindow)
        self.compassButtons.setObjectName(_fromUtf8("compassButtons"))
        self.compassButtons.addButton(self.compassN)
        self.compassButtonsGridLayout.addWidget(self.compassN, 0, 2, 1, 1)
        self.compassS = QtGui.QToolButton(self.uiComponentToolsPanelContentWidget)
        self.compassS.setMinimumSize(QtCore.QSize(30, 30))
        self.compassS.setMaximumSize(QtCore.QSize(30, 30))
        self.compassS.setObjectName(_fromUtf8("compassS"))
        self.compassButtons.addButton(self.compassS)
        self.compassButtonsGridLayout.addWidget(self.compassS, 2, 2, 1, 1)
        self.compassSE = QtGui.QToolButton(self.uiComponentToolsPanelContentWidget)
        self.compassSE.setMinimumSize(QtCore.QSize(30, 30))
        self.compassSE.setMaximumSize(QtCore.QSize(30, 30))
        self.compassSE.setObjectName(_fromUtf8("compassSE"))
        self.compassButtons.addButton(self.compassSE)
        self.compassButtonsGridLayout.addWidget(self.compassSE, 2, 3, 1, 1)
        self.compassSW = QtGui.QToolButton(self.uiComponentToolsPanelContentWidget)
        self.compassSW.setMinimumSize(QtCore.QSize(30, 30))
        self.compassSW.setMaximumSize(QtCore.QSize(30, 30))
        self.compassSW.setObjectName(_fromUtf8("compassSW"))
        self.compassButtons.addButton(self.compassSW)
        self.compassButtonsGridLayout.addWidget(self.compassSW, 2, 1, 1, 1)
        self.compassNW = QtGui.QToolButton(self.uiComponentToolsPanelContentWidget)
        self.compassNW.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.compassNW.sizePolicy().hasHeightForWidth())
        self.compassNW.setSizePolicy(sizePolicy)
        self.compassNW.setMinimumSize(QtCore.QSize(30, 30))
        self.compassNW.setMaximumSize(QtCore.QSize(30, 30))
        self.compassNW.setObjectName(_fromUtf8("compassNW"))
        self.compassButtons.addButton(self.compassNW)
        self.compassButtonsGridLayout.addWidget(self.compassNW, 0, 1, 1, 1)
        self.compassNE = QtGui.QToolButton(self.uiComponentToolsPanelContentWidget)
        self.compassNE.setMinimumSize(QtCore.QSize(30, 30))
        self.compassNE.setMaximumSize(QtCore.QSize(30, 30))
        self.compassNE.setObjectName(_fromUtf8("compassNE"))
        self.compassButtons.addButton(self.compassNE)
        self.compassButtonsGridLayout.addWidget(self.compassNE, 0, 3, 1, 1)
        self.compassE = QtGui.QToolButton(self.uiComponentToolsPanelContentWidget)
        self.compassE.setMinimumSize(QtCore.QSize(30, 30))
        self.compassE.setMaximumSize(QtCore.QSize(30, 30))
        self.compassE.setObjectName(_fromUtf8("compassE"))
        self.compassButtons.addButton(self.compassE)
        self.compassButtonsGridLayout.addWidget(self.compassE, 1, 3, 1, 1)
        self.compassW = QtGui.QToolButton(self.uiComponentToolsPanelContentWidget)
        self.compassW.setMinimumSize(QtCore.QSize(30, 30))
        self.compassW.setMaximumSize(QtCore.QSize(30, 30))
        self.compassW.setObjectName(_fromUtf8("compassW"))
        self.compassButtons.addButton(self.compassW)
        self.compassButtonsGridLayout.addWidget(self.compassW, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 17, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.compassButtonsGridLayout.addItem(spacerItem, 1, 4, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.compassButtonsGridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.compassButtonsGridLayout, 1, 0, 1, 1)
        self.walkerModeSelector = QtGui.QComboBox(self.uiComponentToolsPanelContentWidget)
        self.walkerModeSelector.setObjectName(_fromUtf8("walkerModeSelector"))
        self.walkerModeSelector.addItem(_fromUtf8(""))
        self.walkerModeSelector.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.walkerModeSelector, 0, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(self.uiComponentToolsPanelContentWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout_2.addWidget(self.pushButton, 2, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 3, 0, 1, 1)
        self.zoomSlider = QtGui.QSlider(self.uiComponentToolsPanelContentWidget)
        self.zoomSlider.setOrientation(QtCore.Qt.Horizontal)
        self.zoomSlider.setObjectName(_fromUtf8("zoomSlider"))
        self.gridLayout_2.addWidget(self.zoomSlider, 4, 0, 1, 1)
        self.uiComponentToolsPanel.setWidget(self.uiComponentToolsPanelContentWidget)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.uiComponentToolsPanel)
        self.menuActionNew = QtGui.QAction(MainWindow)
        self.menuActionNew.setObjectName(_fromUtf8("menuActionNew"))
        self.menuActionOpen = QtGui.QAction(MainWindow)
        self.menuActionOpen.setObjectName(_fromUtf8("menuActionOpen"))
        self.menuActionSave = QtGui.QAction(MainWindow)
        self.menuActionSave.setObjectName(_fromUtf8("menuActionSave"))
        self.menuActionSaveAs = QtGui.QAction(MainWindow)
        self.menuActionSaveAs.setObjectName(_fromUtf8("menuActionSaveAs"))
        self.menuActionQuit = QtGui.QAction(MainWindow)
        self.menuActionQuit.setObjectName(_fromUtf8("menuActionQuit"))
        self.menuActionShowToolsPanel = QtGui.QAction(MainWindow)
        self.menuActionShowToolsPanel.setCheckable(True)
        self.menuActionShowToolsPanel.setChecked(True)
        self.menuActionShowToolsPanel.setObjectName(_fromUtf8("menuActionShowToolsPanel"))
        self.menuFile.addAction(self.menuActionNew)
        self.menuFile.addAction(self.menuActionOpen)
        self.menuFile.addAction(self.menuActionSave)
        self.menuFile.addAction(self.menuActionSaveAs)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menuActionQuit)
        self.menuView.addAction(self.menuActionShowToolsPanel)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.menuActionShowToolsPanel, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.uiComponentToolsPanel.setVisible)
        QtCore.QObject.connect(self.menuActionQuit, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuView.setTitle(_translate("MainWindow", "View", None))
        self.compassN.setText(_translate("MainWindow", "N", None))
        self.compassN.setShortcut(_translate("MainWindow", "8", None))
        self.compassS.setText(_translate("MainWindow", "S", None))
        self.compassS.setShortcut(_translate("MainWindow", "2", None))
        self.compassSE.setText(_translate("MainWindow", "SE", None))
        self.compassSE.setShortcut(_translate("MainWindow", "3", None))
        self.compassSW.setText(_translate("MainWindow", "SW", None))
        self.compassSW.setShortcut(_translate("MainWindow", "1", None))
        self.compassNW.setText(_translate("MainWindow", "NW", None))
        self.compassNW.setShortcut(_translate("MainWindow", "7", None))
        self.compassNE.setText(_translate("MainWindow", "NE", None))
        self.compassNE.setShortcut(_translate("MainWindow", "9", None))
        self.compassE.setText(_translate("MainWindow", "E", None))
        self.compassE.setShortcut(_translate("MainWindow", "6", None))
        self.compassW.setText(_translate("MainWindow", "W", None))
        self.compassW.setShortcut(_translate("MainWindow", "4", None))
        self.walkerModeSelector.setItemText(0, _translate("MainWindow", "Walk", None))
        self.walkerModeSelector.setItemText(1, _translate("MainWindow", "Create", None))
        self.pushButton.setText(_translate("MainWindow", "Debug", None))
        self.menuActionNew.setText(_translate("MainWindow", "New", None))
        self.menuActionNew.setShortcut(_translate("MainWindow", "Ctrl+N", None))
        self.menuActionOpen.setText(_translate("MainWindow", "Open", None))
        self.menuActionSave.setText(_translate("MainWindow", "Save", None))
        self.menuActionSaveAs.setText(_translate("MainWindow", "Save As", None))
        self.menuActionQuit.setText(_translate("MainWindow", "Quit", None))
        self.menuActionShowToolsPanel.setText(_translate("MainWindow", "Tools Panel", None))
        self.menuActionShowToolsPanel.setShortcut(_translate("MainWindow", "Ctrl+T", None))

