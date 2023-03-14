import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QListWidget, QSlider
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle("My App")
        self.setWindowIcon(QIcon("icon.png"))
        self.setFixedSize(500, 500)

        # Create some widgets
        self.label = QLabel("Enter your name:")
        self.textbox = QLineEdit()
        self.button = QPushButton("Submit")
        self.button.setStyleSheet("QPushButton { background-color: #4CAF50; color: white; border-radius: 4px; font-weight: bold; }")
        self.button.clicked.connect(self.on_submit)

        # Create a list widget and add some items to it
        self.list_widget = QListWidget()
        for i in range(10):
            self.list_widget.addItem(f"Item {i}")

        # Create a slider and a label to display its value
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 100)
        self.slider.valueChanged.connect(self.on_slider_changed)
        self.slider_label = QLabel("50")
        self.slider_label.setAlignment(Qt.AlignCenter)

        # Create a horizontal layout for the slider and its label
        slider_layout = QHBoxLayout()
        slider_layout.addWidget(self.slider)
        slider_layout.addWidget(self.slider_label)

        # Create a vertical layout to arrange the widgets
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.textbox)
        layout.addWidget(self.button)
        layout.addWidget(self.list_widget)
        layout.addLayout(slider_layout)
        layout.setAlignment(Qt.AlignCenter)
        self.setLayout(layout)

        # Set stylesheet
        self.setStyleSheet("background-color: #F1F1F1;")

    def on_submit(self):
        name = self.textbox.text()
        print(f"Hello, {name}!")

    def on_slider_changed(self, value):
        self.slider_label.setText(str(value))

app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec_())
