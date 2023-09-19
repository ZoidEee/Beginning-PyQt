# lebels.py
# Import necessary modules

import sys

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QWidget, QLabel


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Set up the application"""
        self.setGeometry(100, 100, 250, 250)
        self.setWindowTitle("QLabel Example")
        self.setUpMainWindow()
        self.show()  # Display the window on screen

    def setUpMainWindow(self):
        """ Create QLabel to be displayed in the main window."""
        hello_label = QLabel(self)
        hello_label.setText("Hello")
        hello_label.move(105, 15)

        image = "Images/world.png"
        try:
            with  open(image):
                world_label = QLabel(self)
                pixmap = QPixmap(image)
                world_label.setPixmap(pixmap)
                world_label.move(25, 40)
        except FileNotFoundError as error:
            print(f"Image not found.\nError: {error}")


# Run the program
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
