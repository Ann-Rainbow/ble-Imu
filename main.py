from PyQt5 import QtWidgets
from choose_exercise_EN import Ui_Form as choose_exercise_ui
from home_page_EN import Ui_CorEx as main_window_widget_ui
from leanings_forward import  Ui_Form as leanings_forward_ui
from arm_raisings_to_the_sides_EN import Ui_Form as arm_raisings_to_the_sides_ui
from arm_raisings_forward_EN import Ui_Form as arm_raisings_forward_ui
import sys
from core_main import init, start_test, destroy
# print("tete")


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args):
        QtWidgets.QMainWindow.__init__(self, *args)
        self.mw = home_page()
        self.chex = choose_exercise()

        self.mw.ui.pushButton.clicked.connect(self.ct_chex)
        self.chex.ui.pushButton.clicked.connect(self.ct_mw)
        #self.lfw = leanings_forward_widget()
        self.artts = arm_raisings_to_the_sides_widget()
        self.arf = arm_raisings_forward_widget()
        self.artts.ui.pushButton_2.clicked.connect(self.ct_chex)
        #self.mw.ui.pushButton_5.clicked.connect(self.ctlfw)
        #self.lfw.ui.pushButton_2.clicked.connect(self.ctmw)
        self.chex.ui.pushButton_4.clicked.connect(self.ct_artts)
        # self.artts.ui.pushButton_2.clicked.connect(self.ct_mw)
        self.arf.ui.pushButton_2.clicked.connect(self.ct_chex)
        self.chex.ui.pushButton_5.clicked.connect(self.ct_arf)

        self.mw.show()

    # def ctlfw(self):
    #     self.mw.hide()
    #     self.lfw.show()

    def ct_chex(self):
        self.mw.hide()
        self.artts.hide()
        self.arf.hide()
        self.chex.show()


    def ct_artts(self):
        self.chex.hide()
        self.artts.show()

    def ct_arf(self):
        self.chex.hide()
        self.arf.show()


    def ct_mw(self):
        # self.lfw.hide()
        self.artts.hide()
        self.arf.hide()
        self.chex.hide()
        self.mw.show()



class home_page(QtWidgets.QWidget):
    def __init__(self):
        super(home_page, self).__init__()
        self.ui = main_window_widget_ui()
        self.ui.setupUi(self)
        # self.ui.pushButton_5.click.connect(self.hide)
        # self.ui.pushButton_5.click.connect()
        # self.show()


class choose_exercise(QtWidgets.QWidget):
    def __init__(self):
        super(choose_exercise, self).__init__()
        self.ui = choose_exercise_ui()
        self.ui.setupUi(self)
        # self.ui.pushButton_5.click.connect(self.hide)
        # self.ui.pushButton_5.click.connect()
        # self.show()

# class leanings_forward_widget(QtWidgets.QWidget):
#     def __init__(self):
#         super(leanings_forward_widget, self).__init__()
#         self.ui = leanings_forward_ui()
#         self.ui.setupUi(self)
#         self.ui.pushButton.clicked.connect(self.on_start_clicked)


class arm_raisings_to_the_sides_widget(QtWidgets.QWidget):
    def __init__(self):
        super(arm_raisings_to_the_sides_widget, self).__init__()
        self.ui = arm_raisings_to_the_sides_ui()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.on_start_clicked)

    def on_start_clicked(self):
        self.ui.result.setText(start_test("all_probes/classifier_LogisticRegression"))


class arm_raisings_forward_widget(QtWidgets.QWidget):
    def __init__(self):
        super(arm_raisings_forward_widget, self).__init__()
        self.ui = arm_raisings_forward_ui()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.on_start_clicked)

    def on_start_clicked(self):
        self.ui.result.setText(start_test("all_probes/classifier_LogisticRegression"))



if __name__ == '__main__':
    # print("tets")
    app = QtWidgets.QApplication([])
    app.aboutToQuit.connect(destroy)
    init()
    mw = MainWindow()
    # mw.show()

    sys.exit(app.exec())