import pygame
import sys

from pygame import MOUSEBUTTONDOWN

pygame.init()

#create window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Clicker Game")

#color variables
white = (255, 255, 255)
black = (0, 0, 0)
grey = (150, 150, 150)
red = (255, 0, 0)
pink = (255, 150, 150)

#general variables
clock = pygame.time.Clock()
text_font = pygame.font.SysFont("Arial", 24)
small_text_font = pygame.font.SysFont("Arial", 16)
big_text_font = pygame.font.SysFont("Arial", 30)
current_time = pygame.time.get_ticks()

#button variables
buttons_bought = 0
buyer_button_cost = 15
game_win = False

#parent class for all button types
class GeneralButton:
    def __init__(self, x, y, width, height, text, normal_color, hover_color, border_color,unaffordable_not_hover, unaffordable_color = None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.normal_color = normal_color
        self.hover_color = hover_color
        self.unaffordable_color = unaffordable_color
        self.border_color = border_color
        self.unaffordable_not_hover = unaffordable_not_hover
        self.is_hovered = False
    def mouse_on_button(self):
        self.is_hovered = self.rect.collidepoint(mouse_pos)
    def draw_button(self, afford):
        if self.is_hovered:
            if not afford:
                pygame.draw.rect(window, self.unaffordable_color, self.rect)
                pygame.draw.rect(window, self.border_color, self.rect,3)
            else:
                pygame.draw.rect(window, self.hover_color, self.rect)
                pygame.draw.rect(window, self.border_color, self.rect,3)
        else:
            if not afford:
                pygame.draw.rect(window, self.unaffordable_not_hover, self.rect)
                pygame.draw.rect(window, self.border_color, self.rect,3)
            else:
                pygame.draw.rect(window, self.normal_color, self.rect)
                pygame.draw.rect(window, self.border_color, self.rect,3)
    def draw_text(self):
        button_text = text_font.render(self.text, True, black)
        text_rect = button_text.get_rect(center = self.rect.center)
        window.blit(button_text, text_rect)
    def is_clicked(self):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            return self.rect.collidepoint(mouse_pos)
        return False


class MainButton(GeneralButton):
    def __init__(self, x, y, width, height, text, normal_color, hover_color, border_color, unaffordable_not_hover):
        super().__init__(x, y, width, height, text, normal_color, hover_color, border_color, unaffordable_not_hover)


class BuyButton(GeneralButton):
    def __init__(self, x, y, width, height, text, normal_color, hover_color, border_color, unaffordable_not_hover, unaffordable_color):
        super().__init__(x, y, width, height, text, normal_color, hover_color, border_color, unaffordable_not_hover, unaffordable_color)
    def draw_text(self):
        self.text = "Cost: " + str(round(buyer_button_cost))
        button_text = text_font.render(self.text, True, black)
        text_rect = button_text.get_rect(center = self.rect.center)
        window.blit(button_text, text_rect)


class ClickerButton(GeneralButton):
    def __init__(self, x, y, width, height, text, normal_color, hover_color, border_color, unaffordable_not_hover, unaffordable_color, button_level, cps_income, clicker_cost):
        super().__init__(x, y, width, height, text, normal_color, hover_color, border_color, unaffordable_not_hover, unaffordable_color)
        self.button_level = button_level
        self.cps_income = cps_income
        self.clicker_cost = clicker_cost
    def draw_text(self):
        level_text = str(self.button_level)
        cps_text = str(self.cps_income * self.button_level)
        button_text = small_text_font.render(f"Lvl: {level_text} CPS: {cps_text} ", True, black)
        text_rect = button_text.get_rect(center = self.rect.center)
        window.blit(button_text, text_rect)
        cost_text = small_text_font.render(f"Cost: {round(self.clicker_cost)} ", True, white)
        cost_rect = cost_text.get_rect()
        cost_rect.centerx = self.rect.centerx
        cost_rect.y = self.rect.bottom + 10
        window.blit(cost_text, cost_rect)

    def gain_cps(self):
        score.total_score += self.cps_income * self.button_level

    def update_level(self):
        self.button_level += 1
        self.clicker_cost = self.clicker_cost * 1.9

class WinButton(ClickerButton):
    def __init__(self, x, y, width, height, text, normal_color, hover_color, border_color, unaffordable_not_hover, unaffordable_color, button_level, cps_income, clicker_cost):
        super().__init__( x, y, width, height, text, normal_color, hover_color, border_color, unaffordable_not_hover, unaffordable_color, button_level, cps_income, clicker_cost)
    def draw_text(self):
        win_text = big_text_font.render(self.text, True, black)
        text_rect = win_text.get_rect(center = self.rect.center)
        window.blit(win_text, text_rect)
        cost_text = small_text_font.render(f"Cost: {round(self.clicker_cost)} ", True, white)
        cost_rect = cost_text.get_rect()
        cost_rect.centerx = self.rect.centerx
        cost_rect.y = self.rect.bottom + 10
        window.blit(cost_text, cost_rect)




class Score:
    def __init__(self,total_score):
        self.total_score = total_score
    def draw_score(self):
        score_text = text_font.render("Clicker Score : " + str(round(self.total_score)), True, white)
        text_rect = score_text.get_rect()
        text_rect.topleft = (25,25)
        window.blit(score_text, text_rect)
        cps_text = small_text_font.render(f"CPS: {cps_total} ", True, white)
        text_rect = cps_text.get_rect()
        text_rect.topleft = (25,50)
        window.blit(cps_text, text_rect)


#initializing all buttons
main_button = MainButton(
    x = window_width//2 - 155/2,
    y = window_height//2 - 55/2,
    width = 155,
    height = 55,
    text = "Click me",
    normal_color = white,
    hover_color = grey,
    border_color = white,
    unaffordable_not_hover = pink
)
button_buyer = BuyButton(
    x = window_width//2 + 150,
    y = window_height//2 - 55/2,
    width = 155,
    height = 55,
    text = "Button Price",
    normal_color = white,
    hover_color = grey,
    border_color=white,
    unaffordable_not_hover=pink,
    unaffordable_color=red,
)
clicker_1 = ClickerButton(
    x = window_width//2 - 130/2 - 300,
    y = window_height//2 - 45/2 + 100,
    width = 130,
    height = 45,
    text = "none",
    normal_color = white,
    hover_color=grey,
    border_color = white,
    unaffordable_not_hover = pink,
    unaffordable_color=red,
    button_level = 1,
    cps_income = 1,
    clicker_cost = 3
)
clicker_2 = ClickerButton(
    x = window_width//2 - 130/2 - 150,
    y = window_height//2 - 45/2 + 100,
    width = 130,
    height = 45,
    text = "none",
    normal_color = white,
    hover_color=grey,
    border_color = white,
    unaffordable_not_hover=pink,
    unaffordable_color=red,
    button_level = 1,
    cps_income = 2,
    clicker_cost = 5
)
clicker_3 = ClickerButton(
    x = window_width//2 - 130/2,
    y = window_height//2 - 45/2 + 100,
    width = 130,
    height = 45,
    text = "none",
    normal_color = white,
    hover_color=grey,
    border_color = white,
    unaffordable_not_hover=pink,
    unaffordable_color=red,
    button_level = 1,
    cps_income = 3,
    clicker_cost = 8
)
clicker_4 = ClickerButton(
    x = window_width//2 - 130/2 + 150,
    y = window_height//2 - 45/2 + 100,
    width = 130,
    height = 45,
    text = "none",
    normal_color = white,
    hover_color=grey,
    border_color = white,
    unaffordable_not_hover=pink,
    unaffordable_color=red,
    button_level = 1,
    cps_income = 4,
    clicker_cost = 11
)
clicker_5 = ClickerButton(
    x = window_width//2 - 130/2 + 300,
    y = window_height//2 - 45/2 + 100,
    width = 130,
    height = 45,
    text = "none",
    normal_color = white,
    hover_color=grey,
    border_color = white,
    unaffordable_not_hover=pink,
    unaffordable_color=red,
    button_level = 1,
    cps_income = 5,
    clicker_cost = 15
)
clicker_6 = ClickerButton(
    x = window_width//2 - 130/2 - 300,
    y = window_height//2 - 45/2 + 200,
    width = 130,
    height = 45,
    text = "none",
    normal_color = white,
    hover_color=grey,
    border_color = white,
    unaffordable_not_hover=pink,
    unaffordable_color=red,
    button_level = 1,
    cps_income = 6,
    clicker_cost = 20
)
clicker_7 = ClickerButton(
    x = window_width//2 - 130/2 - 150,
    y = window_height//2 - 45/2 + 200,
    width = 130,
    height = 45,
    text = "none",
    normal_color = white,
    hover_color=grey,
    border_color = white,
    unaffordable_not_hover=pink,
    unaffordable_color=red,
    button_level = 1,
    cps_income = 7,
    clicker_cost = 25
)
clicker_8 = ClickerButton(
    x = window_width//2 - 130/2,
    y = window_height//2 - 45/2 + 200,
    width = 130,
    height = 45,
    text = "none",
    normal_color = white,
    hover_color=grey,
    border_color = white,
    unaffordable_not_hover=pink,
    unaffordable_color=red,
    button_level = 1,
    cps_income = 8,
    clicker_cost = 32
)
clicker_9 = ClickerButton(
    x = window_width//2 - 130/2 + 150,
    y = window_height//2 - 45/2 + 200,
    width = 130,
    height = 45,
    text = "none",
    normal_color = white,
    hover_color=grey,
    border_color = white,
    unaffordable_not_hover=pink,
    unaffordable_color=red,
    button_level = 1,
    cps_income = 9,
    clicker_cost = 40
)
clicker_10 = ClickerButton(
    x = window_width//2 - 130/2 + 300,
    y = window_height//2 - 45/2 + 200,
    width = 130,
    height = 45,
    text = "none",
    normal_color = white,
    hover_color=grey,
    border_color = white,
    unaffordable_not_hover=pink,
    unaffordable_color=red,
    button_level = 1,
    cps_income = 10,
    clicker_cost = 50
)
win_button = WinButton(
    x = window_width//2 - 200/2,
    y = window_height//2 - 70/2 - 200,
    width = 200,
    height = 70,
    text = "Big Button",
    normal_color = white,
    hover_color=grey,
    border_color = white,
    unaffordable_not_hover=pink,
    unaffordable_color=red,
    button_level = 1,
    cps_income = 10,
    clicker_cost = 100000
)
#score logic
score = Score(
    total_score = 0
)

#main game loop
while True:
    #setting up frame variables
    window.fill(black)
    mouse_pos = pygame.mouse.get_pos()
    time_check = pygame.time.get_ticks()
    cps_total = 0
    if game_win:
        break
    #main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.quit()
        if main_button.is_clicked():
            score.total_score += 1
        if button_buyer.is_clicked() and score.total_score >= buyer_button_cost:
            score.total_score -= buyer_button_cost
            buyer_button_cost = buyer_button_cost * 2.1
            buttons_bought += 1
        if clicker_1.is_clicked() and score.total_score >= clicker_1.clicker_cost and buttons_bought > 0:
            score.total_score -= clicker_1.clicker_cost
            clicker_1.update_level()
        if clicker_2.is_clicked() and score.total_score >= clicker_2.clicker_cost and buttons_bought > 1:
            score.total_score -= clicker_2.clicker_cost
            clicker_2.update_level()
        if clicker_3.is_clicked() and score.total_score >= clicker_3.clicker_cost and buttons_bought > 2:
            score.total_score -= clicker_3.clicker_cost
            clicker_3.update_level()
        if clicker_4.is_clicked() and score.total_score >= clicker_4.clicker_cost and buttons_bought > 3:
            score.total_score -= clicker_4.clicker_cost
            clicker_4.update_level()
        if clicker_5.is_clicked() and score.total_score >= clicker_5.clicker_cost and buttons_bought > 4:
            score.total_score -= clicker_5.clicker_cost
            clicker_5.update_level()
        if clicker_6.is_clicked() and score.total_score >= clicker_6.clicker_cost and buttons_bought > 5:
            score.total_score -= clicker_6.clicker_cost
            clicker_6.update_level()
        if clicker_7.is_clicked() and score.total_score >= clicker_7.clicker_cost and buttons_bought > 6:
            score.total_score -= clicker_7.clicker_cost
            clicker_7.update_level()
        if clicker_8.is_clicked() and score.total_score >= clicker_8.clicker_cost and buttons_bought > 7:
            score.total_score -= clicker_8.clicker_cost
            clicker_8.update_level()
        if clicker_9.is_clicked() and score.total_score >= clicker_9.clicker_cost and buttons_bought > 8:
            score.total_score -= clicker_9.clicker_cost
            clicker_9.update_level()
        if clicker_10.is_clicked() and score.total_score >= clicker_10.clicker_cost and buttons_bought > 9:
            score.total_score -= clicker_10.clicker_cost
            clicker_10.update_level()
        if win_button.is_clicked() and score.total_score >= win_button.clicker_cost:
            game_win = True

    #main button creation
    main_button.mouse_on_button()
    main_button.draw_button(afford = True)
    main_button.draw_text()

    #button buyer creation
    if buttons_bought < 10:
        button_buyer.mouse_on_button()
        button_buyer.draw_button(score.total_score >= buyer_button_cost)
        button_buyer.draw_text()

    #clicker creations
    if buttons_bought > 0:
        clicker_1.mouse_on_button()
        clicker_1.draw_button(afford = score.total_score >= clicker_1.clicker_cost)
        clicker_1.draw_text()
        if time_check - current_time >= 1000:
            clicker_1.gain_cps()
        cps_total += clicker_1.cps_income * clicker_1.button_level
    if buttons_bought > 1:
        clicker_2.mouse_on_button()
        clicker_2.draw_button(afford=score.total_score >= clicker_2.clicker_cost)
        clicker_2.draw_text()
        if time_check - current_time >= 1000:
            clicker_2.gain_cps()
        cps_total += clicker_2.cps_income * clicker_2.button_level
    if buttons_bought > 2:
        clicker_3.mouse_on_button()
        clicker_3.draw_button(afford=score.total_score >= clicker_3.clicker_cost)
        clicker_3.draw_text()
        if time_check - current_time >= 1000:
            clicker_3.gain_cps()
        cps_total += clicker_3.cps_income * clicker_3.button_level
    if buttons_bought > 3:
        clicker_4.mouse_on_button()
        clicker_4.draw_button(afford=score.total_score >= clicker_4.clicker_cost)
        clicker_4.draw_text()
        if time_check - current_time >= 1000:
            clicker_4.gain_cps()
        cps_total += clicker_4.cps_income * clicker_4.button_level
    if buttons_bought > 4:
        clicker_5.mouse_on_button()
        clicker_5.draw_button(afford=score.total_score >= clicker_5.clicker_cost)
        clicker_5.draw_text()
        if time_check - current_time >= 1000:
            clicker_5.gain_cps()
        cps_total += clicker_5.cps_income * clicker_5.button_level
    if buttons_bought > 5:
        clicker_6.mouse_on_button()
        clicker_6.draw_button(afford=score.total_score >= clicker_6.clicker_cost)
        clicker_6.draw_text()
        if time_check - current_time >= 1000:
            clicker_6.gain_cps()
        cps_total += clicker_6.cps_income * clicker_6.button_level
    if buttons_bought > 6:
        clicker_7.mouse_on_button()
        clicker_7.draw_button(afford=score.total_score >= clicker_7.clicker_cost)
        clicker_7.draw_text()
        if time_check - current_time >= 1000:
            clicker_7.gain_cps()
        cps_total += clicker_7.cps_income * clicker_7.button_level
    if buttons_bought > 7:
        clicker_8.mouse_on_button()
        clicker_8.draw_button(afford=score.total_score >= clicker_8.clicker_cost)
        clicker_8.draw_text()
        if time_check - current_time >= 1000:
            clicker_8.gain_cps()
        cps_total += clicker_8.cps_income * clicker_8.button_level
    if buttons_bought > 8:
        clicker_9.mouse_on_button()
        clicker_9.draw_button(afford=score.total_score >= clicker_9.clicker_cost)
        clicker_9.draw_text()
        if time_check - current_time >= 1000:
            clicker_9.gain_cps()
        cps_total += clicker_9.cps_income * clicker_9.button_level
    if buttons_bought > 9:
        clicker_10.mouse_on_button()
        clicker_10.draw_button(afford=score.total_score >= clicker_10.clicker_cost)
        clicker_10.draw_text()
        if time_check - current_time >= 1000:
            clicker_10.gain_cps()
        cps_total += clicker_10.cps_income * clicker_10.button_level
    win_button.mouse_on_button()
    win_button.draw_button(afford = score.total_score >= win_button.clicker_cost)
    win_button.draw_text()

    #score creation
    score.draw_score()

    if time_check - current_time >= 1000:
        current_time = time_check
    pygame.display.update()
    clock.tick(60)
#when win condition is met
while True:
    window.fill(black)
    button_text = text_font.render("You Win!", True, white)
    text_rect = button_text.get_rect()
    text_rect.centerx = 400
    text_rect.y = 100
    window.blit(button_text, text_rect)

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.quit()