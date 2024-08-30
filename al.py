import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QStyledItemDelegate
from PyQt5.QtGui import QPainter, QPixmap, QColor
from PyQt5.QtCore import Qt, QPropertyAnimation, QEasingCurve, pyqtProperty

class BackgroundImageDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super(BackgroundImageDelegate, self).__init__(parent)
        self.background_image = QPixmap("login/image/logoo.png")
        self._color = QColor(224, 247, 250, 180)  # Light blue with some transparency

    def paint(self, painter, option, index):
        painter.save()
        
        # Draw the background image
        painter.drawPixmap(option.rect, self.background_image, option.rect)
        
        # Draw the hover color
        painter.fillRect(option.rect, self._color)
        
        painter.restore()
        
        # Draw the default cell content
        super(BackgroundImageDelegate, self).paint(painter, option, index)

    def color(self):
        return self._color

    def setColor(self, color):
        self._color = color

    color = pyqtProperty(QColor, color, setColor)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Table Widget with Background Image")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.table_widget = QTableWidget(5, 4)
        layout.addWidget(self.table_widget)

        # Set up the table
        self.setup_table()

        # Set up the background image and hover effect
        self.setup_background_and_hover()

    def setup_table(self):
        self.table_widget.setHorizontalHeaderLabels(["Name", "Age", "City", "Occupation"])
        
        # Sample data
        data = [
            ("Alice", "28", "New York", "Engineer"),
            ("Bob", "35", "Los Angeles", "Designer"),
            ("Charlie", "42", "Chicago", "Manager"),
            ("David", "31", "Houston", "Developer"),
            ("Eva", "39", "Miami", "Teacher")
        ]

        for row, (name, age, city, occupation) in enumerate(data):
            self.table_widget.setItem(row, 0, QTableWidgetItem(name))
            self.table_widget.setItem(row, 1, QTableWidgetItem(age))
            self.table_widget.setItem(row, 2, QTableWidgetItem(city))
            self.table_widget.setItem(row, 3, QTableWidgetItem(occupation))

        self.table_widget.resizeColumnsToContents()

    def setup_background_and_hover(self):
        delegate = BackgroundImageDelegate(self.table_widget)
        self.table_widget.setItemDelegate(delegate)

        # Make sure the background of the table is transparent
        self.table_widget.setStyleSheet("""
            QTableWidget {
                background-color: transparent;
                font-size: 15px;
                color: black;
                border: none;
            }
            QHeaderView::section {
                background-color: rgba(200, 200, 200, 180);
            }
        """)

        # Create the hover animation
        self.hover_animation = QPropertyAnimation(delegate, b"color")
        self.hover_animation.setDuration(300)  # 300 ms for the animation
        self.hover_animation.setEasingCurve(QEasingCurve.InOutQuad)

        # Connect to the table's entered and left signals
        self.table_widget.entered.connect(self.on_hover_enter)
        self.table_widget.viewportEntered.connect(self.on_hover_leave)

    def on_hover_enter(self, index):
        self.hover_animation.setStartValue(QColor(224, 247, 250, 180))  # Light blue with transparency
        self.hover_animation.setEndValue(QColor(128, 222, 234, 180))    # Darker shade with transparency
        self.hover_animation.start()

    def on_hover_leave(self):
        self.hover_animation.setStartValue(QColor(128, 222, 234, 180))  # Darker shade with transparency
        self.hover_animation.setEndValue(QColor(224, 247, 250, 180))    # Light blue with transparency
        self.hover_animation.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
