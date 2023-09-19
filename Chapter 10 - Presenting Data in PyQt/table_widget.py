# table_widget.py
# Import necessary modules


import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QMenu, QInputDialog
from PyQt6.QtGui import QAction


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """ Set up the application's GUI """
        self.setMinimumSize(1000, 500)
        self.setWindowTitle("Spreadsheet - QTableWidget Example")

        # Used for copy and paste actions

        self.item_text = None

        self.setUpMainWindow()
        self.createActions()
        self.createMenu()
        self.show()

    def setUpMainWindow(self):
        self.table_widget = QTableWidget()

        # Set initial row and column values
        self.table_widget.setRowCount(10)
        self.table_widget.setColumnCount(10)

        # Set focus on cell in the table
        self.table_widget.setCurrentCell(0, 0)

        # When the horizontal headers are double-clicked,
        # emit a signal
        h_header = self.table_widget.horizontalHeader()
        h_header.sectionDoubleClicked.connect(self.changeHeader)

        self.setCentralWidget(self.table_widget)

    def createActions(self):
        """ Create the application's menu actions """
        # Create acitons File menu
        self.quit_act = QAction("Quit", self)
        self.quit_act.setShortcut("Crtl+Q")
        self.quit_act.triggered.connect(self.close)

        # Create actions for Table menu
        self.add_row_above_act = QAction(
            "Add Row Above", self
        )
        self.add_row_above_act.triggered.connect(self.addRowAbove)

        self.add_row_below_act = QAction(
            "Add Row Below", self
        )
        self.add_row_below_act.triggered.connect(self.addRowBelow)

        self.add_col_befor_act = QAction("Add Column Before", self)
        self.add_col_befor_act.triggered.connect(self.addColumnBefore)

        self.add_col_after_act = QAction("Add Column After", self)
        self.add_col_after_act.triggered.connect(self.addColumnAfter)

        self.delete_row_act = QAction("Delete Row", self)
        self.delete_row_act.triggered.connect(self.deleteRow)

        self.delete_col_act = QAction("Delete Column", self)
        self.delete_col_act.triggered.connect(self.deleteColumn)

        self.clear_table_act = QAction("Clear All", self)
        self.clear_table_act.triggered.connect(self.clearTable)

    def createMenu(self):
        """ Create the application's menu bar """
        self.menuBar().setNativeMenuBar(False)

        # Create a file menu and add actions

        file_menu = self.menuBar().addMenu("File")
        file_menu.addAction(self.quit_act)

        # Create a table menu and add actions
        table_menu = self.menuBar().addMenu('Table')
        table_menu.addAction(self.add_row_above_act)
        table_menu.addAction(self.add_row_below_act)
        table_menu.addSeparator()
        table_menu.addAction(self.add_col_befor_act)
        table_menu.addAction(self.add_col_after_act)
        table_menu.addSeparator()
        table_menu.addAction(self.delete_row_act)
        table_menu.addAction(self.delete_col_act)
        table_menu.addSeparator()
        table_menu.addAction(self.clear_table_act)

    def contextMenuEvent(self, event):
        """ Create context menu and additionals actions """
        context_menu = QMenu(self)
        context_menu.addAction(self.add_row_above_act)
        context_menu.addAction(self.add_row_below_act)
        context_menu.addSeparator()
        context_menu.addAction(self.add_col_befor_act)
        context_menu.addAction(self.add_col_after_act)
        context_menu.addSeparator()
        context_menu.addAction(self.delete_row_act)
        context_menu.addAction(self.delete_col_act)
        context_menu.addSeparator()

        # Create actions specific to the context menu
        copy_act = context_menu.addAction("Copy")
        paste_act = context_menu.addAction("Paste")
        context_menu.addSeparator()
        context_menu.addAction(self.clear_table_act)

        # Execute the context_menu and return the actions
        # selected. mapToGlobal() translates the position
        # of the window coordinates to the global screen
        # coordinates. this way we can detect if a right-click
        # occurred inside the GUI and display the context
        # menu
        action = context_menu.exec(self.mapToGlobal(event.pos()))

        # Check for actions selected in the context menu
        # that were not created in the menu bar
        if action == copy_act:
            self.copyItem()
        if action == paste_act:
            self.pasteItem()

    def changeHeader(self):
        """ Change horizontal headers by returning the text from the input dialog """
        col = self.table_widget.currentColumn()
        text, ok = QInputDialog(self, "Enter Header", "Header Text:")
        if ok and text != "":
            self.table_widget.setHorizontalHeaderItem(col, QTableWidgetItem(text))

    def copyItem(self):
        """ If the current cell selected is not empty,
        store the text """
        if self.table_widget.currentItem() != None:
            text = self.table_widget.currentItem().text()
            self.item_text = text

    def pasteItem(self):
        if self.item_text != None:
            row = self.table_widget.currentRow()
            column = self.table_widget.currentColumn()
            self.table_widget.setItem(row,column,QTableWidgetItem(self.item_text))


    def addRowAbove(self):
        current_row = self.table_widget.currentRow()
        self.table_widget.insertRow(current_row + 1)

    def addRowBelow(self):
        current_row = self.table_widget.currentRow()
        self.table_widget.insertRow(current_row)

    def addColumnBefore(self):
        current_col = self.table_widget.currentColumn()
        self.table_widget.insertColumn(current_col + 1)

    def addColumnAfter(self):
        current_col = self.table_widget.currentColumn()
        self.table_widget.insertColumn(current_col)

    def deleteRow(self):
        current_row = self.table_widget.currentRow()
        self.table_widget.removeRow(current_row)

    def deleteColumn(self):
        current_col = self.table_widget.currentColumn()
        self.table_widget.removeColumn(current_col)

    def clearTable(self):
        self.table_widget.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
