# procedural.py
# 1. Import necessary modules
import sys  # use sys to accept command line argument

from PyQt6.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)  # 2. Create QApplication Object
window = QWidget()  # 3. Create window from QWidget object
window.show()  # 4. Call show to display GUI window
sys.exit(app.exec())
