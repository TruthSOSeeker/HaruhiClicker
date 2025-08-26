import sys
import pygame
import random
from GameModules.save_system import *
from GameModules.image_system import *
from GameModules.classes import *
from GameModules.sound_system import *
pygame.init()


#create game window
window_width = 1400
window_height = 930
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Haruhi Clicker")
pygame.display.set_icon(window_icon)

clock = pygame.time.Clock()

#initializing main game components
kyon_clicker = Kyon(
    x = 180,
    y = 275,
    width = 190,
    height = 530,
    image = kyon_image,
    level = 1,
    upgrade_cost = 10,
    normal_color = white,
    hover_color = grey,
    unaffordable_color = pink,
    unaffordable_hover = red,
    total_points = 0
)
itsuki_clicker = Itsuki(
    x = 1060,
    y = 275,
    width = 190,
    height = 540,
    image = itsuki_image,
    buy_button_width = 170,
    buy_button_height = 70,
    cost = 500,
    normal_color = white,
    hover_color = grey,
    unaffordable_color = pink,
    unaffordable_hover = red,
)
mikuru_clicker = Mikuru(
    x = 825,
    y = 400,
    width = 170,
    height = 440,
    image = mikuru_image,
    buy_button_width = 170,
    buy_button_height = 70,
    cost = 21000,
    normal_color = white,
    hover_color = grey,
    unaffordable_color = pink,
    unaffordable_hover = red,
)
nagato_clicker = Nagato(
    x = 415,
    y = 385,
    width = 120,
    height = 450,
    image = nagato_image,
    buy_button_width = 170,
    buy_button_height = 70,
    cost = 860000,
    normal_color = white,
    hover_color = grey,
    unaffordable_color = pink,
    unaffordable_hover = red
)
points = Points(
    x = 18,
    y = 19,
    width = 500,
    height = 80,
    alpha_1=150,
    alpha_2= 50,
    total_points = 1500,
    total_cps = 0,
    total_click_damage = 1
)
background_button = BackgroundButton(
    x = 18,
    y = 864,
    width = 370,
    height = 50,
    alpha_1= 150,
    alpha_2= 50,
    circle_x = 175,
    circle_y = 888,
    radius = 16,
)
#main game loop
while True:
    window.fill((0,0,0))
    #recalculate new frame mouse position
    mouse_pos = pygame.mouse.get_pos()
    kyon_clicker.update_hover_state(mouse_pos)
    kyon_clicker.update_upgrade_hover_state(mouse_pos)
    itsuki_clicker.update_hover_state(mouse_pos)
    itsuki_clicker.update_upgrade_hover_state(mouse_pos)
    mikuru_clicker.update_hover_state(mouse_pos)
    nagato_clicker.update_hover_state(mouse_pos)
    background_button.update_buy_button_hover(mouse_pos)
    #event checks
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.quit()
        if kyon_clicker.is_clicked(event):
            points.total_points += kyon_clicker.level
            kyon_clicker.start_click_animation()
        if kyon_clicker.upgrade_button_clicked(event) and points.total_points >= kyon_clicker.upgrade_cost:
            points.total_points -= kyon_clicker.upgrade_cost
            kyon_clicker.level += 1
            kyon_clicker.upgrade_cost = round(kyon_clicker.upgrade_cost * 1.8)
            random_voice = random.choice(kyon_voices)
            play_sound(random_voice)
        if itsuki_clicker.is_clicked(event):
            points.total_points += kyon_clicker.level
            itsuki_clicker.start_click_animation()
        if  itsuki_clicker.buy_button_clicked(event, afford =points.total_points >= 500): #change value when done with speedrunning itsuki
            points.total_points -= 500
            itsuki_bought = True
            random_voice = random.choice(itsuki_voices)
            play_sound(random_voice)
        if itsuki_clicker.upgrade_button_clicked(event) and points.total_points >= itsuki_clicker.upgrade_cost:
            points.total_points -= itsuki_clicker.upgrade_cost
            itsuki_clicker.level += 1
            itsuki_clicker.upgrade_cost = round(itsuki_clicker.upgrade_cost * 1.6)
            random_voice = random.choice(itsuki_voices)
            play_sound(random_voice)
        if mikuru_clicker.is_clicked(event):
            points.total_points += kyon_clicker.level
            mikuru_clicker.start_click_animation()
        if mikuru_clicker.buy_button_clicked(event, afford =points.total_points >= 21000): #change value when done with speedrunning mikuru
            points.total_points -= 21000
            mikuru_bought = True
        if nagato_clicker.is_clicked(event):
            points.total_points += kyon_clicker.level
            nagato_clicker.start_click_animation()
        if nagato_clicker.buy_button_clicked(event, afford =points.total_points >= 860000): #change value when done with speedrunning nagato
            points.total_points -= 400000
            nagato_bought = True
        if background_button.is_clicked(event) and background_bought:
            if background_button.circle_1_is_clicked:
                current_background = background_1
            if background_button.circle_2_is_clicked:
                current_background = background_2
            if background_button.circle_3_is_clicked:
                current_background = background_3
            if background_button.circle_4_is_clicked:
                current_background = background_4
            if background_button.circle_5_is_clicked:
                current_background = background_5
        if background_button.buy_button_is_clicked(event) and not background_bought and points.total_points >= 1000:
            points.total_points -= 1000
            background_bought = True
    #draw background buttons
    if background_bought:
        window.blit(current_background, (0, 0))
        background_button.draw_score_box(window)
        background_button.draw_text(window)
        background_button.update_hover_state(mouse_pos)
        background_button.draw_buttons(window, current_background)
    else:
        background_button.total_points = points.total_points
        background_button.draw_buy_button(window)
        background_button.draw_buy_button_text(window)
    #draw clickers
    kyon_clicker.total_points = points.total_points
    itsuki_clicker.total_points = points.total_points
    if kyon_image:
        kyon_clicker.update_animation()
        kyon_clicker.draw_scaled_image(window, kyon_image)
        kyon_clicker.draw_level_box(window)
        kyon_clicker.draw_level_up_box(window)
        points.total_click_damage = kyon_clicker.level

    if itsuki_clicker.is_bought:
        itsuki_clicker.update_animation()
        itsuki_clicker.draw_scaled_image(window, itsuki_image)
        points.total_cps += (kyon_clicker.level + itsuki_clicker.level) * itsuki_clicker.level * 0.5
        itsuki_clicker.draw_level_box(window)
        itsuki_clicker.draw_level_up_box(window)
    else:
        itsuki_clicker.draw_buy_button(window, afford =points.total_points >= 500)
        itsuki_clicker.draw_text(window)
    if mikuru_clicker.is_bought:
        mikuru_clicker.update_animation()
        mikuru_clicker.draw_scaled_image(window, mikuru_image)
        points.total_cps += 10
    else:
        mikuru_clicker.draw_buy_button(window, afford =points.total_points >= 21000)
        mikuru_clicker.draw_text(window)

    if nagato_clicker.is_bought:
        nagato_clicker.update_animation()
        nagato_clicker.draw_scaled_image(window, nagato_image)
        points.total_cps += 100
    else:
        nagato_clicker.draw_buy_button(window, afford =points.total_points >= 860000)
        nagato_clicker.draw_text(window)
    if not True: #temporary condition for haruhi_clicker
        window.blit(haruhi_image, (530, 315))

    if points.total_cps > 0:
        points.total_points += points.total_cps/60

    points.draw_score_box(window)
    points.draw_points(window)  #update all points before this function call
    points.total_cps = 0
    pygame.display.update()
    clock.tick(60)