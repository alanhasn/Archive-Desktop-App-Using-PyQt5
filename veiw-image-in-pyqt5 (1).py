import sys
import base64
import sqlite3
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QLabel, QPushButton, QFileDialog, QVBoxLayout, QHBoxLayout, QWidget, QTableWidget, QTableWidgetItem, QMessageBox
from PIL import Image
import io
import os

class ImageApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.db_connection()

    def initUI(self):
        self.layout = QVBoxLayout()

        
        self.input_layout = QHBoxLayout()
        self.image_label = QLabel(self)
        self.image_label.setFixedSize(100, 100) 
        self.input_layout.addWidget(self.image_label)
        
        self.name_input = QtWidgets.QLineEdit(self)
        self.name_input.setPlaceholderText("Enter image name")
        self.input_layout.addWidget(self.name_input)
        
        self.upload_button = QPushButton("Upload Image", self)
        self.upload_button.clicked.connect(self.upload_image)
        self.input_layout.addWidget(self.upload_button)
        
        self.save_button = QPushButton("Save to Database", self)
        self.save_button.clicked.connect(self.save_to_database)
        self.input_layout.addWidget(self.save_button)
        
        self.layout.addLayout(self.input_layout)

        # Create table widget
        self.table = QTableWidget(self)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["ID", "File Name", "View Image", "Delete"])
        self.table.horizontalHeader().setStretchLastSection(True)
        self.layout.addWidget(self.table)
        
        # Add developer information
        self.dev_info = QLabel("Developer: Ciwan", self)
        self.dev_info.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.dev_info)

        self.setLayout(self.layout)
        self.setWindowTitle('Image Viewer')
        self.setGeometry(300, 300, 700, 400)
    
    def db_connection(self):
        self.conn = sqlite3.connect('images.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS images 
                                (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                file_name TEXT, 
                                image_data TEXT)''')
        self.conn.commit()
        self.load_images()

    def upload_image(self):
        options = QFileDialog.Options()
        filePath, _ = QFileDialog.getOpenFileName(self, "Open Image File", "", "Images (*.png *.jpg *.bmp)", options=options)
        if filePath:
            with open(filePath, "rb") as image_file:
                self.current_image_data = base64.b64encode(image_file.read()).decode('utf-8')
                self.show_image(self.current_image_data)
    
    def show_image(self, image_data):
        decoded_data = base64.b64decode(image_data)
        image = Image.open(io.BytesIO(decoded_data))
        image = image.convert("RGBA")
        image.thumbnail((100, 100)) 
        qimage = QtGui.QImage.fromData(decoded_data)
        pixmap = QtGui.QPixmap.fromImage(qimage)
        self.image_label.setPixmap(pixmap)
        self.image_label.setScaledContents(True)

    def save_to_database(self):
        file_name = self.name_input.text()
        if hasattr(self, 'current_image_data') and file_name:
            try:
                self.cursor.execute("INSERT INTO images (file_name, image_data) VALUES (?, ?)", 
                                    (file_name, self.current_image_data))
                self.conn.commit()
                self.load_images()
                self.image_label.clear()
                self.name_input.clear()
                print("Image saved to database successfully")
            except Exception as e:
                print(f"An error occurred while saving the image to the database: {e}")
        else:
            QtWidgets.QMessageBox.warning(self, "Input Error", "Please upload an image and enter a name.")

    def load_images(self):
        self.cursor.execute("SELECT id, file_name, image_data FROM images")
        rows = self.cursor.fetchall()
        
        self.table.setRowCount(0)
        for row in rows:
            id, file_name, image_data = row
            
            
            temp_file_path = f"temp_image_{id}.png"
            with open(temp_file_path, "wb") as image_file:
                image_file.write(base64.b64decode(image_data))
            
            row_position = self.table.rowCount()
            self.table.insertRow(row_position)
            self.table.setItem(row_position, 0, QTableWidgetItem(str(id)))
            self.table.setItem(row_position, 1, QTableWidgetItem(file_name))
            
            view_button = QPushButton("View Image", self)
            view_button.clicked.connect(lambda checked, path=temp_file_path: self.view_image(path))
            self.table.setCellWidget(row_position, 2, view_button)
            
            
            delete_button = QPushButton("Delete", self)
            delete_button.setStyleSheet("background-color: red; color: white;")
            delete_button.clicked.connect(lambda checked, id=id, pos=row_position: self.delete_image(id, pos))
            self.table.setCellWidget(row_position, 3, delete_button)

    def view_image(self, file_path):
        if os.path.exists(file_path):
            os.startfile(file_path)  
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "File not found.")

    def delete_image(self, id, row_position):
        reply = QMessageBox.question(self, 'Confirm Delete', 'Are you sure you want to delete this image?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            try:
                self.cursor.execute("DELETE FROM images WHERE id = ?", (id,))
                self.conn.commit()
                self.table.removeRow(row_position)
                self.load_images()
                print("Image deleted successfully")
            except Exception as e:
                print(f"An error occurred while deleting the image: {e}")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = ImageApp()
    ex.show()
    sys.exit(app.exec_())




