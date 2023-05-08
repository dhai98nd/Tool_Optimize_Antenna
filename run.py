import sys
import PySide6.QtWidgets
from PySide6.QtWidgets import QApplication, QWidget, QLabel,\
      QLineEdit, QPushButton, QVBoxLayout, QGridLayout, QFileDialog, QHBoxLayout, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
                
        # Tạo cửa sổ chính
        self.setWindowTitle("Giao diện PySide6")
        # Tạo grid layout
        grid_layout = QGridLayout()

        #Tao cac widget
        self.file_path_label = QLabel("File path:")
        self.file_path_edit = QLineEdit()
        # Thêm button để mở file
        self.file_path_button = QPushButton("Select File")
        self.file_path_button.clicked.connect(self.show_file_dialog)

        grid_layout.addWidget(self.file_path_label, 0, 0)
        grid_layout.addWidget(self.file_path_edit, 0, 1)
        grid_layout.addWidget(self.file_path_button, 0, 2)

        #Them range frequency
        self.frequence_label = QLabel("Range frequence:")
        self.min_frequence_edit = QLineEdit()
        self.max_frequence_edit = QLineEdit()
        self.min_frequence_edit.editingFinished.connect(self.add_range_frequece)
        self.max_frequence_edit.editingFinished.connect(self.add_range_frequece)


        self.add_range_frequence = QPushButton("Add")
        self.add_range_frequence.clicked.connect(self.add_range_frequece)

        grid_layout.addWidget(self.frequence_label, 3, 0)
        grid_layout.addWidget(self.min_frequence_edit, 3, 1)
        grid_layout.addWidget(self.max_frequence_edit, 3, 2)
        grid_layout.addWidget(self.add_range_frequence, 3,4)

        #Them target
        self.target_layout = QHBoxLayout()
        self.target_label = QLabel("Frequence Target:")
        self.add_target_button = QPushButton("Add")
        self.target_line = QLineEdit()
        self.target_layout.addWidget(self.target_label)
        self.target_layout.addWidget(self.target_line)
        self.target_layout.addWidget(self.add_target_button)
        self.add_target_button.clicked.connect(self.add_target)
        
        #Them thuoc tinh
        self.object_layout = QVBoxLayout()
        self.add_button = QPushButton("Add")
        self.add_button.clicked.connect(self.add_object)
        self.object_layout.addWidget(self.add_button)

        # Tạo vertical layout để chứa grid layout
        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(grid_layout)
        self.main_layout.addLayout(self.target_layout)
        self.main_layout.addLayout(self.object_layout)

        self.setLayout(self.main_layout)

        self.objects_widget = QWidget()
        self.objects_widget.setLayout(self.main_layout)

        # Set the widget as the central widget of the window
        self.setCentralWidget(self.objects_widget)


    def add_range_frequece(self):
        text1 = self.min_frequence_edit.text()
        text2 = self.max_frequence_edit.text()
        print(f"Text 1: {text1}")
        print(f"Text 2: {text2}")
    def show_file_dialog(self):
        file_dialog = QFileDialog()
        file_path = file_dialog.getOpenFileName(self, "Select File")[0]
        self.file_path_edit.setText(file_path)

    def add_target(self):
        text = QLineEdit(self)
        hbox = self.target_layout
        hbox.insertWidget(hbox.count() - 1, text)


    def add_object(self):
        object_layout = QHBoxLayout()
        object_widget = QWidget()

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

        # object_widget.setLayout(object_layout)
        # self.main_layout.addLayout(object_layout,self.main_layout.count() - 1)
        self.main_layout.insertLayout(self.main_layout.count() - 1, object_layout)

        self.object_layout.addWidget(object_widget,self.main_layout.count() - 1)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Tạo cửa sổ chính
    main_window = MainWindow()
    main_window.show()

    # Khởi chạy ứng dụng
    sys.exit(app.exec())