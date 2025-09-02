import os
import sys

import pygame


def load_image(file_path):
    try:
        if getattr(sys, 'frozen', False):
            base_path = sys._MEIPASS
            full_path = os.path.join(base_path, file_path)
        else:
            full_path = file_path

        image = pygame.image.load(full_path)
        return image
    except pygame.error:
        return None
#background images
background_1 = load_image("assets/images/background_1.jpg") #dimensions 1400, 930
background_2 = load_image("assets/images/background_2.jpg")
background_3 = load_image("assets/images/background_3.jpg")
background_4 = load_image("assets/images/background_4.jpg")
background_5 = load_image("assets/images/background_5.jpg")
win_screen = load_image("assets/images/win_screen.jpg")
window_icon = load_image("assets/images/haruhi_icon.png")

current_background = background_1
background_bought = False

#character images
kyon_image = load_image("assets/images/kyon_main.png") #dimensions 335, 573
itsuki_image = load_image("assets/images/itsuki_main.png") #dimensions 304, 624
haruhi_image = load_image("assets/images/haruhi_main.png") #dimensions 359, 590
nagato_image = load_image("assets/images/nagato_main.png") #dimensions 359, 590
mikuru_image = load_image("assets/images/mikuru_main.png")

#music images
pause_button = load_image("assets/images/pause_button.png")
play_button = load_image("assets/images/play_button.png")