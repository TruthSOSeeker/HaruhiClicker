import pygame
import sys
import os

pygame.mixer.init()
def load_background_music(file_path):
    try:
        if getattr(sys, 'frozen', False):
            base_path = sys._MEIPASS
            full_path = os.path.join(base_path, file_path)
        else:
            full_path = file_path

        pygame.mixer.music.load(full_path)
        return True
    except pygame.error:
        return False

def play_background_music(loops = -1):
    pygame.mixer.music.play(loops)

def stop_background_music():
    pygame.mixer.music.stop()

def pause_background_music():
    pygame.mixer.music.pause()

def unpause_background_music():
    pygame.mixer.music.unpause()

def set_music_volume(volume):
    pygame.mixer.music.set_volume(volume)

playing_music = False
music_bought = False