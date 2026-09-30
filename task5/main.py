import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class Antiplag(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("antiplag.ui", self)

        self.spinThreshold.setRange(0.0, 100.0)
        self.spinThreshold.setSuffix(" %")
        self.spinThreshold.setValue(50.0)

        self.btnCompare.clicked.connect(self.compare)

    def compare(self):
        raw1 = self.text1.toPlainText()
        raw2 = self.text2.toPlainText()

        t1 = [line.strip().lower() for line in raw1.splitlines() if line.strip()]
        t2 = [line.strip().lower() for line in raw2.splitlines() if line.strip()]

        if not t1 or not t2:
            self.set_status("Оба поля должны содержать текст!", "orange")
            return

        set1, set2 = set(t1), set(t2)
        common = set1 & set2
        total = max(len(set1), len(set2))
        percent = len(common) / total * 100

        threshold = self.spinThreshold.value()

        if percent >= threshold:
            self.set_status(
                f"⚠️ Плагиат! Совпадение: {percent:.1f}% (порог {threshold:.1f}%)",
                "red"
            )
        else:
            self.set_status(
                f"✅ Уникально. Совпадение: {percent:.1f}% (порог {threshold:.1f}%)",
                "green"
            )

    def set_status(self, text, color):
        bar = self.statusBar()
        bar.setStyleSheet(f"QStatusBar {{ color: {color}; font-weight: bold; }}")
        bar.showMessage(text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Antiplag()
    w.show()
    sys.exit(app.exec_())