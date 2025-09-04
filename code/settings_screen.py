import pygame
from screen_manager import Screen

class SettingsScreen(Screen):
    def __init__(self):
        self.bg_color = (30,30,30)

    def draw(self, screen):
        screen.fill(self.bg_color)