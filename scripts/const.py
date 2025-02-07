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
    '2': 'water',
    '3': 'earth',
    '4': 'tree1',
    '5': 'sand'
}

RECT_OFFSETS = {
    'player': (4, 5),
    'key': (3, 3),
    'boots': (2, 2)
}

# V
WORLD_DIMENSION = 50
WORLD_TILE_DIMENSION = WORLD_DIMENSION * TILE_SIZE
COLLISION_TILES = {'wall', 'water', 'tree', 'tree1'}

# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# PATHS
PLAYER_IMG_PATH = 'data/images/player/'
TILE_IMG_PATH = 'data/images/tiles/'
OBJECT_IMG_PATH = 'data/images/objects/'
MAP_PATH = 'data/maps/'