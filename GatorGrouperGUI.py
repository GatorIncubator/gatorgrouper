# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GatorGrouperGUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import os

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

class Ui_GatorGrouperGUI(object):
    def setupUi(self, GatorGrouperGUI):
        GatorGrouperGUI.setObjectName(_fromUtf8("GatorGrouperGUI"))
        GatorGrouperGUI.resize(334, 494)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Pictures/icon24x24.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        GatorGrouperGUI.setWindowIcon(icon)
        GatorGrouperGUI.setTabShape(QtGui.QTabWidget.Rounded)
        GatorGrouperGUI.setUnifiedTitleAndToolBarOnMac(False)
        self.mainWidge = QtGui.QWidget(GatorGrouperGUI)
        self.mainWidge.setObjectName(_fromUtf8("mainWidge"))
        self.groupListViewer = QtGui.QListView(self.mainWidge)
        self.groupListViewer.setGeometry(QtCore.QRect(10, 60, 311, 381))
        self.groupListViewer.setObjectName(_fromUtf8("groupListViewer"))
        self.widget = QtGui.QWidget(self.mainWidge)
        self.widget.setGeometry(QtCore.QRect(40, 0, 242, 54))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.trueRandButton = QtGui.QRadioButton(self.widget)
        self.trueRandButton.setChecked(True)
        self.trueRandButton.setProperty("rand-type", False)
        self.trueRandButton.setObjectName(_fromUtf8("trueRandButton"))
        self.verticalLayout.addWidget(self.trueRandButton)
        self.rrButton = QtGui.QRadioButton(self.widget)
        self.rrButton.setProperty("rand-type", True)
        self.rrButton.setObjectName(_fromUtf8("rrButton"))
        self.verticalLayout.addWidget(self.rrButton)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.generateButton = QtGui.QPushButton(self.widget)
        self.generateButton.setObjectName(_fromUtf8("generateButton"))
        self.horizontalLayout.addWidget(self.generateButton)
        GatorGrouperGUI.setCentralWidget(self.mainWidge)
        self.menuBar = QtGui.QMenuBar(GatorGrouperGUI)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 334, 25))
        self.menuBar.setMinimumSize(QtCore.QSize(0, 0))
        self.menuBar.setMouseTracking(False)
        self.menuBar.setAcceptDrops(True)
        self.menuBar.setAutoFillBackground(False)
        self.menuBar.setDefaultUp(False)
        self.menuBar.setNativeMenuBar(True)
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuSettings = QtGui.QMenu(self.menuBar)
        self.menuSettings.setObjectName(_fromUtf8("menuSettings"))
        GatorGrouperGUI.setMenuBar(self.menuBar)
        self.statusBar = QtGui.QStatusBar(GatorGrouperGUI)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        GatorGrouperGUI.setStatusBar(self.statusBar)
        self.actionOpenSF = QtGui.QAction(GatorGrouperGUI)
        self.actionOpenSF.setCheckable(False)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("open"))
        self.actionOpenSF.setIcon(icon)
        self.actionOpenSF.setSoftKeyRole(QtGui.QAction.NoSoftKey)
        self.actionOpenSF.setObjectName(_fromUtf8("actionOpenSF"))
        self.actionSave = QtGui.QAction(GatorGrouperGUI)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionSaveAs = QtGui.QAction(GatorGrouperGUI)
        self.actionSaveAs.setObjectName(_fromUtf8("actionSaveAs"))
        self.actionAddAbs = QtGui.QAction(GatorGrouperGUI)
        self.actionAddAbs.setObjectName(_fromUtf8("actionAddAbs"))
        self.actionRemoveAbs = QtGui.QAction(GatorGrouperGUI)
        self.actionRemoveAbs.setObjectName(_fromUtf8("actionRemoveAbs"))
        self.actionConfig = QtGui.QAction(GatorGrouperGUI)
        self.actionConfig.setObjectName(_fromUtf8("actionConfig"))
        self.actionHelp = QtGui.QAction(GatorGrouperGUI)
        self.actionHelp.setObjectName(_fromUtf8("actionHelp"))
        self.actionExit = QtGui.QAction(GatorGrouperGUI)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuFile.addAction(self.actionOpenSF)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSaveAs)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionHelp)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuSettings.addAction(self.actionAddAbs)
        self.menuSettings.addAction(self.actionRemoveAbs)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(GatorGrouperGUI)
        QtCore.QObject.connect(self.generateButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.runGG)
        QtCore.QObject.connect(self.trueRandButton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.generateButton.setChecked)
        QtCore.QObject.connect(self.rrButton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.generateButton.setChecked)
        QtCore.QMetaObject.connectSlotsByName(GatorGrouperGUI)
        GatorGrouperGUI.setTabOrder(self.trueRandButton, self.rrButton)
        GatorGrouperGUI.setTabOrder(self.rrButton, self.generateButton)
        GatorGrouperGUI.setTabOrder(self.generateButton, self.groupListViewer)

    def retranslateUi(self, GatorGrouperGUI):
        GatorGrouperGUI.setWindowTitle(_translate("GatorGrouperGUI", "Gator Grouper", None))
        self.trueRandButton.setText(_translate("GatorGrouperGUI", "True Random", None))
        self.rrButton.setText(_translate("GatorGrouperGUI", "Round-Robin", None))
        self.generateButton.setText(_translate("GatorGrouperGUI", "Generate List", None))
        self.menuFile.setTitle(_translate("GatorGrouperGUI", "File", None))
        self.menuSettings.setTitle(_translate("GatorGrouperGUI", "Settings", None))
        self.actionOpenSF.setText(_translate("GatorGrouperGUI", "Open Student File (Ctrl+O)", None))
        self.actionOpenSF.setShortcut(_translate("GatorGrouperGUI", "Ctrl+O", None))
        self.actionSave.setText(_translate("GatorGrouperGUI", "Save List (Ctrl+S)", None))
        self.actionSave.setShortcut(_translate("GatorGrouperGUI", "Ctrl+S", None))
        self.actionSaveAs.setText(_translate("GatorGrouperGUI", "Save List As... (Ctrl+Shift+S)", None))
        self.actionSaveAs.setShortcut(_translate("GatorGrouperGUI", "Ctrl+Shift+S", None))
        self.actionAddAbs.setText(_translate("GatorGrouperGUI", "Add Absentees", None))
        self.actionRemoveAbs.setText(_translate("GatorGrouperGUI", "Remove Absentees", None))
        self.actionConfig.setText(_translate("GatorGrouperGUI", "Configure...", None))
        self.actionHelp.setText(_translate("GatorGrouperGUI", "Help", None))
        self.actionExit.setText(_translate("GatorGrouperGUI", "Exit", None))

    def runGG(signal1):
        os.system('python3 gatorgrouper.py')

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    GatorGrouperGUI = QtGui.QMainWindow()
    ui = Ui_GatorGrouperGUI()
    ui.setupUi(GatorGrouperGUI)
    GatorGrouperGUI.show()
    sys.exit(app.exec_())
