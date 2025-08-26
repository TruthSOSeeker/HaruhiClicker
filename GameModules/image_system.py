import pygame
def load_image(file_path):
    try:
        image = pygame.image.load(file_path)
        return image
    except pygame.error:
        print("Could not load image")
        return None
#background images
background_1 = load_image("assets/images/background_1.jpg") #dimensions 1400, 930
background_2 = load_image("assets/images/background_2.jpg")
background_3 = load_image("assets/images/background_3.jpg")
background_4 = load_image("assets/images/background_4.jpg")
background_5 = load_image("assets/images/background_5.jpg")
window_icon = load_image("assets/images/haruhi_icon.png")

current_background = background_1
background_bought = False

#character images
kyon_image = load_image("assets/images/kyon_main.png") #dimensions 335, 573
itsuki_image = load_image("assets/images/itsuki_main.png") #dimensions 304, 624
haruhi_image = load_image("assets/images/haruhi_main.png") #dimensions 359, 590
nagato_image = load_image("assets/images/nagato_main.png") #dimensions 359, 590
mikuru_image = load_image("assets/images/mikuru_main.png")
