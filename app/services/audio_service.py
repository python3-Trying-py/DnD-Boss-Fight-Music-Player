import pygame

class AudioService:
    def __init__(self):
        pygame.mixer.init()

    def load(self, path):
        pygame.mixer.music.load(path)

    def play(self):
        pygame.mixer.music.play()

    def stop(self):
        pygame.mixer.music.stop()

    def pause(self):
        pygame.mixer.music.pause()
