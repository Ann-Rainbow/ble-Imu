from PyQt5 import QtWidgets
from choose_exercise import Ui_Form as main_window_widget_ui
from leanings_forward import  Ui_Form as leanings_forward_ui
import sys
from core_main import start_test

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args):
        QtWidgets.QMainWindow.__init__(self, *args)
        self.mw = main_widget()
        self.lfw = leanings_forward_widget()
        self.mw.ui.pushButton_5.clicked.connect(self.ctlfw)
        self.lfw.ui.pushButton_2.clicked.connect(self.ctmw)
        self.mw.show()

    def ctlfw(self):
        self.mw.hide()
        self.lfw.show()

    def ctmw(self):
        self.lfw.hide()
        self.mw.show()


class main_widget(QtWidgets.QWidget):
    def __init__(self):
        super(main_widget, self).__init__()
        self.ui = main_window_widget_ui()
        self.ui.setupUi(self)
        # self.ui.pushButton_5.click.connect(self.hide)
        # self.ui.pushButton_5.click.connect()
        # self.show()

class leanings_forward_widget(QtWidgets.QWidget):
    def __init__(self):
        super(leanings_forward_widget, self).__init__()
        self.ui = leanings_forward_ui()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.on_start_clicked)

    def on_start_clicked(self):
        self.ui.result.setText(start_test())

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    mw = MainWindow()
    # mw.show()

    sys.exit(app.exec())