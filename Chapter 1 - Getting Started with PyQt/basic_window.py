# basic_window.py
# Import necessary modules

import sys

from PyQt6.QtWidgets import QApplication, QWidget


class EmptyWindow(QWidget):
    def __init__(self):
        """ Constructor for Empty Window Class"""
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Set up the application"""
        """ Initialize the window and display its contents to the screen."""
        self.setGeometry(200, 100, 400, 300)  # x, y , width, height
        self.setWindowTitle("Empty Window in PyQt")
        self.show()  # Display the window on screen


# Run the program
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EmptyWindow()
    sys.exit(app.exec())
