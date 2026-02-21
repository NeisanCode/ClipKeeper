import pygame
pygame.mixer.init()

def play_sound():
    pygame.mixer.Sound("assets/sounds/clipadded.mp3").play()