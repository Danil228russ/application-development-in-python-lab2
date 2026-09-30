import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox


class Notebook(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("notebook.ui", self)
        self.btnAdd.clicked.connect(self.add_contact)

    def add_contact(self):
        name = self.editName.text().strip()
        phone = self.editPhone.text().strip()

        if not name or not phone:
            QMessageBox.warning(self, "Ошибка", "Заполните имя и номер!")
            return

        self.listWidget.addItem(f"{name}: {phone}")
        self.statusBar().showMessage(f"Добавлен контакт: {name}", 3000)
        self.editName.clear()
        self.editPhone.clear()
        self.editName.setFocus()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Notebook()
    w.show()
    sys.exit(app.exec_())