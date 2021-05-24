import os.path

from pygame import display

display.init()
# File containing all game constants

# -------------------- Display constants -------------------- #

DISPLAY_WIDTH = display.Info().current_w
DISPLAY_HEIGHT = display.Info().current_h

DISPLAY_SIZE = (DISPLAY_WIDTH, DISPLAY_HEIGHT)
GAME_TITLE = 'Zoooombies'

CLOCK_TICK = 120

PLAYER_WIDTH = int(DISPLAY_WIDTH * 0.15)
PLAYER_HEIGHT = int(DISPLAY_HEIGHT * 0.2)
PLAYER_SIZE = (PLAYER_WIDTH, PLAYER_HEIGHT)

# -------------------- Images constants -------------------- #

# -------------------- Source Url

MAIN_URL = 'https://www.gameart2d.com/uploads/3/0/9/1/30917885/'

NINJA_IMG_SOURCE = MAIN_URL + 'ninjaadventurenew.zip'
ZOMBIE_IMG_SOURCE = MAIN_URL + 'zombiefiles.zip'
BG_IMG_SOURCE = MAIN_URL + 'graveyardtilesetnew.zip'

# -------------------- Paths

MAIN_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGES_PATH = os.path.join(MAIN_DIR, 'Images')

BACKGROUND_IMAGE_PATH = os.path.join(IMAGES_PATH, 'Background/BG/bg1')
PLAYER_IMAGES_PATH = os.path.join(IMAGES_PATH, 'Ninja/')
MALE_ZOMBIE_IMAGES_PATH = os.path.join(IMAGES_PATH, 'Zombie/Male/')

characters = {
    'Background': BG_IMG_SOURCE,
    'Ninja': NINJA_IMG_SOURCE,
    'Zombie': ZOMBIE_IMG_SOURCE,
}

RED = (250, 0, 0)

