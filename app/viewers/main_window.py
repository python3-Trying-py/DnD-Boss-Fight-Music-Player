from PyQt6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QLineEdit

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Music Player")

        self.music_input = QLineEdit()
        self.play_button = QPushButton("Play")
        self.stop_button = QPushButton("Stop")

        layout = QVBoxLayout()
        layout.addWidget(self.music_input)
        layout.addWidget(self.play_button)
        layout.addWidget(self.stop_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
