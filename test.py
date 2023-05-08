import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QFileDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Tạo cửa sổ chính
        self.setWindowTitle("Giao diện PySide6")

        # Tạo widget chứa tất cả các widget cần thiết
        widget = QWidget()

        # Tạo layout dọc để chứa các widget
        self.vbox = QVBoxLayout()

        # Tạo dòng chứa ô hiển thị đường dẫn file và nút thêm file
        hbox1 = QHBoxLayout()
        self.file_path_label = QLabel("Đường dẫn file:")
        hbox1.addWidget(self.file_path_label)
        self.file_path_edit = QLineEdit()
        hbox1.addWidget(self.file_path_edit)
        self.add_file_button = QPushButton("Thêm file")
        self.add_file_button.clicked.connect(self.add_file)
        hbox1.addWidget(self.add_file_button)
        self.vbox.addLayout(hbox1)

        # Tạo dòng chứa 2 ô text để nhập và nút để nhập text vào và in ra terminal
        hbox2 = QHBoxLayout()
        self.text_edit1 = QTextEdit()
        hbox2.addWidget(self.text_edit1)
        self.text_edit2 = QTextEdit()
        hbox2.addWidget(self.text_edit2)
        self.add_text_button = QPushButton("Thêm text")
        self.add_text_button.clicked.connect(self.add_text)
        hbox2.addWidget(self.add_text_button)
        self.vbox.addLayout(hbox2)

        # Tạo dòng chứa 3 ô text để nhập và nút để in ra terminal
        hbox3 = QHBoxLayout()
        self.text_edit3_1 = QTextEdit()
        hbox3.addWidget(self.text_edit3_1)
        self.text_edit3_2 = QTextEdit()
        hbox3.addWidget(self.text_edit3_2)
        self.text_edit3_3 = QTextEdit()
        hbox3.addWidget(self.text_edit3_3)
        self.add_row_button = QPushButton("Thêm dòng mới")
        self.add_row_button.clicked.connect(self.add_row)
        hbox3.addWidget(self.add_row_button)
        self.vbox.addLayout(hbox3)

        # Thiết lập layout dọc là layout chính của widget
        widget.setLayout(self.vbox)

        # Thiết lập widget là widget chính của cửa sổ
        self.setCentralWidget(widget)

    def add_file(self):
        # Mở hộp thoại để chọn file và lấy đường dẫn file
        file_path, _ = QFileDialog.getOpenFileName(self, "Chọn file")
        if file_path:
            self.file_path_edit.setText(file_path)

    def add_text(self):
        # Lấy nội dung của 2 ô text và in ra terminal
        text1 = self.text_edit1.toPlainText()
        text2 = self.text_edit2.toPlainText()
        print(f"Text 1: {text1}")
        print(f"Text 2: {text2}")

    def add_row(self):
        # Lấy nội dung của 3 ô text và in ra terminal
        text1 = self.text_edit3_1.toPlainText()
        text2 = self.text_edit3_2.toPlainText()
        text3 = self.text_edit3_3.toPlainText()
        print(f"Text 1: {text1}")
        print(f"Text 2: {text2}")
        print(f"Text 3: {text3}")


        object_layout = QHBoxLayout()
        object_widget = QWidget()
        object_widget.setLayout(object_layout)

        element_label = QLabel("Thuộc tính:")
        element_min = QLabel("Min:")
        element_max = QLabel("Max:")

        element_label_edit = QLineEdit()
        element_min_edit = QLineEdit()
        element_max_edit = QLineEdit()

        element_label1_value = QLineEdit(element_label_edit.text())
        element_min_value = QLineEdit(element_min_edit.text())
        element_max_value = QLineEdit(element_max_edit.text())

        object_layout.addWidget(element_label)
        object_layout.addWidget(element_label1_value)
        object_layout.addWidget(element_min)
        object_layout.addWidget(element_min_value)
        object_layout.addWidget(element_max)
        object_layout.addWidget(element_max_value)

        self.vbox.addWidget(object_widget)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Tạo cửa sổ chính
    main_window = MainWindow()
    main_window.show()

    # Khởi chạy ứng dụng
    sys.exit(app.exec())