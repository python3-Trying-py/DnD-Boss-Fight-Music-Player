from PyQt6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QComboBox, QLabel, QLineEdit
from PyQt6.QtCore import QTimer
import logging

logger = logging.getLogger(__name__)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Music Player")

        self.CB_fight_selection = QComboBox()
        self.PB_fight_select = QPushButton("Select")

        self.La_current_fight = QLabel("")
        self.La_current_track = QLabel("")

        self.PB_last_track = QPushButton("<<")
        self.LE_track_number = QLineEdit()
        self.La_track_number = QLabel("/ -")
        self.PB_next_track = QPushButton(">>")

        self.PB_Intro_track = QPushButton("Intro")
        self.PB_Ending_track = QPushButton("Ending")

        self.PB_play_button = QPushButton("Play")
        self.PB_stop_button = QPushButton("Stop")

        HL_fight_selection = QHBoxLayout()
        HL_fight_selection.addWidget(self.CB_fight_selection)
        HL_fight_selection.addWidget(self.PB_fight_select)

        VL_track_info = QVBoxLayout()
        VL_track_info.addWidget(self.La_current_fight)
        VL_track_info.addWidget(self.La_current_track)

        HL_track_selection = QHBoxLayout()
        HL_track_selection.addWidget(self.PB_last_track)
        HL_track_selection.addWidget(self.LE_track_number)
        HL_track_selection.addWidget(self.La_track_number)
        HL_track_selection.addWidget(self.PB_next_track)

        HL_track_skip_selection = QHBoxLayout()
        HL_track_skip_selection.addWidget(self.PB_Intro_track)
        HL_track_skip_selection.addWidget(self.PB_Ending_track)

        VL_play_stop = QVBoxLayout()
        VL_play_stop.addWidget(self.PB_play_button)
        VL_play_stop.addWidget(self.PB_stop_button)

        VL_master = QVBoxLayout()
        VL_master.addLayout(HL_fight_selection)
        VL_master.addLayout(VL_track_info)
        VL_master.addLayout(HL_track_selection)
        VL_master.addLayout(HL_track_skip_selection)
        VL_master.addLayout(VL_play_stop)

        container = QWidget()
        container.setLayout(VL_master)
        self.setCentralWidget(container)

        self.Ti_music_timer = QTimer()
        self.Ti_music_timer.setInterval(100)
