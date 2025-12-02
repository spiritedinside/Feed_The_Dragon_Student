import pygame, random

# Initialize pygame
pygame.init()

def make_text(font_object, text, color, background_color):
    # TODO: Use the given font_object to create and return a rendered text Surface.
    #       - Use font_object.render(...)
    #       - Make sure antialias is set to True
    #       - Use the given text, color, and background_color
    pass # TODO: remove this when finished


def blit(surface, item, rect):
    # TODO: Draw (blit) the given item (Surface) onto the given surface at the given rect.
    #       - Use the surface.blit(...) method
    pass # TODO: remove this when finished


def fill(surface, color):
    # TODO: Fill the entire surface with the given color using surface.fill(...)
    pass # TODO: remove this when finished


def update_display():
    # TODO: Update the entire display so that any drawing shows up on the screen.
    #       - Use pygame.display.update()
    pass # TODO: remove this when finished


# Set display surface
# TODO:
#   - Create WINDOW_WIDTH and WINDOW_HEIGHT constants (e.g., 1000 x 400).
#   - Use pygame.display.set_mode to create the display_surface with that size.
#   - Set a window caption like "Feed the Dragon" using pygame.display.set_caption(...).


# Set FPS and clock
# TODO:
#   - Create an FPS constant (e.g., 60).
#   - Create a clock object using pygame.time.Clock() for controlling the frame rate.


# Set game values
# TODO:
#   - Create constants for:
#       * PLAYER_STARTING_LIVES (e.g., 5)
#       * PLAYER_VELOCITY (how fast the dragon moves up/down) (e.g., 10)
#       * COIN_STARTING_VELOCITY (how fast the coin moves at the start) (e.g, 10)
#       * COIN_ACCELERATION (how much faster the coin gets after each catch) (e.g., 0.5)
#       * BUFFER_DISTANCE (how far off-screen to respawn the coin on the right) (e.g, 100)
#   - Create variables for:
#       * score (starting at 0)
#       * player_lives (start at PLAYER_STARTING_LIVES)
#       * coin_velocity (start at COIN_STARTING_VELOCITY)


# Set colors
# TODO:
#   - Define color constants using RGB tuples, such as:
#       * GREEN
#       * DARKGREEN:  RGB value of 10, 50, 10
#       * WHITE
#       * BLACK


# Set fonts
# TODO:
#   - Create a font object using pygame.font.Font(...)
#   - Use the provided font file from the assets folder (e.g., "assets/AttackGraffiti.ttf")
#   - Choose a font size (e.g., 32)


# Set text
# TODO:
#   - Use your make_text function (or font.render directly) to create:
#       * score_text showing "Score: " + current score, with green color, dark green background color
#       * title_text showing "Feed the Dragon", with green color, white background color
#       * lives_text showing "Lives: " + current lives, with green color, and dark green background color
#   - Get rects for each text surface using .get_rect()
#   - Position:
#       * score_rect at the top-left (e.g., (10, 10))
#       * title_rect centered horizontally at the top
#       * lives_rect at the top-right (e.g., (WINDOW_WIDTH - 10, 10))


# Set sounds and music
# TODO:
#   - Load sound effects for:
#       * catching a coin (e.g., "assets/coin_sound.wav")
#       * missing a coin (e.g., "assets/miss_sound.wav")
#   - Optionally adjust the miss sound volume using set_volume(...)
#   - Load background music (e.g., "assets/ftd_background_music.wav") using pygame.mixer.music.load(...)


# Set images
# TODO:
#   - Load the player image (dragon) from "assets/dragon_right.png" using pygame.image.load(...)
#   - Get its rect with .get_rect() and:
#       * place it near the left side of the screen
#       * center it vertically in the window
#   - Load the coin image from "assets/coin.png"
#   - Get its rect and:
#       * start it off to the right of the window by BUFFER_DISTANCE
#       * give it a random y-position somewhere between a top margin (like 64) and near the bottom


# The main game loop
# TODO:
#   - Play the background music in a loop using pygame.mixer.music.play(...)
#   - Create a variable named running and set it to True; this will control the main while loop.


def tick():
    # TODO:
    #   - Use the clock object to pause just enough so the game runs at FPS frames per second.
    #   - Call clock.tick(FPS)
    pass # TODO: remove this when finished


def is_still_running():
    # TODO:
    #   - Get the pygame event list with pygame.event.get()
    #   - If you see an event of type pygame.QUIT, set running to False
    #     so the main loop will end and the game can quit.
    pass # TODO: remove this when finished


def move_player():
    # TODO:
    #   - Get the current state of the keyboard using pygame.key.get_pressed()
    #   - If the up arrow is pressed and the player is not above a top limit (e.g., y > 64),
    #       move the player up by PLAYER_VELOCITY.
    #   - If the down arrow is pressed and the player is not below the bottom of the window,
    #       move the player down by PLAYER_VELOCITY.
    pass # TODO: remove this when finished


def handle_coin():
    # TODO:
    #   - Move the coin to the left each frame by subtracting coin_velocity from coin_rect.x.
    #   - If the coin passes off the left side of the screen (coin_rect.x < 0):
    #       * Subtract 1 from player_lives.
    #       * Play the miss sound.
    #       * Reset the coin's position:
    #           - x: WINDOW_WIDTH + BUFFER_DISTANCE
    #           - y: a random integer between a top margin (e.g., 64) and near the bottom edge.
    pass # TODO: remove this when finished


def handle_collisions():
    # TODO:
    #   - Check if the player_rect and coin_rect are colliding using colliderect(...)
    #   - If they collide:
    #       * Increase score by 1
    #       * Play the coin sound
    #       * Increase coin_velocity by COIN_ACCELERATION
    #       * Reset the coin's position:
    #           - x: WINDOW_WIDTH + BUFFER_DISTANCE
    #           - y: random integer between the same top and bottom margins
    pass # TODO: remove this when finished


def update_hud():
    # TODO:
    #   - Re-create score_text and lives_text each frame using make_text(...),
    #     so they show the updated score and lives values.
    #   - Remember to use the same font and colors (GREEN and DARKGREEN).
    pass # TODO: remove this when finished


def game_over_check():
    # TODO:
    #   - If player_lives reaches 0:
    #       * Draw the game over text and the "press any key to play again" text on the screen.
    #       * Update the display so the player can see the game over screen.
    #       * Stop the background music.
    #       * Create a loop (e.g., is_paused = True) that:
    #           - Waits for events:
    #               + If the player presses any key (KEYDOWN):
    #                   · Reset score to 0
    #                   · Reset player_lives to PLAYER_STARTING_LIVES
    #                   · Reset player position to center vertically
    #                   · Reset coin_velocity to COIN_STARTING_VELOCITY
    #                   · Restart the background music
    #                   · Exit the pause loop (resume game)
    #               + If the player clicks the window close button (QUIT):
    #                   · Set running to False and exit the pause loop so the game can end.
    pass # TODO: remove this when finished


def update_screen():
    # TODO:
    #   - Fill the display_surface with a background color (e.g., BLACK) using your fill(...) helper.
    #   - Draw the HUD elements on the screen:
    #       * score_text, title_text, lives_text at their rect positions using your blit(...) helper.
    #   - Draw a horizontal line across the screen near the top to separate the HUD from the play area.
    #   - Draw the player image and the coin image at their rect positions using your blit(...) helper.
    #   - Finally, call update_display() so that everything appears on the screen.
    pass


while running:
    # Main game loop steps:
    #   1. Handle quit events.
    #   2. Move the player based on keyboard input.
    #   3. Move the coin and handle misses.
    #   4. Check for collisions between player and coin.
    #   5. Update the HUD text to match the current score and lives.
    #   6. Check if the game is over and either reset or quit.
    #   7. Draw everything on the screen.
    #   8. Tick the clock to control the frame rate.

    is_still_running()
    move_player()
    handle_coin()
    handle_collisions()
    update_hud()
    game_over_check()
    update_screen()
    tick()

# End the game
pygame.quit()
