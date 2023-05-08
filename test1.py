import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout, QFileDialog

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Tạo các widget
        self.file_path_label = QLabel("File path:")
        self.file_path_edit = QLineEdit()

        self.value_1_label = QLabel("Value 1:")
        self.value_1_edit = QLineEdit()

        self.value_2_label = QLabel("Value 2:")
        self.value_2_edit = QLineEdit()

        self.object_label = QLabel("Range frequence:")
        self.attribute_1_edit = QLineEdit()
        self.attribute_2_edit = QLineEdit()

        self.add_button = QPushButton("Add")
        self.add_button.clicked.connect(self.add_object)

        # Thêm button để mở file
        self.file_path_button = QPushButton("Select File")
        self.file_path_button.clicked.connect(self.show_file_dialog)

        # Tạo grid layout
        grid_layout = QGridLayout()
        grid_layout.addWidget(self.file_path_label, 0, 0)
        grid_layout.addWidget(self.file_path_edit, 0, 1)
        grid_layout.addWidget(self.file_path_button, 0, 2)

        grid_layout.addWidget(self.value_1_label, 1, 0)
        grid_layout.addWidget(self.value_1_edit, 1, 1)

        grid_layout.addWidget(self.value_2_label, 2, 0)
        grid_layout.addWidget(self.value_2_edit, 2, 1)

        grid_layout.addWidget(self.object_label, 3, 0)
        grid_layout.addWidget(self.attribute_1_edit, 3, 1)
        grid_layout.addWidget(self.attribute_2_edit, 3, 2)

        grid_layout.addWidget(self.add_button, 4, 0, 1, 4)

        # Tạo vertical layout để chứa grid layout
        main_layout = QVBoxLayout()
        main_layout.addLayout(grid_layout)

        self.setLayout(main_layout)

        self.objects_layout = QVBoxLayout()
        self.objects_widget = QWidget()
        self.objects_widget.setLayout(self.objects_layout)

        main_layout.addWidget(self.objects_widget)

    def show_file_dialog(self):
        file_dialog = QFileDialog()
        file_path = file_dialog.getOpenFileName(self, "Select File")[0]
        self.file_path_edit.setText(file_path)
    def add_object(self):
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

        self.objects_layout.addWidget(object_widget)
if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec_()
