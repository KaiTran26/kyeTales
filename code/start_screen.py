import pygame
from button import Button
from screen_manager import Screen

class StartScreen(Screen):
    def __init__(self, window_width, window_height, start_callback, settings_callback):
        self.sprites = pygame.sprite.Group() # Creates the group for sprites to go into

        # Button creation
        self.start_button = Button(
            self.sprites,
            (window_width-(window_width/5), window_height/5),
            (window_width/2,window_height/2),
            "#252940",
            window_height//5,
            "Start game",
            "white",
            callback = start_callback
        )

        self.settings_button = Button(
            self.sprites,
            (window_width-(window_width/5), window_height/5),
            (window_width/2,window_height/2+(window_height/5)),
            "#252940",
            window_height//5,
            "Settings",
            "white",
            callback = settings_callback
        )
        # Prepares the splash screen
        self.splash_screen = pygame.image.load("images/splash_screen.png")

    # Combines the 2 lines to make the main loop cleaner, it just blits the splash screen and draws the sprites
    def draw(self, screen):
        screen.blit(self.splash_screen, (0,0))
        self.sprites.draw(screen)

    def update(self):
        pass

    def handle_event(self, event):
        self.start_button.handle_event(event) # Passes the event forward to button.py
        self.settings_button.handle_event(event) 