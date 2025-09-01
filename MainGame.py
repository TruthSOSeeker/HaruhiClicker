import sys
import pygame
import random
from GameModules.image_system import *
from GameModules.classes import *
from GameModules.sound_system import *
from GameModules.music_system import *
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
    cost = 760000,
    normal_color = white,
    hover_color = grey,
    unaffordable_color = pink,
    unaffordable_hover = red
)
haruhi_clicker = Haruhi(
    x= 630,
    y= 395,
    width=120,
    height=450,
    image=haruhi_image,
    cost = 20000000
)
points = Points(
    x = 18,
    y = 19,
    width = 500,
    height = 80,
    alpha_1=150,
    alpha_2= 50,
    total_points = 10000000000000,
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

big_bang = BigBang()
music_button = MusicButton()
clicker_ability = Ability()
#main game loop
game_running = True
while game_running:
    window.fill((0,0,0))
    #recalculate new frame mouse position
    mouse_pos = pygame.mouse.get_pos()
    kyon_clicker.update_hover_state(mouse_pos)
    kyon_clicker.update_upgrade_hover_state(mouse_pos)
    itsuki_clicker.update_hover_state(mouse_pos)
    itsuki_clicker.update_upgrade_hover_state(mouse_pos)
    mikuru_clicker.update_hover_state(mouse_pos)
    mikuru_clicker.update_upgrade_hover_state(mouse_pos)
    mikuru_clicker.update_time_travel_hover_state(mouse_pos)
    nagato_clicker.update_hover_state(mouse_pos)
    nagato_clicker.update_upgrade_hover_state(mouse_pos)
    haruhi_clicker.update_hover_state(mouse_pos)
    haruhi_clicker.update_upgrade_hover_state(mouse_pos)
    music_button.update_buy_button_hover(mouse_pos)
    music_button.update_pause_hover_state(mouse_pos)
    clicker_ability.update_hover_state(mouse_pos)
    big_bang.is_hovering(mouse_pos)
    background_button.update_buy_button_hover(mouse_pos)
    #event checks
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.quit()
        if kyon_clicker.is_clicked(event):
            points.total_points += kyon_clicker.level
            kyon_clicker.start_click_animation()
            random_sound = random.choice(click_sounds)
            play_sound(random_sound)
        if kyon_clicker.upgrade_button_clicked(event) and points.total_points >= kyon_clicker.upgrade_cost:
            points.total_points -= kyon_clicker.upgrade_cost
            kyon_clicker.level += 1
            kyon_clicker.upgrade_cost = round(kyon_clicker.upgrade_cost * 1.7)
            random_voice = random.choice(kyon_voices)
            play_sound(random_voice)
        if itsuki_clicker.is_clicked(event):
            points.total_points += kyon_clicker.level
            itsuki_clicker.start_click_animation()
            random_sound = random.choice(click_sounds)
            play_sound(random_sound)
        if  itsuki_clicker.buy_button_clicked(event, afford =points.total_points >= 500): #change value when done with speedrunning itsuki
            points.total_points -= 500
            itsuki_bought = True
            random_voice = random.choice(itsuki_voices)
            play_sound(random_voice)
        if itsuki_clicker.upgrade_button_clicked(event) and points.total_points >= itsuki_clicker.upgrade_cost and itsuki_bought:
            points.total_points -= itsuki_clicker.upgrade_cost
            itsuki_clicker.level += 1
            itsuki_clicker.upgrade_cost = round(itsuki_clicker.upgrade_cost * 1.6)
            random_voice = random.choice(itsuki_voices)
            play_sound(random_voice)
        if mikuru_clicker.is_clicked(event):
            if nagato_bought:
                points.total_points += kyon_clicker.level * nagato_clicker.level * 2
            else:
                points.total_points += kyon_clicker.level
            mikuru_clicker.start_click_animation()
            random_sound = random.choice(click_sounds)
            play_sound(random_sound)
        if mikuru_clicker.buy_button_clicked(event, afford =points.total_points >= 21000): #change value when done with speedrunning mikuru
            points.total_points -= 21000
            mikuru_bought = True
            mikuru_clicker.initiate_time = pygame.time.get_ticks()
            random_voice = random.choice(mikuru_voices)
            play_sound(random_voice)
        if mikuru_clicker.upgrade_button_clicked(event) and points.total_points >= mikuru_clicker.upgrade_cost and mikuru_bought and not mikuru_clicker.time_traveling:
            points.total_points -= mikuru_clicker.upgrade_cost
            mikuru_clicker.level += 1
            mikuru_clicker.upgrade_cost = round(mikuru_clicker.upgrade_cost * 1.6)
            random_voice = random.choice(mikuru_voices)
            play_sound(random_voice)
        if mikuru_clicker.time_travel_is_clicked(event) and mikuru_bought and not mikuru_clicker.time_traveling and mikuru_clicker.reward_claimed and mikuru_clicker.time_travel_check <= -60000:
            mikuru_clicker.time_traveling = True
            mikuru_clicker.time_travel_time = pygame.time.get_ticks()
            play_sound(teleport_away)
            mikuru_clicker.return_sound = True
        if mikuru_clicker.reward_claim_is_clicked(event):
            mikuru_clicker.reward_claimed = True
            points.total_points += mikuru_clicker.reward
            mikuru_clicker.initiate_time = pygame.time.get_ticks()
            play_sound(get_reward)
        if nagato_clicker.is_clicked(event):
            points.total_points += kyon_clicker.level * nagato_clicker.level * 2
            nagato_clicker.start_click_animation()
            random_sound = random.choice(click_sounds)
            play_sound(random_sound)
        if nagato_clicker.buy_button_clicked(event, afford =points.total_points >= 760000): #change value when done with speedrunning nagato
            points.total_points -= 760000
            nagato_bought = True
            nagato_clicker.is_bought = True
            random_voice = random.choice(nagato_voices)
            play_sound(random_voice)
        if nagato_clicker.upgrade_button_clicked(event) and nagato_bought and points.total_points >= nagato_clicker.upgrade_cost:
            points.total_points -= nagato_clicker.upgrade_cost
            nagato_clicker.level += 1
            nagato_clicker.upgrade_cost = round(nagato_clicker.upgrade_cost * 1.6)
            random_voice = random.choice(nagato_voices)
            play_sound(random_voice)
        if haruhi_clicker.is_clicked(event):
            if nagato_bought:
                points.total_points += kyon_clicker.level * nagato_clicker.level * 2
            else:
                points.total_points += kyon_clicker.level
            haruhi_clicker.start_click_animation()
            random_sound = random.choice(click_sounds)
            play_sound(random_sound)
        if haruhi_clicker.buy_button_clicked(event, afford = points.total_points >= 20000000):
            points.total_points -= 20000000
            haruhi_bought = True
            haruhi_clicker.is_bought = True
            play_sound(haruhi_voice_3)
        if haruhi_clicker.upgrade_button_clicked(event) and haruhi_bought and points.total_points >= haruhi_clicker.upgrade_cost:
            points.total_points -= haruhi_clicker.upgrade_cost
            haruhi_clicker.level += 1
            haruhi_clicker.upgrade_cost = round(haruhi_clicker.upgrade_cost * 1.6)
            random_voice = random.choice(haruhi_voices)
            play_sound(random_voice)
        if background_button.is_clicked(event) and background_bought:
            if background_button.circle_1_is_clicked:
                current_background = background_1
            elif background_button.circle_2_is_clicked:
                current_background = background_2
            elif background_button.circle_3_is_clicked:
                current_background = background_3
            elif background_button.circle_4_is_clicked:
                current_background = background_4
            else:
                current_background = background_5
        if background_button.buy_button_is_clicked(event) and not background_bought and points.total_points >= 1000:
            points.total_points -= 1000
            background_bought = True
        if music_button.buy_button_clicked(event) and points.total_points >= 10000 and not music_bought:
            points.total_points -= 10000
            playing_music = True
            music_bought = True
            lofi_music = load_background_music("assets/audio/music/lofi_music.mp3")
            play_background_music(lofi_music)
        if music_bought and music_button.pause_button_clicked(event):
            if playing_music:
                pause_background_music()
                playing_music = False
            else:
                unpause_background_music()
                playing_music = True
        if big_bang.is_clicked(event) and points.total_points >= 999999999999:
            game_running = False
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
    #draw music button
    if music_bought:
        music_button.draw_music_box(window)
        music_button.draw_pause_button(window)
        if playing_music:
            window.blit(pause_button, (1335, 25))
        else:
            window.blit(play_button, (1335, 25))
    else:
        music_button.draw_buy_box(window)
    # draw abilities button
    clicker_ability.draw_click_box(window)
    clicker_ability.draw_massive_box(window)
    #draw clickers
    kyon_clicker.total_points = points.total_points
    itsuki_clicker.total_points = points.total_points
    mikuru_clicker.total_points = points.total_points
    nagato_clicker.total_points = points.total_points
    haruhi_clicker.total_points = points.total_points
    big_bang.total_points = points.total_points
    music_button.total_points = points.total_points
    if kyon_image:
        kyon_clicker.update_animation()
        kyon_clicker.draw_scaled_image(window, kyon_image)
        kyon_clicker.draw_level_box(window)
        kyon_clicker.draw_level_up_box(window)
        points.total_click_damage = kyon_clicker.level
        if nagato_bought:
            points.total_click_damage = points.total_click_damage * (2 * nagato_clicker.level)
    if itsuki_clicker.is_bought:
        itsuki_clicker.update_animation()
        itsuki_clicker.draw_scaled_image(window, itsuki_image)
        points.total_cps += kyon_clicker.level + itsuki_clicker.level
        if mikuru_clicker.is_bought:
            points.total_cps += mikuru_clicker.level
        if nagato_bought:
            points.total_cps += nagato_clicker.level
            points.total_cps = points.total_cps * (1 + nagato_clicker.level)
        if haruhi_clicker.is_bought:
            points.total_cps += haruhi_clicker.level
        points.total_cps = points.total_cps * (0.8 * itsuki_clicker.level)
        itsuki_clicker.draw_level_box(window)
        itsuki_clicker.draw_level_up_box(window)
    else:
        itsuki_clicker.draw_buy_button(window, afford =points.total_points >= 500)
        itsuki_clicker.draw_text(window)
    if nagato_clicker.is_bought:
        nagato_clicker.update_animation()
        nagato_clicker.draw_scaled_image(window, nagato_image)
        nagato_clicker.draw_level_box(window)
        nagato_clicker.draw_level_up_box(window)
    else:
        nagato_clicker.draw_buy_button(window, afford =points.total_points >= 860000)
        nagato_clicker.draw_text(window)
    if haruhi_clicker.is_bought:
        haruhi_clicker.update_animation()
        haruhi_clicker.draw_scaled_image(window, haruhi_image)
        haruhi_clicker.draw_level_box(window)
        haruhi_clicker.draw_level_up_box(window)
        haruhi_clicker.get_exponential()
        points.total_cps += haruhi_clicker.level * haruhi_clicker.exponential * points.total_cps
        points.total_click_damage += haruhi_clicker.level * haruhi_clicker.exponential * points.total_click_damage
    else:
        haruhi_clicker.draw_buy_button(window, afford =points.total_points >= 20000000)
        haruhi_clicker.draw_text(window)
    if mikuru_clicker.is_bought:
        if not mikuru_clicker.time_traveling:
            mikuru_clicker.time_travel_check = mikuru_clicker.initiate_time - pygame.time.get_ticks()
            mikuru_clicker.update_animation()
            mikuru_clicker.draw_scaled_image(window, mikuru_image)
            mikuru_clicker.draw_level_box(window)
            mikuru_clicker.draw_level_up_box(window)
            if mikuru_clicker.reward_claimed:
                mikuru_clicker.draw_lower_box(window)
            else:
                mikuru_clicker.draw_lower_box(window)
        else:
            mikuru_clicker.time_check = pygame.time.get_ticks() - mikuru_clicker.time_travel_time
            if mikuru_clicker.time_check >= 60000:
                mikuru_clicker.reward_claimed = False
                mikuru_clicker.time_traveling = False
                mikuru_clicker.reward = points.total_cps * 60 * mikuru_clicker.level * 1.4
    else:
        mikuru_clicker.draw_buy_button(window, afford =points.total_points >= 21000)
        mikuru_clicker.draw_text(window)

    big_bang.draw_box(window)

    if points.total_cps > 0:
        points.total_points += points.total_cps/60
    if points.total_click_damage > 999:
        points.total_click_damage = 999
    if points.total_cps > 99999999:
        points.total_cps = 99999999
    if points.total_points > 999999999999:
        points.total_points = 999999999999
    points.draw_score_box(window)
    points.draw_points(window)  #update all cps points before this function call
    points.total_cps = 0
    # draw abilities button
    clicker_ability.draw_click_box(window)
    clicker_ability.itsuki_bought = itsuki_bought
    clicker_ability.mikuru_bought = mikuru_bought
    clicker_ability.nagato_bought = nagato_bought
    clicker_ability.haruhi_bought = haruhi_bought
    while clicker_ability.circle_hovered:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        window.fill(black)
        if background_bought:
            window.blit(current_background, (0,0))
        clicker_ability.draw_click_box(window)
        mouse_pos = pygame.mouse.get_pos()
        clicker_ability.update_hover_state(mouse_pos)
        clicker_ability.draw_massive_box(window)
        pygame.display.update()
        clock.tick(60)
    #update window
    pygame.display.update()
    clock.tick(60)

playing_music = False
while True:
    window.blit(win_screen, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if not playing_music:
        god_knows = load_background_music("assets/audio/music/god_knows.mp3")
        play_background_music(god_knows)
        playing_music = True
    win_text = large_text_font.render("Thanks for playing!", True, black)
    text_rect = win_text.get_rect()
    text_rect.center = (700, 75)
    window.blit(win_text, text_rect)
    pygame.display.update()