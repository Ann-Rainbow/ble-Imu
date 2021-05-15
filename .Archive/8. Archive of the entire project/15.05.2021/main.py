from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDialog, QDialogButtonBox
from choose_exercise_EN import Ui_CorEx as choose_exercise_ui
from home_page_EN import Ui_CorEx as main_window_widget_ui
from leanings_forward import  Ui_Form as leanings_forward_ui
from arm_raisings_to_the_sides_EN import Ui_Form as arm_raisings_to_the_sides_ui
from arm_raisings_forward_EN import Ui_Form as arm_raisings_forward_ui
import sys
from core_main import init, start_test, destroy
# print("tete")

class CustomDialog(QDialog):
    def __init__(self, str, parent=None):
        super().__init__(parent=parent)

        self.setWindowTitle(" ")

        QBtn = QDialogButtonBox.Ok

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QtWidgets.QVBoxLayout()
        message = QtWidgets.QLabel(str)
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args):
        QtWidgets.QMainWindow.__init__(self, *args)
        self.lang = "English"
        self.mw = home_page()
        self.chex = choose_exercise()

        self.mw.ui.pushButton.clicked.connect(self.ct_chex)
        self.chex.ui.pushButton.clicked.connect(self.ct_mw)
        #self.lfw = leanings_forward_widget()
        self.artts = arm_raisings_to_the_sides_widget()
        self.artts.lang = self.lang
        self.arf = arm_raisings_forward_widget()
        self.arf.lang = self.lang
        self.artts.ui.pushButton_2.clicked.connect(self.ct_chex)
        #self.mw.ui.pushButton_5.clicked.connect(self.ctlfw)
        #self.lfw.ui.pushButton_2.clicked.connect(self.ctmw)
        self.chex.ui.pushButton_4.clicked.connect(self.ct_artts)
        # self.artts.ui.pushButton_2.clicked.connect(self.ct_mw)
        self.arf.ui.pushButton_2.clicked.connect(self.ct_chex)
        self.chex.ui.pushButton_5.clicked.connect(self.ct_arf)

        self.chex.ui.pushButton_9.clicked.connect(self.not_realised)
        self.chex.ui.pushButton_2.clicked.connect(self.not_realised)
        self.chex.ui.pushButton_6.clicked.connect(self.not_realised)
        self.chex.ui.pushButton_3.clicked.connect(self.not_realised)
        self.chex.ui.pushButton_8.clicked.connect(self.not_realised)
        self.chex.ui.pushButton_7.clicked.connect(self.not_realised)
        self.mw.ui.pushButton_2.clicked.connect(self.lang_change)

        self.qt_translator = QtCore.QTranslator()
        # self.qt_translator.load("corex_py.qm")
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

    def not_realised(self):
        if self.lang == "English":
            dlg = CustomDialog("This exercise is not available")
        if self.lang == "Russian":
            dlg = CustomDialog("Данное упражнение недоступно")
        dlg.exec_()


    def lang_change(self):

        if self.lang == "English":
            self.lang = "Russian"
            self.qt_translator.load("corex_py.qm")
            # print("zashel")
            QtCore.QCoreApplication.installTranslator(self.qt_translator)

        else:
            self.lang = "English"
            QtCore.QCoreApplication.removeTranslator(self.qt_translator)

        self.mw.ui.retranslateUi(self.mw)
        self.chex.ui.retranslateUi(self.chex)
        self.arf.ui.retranslateUi(self.arf)
        self.artts.ui.retranslateUi(self.artts)
        self.artts.lang = self.lang
        self.arf.lang = self.lang


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
        self.lang = ""
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
        # _translate = QtCore.QCoreApplication.translate
        res = start_test("all_probes/artts-RandomForest-best_parameters-different_speed") # artts-classifier_RandomForest-98-different_speed
        print(self.lang)
        if res:
            self.ui.result.setStyleSheet('QLabel {color: #1f4f16; }')
            if self.lang == "Russian":

                #(format.arg(color.name(),text)
                print("Zashel")
                self.ui.result.setText("Упражнение выполнено верно.")
            else:
                self.ui.result.setText("Exercise performed correctly.")
        else:
            self.ui.result.setStyleSheet('QLabel {color: #df0000; }')
            if self.lang == "Russian":
                self.ui.result.setText("Упражнение выполнено неверно.")
            else:
                self.ui.result.setText("Exercise performed incorrectly.")


class arm_raisings_forward_widget(QtWidgets.QWidget):
    def __init__(self):
        super(arm_raisings_forward_widget, self).__init__()
        self.ui = arm_raisings_forward_ui()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.on_start_clicked)

    def on_start_clicked(self):
        #_translate = QtCore.QCoreApplication.translate
        #self.ui.result.setText(_translate(start_test("all_probes/arf-classifier_KNeighbors-4")))
        res = start_test("all_probes/arf-SVC-best_parameters") #arf-classifier_SVC
        print(self.lang)
        if res:
            self.ui.result.setStyleSheet('QLabel {color: #1f4f16; }')
            if self.lang == "Russian":

                #(format.arg(color.name(),text)
                print("Zashel")
                self.ui.result.setText("Упражнение выполнено верно.")
            else:
                self.ui.result.setText("Exercise performed correctly.")
        else:
            self.ui.result.setStyleSheet('QLabel {color: #df0000; }')
            if self.lang == "Russian":
                self.ui.result.setText("Упражнение выполнено неверно.")
            else:
                self.ui.result.setText("Exercise performed incorrectly.")


if __name__ == '__main__':
    # print("tets")
    app = QtWidgets.QApplication([])
    app.aboutToQuit.connect(destroy)
    #init()
    mw = MainWindow()
    # mw.show()

    sys.exit(app.exec())