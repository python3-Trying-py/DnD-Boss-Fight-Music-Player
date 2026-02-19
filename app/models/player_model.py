import os

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

    def grab_fights(self) -> list:
        path = "./Musics/"
        folders = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
        return folders
