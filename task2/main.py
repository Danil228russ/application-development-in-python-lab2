import sys
from datetime import datetime
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox


class Diary(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("diary.ui", self)

        self.events = []

        self.btnAdd.clicked.connect(self.add_event)

    def add_event(self):
        name = self.editName.text().strip()
        if not name:
            QMessageBox.warning(self, "Ошибка", "Введите название события!")
            return

        date = self.calendar.selectedDate().toPyDate()
        time = self.timeEdit.time().toPyTime()
        dt = datetime.combine(date, time)

        if any(e[0] == dt and e[1] == name for e in self.events):
            QMessageBox.warning(self, "Ошибка", "Такое событие уже есть!")
            return

        self.events.append((dt, name))
        self.events.sort(key=lambda x: x[0])  # сортировка по дате
        self.refresh_list()
        self.editName.clear()

    def refresh_list(self):
        self.listWidget.clear()
        for dt, name in self.events:
            self.listWidget.addItem(
                f"{dt.strftime('%d.%m.%Y %H:%M')} — {name}"
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Diary()
    w.show()
    sys.exit(app.exec_())