# WINDOW CONFIG
DISPLAY_WIDTH = 256
DISPLAY_HEIGHT = 192
TILE_SIZE = 16
RENDER_SCALE = 3
SCREEN_WIDTH = DISPLAY_WIDTH * RENDER_SCALE
SCREEN_HEIGHT = DISPLAY_HEIGHT * RENDER_SCALE
FPS = 60
CAPTION = "2D Adventure"

RECT_OFFSETS = {
    'player': (3, 4),
    'old_wizard': (2, 4),
    'key': (3, 3),
    'sneakers': (1, 5)
}

# V
WORLD_DIMENSION = 50
WORLD_TILE_DIMENSION = WORLD_DIMENSION * TILE_SIZE

# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# PATHS
PLAYER_IMG_PATH = 'data/images/player/'
TILE_IMG_PATH = 'data/images/tiles/'
WATER_IMG_PATH = 'data/images/tiles/water'
OBJECT_IMG_PATH = 'data/images/objects/'
MAP_PATH = 'data/maps/'
FONT_PATH = 'data/fonts/'