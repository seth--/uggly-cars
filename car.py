import random, pygame, sprites, os

masterImage = pygame.image.load(os.path.join('images', "cars.png"))
masterImage.set_colorkey((163, 163, 13), pygame.RLEACCEL)

PLAYER_SPRITE_COORDS = ({"left":126, "top":104, "right":155, "bottom":143},
                        {"left":168, "top":104, "right":191, "bottom":143},
                        {"left":204, "top":104, "right":233, "bottom":143})
PLAYER_SPRITES = sprites.loadSliced(masterImage, PLAYER_SPRITE_COORDS)

OPONENT_SPRITE_COORDS = ({"left":133,   "top":2,    "right":154,    "bottom":29},
                         {"left":168,   "top":64,   "right":191,    "bottom":103},
                         {"left":169,   "top":144,  "right":190,    "bottom":183},
                         {"left":169,   "top":224,  "right":190,    "bottom":263},
                         {"left":167,   "top":304,  "right":192,    "bottom":342},
                         {"left":169,   "top":383,  "right":190,    "bottom":423},
                         {"left":205,   "top":464,  "right":224,    "bottom":511})
OPONENT_SPRITES = sprites.loadSliced(masterImage, OPONENT_SPRITE_COORDS)


class car(object):
    
    def __init__(self, width, height):
        self.mapHeight = height
        self.mapWidth = width
        
    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height
    
    def getPosX(self):        
        return self.posX

    def getPosY(self):
        return self.posY

    def getSpeed(self):
        return self.speed
    
    def getCurrentSprite(self):
        return self.currentSprite
    
    
class playerCar(car):
    
    def __init__(self, width, height):
        super(playerCar, self).__init__(width, height);
        self.posX = width / 2 - 15
        self.posY = height - 80
        self.height = 70
        self.width = 30
        self.currentSprite = 1


    def move(self, key):
        if key == 'left':
            self.posX = self.posX - 5
            self.currentSprite = 0
            
        elif key == 'right':
            self.posX = self.posX +5
            self.currentSprite = 2
        
    def stopMoving(self, key):
        pressedKeys = pygame.key.get_pressed()
        if (pressedKeys[276] == 0 and key == 'left') or (pressedKeys[275] == 0 and key == 'right'):
            self.currentSprite = 1
    
    def getWidth(self):
        return PLAYER_SPRITE_COORDS[self.currentSprite]["right"] - PLAYER_SPRITE_COORDS[self.currentSprite]["left"]

class oponentCar(car):
    
    def __init__(self, width, height, spritesImage, level):
        super(oponentCar, self).__init__(width, height);
        self.height = 70
        self.width = 30
        self.posX = random.randint(0, width - self.width)
        self.posY = 0 - self.height + 100
        self.brakingTime = 0
        self.speed = random.randint(8*level, 5*level+50)
        self.currentSprite = random.randint(0, 6)

    def move(self):
        self.posY = self.posY + (self.mapHeight / (5*(3*self.speed-380)/(-8)))
        
    def getBrakingTime(self):
        return self.brakingTime
    
    def setBrakingTime(self, brakingTime):
        self.brakingTime = brakingTime
            