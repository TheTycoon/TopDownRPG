# Game Options and Settings

# define colors
WHITE  = (255, 255, 255)
BLACK  = (  0,   0,   0)
GRAY   = (128, 128, 128)
RED    = (255,   0,   0)
ORANGE = (255, 165,   0)
YELLOW = (255, 255,   0)
GREEN  = (  0, 128,   0)
BLUE   = (  0,   0, 255)
PURPLE = (128,   0, 128)
BROWN  = (165,  42,  42)

# game settings
WIDTH = 640
HEIGHT = 640
TILESIZE = 32
FPS = 60
TITLE = 'Top-down RPG'

PLAYER_HEALTH = 100
PLAYER_SPEED = 5
PLAYER_ATTACK_SPEED = 200       # time in milliseconds the players melee attack lasts for

# Controller / Joystick Dictionaries
JOYBUTTONS = {
            'D_Up'        : 0,
            'D_Down'      : 1,
            'D_Left'      : 2,
            'D_Right'     : 3,
            'Start'       : 4,
            'Back'        : 5,
            'LeftStick'   : 6,
            'RightStick'  : 7,
            'LeftBumper'  : 8,
            'RightBumper' : 9,
            'A'           : 11,
            'B'           : 12,
            'X'           : 13,
            'Y'           : 14
           }

JOYAXIS = {
    'LeftHorizontal': 0,
    'LeftVertical'  : 1,
    'LeftTrigger'   : 4,
    'RightTrigger'  : 5
}