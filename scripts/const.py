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
    '00' : 'plain_grass',
    '01': 'grass',
    '02': 'earth',
    '03': 'earth',
    '04': 'tree',
    '05': 'sand',
    '06': 'wall',
    
    '10': 'water_0', # topleft
    '11': 'water_1', # top middle
    '12': 'water_2', # top right
    '13': 'water_3', # left
    '14': 'water_4', # middle
    '15': 'water_5', # right
    '16': 'water_6', # bottom left
    '17': 'water_7', # bottom middle
    '18': 'water_8', # bottom right
    '19': 'water_9', # top left water edge
    '20': 'water_10', # top right water edge
    '21': 'water_11', # bottom left water edge
    '22': 'water_12', # bottom right water edge
    '23': 'water_13', # water light
    '24': 'water_14', # water
}

TILE_SETS = {
    'water'
}

RECT_OFFSETS = {
    'player': (3, 4),
    'key': (3, 3),
    'sneakers': (1, 5)
}

# V
WORLD_DIMENSION = 50
WORLD_TILE_DIMENSION = WORLD_DIMENSION * TILE_SIZE
COLLISION_TILES = {'wall', 'tree', 'water'}

# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# PATHS
PLAYER_IMG_PATH = 'data/images/player/'
TILE_IMG_PATH = 'data/images/tiles/tile'
WATER_IMG_PATH = 'data/images/tiles/water'
OBJECT_IMG_PATH = 'data/images/objects/'
MAP_PATH = 'data/maps/'
FONT_PATH = 'data/fonts/'