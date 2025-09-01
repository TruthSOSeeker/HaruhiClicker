import pygame

pygame.mixer.init()

def load_sound(file_path):
    try:
        sound = pygame.mixer.Sound(file_path)
        return sound
    except pygame.error as e:
        print(f"Could not load sound: {e}")
        return None
def play_sound(sound):
    sound.play()

#initialize sounds
kyon_voice_1 = load_sound("assets/audio/kyon_voice_1.mp3")
kyon_voice_2 = load_sound("assets/audio/kyon_voice_2.mp3")
kyon_voice_3 = load_sound("assets/audio/kyon_voice_3.mp3")
itsuki_voice_1 = load_sound("assets/audio/itsuki_voice_1.mp3")
itsuki_voice_2 = load_sound("assets/audio/itsuki_voice_2.mp3")
itsuki_voice_3 = load_sound("assets/audio/itsuki_voice_3.mp3")
mikuru_voice_1 = load_sound("assets/audio/mikuru_voice_1.mp3")
mikuru_voice_2 = load_sound("assets/audio/mikuru_voice_2.mp3")
mikuru_voice_3 = load_sound("assets/audio/mikuru_voice_3.mp3")
nagato_voice_1 = load_sound("assets/audio/nagato_voice_1.mp3")
nagato_voice_2 = load_sound("assets/audio/nagato_voice_2.mp3")
nagato_voice_3 = load_sound("assets/audio/nagato_voice_3.mp3")
haruhi_voice_1 = load_sound("assets/audio/haruhi_voice_1.mp3")
haruhi_voice_2 = load_sound("assets/audio/haruhi_voice_2.mp3")
haruhi_voice_3 = load_sound("assets/audio/haruhi_voice_3.mp3")
teleport_away = load_sound("assets/audio/teleport_away.mp3")
teleport_back = load_sound("assets/audio/teleport_back.mp3")
get_reward = load_sound("assets/audio/get_reward.mp3")
water_drop = load_sound("assets/audio/water_drop.mp3")
click_sound_1 = load_sound("assets/audio/click_sound_1.mp3")
click_sound_2 = load_sound("assets/audio/click_sound_2.mp3")
click_sound_3 = load_sound("assets/audio/click_sound_3.mp3")
click_sound_4 = load_sound("assets/audio/click_sound_4.mp3")

#assign upgrades to each person
kyon_voices = [kyon_voice_1, kyon_voice_2, kyon_voice_3]
itsuki_voices = [itsuki_voice_1, itsuki_voice_2, itsuki_voice_3]
mikuru_voices = [mikuru_voice_1, mikuru_voice_2, mikuru_voice_3]
nagato_voices = [nagato_voice_1, nagato_voice_2, nagato_voice_3]
haruhi_voices = [haruhi_voice_1, haruhi_voice_2, haruhi_voice_3]

click_sounds = [click_sound_1, click_sound_2, click_sound_3, click_sound_4]