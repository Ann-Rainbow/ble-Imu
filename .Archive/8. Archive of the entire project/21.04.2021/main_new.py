from PyQt5 import QtWidgets
from home_page_RU import Ui_Form as home_page_RU_ui # commented  home_page_RU_ui
from home_page_EN import Ui_Form as  home_page_EN_ui
from choose_exercise_EN import Ui_Form as choose_exercise_EN_ui
from choose_exercise_RU import Ui_Form as choose_exercise_RU_ui
from arm_raisings_to_the_sides_EN import Ui_Form as arm_raisings_to_the_sides_EN_ui
from arm_raisings_to_the_sides_RU import Ui_Form as arm_raisings_to_the_sides_RU_ui
from arm_raisings_forward_EN import Ui_From as arm_raisings_forward_EN_ui
from arm_raisings_forward_RU import Ui_From as arm_raisings_forward_RU_ui
import sys
from core_main import start_test

class hpRU_widget(QtWidgets.QMainWindow):
    def __init__(self, *args):
        QtWidgets.QMainWindow.__init__(self, *args)

    # def __init__(self):
    #     super(ceRU_widget, self).__init__()
        self.ui = home_page_RU_ui()
        self.ui.setupUi(self)

        self.hpRU = home_page_RU_widget()
        self.hpEN = home_page_EN_widget()
        self.ceRU = choose_exercise_RU_widget()

        self.hpRU.ui.pushButton.clicked.connect(self.ct_ceRU)
        self.hpRU.ui.pushButton_2.clicked.connect(self.ct_hpEN)
        self.hpRU.show()

    def ct_ceRU(self):
        hpRU_widget.hide()
        ceRU_widget.show()

    def ct_hpEN(self):
        hpRU_widget.hide()
        hpEN_widget.show()

class ceRU_widget(QtWidgets.QWidget):
    def __init__(self):
        super(ceRU_widget, self).__init__()
        self.ui = choose_exercise_RU_ui()
        self.ui.setupUi(self)

        self.ceRU = choose_exercise_RU_widget()
        self.arfRU = arm_raisings_forward_RU_widget()
        self.arttsRU = arm_raisings_to_the_sides_RU_widget()

        self.ceRU.ui.pushButton_5.clicked.connect(self.ct_arfRU)
        self.ceRU.ui.pushButton_4.clicked.connect(self.ct_arttsRU)
        self.ceRU.ui.pushButton.clicked.connect(self.ct_back)
        self.show()

    def ct_arfRU(self):
        self.ceRU.hide()
        self.arfRU.show()

    def ct_arttsRU(self):
        self.ceRU.hide()
        self.arttsRU.show()

    def ct_back(self):
        self.ceRU.hide()
        self.hpRU.show()

class arfRU_widget(QtWidgets.QWidget):
    def __init__(self):
        super(arfRU_widget, self).__init__()
        self.ui = arm_raisings_forward_RU_ui()
        self.ui.setupUi(self)

        self.arfRU = arm_raisings_forward_RU_widget()
        self.arfRU.ui.pushButton.clicked.connect(self.on_start_clicked2) # используется модель подьема руки через перёд.
        self.arfRU.ui.pushButton_2.clicked.connect(self.ct_back)
        self.show()

    def on_start_clicked2(self):
        self.ui.result.setText(start_test2()) # воображаемая функция, использует другую модель, написать в главном коде.

    def ct_back(self):
        self.arfRU.hide()
        self.ceRU.show()

class arttsRU_widget(QtWidgets.QWidget):
    def __init__(self):
        super(arttsRU_widget, self).__init__()
        self.ui = arm_raisings_to_the_sides_RU_ui()
        self.ui.setupUi(self)

        self.arttsRU = arm_raisings_to_the_sides_RU_widget()
        self.arttsRU.ui.pushButton.clicked.connect(self.on_start_clicked)  # используется модель подьема руки через сторону.
        self.arttsRU.ui.pushButton_2.clicked.connect(self.ct_back)
        self.show()

    def on_start_clicked(self): # реальная функция, использует одну модель, подъем руки через сторону.
        self.ui.result.setText(start_test()) # сделала одинаковое start_test, как в русском, так и в английском интерфейсе

    def ct_back(self):
        self.arttsRU.hide()
        self.ceRU.show()

class hpEN_widget(QTWidgets.QWidget):
    def __init__(self):
        super(hpEN_widget, self).__init__()
        self.ui = home_page_EN_ui()
        self.ui.setupUi(self)

        self.hpEN = home_page_EN_widget()
        self.hpEN.ui.pushButton.clicked.connect(self.ct_ceEN)
        self.hpEN.ui.pushButton_2.clicked.connect(self.ct_hpRU)
        self.show()

    def ct_ceEN(self):
        self.hpEN.hide()
        self.ceEN.show()

    def ct_hpRU(self):
        self.hpEN.hide()
        self.hpRU.show()

class ceEN_widget(QTWidgets.QWidget):
    def __init__(self):
        super(ceEN_widget, self).__init__()
        self.ui = choose_exercise_EN_ui()
        self.ui.setupUi(self)

        self.ceEN = choose_exercise_EN_widget()
        self.ceEN.ui.pushButton_5.clicked.connect(self.ct_arfEN)
        self.ceEN.ui.pushButton_4.clicked.connect(self.ct_arttsEN)
        self.ceEN.ui.pushButton.clicked.connect(self.ct_back)
        self.show()

    def ct_arfEN(self):
        self.ceEN.hide()
        self.arfEN.show()

    def ct_arttsEN(self):
        self.ceEN.hide()
        self.arttsEN.show()

    def ct_back(self):
        self.ceEN.hide()
        self.hpEN.show()

class arfEN_widget(QTWidgets.QWidget):
    def __init__(self):
        super(arfEN_widget, self).__init__()
        self.ui = arm_raisings_forward_EN_ui()
        self.ui.setupUi(self)

        self.arfEN = arm_raisings_forward_EN_widget()
        self.arfEN.ui.pushButton.clicked.connect(self.on_start_clicked2) # сделала одинаковое on_start_clicked, как в русском, так и в английском интерфейсе
        self.arfEN.ui.pushButton_2.clicked.connect(self.ct_back)
        self.show()

    def on_start_clicked2(self):
        self.ui.result.setText(start_test2())

    def ct_back(self):
        self.arfEN.hide()
        self.ceEN.show()

class arttsEN_widget(QTWidgets.QWidget):
    def __init__(self):
        super(artts_widget, self).__init__()
        self.ui = arm_raisings_to_the_sides_EN_ui()
        self.ui.setupUi(self)

        self.arttsEN = arm_raisings_to_the_sides_EN_widget()
        self.arttsEN.ui.pushButton.clicked.connect(self.on_start_clicked) # сделала одинаковое on_start_clicked, как в русском, так и в английском интерфейсе
        self.arttsEN.ui.pushButton_2.clicked.connect(self.ct_back)
        self.show()

    def on_start_clicked(self):
        self.ui.result.setText(start_test) # сделала одинаковое start_test, как в русском, так и в английском интерфейсе

    def ct_back(self):
        self.arttsEN.hide()
        self.ceEN.show()









if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    # mw = MainWindow()
    # mw.show()
    hpRU = home_page_RU_widget()
    hpRU_widget.show()

    sys.exit(app.exec())