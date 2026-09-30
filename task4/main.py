import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox


class NimGame(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("game.ui", self)

        self.stones = 0
        self.game_active = False

        self.btnNew.clicked.connect(self.new_game)
        self.btnTake.clicked.connect(self.player_move)

        self.spinTake.setRange(1, 3)
        self.update_label()

    def new_game(self):
        self.stones = self.spinN.value()
        self.game_active = True
        self.logView.clear()
        self.logView.append(f"🆕 Новая игра. Камней: {self.stones}")
        self.update_label()
        self.statusBar().showMessage("Игра началась! Ваш ход.")

    def update_label(self):
        self.labelStones.setText(f"Камней на столе: {self.stones}")

    def player_move(self):
        if not self.game_active:
            QMessageBox.warning(self, "Ошибка", "Начните новую игру!")
            return

        take = self.spinTake.value()
        if take < 1 or take > 3:
            QMessageBox.warning(self, "Ошибка", "Можно взять от 1 до 3 камней!")
            return
        if take > self.stones:
            QMessageBox.warning(self, "Ошибка", "Нельзя взять больше, чем есть!")
            return

        self.stones -= take
        self.logView.append(f"🧑 Игрок взял {take}. Осталось: {self.stones}")
        self.update_label()

        if self.stones == 0:
            self.finish("🎉 Победил игрок!")
            return

        self.ai_move()

    def ai_move(self):

        if self.stones % 4 == 0:
            take = 1
        else:
            take = self.stones % 4

        take = min(take, 3, self.stones)

        self.stones -= take
        self.logView.append(f"💻 ИИ взял {take}. Осталось: {self.stones}")
        self.update_label()

        if self.stones == 0:
            self.finish("💻 Победил компьютер!")

    def finish(self, msg):
        self.game_active = False
        self.logView.append(msg)
        self.statusBar().showMessage(msg)
        QMessageBox.information(self, "Игра окончена", msg)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = NimGame()
    w.show()
    sys.exit(app.exec_())