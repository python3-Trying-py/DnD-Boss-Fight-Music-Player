import logging
import sys
from PyQt6.QtWidgets import QApplication
from app.models.player_model import PlayerModel
from app.viewers.main_window import MainWindow
from app.controllers.main_controller import MainController
from app.services.audio_service import AudioService

def setup_logging():
    logging.basicConfig(
        filename = 'music_player.log',
        level=logging.DEBUG,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%H:%M:%S",
        )

def main():
    setup_logging()
    app = QApplication(sys.argv)

    model = PlayerModel()
    view = MainWindow()
    audio = AudioService()
    controller = MainController(model, view, audio)

    view.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
