from pickle import GLOBAL

import pygame
from pygame import MOUSEBUTTONDOWN
from GameModules.image_system import *

pygame.init()

#colors
white = (255,255,255)
black = (0,0,0)
grey = (200,200,200)
dark_grey = (100,100,100)
red = (255,0,0)
pink = (255,170,170)

#text variables
small_text_font = pygame.font.SysFont('Arial', 20)
normal_text_font = pygame.font.SysFont('Arial', 30)
large_text_font = pygame.font.SysFont('Arial', 40)
massive_text_font = pygame.font.SysFont('Arial', 70)

#set buy status to False
itsuki_bought = False
mikuru_bought = False
nagato_bought = False
haruhi_bought = False

class Clicker:
    def __init__(self, x, y, width, height, image):
        self.rect = pygame.Rect(x, y, width, height)
        self.x = x
        self.y = y
        self.image = image
        self.is_hovered = False

        self.current_scale = 1.0
        self.target_scale = 1.0
        self.animation_speed = 0.3

        self.is_being_clicked = False
        self.click_timer = 0
        self.click_duration = 5
    def update_animation(self):
        if self.is_being_clicked:
            self.target_scale =  0.9
        elif self.is_hovered:
            self.target_scale = 0.95
        else:
            self.target_scale = 1.0

        target_difference = self.target_scale - self.current_scale
        self.current_scale += target_difference * self.animation_speed

        if self.is_being_clicked:
            self.click_timer -= 1
            if self.click_timer < 0:
                self.is_being_clicked = False
    def start_click_animation(self):
        self.is_being_clicked = True
        self.click_timer = self.click_duration

    def draw_hurt_box(self, window):
        pygame.draw.rect(window, white, self.rect)
    def update_hover_state(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)
    def is_clicked(self, event):
        if self.is_hovered and event.type == MOUSEBUTTONDOWN and event.button == 1:
            return True
        else:
            return False

    def draw_scaled_image(self, window, image):
        original_width = image.get_width()
        original_height = image.get_height()

        new_width = int(original_width * self.target_scale)
        new_height = int(original_height * self.target_scale)

        scaled_image = pygame.transform.scale(image, (new_width, new_height))

        center_x = self.rect.centerx
        center_y = self.rect.centery

        draw_x = center_x - new_width / 2
        draw_y = center_y - new_height / 2

        window.blit(scaled_image, (draw_x, draw_y))


class Kyon(Clicker):
    def __init__(self, x, y, width, height, image, level, upgrade_cost, normal_color, hover_color, unaffordable_color, unaffordable_hover, total_points):
        super().__init__( x, y, width, height, image)
        self.level_width = 225
        self.level_height = 815
        self.upgrade_button = pygame.Rect(190, 170, 170, 50)
        self.level = level
        self.upgrade_cost = upgrade_cost
        self.normal_color = normal_color
        self.hover_color = hover_color
        self.unaffordable_color = unaffordable_color
        self.unaffordable_hover = unaffordable_hover
        self.is_hovered = False
        self.upgrade_button_hovered = False
        self.is_bought = False
        self.total_points = total_points
    def update_hover_state(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)
    def update_upgrade_hover_state(self, mouse_pos):
        self.upgrade_button_hovered = self.upgrade_button.collidepoint(mouse_pos)
    def is_clicked(self, event):
        if self.is_hovered and event.type == MOUSEBUTTONDOWN and event.button == 1:
            return True
        else:
            return False
    def upgrade_button_clicked(self, event):
        if self.upgrade_button_hovered and event.type == MOUSEBUTTONDOWN and event.button == 1:
            return True
        else:
            return False
    def draw_level_box(self, window):
        pygame.draw.rect(window, grey, (220, 240, 110, 25), )
        pygame.draw.rect(window, black, (220, 240, 110, 25), 2)

        level_text = small_text_font.render(f"Level: {self.level}", True, black)
        level_rect = level_text.get_rect()
        level_rect.center = (275, 251)
        window.blit(level_text, level_rect)
    def draw_level_up_box(self, window):
        if self.upgrade_button_hovered:
            if self.total_points >= self.upgrade_cost:
                pygame.draw.rect(window, grey, (220 - 30, 170, 170, 50))
                pygame.draw.rect(window, black, (220 - 30, 170, 170, 50), 3)
            else:
                pygame.draw.rect(window, red, (220 - 30, 170, 170, 50))
                pygame.draw.rect(window, black, (220 - 30, 170, 170, 50), 3)
        else:
            if self.total_points >= self.upgrade_cost:
                pygame.draw.rect(window, white, (220 - 30, 170, 170, 50))
                pygame.draw.rect(window, black, (220 - 30, 170, 170, 50), 3)
            else:
                pygame.draw.rect(window, pink, (220 - 30, 170, 170, 50))
                pygame.draw.rect(window, black, (220 - 30, 170, 170, 50), 3)
        upgrade_text = small_text_font.render(f"Upgrade Cost", True, black) #I want a thin line of only about 1 or 2 pixel width directly below this text
        upgrade_rect = upgrade_text.get_rect()
        upgrade_rect.center = (220 + 53, 170 + 14)
        window.blit(upgrade_text, upgrade_rect)

        level_up_cost = small_text_font.render(f"{self.upgrade_cost}", True, black) #This can stay the same, no change needed
        level_up_rect = level_up_cost.get_rect()
        level_up_rect.center = (200 + 75, 170 + 35)
        window.blit(level_up_cost, level_up_rect)


class Itsuki(Clicker):
    def __init__(self, x, y, width, height, image, buy_button_width, buy_button_height, cost, normal_color, hover_color, unaffordable_color, unaffordable_hover):
        super().__init__(x, y, width, height, image)
        self.level_width = 225
        self.level_height = 815
        self.upgrade_button = pygame.Rect(220 - 30 + 875, 170, 170, 50)
        self.rect_buy = pygame.Rect(x + 20, y + 225, buy_button_width, buy_button_height)
        self.cost = cost
        self.normal_color = normal_color
        self.hover_color = hover_color
        self.unaffordable_color = unaffordable_color
        self.unaffordable_hover = unaffordable_hover
        self.level = 1
        self.upgrade_cost = 620
        self.total_points = 0
        self.is_hovered = False
        self.upgrade_button_hovered = False
        self.is_bought = False
    def update_hover_state(self, mouse_pos):
        if not self.is_bought:
            self.is_hovered = self.rect_buy.collidepoint(mouse_pos)
        else:
            self.is_hovered = self.rect.collidepoint(mouse_pos)
    def update_upgrade_hover_state(self, mouse_pos):
        self.upgrade_button_hovered = self.upgrade_button.collidepoint(mouse_pos)
    def draw_buy_button(self, window, afford):
        if self.is_hovered:
            if afford:
                pygame.draw.rect(window, grey, self.rect_buy)
            else:
                pygame.draw.rect(window, red, self.rect_buy)
        else:
            if afford:
                pygame.draw.rect(window, white, self.rect_buy)
            else:
                pygame.draw.rect(window, pink, self.rect_buy)
        pygame.draw.rect(window, black, self.rect_buy, 3)
    def draw_text(self, window):
        buy_text = small_text_font.render(f"Unlock Itsuki", True, black)
        text_rect = buy_text.get_rect()
        text_rect.x = self.rect_buy.x + 30
        text_rect.y = 510
        window.blit(buy_text, text_rect)
        buy_cost = small_text_font.render(f"Cost: {self.cost}", True, black)
        text_rect = buy_cost.get_rect()
        text_rect.x = self.rect_buy.x + 45
        text_rect.y = 535
        window.blit(buy_cost, text_rect)
    def is_clicked(self, event):
        if self.is_bought:
            if self.is_hovered and event.type == MOUSEBUTTONDOWN and event.button == 1:
                return True
        return False
    def buy_button_clicked(self, event, afford):
        if not self.is_bought:
            if self.is_hovered and afford and event.type == MOUSEBUTTONDOWN and event.button == 1:
                self.is_bought = True
                return True
        return False
    def upgrade_button_clicked(self, event):
        if self.upgrade_button_hovered and event.type == MOUSEBUTTONDOWN and event.button == 1:
            return True
        else:
            return False
    def draw_level_box(self, window):
        pygame.draw.rect(window, grey, (220 + 875, 240, 110, 25), )#####################################
        pygame.draw.rect(window, black, (220 + 875, 240, 110, 25), 2)##################################

        level_text = small_text_font.render(f"Level: {self.level}", True, black)
        level_rect = level_text.get_rect()
        level_rect.center = (220 + 930, 252)
        window.blit(level_text, level_rect)
    def draw_level_up_box(self, window):
        if self.upgrade_button_hovered:
            if self.total_points >= self.upgrade_cost:
                pygame.draw.rect(window, grey, (220 - 30 + 875, 170, 170, 50))#################################
                pygame.draw.rect(window, black, (220 - 30 + 875, 170, 170, 50), 3)#############################
            else:
                pygame.draw.rect(window, red, (220 - 30 + 875, 170, 170, 50))#################################
                pygame.draw.rect(window, black, (220 - 30 + 875, 170, 170, 50), 3)#####################################
        else:
            if self.total_points >= self.upgrade_cost:
                pygame.draw.rect(window, white, (220 - 30 + 875, 170, 170, 50))###########################################
                pygame.draw.rect(window, black, (220 - 30 + 875, 170, 170, 50), 3)######################################
            else:
                pygame.draw.rect(window, pink, (220 - 30 + 875, 170, 170, 50))###################################
                pygame.draw.rect(window, black, (220 - 30 + 875, 170, 170, 50), 3)####################################
        upgrade_text = small_text_font.render(f"Upgrade Cost", True, black) #I want a thin line of only about 1 or 2 pixel width directly below this text
        upgrade_rect = upgrade_text.get_rect()
        upgrade_rect.center = (220 + 53 + 875, 170 + 14)
        window.blit(upgrade_text, upgrade_rect)

        level_up_cost = small_text_font.render(f"{self.upgrade_cost}", True, black) #This can stay the same, no change needed
        level_up_rect = level_up_cost.get_rect()
        level_up_rect.center = (200 + 75 + 875, 170 + 35)
        window.blit(level_up_cost, level_up_rect)


class Mikuru(Clicker):
    def __init__(self, x, y, width, height, image, buy_button_width, buy_button_height, cost, normal_color, hover_color, unaffordable_color, unaffordable_hover):
        super().__init__(x, y, width, height, image)
        self.rect_buy = pygame.Rect(x + 30, y + 130, buy_button_width, buy_button_height)
        self.cost = cost
        self.normal_color = normal_color
        self.hover_color = hover_color
        self.unaffordable_color = unaffordable_color
        self.unaffordable_hover = unaffordable_hover
        self.is_hovered = False
        self.is_bought = False
    def update_hover_state(self, mouse_pos):
        if not self.is_bought:
            self.is_hovered = self.rect_buy.collidepoint(mouse_pos)
        else:
            self.is_hovered = self.rect.collidepoint(mouse_pos)
    def draw_buy_button(self, window, afford):
        if self.is_hovered:
            if afford:
                pygame.draw.rect(window, grey, self.rect_buy)
            else:
                pygame.draw.rect(window, red, self.rect_buy)
        else:
            if afford:
                pygame.draw.rect(window, white, self.rect_buy)
            else:
                pygame.draw.rect(window, pink, self.rect_buy)
        pygame.draw.rect(window, black, self.rect_buy, 3)
    def draw_text(self, window):
        buy_text = small_text_font.render(f"Unlock Mikuru", True, black)
        text_rect = buy_text.get_rect()
        text_rect.x = self.rect_buy.x + 23
        text_rect.y = 540
        window.blit(buy_text, text_rect)
        buy_cost = small_text_font.render(f"Cost: {self.cost}", True, black)
        text_rect = buy_cost.get_rect()
        text_rect.x = self.rect_buy.x + 30
        text_rect.y = 565
        window.blit(buy_cost, text_rect)
    def is_clicked(self, event):
        if self.is_bought:
            if self.is_hovered and event.type == MOUSEBUTTONDOWN and event.button == 1:
                return True
        return False
    def buy_button_clicked(self, event, afford):
        if not self.is_bought:
            if self.is_hovered and afford and event.type == MOUSEBUTTONDOWN and event.button == 1:
                self.is_bought = True
                return True
        return False


class Nagato(Clicker):
    def __init__(self, x, y, width, height, image, buy_button_width, buy_button_height, cost, normal_color, hover_color, unaffordable_color, unaffordable_hover):
        super().__init__(x, y, width, height, image)
        self.rect_buy = pygame.Rect(x, y + 145, buy_button_width, buy_button_height)
        self.cost = cost
        self.normal_color = normal_color
        self.hover_color = hover_color
        self.unaffordable_color = unaffordable_color
        self.unaffordable_hover = unaffordable_hover
        self.is_hovered = False
        self.is_bought = False
    def update_hover_state(self, mouse_pos):
        if not self.is_bought:
            self.is_hovered = self.rect_buy.collidepoint(mouse_pos)
        else:
            self.is_hovered = self.rect.collidepoint(mouse_pos)
    def draw_buy_button(self, window, afford):
        if self.is_hovered:
            if afford:
                pygame.draw.rect(window, grey, self.rect_buy)
            else:
                pygame.draw.rect(window, red, self.rect_buy)
        else:
            if afford:
                pygame.draw.rect(window, white, self.rect_buy)
            else:
                pygame.draw.rect(window, pink, self.rect_buy)
        pygame.draw.rect(window, black, self.rect_buy, 3)
    def draw_text(self, window):
        buy_text = small_text_font.render(f"Unlock Nagato", True, black)
        text_rect = buy_text.get_rect()
        text_rect.x = self.rect_buy.x + 21
        text_rect.y = 540
        window.blit(buy_text, text_rect)
        buy_cost = small_text_font.render(f"Cost: {self.cost}", True, black)
        text_rect = buy_cost.get_rect()
        text_rect.x = self.rect_buy.x + 37
        text_rect.y = 565
        window.blit(buy_cost, text_rect)
    def is_clicked(self, event):
        if self.is_bought:
            if self.is_hovered and event.type == MOUSEBUTTONDOWN and event.button == 1:
                return True
        return False
    def buy_button_clicked(self, event, afford):
        if not self.is_bought:
            if self.is_hovered and afford and event.type == MOUSEBUTTONDOWN and event.button == 1:
                self.is_bought = True
                return True
        return False


class TransparentBox():
    def __init__(self, x, y, width, height, alpha_1, alpha_2):
        self.rect = pygame.Rect(x, y, width, height)
        self.alpha_1 = alpha_1
        self.alpha_2 = alpha_2

    def draw_score_box(self, window):
        border_width = 3

        border_box = pygame.Surface((self.rect.width, self.rect.height))
        border_box.set_alpha(self.alpha_1)
        border_box.fill(black)
        window.blit(border_box, (self.rect.x, self.rect.y))

        inner_box = pygame.Surface((self.rect.width - border_width * 2, self.rect.height - border_width * 2))
        inner_box.set_alpha(self.alpha_2)
        inner_box.fill(black)
        window.blit(inner_box, (self.rect.x + border_width, self.rect.y + border_width))


class Points(TransparentBox):
    def __init__(self, x, y, width, height,alpha_1, alpha_2, total_points, total_cps, total_click_damage):
        super().__init__(x, y, width, height, alpha_1, alpha_2)
        self.rect = pygame.Rect(x, y, width, height)
        self.alpha_1 = alpha_1
        self.alpha_2 = alpha_2
        self.total_points = total_points
        self.total_cps = total_cps
        self.total_click_damage = total_click_damage
    def draw_points(self, window):
        points_text = large_text_font.render("SOS Points: " + str(round(self.total_points)), True, white)
        text_rect = points_text.get_rect()
        text_rect.topleft = (20, 20)
        window.blit(points_text, text_rect)

        damage_click_text = normal_text_font.render("Click Damage: " + str(round(self.total_click_damage)), True, white)
        text_rect = damage_click_text.get_rect()
        text_rect.topleft = (20, 60)
        window.blit(damage_click_text, text_rect)

        cps_text = normal_text_font.render("CPS: " + str(round(self.total_cps)), True, white)
        text_rect = cps_text.get_rect()
        text_rect.topleft = (285, 60)
        window.blit(cps_text, text_rect)

class BackgroundButton(TransparentBox):
    def __init__(self, x, y, width, height, alpha_1, alpha_2, circle_x, circle_y, radius):
        super().__init__(x, y, width, height, alpha_1, alpha_2)
        self.circle_x = circle_x
        self.circle_y = circle_y
        self.radius = radius
        self.buy_button_rect = pygame.Rect(20, 835, 170, 75)
        self.total_points = 0
        self.circle_1_center = circle_x, circle_y
        self.circle_2_center = circle_x + 45, circle_y
        self.circle_3_center = circle_x + 90, circle_y
        self.circle_4_center = circle_x + 135, circle_y
        self.circle_5_center = circle_x + 180, circle_y
        self.circle_1_rect = pygame.Rect(self.circle_x, self.circle_y, self.radius, self.radius)
        self.circle_1_hovered = False
        self.circle_2_hovered = False
        self.circle_3_hovered = False
        self.circle_4_hovered = False
        self.circle_5_hovered = False
        self.circle_1_is_clicked = False
        self.circle_2_is_clicked = False
        self.circle_3_is_clicked = False
        self.circle_4_is_clicked = False
        self.circle_5_is_clicked = False
        self.buy_button_hovered = False
    def update_buy_button_hover(self, mouse_pos):
        self.buy_button_hovered = self.buy_button_rect.collidepoint(mouse_pos)
    def update_hover_state(self, mouse_pos):
        mouse_x, mouse_y = mouse_pos
        center_x, center_y = self.circle_1_center
        distance = ((mouse_x - center_x) ** 2 + (mouse_y - center_y) ** 2) ** 0.5
        self.circle_1_hovered = distance <= self.radius

        center_x, center_y = self.circle_2_center
        distance = ((mouse_x - center_x) ** 2 + (mouse_y - center_y) ** 2) ** 0.5
        self.circle_2_hovered = distance <= self.radius

        center_x, center_y = self.circle_3_center
        distance = ((mouse_x - center_x) ** 2 + (mouse_y - center_y) ** 2) ** 0.5
        self.circle_3_hovered = distance <= self.radius

        center_x, center_y = self.circle_4_center
        distance = ((mouse_x - center_x) ** 2 + (mouse_y - center_y) ** 2) ** 0.5
        self.circle_4_hovered = distance <= self.radius

        center_x, center_y = self.circle_5_center
        distance = ((mouse_x - center_x) ** 2 + (mouse_y - center_y) ** 2) ** 0.5
        self.circle_5_hovered = distance <= self.radius

    def draw_text(self, window):
        text = small_text_font.render("Backgrounds:", True, white)
        text_rect = text.get_rect()
        text_rect.topleft = (25, 875)
        window.blit(text, text_rect)
    def draw_buy_button(self, window):
        if self.buy_button_hovered:
            if self.total_points >= 1000:
                pygame.draw.rect(window, grey, (20, 835, 200, 75))
                pygame.draw.rect(window, black, (20, 835, 200, 75), 3)
            else:
                pygame.draw.rect(window, red, (20, 835, 200, 75))
                pygame.draw.rect(window, black, (20, 835, 200, 75), 3)
        else:
            if self.total_points >= 1000:
                pygame.draw.rect(window, white, (20, 835, 200, 75))
                pygame.draw.rect(window, black, (20, 835, 200, 75), 3)
            else:
                pygame.draw.rect(window, pink, (20, 835, 200, 75))
                pygame.draw.rect(window, black, (20, 835, 200, 75), 3)
    def draw_buy_button_text(self, window):
        text = small_text_font.render("Unlock Backgrounds", True, black)
        text_rect = text.get_rect()
        text_rect.topleft = (29, 845)
        window.blit(text, text_rect)

        text = small_text_font.render("Cost: 1000", True, black)
        text_rect = text.get_rect()
        text_rect.topleft = (70, 875)
        window.blit(text, text_rect)

    def draw_buttons(self, window, current_background):
        if current_background == background_1:
            pygame.draw.circle(window, dark_grey, (self.circle_x, self.circle_y), self.radius)
        else:
            if self.circle_1_hovered:
                pygame.draw.circle(window, grey, (self.circle_x, self.circle_y), self.radius)
            else:
                pygame.draw.circle(window, white, (self.circle_x, self.circle_y), self.radius)
        if current_background == background_2:
            pygame.draw.circle(window, dark_grey, (self.circle_x + 45, self.circle_y), self.radius)
        else:
            if self.circle_2_hovered:
                pygame.draw.circle(window, grey, (self.circle_x + 45, self.circle_y), self.radius)
            else:
                pygame.draw.circle(window, white, (self.circle_x + 45, self.circle_y), self.radius)
        if current_background == background_3:
            pygame.draw.circle(window, dark_grey, (self.circle_x + 90, self.circle_y), self.radius)
        else:
            if self.circle_3_hovered:
                pygame.draw.circle(window, grey, (self.circle_x + 90, self.circle_y), self.radius)
            else:
                pygame.draw.circle(window, white, (self.circle_x + 90, self.circle_y), self.radius)
        if current_background == background_4:
            pygame.draw.circle(window, dark_grey, (self.circle_x + 135, self.circle_y), self.radius)
        else:
            if self.circle_4_hovered:
                pygame.draw.circle(window, grey, (self.circle_x + 135, self.circle_y), self.radius)
            else:
                pygame.draw.circle(window, white, (self.circle_x + 135, self.circle_y), self.radius)
        if current_background == background_5:
            pygame.draw.circle(window, dark_grey, (self.circle_x + 180, self.circle_y), self.radius)
        else:
            if self.circle_5_hovered:
                pygame.draw.circle(window, grey, (self.circle_x + 180, self.circle_y), self.radius)
            else:
                pygame.draw.circle(window, white, (self.circle_x + 180, self.circle_y), self.radius)

        text = small_text_font.render("1", True, black)
        text_rect = text.get_rect()
        text_rect.center = (174, 888)
        window.blit(text, text_rect)

        text = small_text_font.render("2", True, black)
        text_rect = text.get_rect()
        text_rect.center = (174 + 45, 888)
        window.blit(text, text_rect)

        text = small_text_font.render("3", True, black)
        text_rect = text.get_rect()
        text_rect.center = (174 + 90, 888)
        window.blit(text, text_rect)

        text = small_text_font.render("4", True, black)
        text_rect = text.get_rect()
        text_rect.center = (174 + 135, 888)
        window.blit(text, text_rect)

        text = small_text_font.render("5", True, black)
        text_rect = text.get_rect()
        text_rect.center = (174 + 180, 888)
        window.blit(text, text_rect)
    def is_clicked(self, event):
        if self.circle_1_hovered and event.type == MOUSEBUTTONDOWN and event.button == 1:
            self.circle_1_is_clicked = True
            return True
        else:
            self.circle_1_is_clicked = False
        if self.circle_2_hovered and event.type == MOUSEBUTTONDOWN and event.button == 1:
            self.circle_2_is_clicked = True
            return True
        else:
            self.circle_2_is_clicked = False
        if self.circle_3_hovered and event.type == MOUSEBUTTONDOWN and event.button == 1:
            self.circle_3_is_clicked = True
            return True
        else:
            self.circle_3_is_clicked = False
        if self.circle_4_hovered and event.type == MOUSEBUTTONDOWN and event.button == 1:
            self.circle_4_is_clicked = True
            return True
        else:
            self.circle_4_is_clicked = False
        if self.circle_5_hovered and event.type == MOUSEBUTTONDOWN and event.button == 1:
            self.circle_5_is_clicked = True
            return True
        else:
            self.circle_5_is_clicked = False
    def buy_button_is_clicked(self, event):
        if self.buy_button_hovered and event.type == MOUSEBUTTONDOWN and event.button == 1:
            return True
        return False