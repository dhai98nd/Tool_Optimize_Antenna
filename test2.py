import sys
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QLineEdit, QPushButton

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout()
        self.button = QPushButton('Add', self)
        self.button.clicked.connect(self.addText)
        hbox.addWidget(self.button)
        self.setLayout(hbox)

        self.show()

    def addText(self):
        text = QLineEdit(self)
        hbox = self.layout()
        hbox.insertWidget(hbox.count() - 1, text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
