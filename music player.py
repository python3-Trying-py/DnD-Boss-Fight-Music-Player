import pygame
import time

#C:/Users/payta/Downloads/God Shattering Star - (Rain and Thunder Mix) - Lyrics.wav

# Initialize mixer
pygame.mixer.init()

# Load music file
pygame.mixer.music.load("C:/Users/payta/Downloads/God Shattering Star - (Rain and Thunder Mix) - Lyrics.wav")

# Play music
pygame.mixer.music.play()

print("Playing music...")

# Keep program running while music plays
while pygame.mixer.music.get_busy():
    time.sleep(1)

print("Done.")