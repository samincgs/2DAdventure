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
    'player': [3, 4],
    'key': (3, 3),
    'sneakers': (1, 5)
}

DIALOGUES = {
    'player': [],
    'old_wizard': ['Hello lad.', 
                   "Welcome to this island, I don't think I have\nseen you around.", 
                   "So you've come to this island to find the\ntreasure?", 
                   "I used to be a great wizard but now I'm a bit\ntoo old to go on an adventure."
                   ]
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