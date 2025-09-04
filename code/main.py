import pygame
from sys import exit
from start_screen import StartScreen
from settings_screen import SettingsScreen
from combat_screen import CombatScreen

pygame.init()

# General set up
window_width, window_height = 1920, 1080
screen = pygame.display.set_mode((window_width, window_height)) # Creates a display surface and makes it the size of the tuple
pygame.display.set_caption("KyeTale") # Names the window "KyeTale"
clock = pygame.time.Clock() # Creates a clock object

# Callbacks
def start_game():
    global current_screen
     # Where the function will change
    current_screen = CombatScreen(window_width, window_height) # Temporary, add game screen # Changes state

def open_settings():
    global current_screen
    print("Opening settings")
    current_screen = SettingsScreen()

current_screen = StartScreen(window_width, window_height, start_game, open_settings) # Starts on start screen

while True:
    for event in pygame.event.get(): # Checks the events that happen
        if event.type == pygame.QUIT: # Checks if the event is a quit
            pygame.quit()
            exit()

        current_screen.handle_event(event)

    current_screen.update()
    current_screen.draw(screen)

    pygame.display.update() # Updates the display surface
    clock.tick(60) # Limits the amount of times that the while loop can run seconds in a second to 60 times
