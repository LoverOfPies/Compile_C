import sys
from PyQt5.QtWidgets import QMainWindow, QWidget, QAction, qApp, QApplication, QGridLayout, QTextEdit, QLabel
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt


class Canvas(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.square.setGeometry(150, 20, 100, 100)
        self.square.setStyleSheet("QWidget { background-color: %s }" %
                                  self.col.name())
        self.show()


class MainLayout(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        canvas = Canvas()
        grid.addWidget(canvas, 0, 0)
        code = QLabel('Code')
        codeEdit = QTextEdit()
        grid.addWidget(code, 3, 0)
        grid.addWidget(codeEdit, 3, 1, 5, 1)

        self.setLayout(grid)

    def test(self):
        print("123")


class MyApplication(QMainWindow):
    __ex = None

    def __init__(self):
        super().__init__()
        self.__ex = MainLayout()
        self.initUI()

    def initUI(self):
        newAction = QAction('&New file', self)
        newAction.setShortcut('Ctrl+N')
        newAction.setStatusTip('New file')
        newAction.triggered.connect(self.new)

        exitAction = QAction('&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(newAction)
        fileMenu.addAction(exitAction)

        self.setCentralWidget(self.getMainLayout())

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Menubar')
        self.show()

    def getMainLayout(self):
        return self.__ex

    def new(self):
        self.getMainLayout().test()


def run():
    app = QApplication(sys.argv)
    my = MyApplication()
    sys.exit(app.exec_())
