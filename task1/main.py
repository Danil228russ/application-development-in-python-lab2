import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QButtonGroup, QRadioButton


class FlagWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("flag.ui", self)

        self.setFixedSize(self.size())

        self.group1 = QButtonGroup(self)
        self.group2 = QButtonGroup(self)
        self.group3 = QButtonGroup(self)

        for rb in self.findChildren(QRadioButton):
            name = rb.objectName()
            if name.startswith("r1_"):
                self.group1.addButton(rb)
            elif name.startswith("r2_"):
                self.group2.addButton(rb)
            elif name.startswith("r3_"):
                self.group3.addButton(rb)

        self.btnDraw.clicked.connect(self.draw_flag)

    def draw_flag(self):
        colors = []
        for grp in (self.group1, self.group2, self.group3):
            btn = grp.checkedButton()
            if btn is None:
                QMessageBox.warning(self, "Ошибка", "Выберите цвет для каждой полосы!")
                return
            colors.append(btn.text())
        QMessageBox.information(self, "Флаг", ", ".join(colors))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = FlagWindow()
    w.show()
    sys.exit(app.exec_())