import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget, QPushButton, QLineEdit, QHBoxLayout

class AddWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        # Tạo 2 ô text
        self.text1 = QLineEdit()
        self.text2 = QLineEdit()

        # Tạo layout cho 2 ô text
        hbox = QHBoxLayout()
        hbox.addWidget(self.text1)
        hbox.addWidget(self.text2)

        # Tạo nút add
        self.add_button = QPushButton('Add')
        self.add_button.clicked.connect(self.on_add_clicked)

        # Tạo layout cho add button và hbox
        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addWidget(self.add_button)

        self.setLayout(vbox)

    def on_add_clicked(self):
        # In ra nội dung của 2 ô text khi nút add được nhấn
        print(self.text1.text(), self.text2.text())

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Tạo layout chính
        vbox = QVBoxLayout()

        # Tạo nút để thêm AddWidget
        self.add_widget_button = QPushButton('Add Widget')
        self.add_widget_button.clicked.connect(self.on_add_widget_clicked)

        vbox.addWidget(self.add_widget_button)

        self.setLayout(vbox)

    def on_add_widget_clicked(self):
        # Thêm AddWidget vào layout chính
        self.layout().addWidget(AddWidget())

if __name__ == '__main__':
    # Khởi tạo ứng dụng Qt
    app = QApplication(sys.argv)

    # Tạo cửa sổ chính
    main_window = MainWindow()
    main_window.show()

    # Chạy ứng dụng Qt
    sys.exit(app.exec_())
