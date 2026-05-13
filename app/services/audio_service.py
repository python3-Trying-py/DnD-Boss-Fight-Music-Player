import pygame
import re
from PyQt6.QtCore import QObject, pyqtSignal
import logging

logger = logging.getLogger(__name__)

class AudioService(QObject):
    intro_finished = pyqtSignal()
    fight_finished = pyqtSignal()

    def __init__(self):
        super().__init__()
        pygame.mixer.init()
        self.track_type = "intro"

    def load(self, path):
        pygame.mixer.music.load(f"./Musics/{path}")
        self.track_type = re.sub(r'\d+', '', path.split("_")[0]).split("/")[1].lower()
        logger.info(f"loaded {path}")
        logger.debug(f"Track type: {self.track_type}")

    def play(self):
        pygame.mixer.music.play()
        logger.info("playing")

    def stop(self):
        pygame.mixer.music.stop()

    def pause(self):
        pygame.mixer.music.pause()

    def check_music(self):
        if not pygame.mixer.music.get_busy():
            logger.info("Track Ended")
            if self.track_type == "intro":
                self.intro_finished.emit()
                logger.debug("intro_finished emmited signal")
            elif self.track_type == "phase":
                pygame.mixer.music.rewind()
                logger.debug("music rewinded")
            else:
                pygame.mixer.music.stop()
                self.fight_finished.emit()
                logger.debug("Fight Ended")

                
