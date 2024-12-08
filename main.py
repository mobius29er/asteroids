# this allows us to use code from
# the open-source pygame library
# throughout this file
# import the function_hello function
# and the variable_player variable
# into the current file
# from module import function_hello, variable_player
# import everything from a module
# into the current file
# from module import *
import pygame
from constants import *
from player import Player

# 1 Event Handling: Process all input events at the start of the loop.
# 2 Game Logic Updates: Process your game state changes next.
# 3 Screen Clearing: Use screen.fill((0, 0, 0)) early in the drawing phase to ensure a clean background for your new frame.
# 4 Drawing Operations: Render all necessary game objects, text, and other visuals after clearing.
# 5 Display Update: Finally, call pygame.display.update() to swap the newly prepared frame with the on-screen buffer, showing all updates to the player.

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Create player in middle of screen
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        # Fill screen with black
        screen.fill("black")
        
        # Draw the player
        player.draw(screen)
        player.update(dt)
        
        # Flip the display
        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()