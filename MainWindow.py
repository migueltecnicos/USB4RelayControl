from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPixmap, QPalette
from MainWindow_ui import Ui_MainWindow
from UsbRelayBoard import UsbRelayBoard

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configure GUI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect click signals to slots
        self.ui.cmd_r1_on.clicked.connect(lambda: self.button_clicked(1, 1))
        self.ui.cmd_r1_off.clicked.connect(lambda: self.button_clicked(1, 0))
        self.ui.cmd_r2_on.clicked.connect(lambda: self.button_clicked(2, 1))
        self.ui.cmd_r2_off.clicked.connect(lambda: self.button_clicked(2, 0))
        self.ui.cmd_r3_on.clicked.connect(lambda: self.button_clicked(3, 1))
        self.ui.cmd_r3_off.clicked.connect(lambda: self.button_clicked(3, 0))
        self.ui.cmd_r4_on.clicked.connect(lambda: self.button_clicked(4, 1))
        self.ui.cmd_r4_off.clicked.connect(lambda: self.button_clicked(4, 0))

        # Board object, it should be moved, depending on serial port
        self.board = UsbRelayBoard('COM21', False, 1)

    def button_clicked(self, relay, value):
        # Código del slot
        self.board.turn_on_off(relay, value)
