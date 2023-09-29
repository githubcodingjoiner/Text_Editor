from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtGui import QFont
import sys
class MYGUI(QMainWindow):

    def __init__(self):
        super(MYGUI, self).__init__()
        loadUi('Editor.ui', self)
        self.show()

        self.current_path = None
        self.current_size = 8
        self.setWindowTitle("Python text editor ")

        self.actionNew.triggered.connect(self.new_File)
        self.actionOpen.triggered.connect(self.open_file)
        self.actionSave.triggered.connect(self.save_file)
        self.actionUndo.triggered.connect(self.undo)
        self.actionRedo.triggered.connect(self.redo)
        self.actionCut.triggered.connect(self.cut)
        self.actionCopy.triggered.connect(self.copy)
        self.actionPaste.triggered.connect(self.paste)
        self.actionLightMode.triggered.connect(self.setLightMode)
        self.actionDarkMode.triggered.connect(self.setDarkMode)
        self.actionDecrease_Font_Size.triggered.connect(self.dec_size)
        self.actionIncrease_Font_Size.triggered.connect(self.inc_size)
        self.actionClose.triggered.connect(exit)

    def inc_size(self):
        self.current_size += 1
        self.plainTextEdit.setFont(QFont("Arial",self.current_size))

    def dec_size(self):
        self.current_size -= 1
        self.plainTextEdit.setFont(QFont("Arial",self.current_size))

    def new_File(self):
        self.plainTextEdit.clear()
        self.setWindowTitle("Python text editor")

    def undo(self):
        self.plainTextEdit.undo()

    def redo(self):
        self.plainTextEdit.redo()

    def cut(self):
        self.plainTextEdit.cut()

    def copy(self):
        self.plainTextEdit.copy()

    def paste(self):
        self.plainTextEdit.paste()

    def setLightMode(self):
        self.setStyleSheet("")

    def setDarkMode(self):
        self.setStyleSheet(''' QWidget{
        background-color: rgb(33,33,33);
    color: #ffffff;
    }
    QTextEdit{
    background-color:rgb(46,46,46);
    }
    QMenuBar::item:selected{
    color: #000000;
    }''')

    def open_file(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;Python Files (*.py)",options =options)
        if filename != "":
            with open(filename, "r") as f:
                self.plainTextEdit.setPlainText(f.read())

    def save_file(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getSaveFileName(self, "Save File", "" , "Text Files (*.txt);;All Files(*) ", options=options)
        if filename != "":
            with open(filename,"w") as f:
                f.write(self.plainTextEdit.toPlainText())

    def closeEvent(self, event):
        dialog = QMessageBox()
        dialog.setText("DO YOU WANT TO SAVE YOUR TEXT ?")
        dialog.addButton(QPushButton("YES"), QMessageBox.YesRole)#0
        dialog.addButton(QPushButton("NO"), QMessageBox.NoRole)#1
        dialog.addButton(QPushButton("CANCEL"), QMessageBox.RejectRole)#2

        answer = dialog.exec_()

        if answer == 0:
            self.save_file()
            event.accept()

        elif answer == 2:
            event.ignore()


def main():
    app=QApplication(sys.argv)
    window = MYGUI()
    window.show()
    app.exec_()

if __name__=='__main__':
    main()