# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Archive_app.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp
class ButtonHandler(QtCore.QObject):
    def __init__(self, widget):
        super().__init__()
        self.widget = widget
        self.widget.enterEvent = self.show_tooltip

    def show_tooltip(self, event):
        self.widget.setToolTip(self.widget.toolTip())

class Ui2_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setStyleSheet("background-color:white;")
        MainWindow.resize(1851, 1004)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 2101, 951))
        
        self.tabWidget.setStyleSheet("    QTabBar::tab {\n"
"        background:#CE93D8;  /* Default tab background color */\n"
"        padding: 10px;\n"
"        border:none;\n"
"        \n"
"    }\n"
"    QTabBar::tab:selected {\n"
"        background: #E1BEE7;  /* Background color of the selected tab */\n"
"        color: black;\n"
"    }\n"
"    QTabWidget::pane {\n"
"  \n"
"    }\n"
"")
        self.tabWidget.setObjectName("tabWidget")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab1)
        self.tabWidget_2.setGeometry(QtCore.QRect(-30, -50, 2091, 1091))
        self.tabWidget_2.setMinimumSize(QtCore.QSize(2091, 1091))
        self.tabWidget_2.setMaximumSize(QtCore.QSize(2091, 16777215))
        self.tabWidget_2.setStyleSheet("QTabBar::tab {\n"
"    background: #CE93D8;\n"
"    padding: 10px;\n"
"    border: none;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: #E1BEE7;\n"
"    color: white;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border-radius: 0px;\n"
"    border-bottom: 3px solid #7E57C2;\n"
"    background-color: #fff;\n"
"    height: 20px;\n"
"    color: #000;\n"
"    font-size: 18px;\n"
"}\n"
"QLineEdit:hover{\n"
"    border-bottom: 3px solid #42A5F5;\n"
"}\n"
"QLabel {\n"
"    color:#000;"
"    font-size: 15px;\n"
"}\n"
"\n"
"QComboBox {\n"
"    border: 3px solid #7E57C2;\n"
"    background-color: white;\n"
"}\n"
"QComboBox:hover {\n"
"    border: 3px solid #42A5F5;\n"
"}\n"
"\n"
"QDateEdit {\n"
"    border: 3px solid #7E57C2;\n"
"    background-color: white;\n"
"}\n"
"QDateEdit:hover {\n"
"    border: 3px solid #42A5F5;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #CE93D8;\n"
"    border: 3px solid #000;\n"
"    border-radius: 15px;\n"
"    color: black;\n"
"    font-size: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #E1BEE7;\n"
"    border: 3px solid #000;\n"
"    color: black;\n"
"}\n"
"\n"
"QTableWidget {\n"
"    font-size:15px\n;"
"    color:#000;\n"
"    border:none;\n"
"}\n"
"QTableWidget::item:hover {\n"
"    background-color: #7E57C2;\n"
"}"
"QHeaderView::section {\n"
"        color: black;\n"
"}\n"
"\n"
"\n"
"")
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tabWidget_2Page1 = QtWidgets.QWidget()
        self.tabWidget_2Page1.setObjectName("tabWidget_2Page1")
        self.lineEdit_23 = QtWidgets.QLineEdit(self.tabWidget_2Page1)
        self.lineEdit_23.setGeometry(QtCore.QRect(70, 410, 231, 31))
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.lineEdit_23.setToolTip("Enter your Age ")  # Set the tooltip
        self.button_handler = ButtonHandler(self.lineEdit_23)
        Age_regex = QRegExp(r"^\d{2}$")
        Age_validetar = QRegExpValidator(Age_regex)
        self.lineEdit_23.setValidator(Age_validetar)

        
        self.lineEdit_24 = QtWidgets.QLineEdit(self.tabWidget_2Page1)
        self.lineEdit_24.setGeometry(QtCore.QRect(70, 80, 231, 31))
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.lineEdit_24.setToolTip("Enter your name")  # Set the tooltip
        # self.lineEdit_24.setPlaceholderText("Name")
        self.button_handler = ButtonHandler(self.lineEdit_24)
        Name_regex = QRegExp(r"^[a-zA-Z\s]+$")
        Name_validator = QRegExpValidator(Name_regex)
        self.lineEdit_24.setValidator(Name_validator)
        self.button_handler = ButtonHandler(self.lineEdit_24)
        self.label_31 = QtWidgets.QLabel(self.tabWidget_2Page1)
        self.label_31.setGeometry(QtCore.QRect(70, 370, 81, 31))
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.tabWidget_2Page1)
        self.label_32.setGeometry(QtCore.QRect(140, 805, 101, 31))
        self.label_32.setObjectName("label_32")
        self.comboBox_9 = QtWidgets.QComboBox(self.tabWidget_2Page1)
        self.comboBox_9.setGeometry(QtCore.QRect(370, 570, 131, 35))
        self.comboBox_9.setObjectName("comboBox_9")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.lineEdit_25 = QtWidgets.QLineEdit(self.tabWidget_2Page1)
        self.lineEdit_25.setGeometry(QtCore.QRect(340, 160, 231, 31))
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.lineEdit_25.setToolTip("Enter your Father name")  # Set the tooltip
        Name_regex2 = QRegExp(r"^[a-zA-Z\s]+$")
        Name_validator2 = QRegExpValidator(Name_regex2)
        self.lineEdit_25.setValidator(Name_validator2)
        self.button_handler = ButtonHandler(self.lineEdit_25)
        self.label_33 = QtWidgets.QLabel(self.tabWidget_2Page1)
        self.label_33.setGeometry(QtCore.QRect(340, 40, 181, 31))
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.tabWidget_2Page1)
        self.label_34.setGeometry(QtCore.QRect(140, 625, 71, 51))
        self.label_34.setObjectName("label_34")
        self.lineEdit_26 = QtWidgets.QLineEdit(self.tabWidget_2Page1)
        self.lineEdit_26.setGeometry(QtCore.QRect(70, 320, 231, 31))
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.lineEdit_26.setToolTip("Enter your country name")  # Set the tooltip
        Name_regex3 = QRegExp(r"^[a-zA-Z\s]+$")
        Name_validator3 = QRegExpValidator(Name_regex3)
        self.lineEdit_26.setValidator(Name_validator3)
        self.button_handler = ButtonHandler(self.lineEdit_26)
        self.dateEdit_3 = QtWidgets.QDateEdit(self.tabWidget_2Page1)
        self.dateEdit_3.setGeometry(QtCore.QRect(370, 750, 131, 35))
        self.dateEdit_3.setObjectName("dateEdit_3")
        self.dateEdit_3.setToolTip("enter your day of birth")  # Set the tooltip
        self.button_handler = ButtonHandler(self.dateEdit_3)
        self.lineEdit_27 = QtWidgets.QLineEdit(self.tabWidget_2Page1)
        self.lineEdit_27.setGeometry(QtCore.QRect(340, 240, 231, 31))
        self.lineEdit_27.setObjectName("lineEdit_27")
        self.lineEdit_27.setToolTip("Enter your Phone number")  # Set the tooltip
        # Create the regular expression validator
        phone_regex = QRegExp(r"^\d{10}$")
        phone_validator = QRegExpValidator(phone_regex)

        # Set the validator on the lineEdit_27 widget
        self.lineEdit_27.setValidator(phone_validator)

        self.button_handler = ButtonHandler(self.lineEdit_27)
        self.label_35 = QtWidgets.QLabel(self.tabWidget_2Page1)
        self.label_35.setGeometry(QtCore.QRect(70, 200, 61, 31))
        self.label_35.setObjectName("label_35")
        self.comboBox_10 = QtWidgets.QComboBox(self.tabWidget_2Page1)
        self.comboBox_10.setGeometry(QtCore.QRect(370, 805, 131, 35))
        self.comboBox_10.setObjectName("comboBox_10")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.setToolTip("Enter your pathological condition")  # Set the tooltip
        self.button_handler = ButtonHandler(self.comboBox_10)
        self.lineEdit_28 = QtWidgets.QLineEdit(self.tabWidget_2Page1)
        self.lineEdit_28.setGeometry(QtCore.QRect(340, 320, 231, 31))
        self.lineEdit_28.setObjectName("lineEdit_28")
        self.lineEdit_28.setToolTip("Enter your city name")  # Set the tooltip
        Name_regex4 = QRegExp(r"^[a-zA-Z\s]+$")
        Name_validator4 = QRegExpValidator(Name_regex4)
        self.lineEdit_28.setValidator(Name_validator4)
        self.button_handler = ButtonHandler(self.lineEdit_28)
        self.lineEdit_29 = QtWidgets.QLineEdit(self.tabWidget_2Page1)
        self.lineEdit_29.setGeometry(QtCore.QRect(340, 80, 231, 31))
        self.lineEdit_29.setMaxLength(10)
        self.lineEdit_29.setObjectName("lineEdit_29")
        self.lineEdit_29.setToolTip("Enter your last name")  # Set the tooltip
        Name_regex5 = QRegExp(r"^[a-zA-Z\s]+$")
        Name_validator5 = QRegExpValidator(Name_regex5)
        self.lineEdit_29.setValidator(Name_validator5)
        self.button_handler = ButtonHandler(self.lineEdit_29)
        self.label_36 = QtWidgets.QLabel(self.tabWidget_2Page1)
        self.label_36.setGeometry(QtCore.QRect(140, 560, 61, 51))
        self.label_36.setObjectName("label_36")
        self.label_37 = QtWidgets.QLabel(self.tabWidget_2Page1)
        self.label_37.setGeometry(QtCore.QRect(70, 280, 81, 31))
        self.label_37.setObjectName("label_37")
        self.lineEdit_30 = QtWidgets.QLineEdit(self.tabWidget_2Page1)
        self.lineEdit_30.setGeometry(QtCore.QRect(70, 160, 231, 31))
        self.lineEdit_30.setObjectName("lineEdit_30")
        self.lineEdit_30.setToolTip("Enter your mother name")  # Set the tooltip
        Name_regex6 = QRegExp(r"^[a-zA-Z\s]+$")
        Name_validator6 = QRegExpValidator(Name_regex6)
        self.lineEdit_30.setValidator(Name_validator6)
        self.button_handler = ButtonHandler(self.lineEdit_30)
        self.comboBox_11 = QtWidgets.QComboBox(self.tabWidget_2Page1)
        self.comboBox_11.setGeometry(QtCore.QRect(370, 500, 131, 35))
        self.comboBox_11.setObjectName("comboBox_11")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.setToolTip("Enter your pathological condition")  # Set the tooltip
        self.button_handler = ButtonHandler(self.comboBox_11)
        self.label_38 = QtWidgets.QLabel(self.tabWidget_2Page1)
        self.label_38.setGeometry(QtCore.QRect(340, 280, 81, 31))
        self.label_38.setObjectName("label_38")
        self.label_39 = QtWidgets.QLabel(self.tabWidget_2Page1)
        self.label_39.setGeometry(QtCore.QRect(340, 200, 91, 31))
        self.label_39.setObjectName("label_39")
        self.label_40 = QtWidgets.QLabel(self.tabWidget_2Page1)
        self.label_40.setGeometry(QtCore.QRect(140, 750, 61, 31))
        self.label_40.setObjectName("label_40")
        self.comboBox_12 = QtWidgets.QComboBox(self.tabWidget_2Page1)
        self.comboBox_12.setGeometry(QtCore.QRect(370, 635, 131, 35))
        self.comboBox_12.setObjectName("comboBox_12")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.label_41 = QtWidgets.QLabel(self.tabWidget_2Page1)
        self.label_41.setGeometry(QtCore.QRect(340, 370, 111, 31))
        self.label_41.setObjectName("label_41")
        self.label_42 = QtWidgets.QLabel(self.tabWidget_2Page1)
        self.label_42.setGeometry(QtCore.QRect(70, 120, 121, 31))
        self.label_42.setObjectName("label_42")
        self.label_43 = QtWidgets.QLabel(self.tabWidget_2Page1)
        self.label_43.setGeometry(QtCore.QRect(140, 500, 151, 31))
        self.label_43.setObjectName("label_43")
        self.label_44 = QtWidgets.QLabel(self.tabWidget_2Page1)
        self.label_44.setGeometry(QtCore.QRect(340, 120, 211, 31))
        self.label_44.setObjectName("label_44")
        self.lineEdit_31 = QtWidgets.QLineEdit(self.tabWidget_2Page1)
        self.lineEdit_31.setGeometry(QtCore.QRect(70, 240, 231, 31))
        self.lineEdit_31.setObjectName("lineEdit_31")
        self.lineEdit_31.setToolTip("Enter your email")  # Set the tooltip
        self.button_handler = ButtonHandler(self.lineEdit_31)
        self.lineEdit_32 = QtWidgets.QLineEdit(self.tabWidget_2Page1)
        self.lineEdit_32.setGeometry(QtCore.QRect(340, 410, 231, 31))
        self.lineEdit_32.setObjectName("lineEdit_32")
        self.lineEdit_32.setToolTip("Enter your native language")  # Set the tooltip
        Name_regex7 = QRegExp(r"^[a-zA-Z\s]+$")
        Name_validator7 = QRegExpValidator(Name_regex7)
        self.lineEdit_32.setValidator(Name_validator7)
        self.button_handler = ButtonHandler(self.lineEdit_32)

        # Set the button to be flat (without a frame)
        self.label_45 = QtWidgets.QLabel(self.tabWidget_2Page1)
        self.label_45.setGeometry(QtCore.QRect(70, 40, 51, 31))
        self.label_45.setObjectName("label_45")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.tabWidget_2Page1)
        self.tableWidget_3.setGeometry(QtCore.QRect(590, 150, 1340, 780))
        self.tableWidget_3.setStyleSheet("background-color:#B39DDB;\n"
"\n"
"\n"
"")
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(16)
        self.tableWidget_3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(16, item)

        self.lineEdit_33 = QtWidgets.QLineEdit(self.tabWidget_2Page1)
        self.lineEdit_33.setStyleSheet("""
        QLineEdit {
                background-color: white;
                color: black;
                font-size: 16px;
                border: 3px solid #000;
                border-radius: 15px;
                padding: 5px 15px;
                margin-right: 10px;
        }
        """)
        self.lineEdit_33.setPlaceholderText("Search For Name")
        self.lineEdit_33.setFixedSize(300, 40)
        self.lineEdit_33.setToolTip("Enter the name of item you want to search")  # Set the tooltip
        self.button_handler = ButtonHandler(self.lineEdit_33)


        self.search_button = QtWidgets.QPushButton(self.tabWidget_2Page1)
        self.search_button.setStyleSheet("""
        QPushButton {
                background-color:#CE93D8;
                color: black;
                font-size: 20px;
                border: 3px solid #000;
                border-radius: 15px;
                padding: 5px 15px;
        }
        QPushButton:hover {
                background-color: #E1BEE7;
                border: 3px solid #00A;
                color:black;
        }
        """)

        self.search_button.setText("Search")
        self.search_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.search_button.setFixedSize(120, 50)
        self.search_button.setToolTip("write the item you want to search about and press search")  # Set the tooltip
        self.button_handler = ButtonHandler(self.search_button)

        search_layout = QtWidgets.QHBoxLayout()
        search_layout.addWidget(self.lineEdit_33)
        search_layout.addWidget(self.search_button)
        search_layout.setSpacing(10)
        search_layout.setContentsMargins(0, 0, 0, 0)

        search_container = QtWidgets.QWidget(self.tabWidget_2Page1)
        search_container.setGeometry(QtCore.QRect(1400, 70, 420, 50))
        search_container.setLayout(search_layout)

        self.pushButton_10 = QtWidgets.QPushButton(self.tabWidget_2Page1)
        self.pushButton_10.setGeometry(QtCore.QRect(200, 850, 211, 61))
        self.pushButton_10.setStyleSheet("QPushButton{\n"
                                                "background-color:#CE93D8;\n"
                                                "border:3px solid #000;\n"
                                                "border-radius:15px;\n"
                                                "color:black;\n"
                                                "font-size:20px;\n"
                                                "\n"
                                                "}\n"
                                                "\n"
                                                "\n"
                                                "QPushButton:hover{\n"
                                                "           background-color:#E1BEE7;\n"
                                                "           border:3px solid #000;\n"
                                                "           color:black;\n"
                                                "\n"
                                "}")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.setToolTip("Fill all blank with data and Press to save")  # Set the tooltip
        self.button_handler = ButtonHandler(self.pushButton_10)
        self.pushButton_11 = QtWidgets.QPushButton(self.tabWidget_2Page1)
        self.pushButton_11.setGeometry(QtCore.QRect(950, 70, 161, 51))
        self.pushButton_11.setStyleSheet("QPushButton{\n"
"background-color:#CE93D8;\n"
"border:3px solid #000;\n"
"border-radius:15px;\n"
"color:black;\n"
"font-size:20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"           background-color:#E1BEE7;\n"
"           border:3px solid #000;\n"
"           color:black;\n"
"\n"
"\n"
"}")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_11.setToolTip("Select item and press to change the item")  # Set the tooltip
        self.button_handler = ButtonHandler(self.pushButton_11)

        self.pushButton_12 = QtWidgets.QPushButton(self.tabWidget_2Page1)
        self.pushButton_12.setGeometry(QtCore.QRect(1150, 70, 161, 51))
        self.pushButton_12.setStyleSheet("\n"
"QPushButton{\n"
"background-color:#CE93D8;\n"
"border:3px solid #000;\n"
"border-radius:15px;\n"
"color:black;\n"
"font-size:20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"           background-color:#E1BEE7;\n"
"           border:3px solid #000;\n"
"           color:black;\n"
"\n"
"\n"
"}")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_12.setToolTip("Select item and press delete to delete the item")  # Set the tooltip


        self.show_button = QtWidgets.QPushButton(self.tabWidget_2Page1)
        self.show_button.setGeometry(QtCore.QRect(700, 70, 211, 61))
        width=200
        hight=50
        self.show_button.resize(width,hight)
        self.show_button.setText("Show Student Score")
        self.show_button.setToolTip('To show all student Score Press in this button')


        # self.image_viewer = QtWidgets.QPushButton(self.tabWidget_2Page1)
        # self.image_viewer.setGeometry(QtCore.QRect(630, 70, 211, 61))
        # width=150
        # hight=50
        # self.image_viewer.resize(width,hight)
        # self.image_viewer.setText("Show Photo")
        # self.image_viewer.setToolTip('Select the Item and Press in this button to show the photo for the Student')
        


        self.button_handler = ButtonHandler(self.pushButton_12)
        self.tabWidget_2.addTab(self.tabWidget_2Page1, "")
        self.tabWidget_2Page2 = QtWidgets.QWidget()
        self.tabWidget_2Page2.setObjectName("tabWidget_2Page2")
        self.tabWidget_2.addTab(self.tabWidget_2Page2, "")
        self.tabWidget.addTab(self.tab1, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1851, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout_app = QtWidgets.QAction(MainWindow)
        self.actionAbout_app.setObjectName("actionAbout_app")
        self.actionUsage = QtWidgets.QAction(MainWindow)
        self.actionUsage.setObjectName("actionUsage")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionAbout_app)
        self.menuFile.addAction(self.actionUsage)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        #         # Add new Mode menu
        # self.menuMode = QtWidgets.QMenu(self.menubar)
        # self.menuMode.setObjectName("menuMode")

        # # Add Dark Mode action
        # self.actionDarkMode = QtWidgets.QAction(MainWindow)
        # self.actionDarkMode.setObjectName("actionDarkMode")

        # # Add the action to the Mode menu
        # self.menuMode.addAction(self.actionDarkMode)

        # # Add Mode menu to the menu bar
        # self.menubar.addAction(self.menuMode.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_31.setText(_translate("MainWindow", "Age "))
        self.label_32.setText(_translate("MainWindow", "Martial Status"))
        self.comboBox_9.setItemText(0, _translate("MainWindow", "Male"))
        self.comboBox_9.setItemText(1, _translate("MainWindow", "Female"))
        self.comboBox_9.setToolTip("Enter your Gender")  # Set the tooltip
        self.button_handler = ButtonHandler(self.comboBox_9)
        self.label_33.setText(_translate("MainWindow", "Lastname"))
        self.label_34.setText(_translate("MainWindow", "Study"))
        self.label_35.setText(_translate("MainWindow", "Email"))
        self.comboBox_10.setItemText(0, _translate("MainWindow", "Single"))
        self.comboBox_10.setItemText(1, _translate("MainWindow", "maried"))
        self.comboBox_10.setToolTip("Enter your Martial status")  # Set the tooltip
        self.button_handler = ButtonHandler(self.comboBox_10)
        self.label_36.setText(_translate("MainWindow", "Gender"))
        self.label_37.setText(_translate("MainWindow", "Country"))
        self.comboBox_11.setItemText(0, _translate("MainWindow", "Sick"))
        self.comboBox_11.setItemText(1, _translate("MainWindow", "Not sick"))
        self.label_38.setText(_translate("MainWindow", "City"))
        self.label_39.setText(_translate("MainWindow", "Phonenumber"))
        self.label_40.setText(_translate("MainWindow", "Birthday"))
        self.comboBox_12.setItemText(0, _translate("MainWindow", "Collage"))
        self.comboBox_12.setItemText(1, _translate("MainWindow", "School"))
        self.comboBox_12.setItemText(2, _translate("MainWindow", "Akadimy"))
        self.comboBox_12.setItemText(3, _translate("MainWindow", "University"))
        self.comboBox_12.setToolTip("where you study")  # Set the tooltip
        self.button_handler = ButtonHandler(self.comboBox_12)
        self.label_41.setText(_translate("MainWindow", "Native Languages"))
        self.label_42.setText(_translate("MainWindow", "Mother name"))
        self.label_43.setText(_translate("MainWindow", "Pathological condition"))
        self.label_44.setText(_translate("MainWindow", "Father name"))
        self.label_45.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Last name"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Mother name"))
        item = self.tableWidget_3.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Father Name"))
        item = self.tableWidget_3.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Email"))
        item = self.tableWidget_3.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Phonenumber"))
        item = self.tableWidget_3.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Country"))
        item = self.tableWidget_3.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "City"))
        item = self.tableWidget_3.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Age "))
        item = self.tableWidget_3.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Native Language"))
        item = self.tableWidget_3.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Health"))
        item = self.tableWidget_3.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "Gender"))
        item = self.tableWidget_3.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "Study"))
        item = self.tableWidget_3.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "Birthday"))
        item = self.tableWidget_3.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "Martial Status"))
        item = self.tableWidget_3.horizontalHeaderItem(15)
        item.setText(_translate("MainWindow", "Image"))
        self.lineEdit_33.setPlaceholderText(_translate("MainWindow", "Search For Item"))
        self.pushButton_10.setText(_translate("MainWindow", "Save"))
        self.pushButton_11.setText(_translate("MainWindow", "Change"))
        self.pushButton_12.setText(_translate("MainWindow", "Delete"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("MainWindow", "INFO"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        # ... (your existing translations)

        # Add translations for new menu and action
        # self.menuMode.setTitle(_translate("MainWindow", "Mode"))
        # self.actionDarkMode.setText(_translate("MainWindow", "Dark Mode"))
        self.actionAbout_app.setText(_translate("MainWindow", "About app"))
        self.actionUsage.setText(_translate("MainWindow", "Usage"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
