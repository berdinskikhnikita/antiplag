import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from anti import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.text = list(filter(lambda x: x != '', self.plainTextEdit.toPlainText().split()))
        self.text2 = list(filter(lambda x: x != '', self.plainTextEdit_2.toPlainText().split()))
        value = self.doubleSpinBox.value()
        original = len(self.text)
        unit = 100 / original
        count = 0
        for i in range(len(self.text)):
            try:
                if self.text[i] == self.text2[i]:
                    count += unit
            except Exception:
                break
        self.statusBar().showMessage(f'Код похож на {round(count, 2)}%')
        if count >= value:
            self.statusBar().setStyleSheet("background-color : red")
        else:
            self.statusBar().setStyleSheet("background-color : green")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())