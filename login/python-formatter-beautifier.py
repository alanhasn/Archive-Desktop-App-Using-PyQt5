# Import necessary modules
from PyQt5.QtWidgets import (
    QTableWidget,
    QApplication,
    QMainWindow,
    QPushButton,
    QLineEdit,
    QLabel,
    QVBoxLayout,
    QWidget,
    QMessageBox,
    QTableWidgetItem,
)  # import the main thing from Qtwidget class
from PyQt5.QtGui import *  # import all method from Qtgui
from PyQt5.QtCore import *  # import all method from Qtcore
from PyQt5.QtWidgets import (
    QScrollArea,
    QFileDialog,
    QDialog,
    QHBoxLayout,
)  # to add the file dialog when the user press in the add photo
import sqlite3  # to use the sqlit database
import base64  # to encrypt the image and added in the database
from login_page import Ui_MainWindow  # import the file design for login page
from Archive_app import Ui2_MainWindow  # import the file design for Archive page
import sys  # import system module
from io import BytesIO
from PIL import Image
import os  # for use the path method
from grade_page import Ui3_MainWindow
from Show_grade_page import Ui4_MainWindow

# Define the main window class
class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.M_initUI()  # Initialize the user interface
        self.M_perform_login()  # login function

    # Method to close the window
    def close_window(self):
        quit()  # quit function

    # Method to initialize the user interface
    def M_initUI(self):
        # set the window title
        self.setWindowTitle("Login")
        # Set fixed size for the window
        self.setFixedSize(430, 500)

        # add the icon in the login page
        icon_path = "login/image/locked.png"  # path of icon
        self.setWindowIcon(QIcon(icon_path))  # add it into the Qicon

        # Create a label to display an image
        self.label1 = QLabel(self)
        # Load the logo and app image
        image_path = os.path.join(os.path.dirname(__file__), "image/logoo.png")
        self.pixmap1 = QPixmap(image_path)

        # Resize the images
        pixmap_width = 140
        pixmap_height = 140
        self.pixmap1 = self.pixmap1.scaled(pixmap_width, pixmap_height)

        # Set the logo image to the label
        self.label1.setPixmap(self.pixmap1)

        # Resize the label to fit the image
        self.label1.resize(pixmap_width, pixmap_height)

        # Set the position of the label
        x_position1 = 140
        y_position1 = 30
        self.label1.move(x_position1, y_position1)

        # Create a close button
        self.close_button = QPushButton(self)

        # Set the text and style of the close button
        self.close_button.setText("❌")
        self.close_button.setStyleSheet("font-size:20px;")
        self.close_button.resize(30, 30)
        x = 400
        y = 2
        self.close_button.move(x, y)
        self.close_button.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                color: #FFFFFF;
                border: none;
                font-size:15px;
            }
            QPushButton:hover {
                background-color:white;
                font-size:20px;
            }
        """
        )

        # Connect the button's clicked signal to the close_window method
        self.close_button.clicked.connect(self.close_window)

        # Set the window to be frameless
        self.setWindowFlag(Qt.FramelessWindowHint)

        x = 130
        y = 380
        self.ui.pushButton.move(x, y)

    # Method for login functionality
    def M_perform_login(self):
        self.ui.pushButton.clicked.connect(
            self.M_login
        )  # connect the logtin button with M_perform_login function

    # function for perform login process
    def M_login(self):
        self.username = self.ui.lineEdit_2.text()  # take a text from lineEdit 1
        self.password = self.ui.lineEdit_3.text()  # take a text from lineEdit 2

        conn = sqlite3.connect("login/admin.db")  # connect with the database
        cursor = conn.cursor()  # create chanel between database and python

        query = "SELECT * FROM admin_data WHERE username=? AND password=?"  # the query to perform from data in database and admin input
        cursor.execute(query, (self.username, self.password))  # execute the query

        result = (
            cursor.fetchall()
        )  # استيراد كافة الصفوف التي تم إرجاعها بواسطة استعلام SQL الذي تم تنفيذه مسبقًا
        if result:  # if the result is true
            self.open_app_window()  # run the open_app_window function
            self.ui.lineEdit_2.setText("")  # clean the line Edit1
            self.ui.lineEdit_3.setText("")  # clean the line Edit2

        else:  # else the result is not true
            # show message box warning the username and password is incorrect
            self.message = QMessageBox(self)
            self.message.setIcon(QMessageBox.Warning)
            self.message.setText("The Username And Password is incorrect")
            self.message.setWindowTitle("Incorrect DATA")
            # Apply custom stylesheet
            self.message.setStyleSheet(
                """
                QMessageBox {
                    background-color:black;
                    font-size: 15px;
                }
                QMessageBox QLabel {
                    color:rgb(0, 229, 255);                                   
                    font-size:20px;                   
                }
                QMessageBox QPushButton {
                    background-color:#000;
                    color: white;
                    padding: 5px;
                    border-radius: 10px;
                    border: 1px solid rgb(0, 229, 255);
                }
                QMessageBox QPushButton:hover {
                    background-color: rgb(0, 229, 255);
                    color:black;                   
                
                }
            """
            )

            self.message.exec_()

        cursor.close()  # close the cursor
        conn.close()  # close the connection

    def open_app_window(self):  # open app window function for run the app_window class
        self.app_window = AppWindow()
        self.app_window.show()  # display the app window
        self.close()  # to close the Login window when i login in the app
        # this is the method in QMainWindow class becouse LoginWindow is inheritins  from QmainWindow


class AppWindow(QMainWindow):  # app window class for import the UI2_Mainwindow function from the archive_app file design
    def __init__(self):
        super().__init__()
        self.UI = Ui2_MainWindow()
        self.UI.setupUi(self)
        self.init_UI()  # the function for initialize the user interface
        self.perform_save()  # the function for run the save function
        self.perform_delete()  # the function for run the delete function
        self.perform_change()  # the function for run the change function
        self.Menufile_Actions()  # the menu file action for run all function for munu file action
        self.setup_menu_styles()  # the function for set style for munu file action
        self.load_images()
        # self.import_data_from_database()
        self.search_perform()
        # self.perform_mode()
        # self.dark_mode=False
        self.add_grade_perform()
        self.show_grade_perform()
        # self.perform_show()
        self.current_image_data = None

    def init_UI(self):  # the # Initialize User interface for Archive app
        self.setWindowTitle("Simorx Archive")  # add the Window title
        self.setFixedSize(1920, 1005)  # set the fixed size

        # add icon in app
        image_path = "login/image/simorg_logo.png"  # image path
        self.setWindowIcon(QIcon(image_path))  # set the icon use The QIcon method
        self.grade_button = QPushButton("Add Grade", self)
        self.grade_button.setToolTip("")
        self.grade_button.setGeometry(340, 740, 131, 35)
        self.grade_button.setToolTip("Add the Grade of the Student")
        self.grade_button.setStyleSheet(
            """
            QPushButton{
            border: 3px solid #7E57C2;
            background-color: white;}
                                                                    
            QPushButton:hover{
            background-color:#CE93D8;
            color: black ;      
            border: 3px solid #000;
            }"""
        )
        label = QLabel("Add the subjects grade", self)
        label.setGeometry(106, 740, 160, 35)
        label.setStyleSheet(
            """  
        QLabel{
            background-color:transparent;                
            color:black;
            font-size:15px;                
            }                  
    """
        )
        Browse = QPushButton(self)
        Browse.setIcon(QIcon("login/image/image (2).png"))
        Browse.setIconSize(QSize(40, 40))
        Browse.setToolTip("Add the Photo")
        Browse.setFlat(True)
        Browse.setGeometry(290, 495, 250, 50)
        Browse.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                border: none;
                padding: 0;
            }
            QPushButton:hover, QPushButton:pressed {
                background-color: transparent;
            }
        """
        )
        Browse.clicked.connect(self.upload_image)

        label = QLabel("Add Photo", self)
        label.setGeometry(120, 500, 200, 50)
        label.setStyleSheet(
            """
                QLabel{
                    color:black; 
                    font-size:15px;      
                }
        """
        )
        self.input_layout = QHBoxLayout()
        self.image_label = QLabel(self)
        self.image_label.setFixedSize(50, 50)
        self.image_label.move(450, 495)

    def upload_image(self):
        options = QFileDialog.Options()
        self.filePath, _ = QFileDialog.getOpenFileName(
            self, "Open Image File", "", "Images (*.png *.jpg *.bmp)", options=options
        )
        if self.filePath:
            with open(self.filePath, "rb") as image_file:
                self.current_image_data = base64.b64encode(image_file.read()).decode(
                    "utf-8"
                )
                self.show_image(self.current_image_data)

    def show_image(self, image_data):
        decoded_data = base64.b64decode(image_data)
        image = Image.open(BytesIO(decoded_data))
        image = image.convert("RGBA")
        image.thumbnail((200, 200))
        qimage = QImage.fromData(decoded_data)
        pixmap = QPixmap.fromImage(qimage)
        self.image_label.setPixmap(pixmap)
        self.image_label.setScaledContents(True)
        self.input_layout.addWidget(self.image_label)

    def load_images(self):
        conn = sqlite3.connect("login/Archive.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM Archive_data")
        rows = cur.fetchall()

        self.UI.tableWidget_3.setRowCount(0)
        for index, row in enumerate(rows):
            (
                name,
                L_name,
                M_name,
                F_name,
                Email,
                PH_num,
                Country,
                City,
                Age,
                N_lang,
                Health,
                Gender,
                Study,
                Birth,
                Mar_status,
                image_data,
            ) = row

            temp_file_path = f"temp_image_{index}.png"
            with open(temp_file_path, "wb") as image_file:
                image_file.write(base64.b64decode(image_data))

            row_position = self.UI.tableWidget_3.rowCount()
            self.UI.tableWidget_3.insertRow(row_position)
            self.UI.tableWidget_3.setItem(row_position, 0, QTableWidgetItem(name))
            self.UI.tableWidget_3.setItem(row_position, 1, QTableWidgetItem(L_name))
            self.UI.tableWidget_3.setItem(row_position, 2, QTableWidgetItem(M_name))
            self.UI.tableWidget_3.setItem(row_position, 3, QTableWidgetItem(F_name))
            self.UI.tableWidget_3.setItem(row_position, 4, QTableWidgetItem(Email))
            self.UI.tableWidget_3.setItem(row_position, 5, QTableWidgetItem(PH_num))
            self.UI.tableWidget_3.setItem(row_position, 6, QTableWidgetItem(Country))
            self.UI.tableWidget_3.setItem(row_position, 7, QTableWidgetItem(City))
            self.UI.tableWidget_3.setItem(row_position, 8, QTableWidgetItem(Age))
            self.UI.tableWidget_3.setItem(row_position, 9, QTableWidgetItem(N_lang))
            self.UI.tableWidget_3.setItem(row_position, 10, QTableWidgetItem(Health))
            self.UI.tableWidget_3.setItem(row_position, 11, QTableWidgetItem(Gender))
            self.UI.tableWidget_3.setItem(row_position, 12, QTableWidgetItem(Study))
            self.UI.tableWidget_3.setItem(row_position, 13, QTableWidgetItem(Birth))
            self.UI.tableWidget_3.setItem(
                row_position, 14, QTableWidgetItem(Mar_status)
            )

            view_button = QPushButton("View Image", self)
            view_button.clicked.connect(
                lambda checked, path=temp_file_path: self.view_image(path)
            )
            self.UI.tableWidget_3.setCellWidget(row_position, 15, view_button)
            view_button.setStyleSheet(
                """
                    QPushButton{
                       background-color:#CE93D8;
                        border:2px solid #000 ;
                       color:black;
        
                                      
                    }
                      """
            )

    def view_image(self, file_path):
        if os.path.exists(file_path):
            os.startfile(file_path)
        else:
            QMessageBox.warning(self, "Error", "File not found.")

    def mesageBox_sytle(self, title, text, icon):
        # show warning message box
        self.message = QMessageBox(self)
        self.message.setIcon(icon)
        self.message.setText(text)
        self.message.setWindowTitle(title)
        # Apply custom stylesheet
        self.message.setStyleSheet(
            """
            QMessageBox {
                background-color:#CE93D8;
                color:black;
                font-size: 15px;
            }
            QMessageBox QLabel {
                background-color:#CE93D8;  
                color: #000;                  
                font-size:20px;                   
            }
            QMessageBox QPushButton {
                background-color:#42A5F5;
                color: black;
                padding: 5px;
                border-radius: 5px;
                border: 1px solid #CE93D8;
            }
            QMessageBox QPushButton:hover {
                background-color: #8E24AA;
            }
        """
        )
        self.message.exec_()  # show the message box

    # save button functions
    def perform_save(self):  # for connect the save button with Save button function
        self.UI.pushButton_10.clicked.connect(
            self.save_button
        )  # connect the function with the save button

    def save_button(self):  # save button function
        # Take the Data from LineEdits and Comboboxs and DataEdit and save it in the variabel
        self.Age = self.UI.lineEdit_23.text()
        self.name = self.UI.lineEdit_24.text()
        self.F_name = self.UI.lineEdit_25.text()
        self.country = self.UI.lineEdit_26.text()
        self.phone_N = self.UI.lineEdit_27.text()
        self.City = self.UI.lineEdit_28.text()
        self.L_name = self.UI.lineEdit_29.text()
        self.M_name = self.UI.lineEdit_30.text()
        self.Email = self.UI.lineEdit_31.text()
        self.native_Lang = self.UI.lineEdit_32.text()
        self.health = self.UI.comboBox_11.currentText()
        self.gender = self.UI.comboBox_9.currentText()
        self.study = self.UI.comboBox_12.currentText()
        self.birthday = self.UI.dateEdit_3.text()
        self.martial_s = self.UI.comboBox_10.currentText()

        # التأكد من ان جميع البيانات مملوء
        # if this lineEdits is empty show warning message  box
        if not all(
            [
                self.name
                and self.L_name
                and self.M_name
                and self.F_name
                and self.Email
                and self.country
                and self.City
                and self.Age
                and self.phone_N
                and self.native_Lang,
                self.current_image_data,
            ]
        ):
            self.mesageBox_sytle(
                "Save Error",
                "Please Fill all blank with the Data to Complete and upload an image",
                QMessageBox.Warning,
            )

        elif all(
            [
                self.name
                and self.L_name
                and self.M_name
                and self.F_name
                and self.Email
                and self.country
                and self.City
                and self.Age
                and self.phone_N
                and self.native_Lang,
                self.current_image_data,
            ]
        ):
            # check if the email feild content the valid and @ symbol
            for i in self.Email:
                if i == "@":
                    break
            at_index = self.Email.find("@")
            if at_index != -1:
                if self.Email[at_index:] == "@gmail.com":
                    cc = self.Email[at_index:]
                else:
                    QMessageBox.about(
                        self, "Envalid Email", "please enter the valid Email address"
                    )
                    return
            else:
                QMessageBox.about(
                    self, "symbol Error", "the Email is not content the @ symbol"
                )
                return
            if hasattr(self, "current_image_data"):
                try:
                    conn = sqlite3.connect("login/Archive.db")
                    cur = conn.cursor()
                    QUERY = "INSERT INTO Archive_data (Name, Last_name, Mother_name, Father_name, Email, Phone_number, Country, City, Age, Native_language, Health, Gender, Study, Birthday, Martial_Status,Image_data) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"

                    cur.execute(
                        QUERY,
                        (
                            self.name,
                            self.L_name,
                            self.M_name,
                            self.F_name,
                            self.Email,
                            self.phone_N,
                            self.country,
                            self.City,
                            self.Age,
                            self.native_Lang,
                            self.health,
                            self.gender,
                            self.study,
                            self.birthday,
                            self.martial_s,
                            self.current_image_data,
                        ),
                    )
                    conn.commit()
                    self.load_images()
                    self.image_label.clear()
                    cur.close()
                    conn.close()
                except Exception as e:
                    QMessageBox.about(self, "Error", f"the error {e}")

            # clean all line edit set the default
            self.UI.lineEdit_24.setText("")
            self.UI.lineEdit_29.setText("")
            self.UI.lineEdit_30.setText("")
            self.UI.lineEdit_25.setText("")
            self.UI.lineEdit_31.setText("")
            self.UI.lineEdit_27.setText("")
            self.UI.lineEdit_26.setText("")
            self.UI.lineEdit_28.setText("")
            self.UI.lineEdit_23.setText("")
            self.UI.lineEdit_32.setText("")
            self.UI.comboBox_11.setCurrentText("sick")
            self.UI.comboBox_9.setCurrentText("male")
            self.UI.comboBox_12.setCurrentText("Collage")
            self.UI.dateEdit_3.setDate(QDate.fromString("00/00/0000", "dd/MM/yyyy"))
            self.UI.comboBox_10.setCurrentText("")

    def perform_delete(self):  # connect the delete buttom with the delete function
        self.UI.pushButton_12.clicked.connect(self.Delete_Func)

    def Delete_Func(self):

        selected_row = (
            self.UI.tableWidget_3.currentRow()
        )  # take the row the user is selected
        if selected_row >= 0:  # if the selected row is > or equal 0
            name = self.UI.tableWidget_3.item(
                selected_row, 0
            ).text()  # take the text from the selected row
            # delete the selected row from database
            conn = sqlite3.connect("login/Archive.db")
            cur = conn.cursor()
            q2 = "DELETE FROM Archive_data WHERE name=?"  # quary to delete the selected row where the name is like the user is select
            cur.execute(q2, (name,))  # execute the quary

            conn.commit()  # commit change
            cur.close()
            conn.close()
            self.load_images()
        else:
            self.mesageBox_sytle(
                "Select Error", "Select Item to Delete", QMessageBox.Warning
            )

    # change button functions
    def perform_change(self):
        self.UI.pushButton_11.clicked.connect(
            self.change
        )  # connect the the change button with the change function

    def change(self):  # change func for the change item in table widget
        selected_row = self.UI.tableWidget_3.currentRow()  # take the selected row
        if selected_row >= 0:

            # Retrieve data from the selected row to the variable
            name = self.UI.tableWidget_3.item(selected_row, 0).text()
            l_name = self.UI.tableWidget_3.item(selected_row, 1).text()
            m_name = self.UI.tableWidget_3.item(selected_row, 2).text()
            f_name = self.UI.tableWidget_3.item(selected_row, 3).text()
            email = self.UI.tableWidget_3.item(selected_row, 4).text()
            phone = self.UI.tableWidget_3.item(selected_row, 5).text()
            country = self.UI.tableWidget_3.item(selected_row, 6).text()
            city = self.UI.tableWidget_3.item(selected_row, 7).text()
            Age = self.UI.tableWidget_3.item(selected_row, 8).text()
            native_lang = self.UI.tableWidget_3.item(selected_row, 9).text()
            health = self.UI.tableWidget_3.item(selected_row, 10).text()
            gender = self.UI.tableWidget_3.item(selected_row, 11).text()
            study = self.UI.tableWidget_3.item(selected_row, 12).text()
            birthday = self.UI.tableWidget_3.item(selected_row, 13).text()
            martial_s = self.UI.tableWidget_3.item(selected_row, 14).text()

            # Fill the line edits with the retrieved data
            self.UI.lineEdit_24.setText(name)
            self.UI.lineEdit_29.setText(l_name)
            self.UI.lineEdit_30.setText(m_name)
            self.UI.lineEdit_25.setText(f_name)
            self.UI.lineEdit_31.setText(email)
            self.UI.lineEdit_27.setText(phone)
            self.UI.lineEdit_26.setText(country)
            self.UI.lineEdit_28.setText(city)
            self.UI.lineEdit_23.setText(Age)
            self.UI.lineEdit_32.setText(native_lang)
            self.UI.comboBox_11.setCurrentText(health)
            self.UI.comboBox_9.setCurrentText(gender)
            self.UI.comboBox_12.setCurrentText(study)
            self.UI.dateEdit_3.setDate(QDate.fromString(birthday, "dd/MM/yyyy"))
            self.UI.comboBox_10.setCurrentText(martial_s)

            # Connect the save button to update function
            self.UI.pushButton_10.clicked.disconnect()  # disconnect the save button  with the save function and connect them with update function
            self.UI.pushButton_10.clicked.connect(
                lambda: self.update_item(selected_row)
            )  # connect the save button with update function

        else:  # else if the user is not select the item
            self.mesageBox_sytle(
                "Select Error", "Select Item to change", QMessageBox.Warning
            )

    def update_item(
        self, row
    ):  # for update the item the user is changed in table widget and in the database
        # Get the updated data from line edits
        name = self.UI.lineEdit_24.text()
        l_name = self.UI.lineEdit_29.text()
        m_name = self.UI.lineEdit_30.text()
        f_name = self.UI.lineEdit_25.text()
        email = self.UI.lineEdit_31.text()
        phone = self.UI.lineEdit_27.text()
        country = self.UI.lineEdit_26.text()
        city = self.UI.lineEdit_28.text()
        Age = self.UI.lineEdit_23.text()
        native_lang = self.UI.lineEdit_32.text()
        health = self.UI.comboBox_11.currentText()
        gender = self.UI.comboBox_9.currentText()
        study = self.UI.comboBox_12.currentText()
        birthday = self.UI.dateEdit_3.text()
        martial_s = self.UI.comboBox_10.currentText()

        # check if the Email field content the @ and valid email
        x = []
        for i in email:
            if i == "@":
                break
            x.append(i)
        at_index = email.find("@")
        if at_index != -1:
            if email[at_index:] == "@gmail.com":
                cc = email[at_index:]
            else:
                QMessageBox.about(
                    self, "Envalid Email", "please enter the valid Email address"
                )
                return
        if at_index == -1:
            QMessageBox.about(
                self, "symbol Error", "the Email is not content the @ symbol"
            )
            return

        # update database
        conn = sqlite3.connect("login/Archive.db")  # connect with database
        cur = conn.cursor()
        # the quary to update
        q = """UPDATE Archive_data SET  
            Name=?, Last_name=?, Mother_name=?, Father_name=?, Email=?, 
            Phone_number=?, Country=?, City=?, Age=?, Native_language=?, 
            Health=?, Gender=?, Study=?, Birthday=?, Martial_Status=?,
            image_data=? 
            WHERE Name =?
            """
        self.selected_row = self.UI.tableWidget_3.item(row, 0).text()
        cur.execute(
            q,
            (
                name,
                l_name,
                m_name,
                f_name,
                email,
                phone,
                country,  # execute the quary
                city,
                Age,
                native_lang,
                health,
                gender,
                study,
                birthday,
                martial_s,
                self.selected_row,
                self.current_image_data,
            ),
        )  # where the selected row

        conn.commit()  # commit change
        cur.close()  # close cursor
        conn.close()  # close database

        # Update the table widget
        self.UI.tableWidget_3.setItem(row, 0, QTableWidgetItem(name))
        self.UI.tableWidget_3.setItem(row, 1, QTableWidgetItem(l_name))
        self.UI.tableWidget_3.setItem(row, 2, QTableWidgetItem(m_name))
        self.UI.tableWidget_3.setItem(row, 3, QTableWidgetItem(f_name))
        self.UI.tableWidget_3.setItem(row, 4, QTableWidgetItem(email))
        self.UI.tableWidget_3.setItem(row, 5, QTableWidgetItem(phone))
        self.UI.tableWidget_3.setItem(row, 6, QTableWidgetItem(country))
        self.UI.tableWidget_3.setItem(row, 7, QTableWidgetItem(city))
        self.UI.tableWidget_3.setItem(row, 8, QTableWidgetItem(Age))
        self.UI.tableWidget_3.setItem(row, 9, QTableWidgetItem(native_lang))
        self.UI.tableWidget_3.setItem(row, 10, QTableWidgetItem(health))
        self.UI.tableWidget_3.setItem(row, 11, QTableWidgetItem(gender))
        self.UI.tableWidget_3.setItem(row, 12, QTableWidgetItem(study))
        self.UI.tableWidget_3.setItem(row, 13, QTableWidgetItem(birthday))
        self.UI.tableWidget_3.setItem(row, 14, QTableWidgetItem(martial_s))
        self.image_label.clear()
        self.load_images()

        # Reconnect the save button to the original save function
        self.UI.pushButton_10.clicked.disconnect()  # disconnect with update function
        self.UI.pushButton_10.clicked.connect(
            self.save_button
        )  # connect with save function again

        self.mesageBox_sytle(
            "Update", "The item Updated succesfully", QMessageBox.Information
        )

        # clear all entry after change
        self.UI.lineEdit_24.setText("")
        self.UI.lineEdit_29.setText("")
        self.UI.lineEdit_30.setText("")
        self.UI.lineEdit_25.setText("")
        self.UI.lineEdit_31.setText("")
        self.UI.lineEdit_27.setText("")
        self.UI.lineEdit_26.setText("")
        self.UI.lineEdit_28.setText("")
        self.UI.lineEdit_23.setText("")
        self.UI.lineEdit_32.setText("")
        self.UI.comboBox_11.setCurrentText("sick")
        self.UI.comboBox_9.setCurrentText("male")
        self.UI.comboBox_12.setCurrentText("Collage")
        self.UI.dateEdit_3.setDate(QDate.fromString("00/00/0000", "dd/MM/yyyy"))
        self.UI.comboBox_10.setCurrentText("")

    # import data from database

    # def import_data_from_database(self):
    #     conn = sqlite3.connect('login/Archive.db')
    #     cur = conn.cursor()
    #     cur.execute("SELECT * FROM Archive_data")
    #     rows = cur.fetchall()

    # self.UI.tableWidget_3.setRowCount(0)
    # for row_number, row_data in enumerate(rows):
    #     self.UI.tableWidget_3.insertRow(row_number)
    #     for column_number, data in enumerate(row_data[:-1]):  #[:-1]
    #         self.UI.tableWidget_3.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    #         # view_button = QPushButton("View Image", self)
    #         # view_button.clicked.connect(lambda checked, path=self.temp_file_path: self.view_image(path))
    #         # self.UI.tableWidget_3.setCellWidget(row_number, 16, view_button)

    #     cur.close()
    #     conn.close()
    # Action Menu Functions
    def setup_menu_styles(self):  # Add style to Action menu
        # Style for the menu
        menu_style = """
            QMenuBar {
                background-color: #CE93D8;
                color: black;
            }
            QMenuBar::item:selected {
                background-color: #42A5F5;
                color: black;
            }
            QMenu {
                background-color: #CE93D8;
                color: black;
            }
            QMenu::item:selected {
                background-color: #42A5F5;
                color: black;
            }
        """

        # Apply the style to the menu bar
        self.menuBar().setStyleSheet(menu_style)

    def Menufile_Actions(self):  # connect the action with it functions
        self.UI.actionAbout_app.triggered.connect(self.about_appAction)
        self.UI.actionExit.triggered.connect(self.exitAction)
        self.UI.actionUsage.triggered.connect(self.usageAction)

    def about_appAction(self):  # about app action to display the about QmessageBox
        about_text = """
        <ol>
            Simorx Archive Application
            Version 2.0<br><br>

        <li> This application is designed to manage and archive data and personal Info and The students subjects grade.</li><br><br>

            <strong style="color:#023e8a;">"Project Manager: H.Ciwan"</strong><br>
            <strong style="color:#000;">"Developed by: Alan Hassan"</strong>
        </ol>
        """
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("App Usage")
        msg_box.setText(about_text)
        msg_box.setIcon(QMessageBox.Information)

        # Apply custom stylesheet
        msg_box.setStyleSheet(
            """
        QMessageBox {
            background-color: #CE93D8;                  
        }
        QMessageBox QLabel {
            color: black;
            font-size: 20px;
            margin: 20px;
            padding: 20px;
            background-color: #7E57C2;
            border: 2px solid #000;
            border-radius: 10px;
        }
        QMessageBox QPushButton {
            background-color: #CE93D8;
            color: white;
            padding: 10px 20px;
            margin: 10px 5px;
            border: solid;
            border-radius: 5px;
            font-size: 16px;
            font-weight: bold;
        }
        QMessageBox QPushButton:hover {
            background-color:#AB47BC;
            color:black;                  
        }
        QLabel {
            min-width: 500px;
            min-height: 300px;
        }
    """
        )

        msg_box.exec_()

    def exitAction(self):  # exit action
        quit()

    def usageAction(self):  # usage action for display message how to use the app
        usage_text = """
        <ol>
        <strong>
            <li>Fill all blanks with the correct data.</li><br>
            <li>To add to the database, press the save button (it will also be added to the table).</li><br>
            <li>To add the Student Score  Press in the Add grade Button to add the score for student subject If you want to know Another info about using the Add grade window you can press in file menu bar in the new window and press in Usage.</li><br>
            <li>If you want to show all studnet Score press on the Show Student score Button</li><br>
            <li>To show the photo for the Users just select item and press on show Photo button.</li><br>
            <li>To search for any item or data in the table, write in the search entry and press the Search button.</li><br>
            <li>To change an item, select it, edit the data in the entries, and press save again to update.</li><br>
            <li>To delete an item, click on it and press the Delete Button.</li><br>
            <li>For more info about our program, click the File menu in the top left corner and select About app.</li><br>
        </strong>    
        </ol>
    """
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("App Usage")
        msg_box.setText(usage_text)
        msg_box.setIcon(QMessageBox.Information)

        # Apply custom stylesheet
        msg_box.setStyleSheet(
            """
        QMessageBox {
            background-color: #CE93D8;
        }
        QMessageBox QLabel {
            color: black;
            font-size: 16px;
            margin: 20px;
            padding: 20px;
            background-color: #BA68C8;
            border: 2px solid #000;
            border-radius: 10px;
        }
        QMessageBox QPushButton {
            background-color: #CE93D8;
            color: white;
            padding: 10px 20px;
            margin: 10px 5px;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            font-weight: bold;
        }
        QMessageBox QPushButton:hover {
            background-color: #AB47BC;
        }
        QLabel {
            min-width: 500px;
            min-height: 500px;
        }
    """
        )

        msg_box.exec_()

    # search and mode functions
    def search_perform(self):
        self.UI.search_button.clicked.connect(self.search_data)

    def search_data(self):
        search_text = (
            self.UI.lineEdit_33.text().lower()
        )  # take the text from the search line edit and turn it into lowecase
        if not search_text:  # if the search line edit is empty
            # If search text is empty, show all rows
            for row in range(self.UI.tableWidget_3.rowCount()):  # loop on all row
                self.UI.tableWidget_3.setRowHidden(row, False)  #  and show all row
            return

        found_items = False  # متغير للتحقق من وجود نتائج
        for row in range(self.UI.tableWidget_3.rowCount()):  # loop in all item
            match = False  # this var for see if it there the تطابق or not
            for column in range(
                self.UI.tableWidget_3.columnCount()
            ):  # this loop is run on all column in the current row
                item = self.UI.tableWidget_3.item(
                    row, column
                )  # take the item with the current row and column and save ot in var
                if (
                    item and search_text in item.text().lower()
                ):  # it compare if the search text is it in  the text of the item
                    match = True  # turn the match var to true if it see the تطابق
                    found_items = True  # تم العثور على الأقل على عنصر واحد
                    break  # and break
            self.UI.tableWidget_3.setRowHidden(
                row, not match
            )  # the Match = True it means the Not match = False , the match = False it means the Not match = True

        if not found_items:  # appear the message if there was no items found
            QMessageBox.about(self, "Search result", "No Items Found")

    # def perform_mode(self):
    #     self.UI.actionDarkMode.triggered.connect(self.toggle_dark_mode)
    def toggle_dark_mode(self):
        self.dark_mode = not self.dark_mode  # Toggle the dark mode state
        dark_mode_stylesheet = """
            QTabWidget {
                background-color: #000;
                color: #000;
            }
            QWidget {
                background-color: #000;
                color: #000;
            }
            QPushButton {
                background-color: #333;
                color: #eee;
            }
            QLineEdit {
                background-color: #333;
                color: #eee;
            }
            QLabel {
                background-color:#000;

            }
            QComboBox {
                background-color: #333;
                color: #eee;
            }
            QTableWidget, QTableWidget::item {
                background-color: #333;
                color: #fff;
            }
        """
        light_mode_stylesheet = """
            QTabWidget {
                background-color: #fff;
                color: #000;
            }
            QWidget {
                background-color: #fff;
                color: #000;
            }
            QPushButton {
                background-color: #fff;
                color: #000;
            }
            QLineEdit {
                background-color: #fff;
                color: #000;
            }
            QLabel {
                color: #000;
            }
            QComboBox {
                background-color: #fff;
                color: #000;
            }
            QTableWidget, QTableWidget::item {
                background-color: #fff;
                color: #000;
            }
        """

        if self.dark_mode:
            self.UI.tabWidget.setStyleSheet(dark_mode_stylesheet)
            self.UI.actionDarkMode.setText("Light mode")
        else:
            self.UI.tabWidget.setStyleSheet(light_mode_stylesheet)
            self.UI.actionDarkMode.setText("Dark mode")

    # grade page finctions
    def get_name_and_lastname(
        self,
    ):  # this func for get the data from the name and lastname entry
        name = self.UI.lineEdit_24.text()
        lastname = self.UI.lineEdit_29.text()
        return name, lastname

    def add_grade_perform(
        self,
    ):  # connect the grade buttoon with the open add grade func
        self.grade_button.clicked.connect(self.open_add_grade_window)

    def open_add_grade_window(self):  # this func for open the Add grade window
        self.add_grade_window = Add_grade_window()
        (
            name,
            lastname,
        ) = (
            self.get_name_and_lastname()
        )  # call the getname func for add the name and lastname in the var
        # here we call the setname func for set the name and
        self.add_grade_window.set_name_and_lastname(
            name, lastname
        )  # last name in the enry for the Add grade window
        self.add_grade_window.show()

    def show_grade_perform(self):
        self.UI.show_button.clicked.connect(self.show_grade_button)

    def show_grade_button(self):
        self.show_score = show_GradeWindow()
        self.show_score.show()


class Add_grade_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui3_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()
        self.save()
        self.import_data_from_database_grade()
        self.perform_delete()
        self.perform_change()
        self.search_perform()
        self.Menufile_action()
        self.setup_menu_styles()

    def set_name_and_lastname(
        self, name, lastname
    ):  # this the function for set name and lastname in the entry
        self.ui.lineEdit_24.setText(name)
        self.ui.lineEdit_29.setText(lastname)

    def init_ui(self):
        self.setWindowTitle("Simorg Grade  Archive")  # the title of the window
        self.setFixedSize(1666, 979)  # set the fixef size
        # add icon in app
        image_path = "login/image/simorg_logo.png"
        self.setWindowIcon(QIcon(image_path))

    def mesageBox_sytle(self, title, text, icon):
        # show warning message box
        self.message = QMessageBox(self)
        self.message.setIcon(icon)
        self.message.setText(text)
        self.message.setWindowTitle(title)
        # Apply custom stylesheet
        self.message.setStyleSheet(
            """
            QMessageBox {
                background-color:#006769;
                color:white;
                font-size: 15px;
            }
            QMessageBox QLabel {
                background-color:#006769 ;  
                color: white;                  
                font-size:20px;                   
            }
            QMessageBox QPushButton {
                background-color:#ECB159;
                color: black;
                padding: 5px;
                border-radius: 5px;
                border: 1px solid rgb(0, 229, 255);
            }
            QMessageBox QPushButton:hover {
                background-color: rgb(0, 179, 204);
            }
        """
        )
        self.message.exec_()  # show the message box

    def save(self):
        self.ui.pushButton.clicked.connect(self.save_button)

    def save_button(self):

        self.name = self.ui.lineEdit_24.text()
        self.last_name = self.ui.lineEdit_29.text()
        self.math = self.ui.comboBox.currentText()
        self.A = self.ui.comboBox_2.currentText()
        self.English = self.ui.comboBox_3.currentText()
        self.Android = self.ui.comboBox_4.currentText()
        self.python = self.ui.comboBox_5.currentText()
        self.Django = self.ui.comboBox_6.currentText()
        self.sql = self.ui.comboBox_7.currentText()
        self.server = self.ui.comboBox_8.currentText()
        self.Linux = self.ui.comboBox_9.currentText()

        if not all(
            [
                self.name,
                self.last_name,
                self.math,
                self.A,
                self.English,
                self.Android,
                self.python,
                self.Django,
                self.sql,
                self.server,
                self.Linux,
            ]
        ):
            self.mesageBox_sytle(
                "Save Error",
                "Please Fill all blank with the Data to Complete",
                QMessageBox.Warning,
            )

        else:
            # save the data in Database
            conn = sqlite3.connect("login/Archive.db")  # connect with Database
            cur = conn.cursor()  # create Chanel
            # the Query for add Data in database
            QUERY = "INSERT INTO student_grade (name,last_name,math_score,A_plus_score,English_score,Android_score,python_score,Django_score,Sql_score,server_score,linux_score)  VALUES(?,?,?,?,?,?,?,?,?,?,?)"
            # execute the Query
            cur.execute(
                QUERY,
                (
                    self.name,
                    self.last_name,
                    self.math,
                    self.A,
                    self.English,
                    self.Android,
                    self.python,
                    self.Django,
                    self.sql,
                    self.server,
                    self.Linux,
                ),
            )

            conn.commit()  # commit the changes
            cur.close()  # close the chanel
            conn.close()  # close the Connection

            row_position = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(row_position)

            self.ui.tableWidget.setItem(row_position, 0, QTableWidgetItem(self.name))
            self.ui.tableWidget.setItem(
                row_position, 1, QTableWidgetItem(self.last_name)
            )
            self.ui.tableWidget.setItem(row_position, 2, QTableWidgetItem(self.math))
            self.ui.tableWidget.setItem(row_position, 3, QTableWidgetItem(self.A))
            self.ui.tableWidget.setItem(row_position, 4, QTableWidgetItem(self.English))
            self.ui.tableWidget.setItem(row_position, 5, QTableWidgetItem(self.Android))
            self.ui.tableWidget.setItem(row_position, 6, QTableWidgetItem(self.python))
            self.ui.tableWidget.setItem(row_position, 7, QTableWidgetItem(self.Django))
            self.ui.tableWidget.setItem(row_position, 8, QTableWidgetItem(self.sql))
            self.ui.tableWidget.setItem(row_position, 9, QTableWidgetItem(self.server))
            self.ui.tableWidget.setItem(row_position, 10, QTableWidgetItem(self.Linux))

            self.ui.lineEdit_24.setText("")
            self.ui.lineEdit_29.setText("")
            self.ui.comboBox.setCurrentText("Good")
            self.ui.comboBox_2.setCurrentText("Good")
            self.ui.comboBox_3.setCurrentText("Good")
            self.ui.comboBox_4.setCurrentText("Good")
            self.ui.comboBox_5.setCurrentText("Good")
            self.ui.comboBox_6.setCurrentText("Good")
            self.ui.comboBox_7.setCurrentText("Good")
            self.ui.comboBox_8.setCurrentText("Good")
            self.ui.comboBox_9.setCurrentText("Good")

    def import_data_from_database_grade(self):
        conn = sqlite3.connect("login/Archive.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM student_grade")
        data = cur.fetchall()

        self.ui.tableWidget.setRowCount(
            0
        )  # set the row count  to 0 it means it will delete all data before add the database data
        for row_data in data:  # create for loop in all data in the data variable
            row = (
                self.ui.tableWidget.rowCount()
            )  # count the number of row in the table widget
            self.ui.tableWidget.insertRow(row)  # add the new row in the table widget
            for column, item in enumerate(
                row_data
            ):  # create enumeration in the row_data:    column=index of item  , item=the row
                self.ui.tableWidget.setItem(
                    row, column, QTableWidgetItem(str(item))
                )  # add the item in the table widget

        conn.commit()
        cur.close()
        conn.close()  # close connection

    def perform_delete(self):
        self.ui.pushButton_3.clicked.connect(self.delete_button)

    def delete_button(self):
        selected_row = (
            self.ui.tableWidget.currentRow()
        )  # take the row the user is selected
        if selected_row >= 0:  # if the selected row is > or equal 0

            name = self.ui.tableWidget.item(
                selected_row, 0
            ).text()  # take the text from the selected row

            # delete the selected row from database
            conn = sqlite3.connect("login/Archive.db")
            cur = conn.cursor()
            q2 = "DELETE FROM student_grade WHERE name=?"  # quary to delete the selected row where the name is like the user is select
            cur.execute(q2, (name,))  # execute the quary

            conn.commit()  # commit change
            cur.close()
            conn.close()
            self.import_data_from_database_grade()

        else:
            self.mesageBox_sytle(
                "Select Error", "Select Item to Delete", QMessageBox.Warning
            )

    def perform_change(self):
        self.ui.pushButton_2.clicked.connect(self.change_button)

    def change_button(self):
        selected_row = self.ui.tableWidget.currentRow()  # take the selected row
        if selected_row >= 0:

            # Retrieve data from the selected row to the variable
            id = self.ui.tableWidget.item(selected_row, 0).text()
            name = self.ui.tableWidget.item(selected_row, 0).text()
            last_name = self.ui.tableWidget.item(selected_row, 1).text()
            math = self.ui.tableWidget.item(selected_row, 2).text()
            A = self.ui.tableWidget.item(selected_row, 3).text()
            English = self.ui.tableWidget.item(selected_row, 4).text()
            Android = self.ui.tableWidget.item(selected_row, 5).text()
            Python = self.ui.tableWidget.item(selected_row, 6).text()
            django = self.ui.tableWidget.item(selected_row, 7).text()
            sql = self.ui.tableWidget.item(selected_row, 8).text()
            server = self.ui.tableWidget.item(selected_row, 9).text()
            if self.ui.tableWidget.item(selected_row, 10) is not None:
                linux = self.ui.tableWidget.item(selected_row, 10).text()

            else:
                linux = ""

            # Fill the line edits with the retrieved data
            self.ui.lineEdit_24.setText(name)
            self.ui.lineEdit_29.setText(last_name)
            self.ui.comboBox.setCurrentText(math)
            self.ui.comboBox_2.setCurrentText(A)
            self.ui.comboBox_3.setCurrentText(English)
            self.ui.comboBox_4.setCurrentText(Android)
            self.ui.comboBox_5.setCurrentText(Python)
            self.ui.comboBox_6.setCurrentText(django)
            self.ui.comboBox_7.setCurrentText(sql)
            self.ui.comboBox_8.setCurrentText(server)
            self.ui.comboBox_9.setCurrentText(linux)

            # Connect the save button to update function
            self.ui.pushButton.clicked.disconnect()  # disconnect the save button  with the save function and connect them with update function
            self.ui.pushButton.clicked.connect(
                lambda: self.update_item(selected_row)
            )  # connect the save button with update function

        else:  # else if the user is not select the item
            self.mesageBox_sytle(
                "Select Error", "Select Item to change", QMessageBox.Warning
            )

    def update_item(self, row):
        try:
            # Fill the line edits with the retrieved data
            name = self.ui.lineEdit_24.text()
            last_name = self.ui.lineEdit_29.text()
            math = self.ui.comboBox.currentText()
            A = self.ui.comboBox_2.currentText()
            english = self.ui.comboBox_3.currentText()
            Android = self.ui.comboBox_4.currentText()
            python = self.ui.comboBox_5.currentText()
            django = self.ui.comboBox_6.currentText()
            sql = self.ui.comboBox_7.currentText()
            server = self.ui.comboBox_8.currentText()
            linux = self.ui.comboBox_9.currentText()

            # update database
            conn = sqlite3.connect("login/Archive.db")  # connect with database
            cur = conn.cursor()
            # the quary to update
            q = """UPDATE student_grade 
                        SET name=?, last_name=?, math_score=?, A_plus_score=?, English_score=?,
                            Android_score=?, python_score=?, Django_score=?, Sql_score=?, server_score=?,
                            linux_score=?
                        WHERE Name=?
                        """
            cur.execute(
                q,
                (
                    name,
                    last_name,
                    math,
                    A,
                    english,
                    Android,
                    python,  # execute the quary
                    django,
                    sql,
                    server,
                    linux,
                    self.ui.tableWidget.item(row, 0).text(),
                ),
            )  # where the selected row
            conn.commit()  # commit change
            cur.close()  # close cursor
            conn.close()  # close database

            # Update the table widget
            # Update the table widget
            self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(name))
            self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(last_name))
            self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(math))
            self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(A))
            self.ui.tableWidget.setItem(row, 4, QTableWidgetItem(english))
            self.ui.tableWidget.setItem(row, 5, QTableWidgetItem(Android))
            self.ui.tableWidget.setItem(row, 6, QTableWidgetItem(python))
            self.ui.tableWidget.setItem(row, 7, QTableWidgetItem(django))
            self.ui.tableWidget.setItem(row, 8, QTableWidgetItem(sql))
            self.ui.tableWidget.setItem(row, 9, QTableWidgetItem(server))
            self.ui.tableWidget.setItem(row, 10, QTableWidgetItem(linux))

            # Reconnect the save button to the original save function
            self.ui.pushButton.clicked.disconnect()  # disconnect with update function
            self.ui.pushButton.clicked.connect(
                self.save
            )  # connect with save function again
            self.mesageBox_sytle(
                "Update", "The item Updated succesfully", QMessageBox.Information
            )

            # clear all entry after change
            self.ui.lineEdit_24.setText("")
            self.ui.lineEdit_29.setText("")
            self.ui.comboBox.setCurrentIndex(0)
            self.ui.comboBox_2.setCurrentIndex(0)
            self.ui.comboBox_3.setCurrentIndex(0)
            self.ui.comboBox_4.setCurrentIndex(0)
            self.ui.comboBox_5.setCurrentIndex(0)
            self.ui.comboBox_6.setCurrentIndex(0)
            self.ui.comboBox_7.setCurrentIndex(0)
            self.ui.comboBox_8.setCurrentIndex(0)
            self.ui.comboBox_9.setCurrentIndex(0)
        except AttributeError as A:
            QMessageBox.about(self, "Error", "Unknown Error Please Try again")

    def search_perform(self):
        self.ui.pushButton_5.clicked.connect(self.search_data)

    def search_data(self):

        search_text = (
            self.ui.lineEdit.text().lower()
        )  # take the text from the search line edit and turn it into lowecase
        if not search_text:  # if the search line edit is empty
            # If search text is empty, show all rows
            for row in range(self.ui.tableWidget.rowCount()):  # loop on all row
                self.ui.tableWidget.setRowHidden(row, False)  #  and show all row
            return

        found_items = False  # متغير للتحقق من وجود نتائج
        for row in range(self.ui.tableWidget.rowCount()):  # loop in all item
            match = False  # this var for see if it there the تطابق or not
            for column in range(
                self.ui.tableWidget.columnCount()
            ):  # this loop is run on all column in the current row
                item = self.ui.tableWidget.item(
                    row, column
                )  # take the item with the current row and column and save ot in var
                if (
                    item and search_text in item.text().lower()
                ):  # it compare if the search text is it in  the text of the item
                    match = True  # turn the match var to true if it see the تطابق
                    found_items = True  # تم العثور على الأقل على عنصر واحد
                    break  # and break
            self.ui.tableWidget.setRowHidden(
                row, not match
            )  # the Match = True it means the Not match = False , the match = False it means the Not match = True

        if not found_items:  # appear the message if there was no items found
            QMessageBox.about(self, "Search result", "No Items Found")

    def setup_menu_styles(self):  # Add style to Action menu
        # Style for the menu
        menu_style = """
            QMenuBar {
                background-color: #CE93D8;
                color: #CE93D8;
            }
            QMenuBar::item:selected {
                background-color: #E1BEE7;
                color: black;
            }
            QMenu {
                background-color: #CE93D8;
                color: #CE93D8;
            }
            QMenu::item:selected {
                background-color: #E1BEE7;
                color: black;
            }
        """

        # Apply the style to the menu bar
        self.menuBar().setStyleSheet(menu_style)

    def Menufile_action(self):
        self.ui.actionUsgae.triggered.connect(self.UsageAction)
        self.ui.actionExit.triggered.connect(self.Quit)
        self.ui.actionAbout_Us.triggered.connect(self.About_Action)

    def Quit(self):
        quit()

    def UsageAction(self):
        usage_text = """
        <ol>
        <strong>
            <li>Fill all blanks with the correct score.</li><br>
            <li>To add to the score in the database, press the save button (it will also be added to the table).</li><br>
            <li>To Change The Item Select Item and Press Change button the data wil be retrieved in the Entrys and press save to change.</li><br>
            <li>To delete the Item From Database Select the Item and press Delete button.</li><br>
            <li>To search in the Items Write the Name of any info in the Search entry and press in the search button</li><br>
            <li>For more info about our program, click the File menu in the top left corner and select About app.</li><br>
        </strong>    
        </ol>
                    """
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("App Usage")
        msg_box.setText(usage_text)
        msg_box.setIcon(QMessageBox.Information)

        # Apply custom stylesheet
        msg_box.setStyleSheet(
            """
        QMessageBox {
            background-color: #CE93D8;
        }
        QMessageBox QLabel {
            color: #000;
            font-size: 16px;
            margin: 20px;
            padding: 20px;
            background-color: #CE93D8;
            border: 2px solid #E1BEE7;
            border-radius: 10px;
        }
        QMessageBox QPushButton {
            background-color: #CE93D8;
            color: white;
            padding: 10px 20px;
            margin: 10px 5px;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            font-weight: bold;
        }
        QMessageBox QPushButton:hover {
            background-color: #E1BEE7;
        }
        QLabel {
            min-width: 500px;
            min-height: 500px;
        }
    """
        )

        msg_box.exec_()

    def About_Action(self):
        about_text = """
        <ol>
            Simorx Archive Application
            Version 2.0<br><br>

        <li> This Window is designed for Add the student subjects Score In the Database</li><br><br>

            <strong style="color:#006769;">" Project Manageer: H.ciwan"</strong><br>
            <strong style="color:#006769;">"Developed by: Alan Hassan"</strong>
        </ol>
        """
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("App Usage")
        msg_box.setText(about_text)
        msg_box.setIcon(QMessageBox.Information)

        # Apply custom stylesheet
        msg_box.setStyleSheet(
            """
        QMessageBox {
            background-color: #00b4d8;                  
        }
        QMessageBox QLabel {
            color: #000;
            font-size: 20px;
            margin: 20px;
            padding: 20px;
            background-color: #ffffff;
            border: 2px solid #cccccc;
            border-radius: 10px;
        }
        QMessageBox QPushButton {
            background-color: #006769;
            color: white;
            padding: 10px 20px;
            margin: 10px 5px;
            border: solid;
            border-radius: 5px;
            font-size: 16px;
            font-weight: bold;
        }
        QMessageBox QPushButton:hover {
            background-color:#ECB159;
            color:black;                  
        }
        QLabel {
            min-width: 500px;
            min-height: 300px;
        }
    """
        )

        msg_box.exec_()


class show_GradeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui4_MainWindow()
        self.ui.setupUi(self)
        self.import_data_from_database()
        self.search_perform()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Student Score")  # add the Window title
        self.setFixedSize(1384, 770)  # set the fixed size

        # add icon in app
        image_path = "login/image/simorg_logo.png"  # image path
        self.setWindowIcon(QIcon(image_path))  # set the icon use The QIcon method

    def import_data_from_database(self):
        conn = sqlite3.connect("login/Archive.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM student_grade")
        data = cur.fetchall()

        self.ui.tableWidget.setRowCount(
            0
        )  # set the row count  to 0 it means it will delete all data before add the database data
        for row_data in data:  # create for loop in all data in the data variable
            row = (
                self.ui.tableWidget.rowCount()
            )  # count the number of row in the table widget
            self.ui.tableWidget.insertRow(row)  # add the new row in the table widget
            for column, item in enumerate(
                row_data
            ):  # create enumeration in the row_data:    column=index of item  , item=the row
                self.ui.tableWidget.setItem(
                    row, column, QTableWidgetItem(str(item))
                )  # add the item in the table widget

        conn.commit()
        cur.close()
        conn.close()  # close connection

    def search_perform(self):
        self.ui.pushButton.clicked.connect(self.search_data)

    def search_data(self):

        search_text = (
            self.ui.lineEdit.text().lower()
        )  # take the text from the search line edit and turn it into lowecase
        if not search_text:  # if the search line edit is empty
            # If search text is empty, show all rows
            for row in range(self.ui.tableWidget.rowCount()):  # loop on all row
                self.ui.tableWidget.setRowHidden(row, False)  #  and show all row
            return

        found_items = False  # متغير للتحقق من وجود نتائج
        for row in range(self.ui.tableWidget.rowCount()):  # loop in all item
            match = False  # this var for see if it there the تطابق or not
            for column in range(
                self.ui.tableWidget.columnCount()
            ):  # this loop is run on all column in the current row
                item = self.ui.tableWidget.item(
                    row, column
                )  # take the item with the current row and column and save ot in var
                if (
                    item and search_text in item.text().lower()
                ):  # it compare if the search text is it in  the text of the item
                    match = True  # turn the match var to true if it see the تطابق
                    found_items = True  # تم العثور على الأقل على عنصر واحد
                    break  # and break
            self.ui.tableWidget.setRowHidden(
                row, not match
            )  # the Match = True it means the Not match = False , the match = False it means the Not match = True

        if not found_items:  # appear the message if there was no items found
            QMessageBox.about(self, "Search result", "No Items Found")


def main():  # the main function for run the main window  logon window.clicked,c
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    app.exec_()


if __name__ == "__main__":  # to run the main function
    main()
