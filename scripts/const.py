# WINDOW CONFIG
DISPLAY_WIDTH = 256
DISPLAY_HEIGHT = 192
TILE_SIZE = 16
RENDER_SCALE = 3
SCREEN_WIDTH = DISPLAY_WIDTH * RENDER_SCALE
SCREEN_HEIGHT = DISPLAY_HEIGHT * RENDER_SCALE
FPS = 60
CAPTION = "2D Adventure"

# TYPES
TILE_VARIANTS = {
    '0' : 'grass',
    '1': 'wall',
    '2': 'water'
}

# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# PATHS
PLAYER_IMG_PATH = 'data/images/player/'
TILE_IMG_PATH = 'data/images/tiles/'
MAP_PATH = 'data/maps/'