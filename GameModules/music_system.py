import pygame

pygame.mixer.init()
def load_background_music(file_path):
    try:
        pygame.mixer.music.load(file_path)
        print("Music loaded")
        return True
    except pygame.error:
        print("Could not load music")
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