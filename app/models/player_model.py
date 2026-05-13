import os
import logging

logger = logging.getLogger(__name__)

class PlayerModel:
    def __init__(self):
        self.current_song = None
        self.is_playing = False

    def set_song(self, path):
        self.current_song = path

    def play(self):
        self.is_playing = True

    def stop(self):
        self.is_playing = False

    def grab_tracks(self, path:str) -> list:
        tracks = [ track for track in os.listdir(f"./Musics/{path}") if not os.path.isdir(os.path.join(f"./Musics/{path}", track))]

        logger.debug(f"grab_tracks returns: {tracks}")
        return tracks

    def grab_fights(self) -> list:
        path = "./Musics/"
        folders = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
        logger.debug(f"grab_fights returns: {folders}")
        return folders
