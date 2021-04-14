from PyQt5 import QtWidgets
from 1.home_page_EN









    def on_start_clicked(self):
        self.ui.result.setText(start_test())

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    mw = MainWindow()
    # mw.show()

    sys.exit(app.exec())