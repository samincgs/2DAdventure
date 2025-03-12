# WINDOW CONFIG
DISPLAY_WIDTH = 256
DISPLAY_HEIGHT = 192
TILE_SIZE = 16
RENDER_SCALE = 3
SCREEN_WIDTH = DISPLAY_WIDTH * RENDER_SCALE
SCREEN_HEIGHT = DISPLAY_HEIGHT * RENDER_SCALE
FPS = 60
CAPTION = "2D Adventure"
WORLD_DIMENSION = 50
WORLD_TILE_DIMENSION = WORLD_DIMENSION * TILE_SIZE

# CHARACTER VARIABLES
ENTITY_RECT_OFFSETS = {
    'player': (4, 9),
    'old_wizard': (1, 6),
    'knight': (2, 2),
    'green_slime': (2, 6),
}

WEAPON_RECT = {
    'sword': {
        'size': {
            'up': [6, 8],
            'down': [6, 8],
            'right': [8 , 6],
            'left': [8, 6],
        },
        'offset': {
            'up': [3, -16],
            'down': [-1, 9],
            'right': [11 , -1],
            'left': [-11, -1],
            }
    }
}

DIALOGUES = {
    'player': [],
    'old_wizard': ['Hello lad.', 
                   "Welcome to this island, I don't think I have\nseen you around.", 
                   "So you've come to this island to find the\ntreasure?", 
                   "I used to be a great wizard but now I'm a\nbit too old to go on an adventure."
                   ],
    'knight': ["Don't talk to me stranger."]
}

ITEM_AMOUNT_DEFAULT = 1
MAX_INVENTORY_SIZE = 10
ITEM_DESCRIPTIONS = {
    'sword': '[ Sword ]\n\nAn old sword.',
    'key': '[ Key ]\n\nA rusty key which is used\nto open doors.',
    'sneaker': '[ Sneaker ]\n\nShoes that allow you to\nmove faster for a short\nduration.'
}

MONSTERS = {'green_slime'}

# COLORS
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
