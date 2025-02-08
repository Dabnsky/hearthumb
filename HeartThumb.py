import time
import thumby
import math



# TODO: redo this whole thing. You have one giant thing doing everything. You need to split up every event into it's own function
# you need to make this more modular and have each peice work independently.

# ---------------------------------------------
# Elf sprites

# Big 16x16
# 4 frames
bigElfWalkingLeftFrames = bytearray([0,64,64,208,208,240,240,228,200,20,72,4,8,0,0,0,0,0,0,144,217,93,189,254,222,214,9,0,0,0,0,0,
                                    0,16,16,52,116,124,124,185,178,133,82,1,2,0,0,0,0,4,12,28,30,23,15,15,7,21,26,28,12,0,0,0])
                                
bigElfWalkingRightFrames = bytearray([0,0,0,8,4,72,20,200,228,240,240,208,208,64,64,0,0,0,0,0,0,9,214,222,254,189,93,217,144,0,0,0,
                                    0,0,0,2,1,82,133,178,185,124,124,116,52,16,16,0,0,0,0,12,28,26,21,7,15,15,23,30,28,12,4,0])

# 2 frames
bigElfExplodeFrames = bytearray([0,0,240,248,64,88,116,90,84,240,120,248,240,0,0,0,0,0,1,131,222,248,145,33,176,248,242,143,3,0,0,0,
                                0,0,0,240,248,120,248,84,90,116,80,72,248,240,0,0,0,0,0,131,223,254,136,16,161,241,248,142,3,1,0,0])

# 2 frames
bigElfHappyFrames =   bytearray([0,0,0,0,192,176,168,244,232,180,168,192,0,0,0,0,0,12,14,143,222,248,146,34,34,242,248,222,143,14,12,0,
                                128,128,192,192,176,44,170,189,186,173,42,176,192,192,128,128,1,1,25,56,55,46,4,9,9,28,62,55,56,25,1,1])

# Small 8x8
# 4 frames
smallElfWalkingLeftFrames = bytearray([8,8,236,250,244,186,4,0,
                                    36,100,118,61,122,125,34,0])
                                
smallElfWalkingRightFrames = bytearray([0,4,186,244,250,236,8,8,
                                        0,34,125,122,61,118,100,36])

# 2 frames
smallElfExplodeFrames = bytearray([24,60,196,142,196,172,60,24,24,60,236,198,140,196,60,24])

# 2 frames
smallElfHappyFrames = bytearray([48,184,196,142,196,172,184,48,46,124,98,7,34,86,124,46])
# ---------------------------------------------
# Heart sprites

# Big16x16
# 6 frames
bigHeartFrames = bytearray([0,124,254,254,254,252,248,240,248,252,254,254,254,62,0,0,0,0,1,3,7,15,15,31,15,7,7,15,4,0,0,0,
                            0,124,254,254,254,252,248,240,248,252,254,254,254,62,0,0,0,0,1,3,7,15,15,31,15,7,7,7,0,0,0,0,
                            0,124,254,254,254,252,248,240,248,252,254,254,254,62,0,0,0,0,1,3,7,15,15,31,15,7,3,5,0,0,0,0,
                            4,124,255,254,254,252,248,240,248,252,254,254,254,62,0,0,0,0,1,3,7,15,15,31,15,7,3,1,0,0,0,0,
                            0,124,254,254,254,252,248,240,248,252,254,254,254,62,0,0,0,0,1,3,7,15,15,31,15,7,3,5,0,0,0,0,
                            0,124,254,254,254,252,248,240,248,252,254,254,254,62,0,0,0,0,1,3,7,15,15,31,15,7,7,7,0,0,0,0])

# Small 8x8
# 6 frames
smallHeartFrames = bytearray([28,62,126,252,252,126,62,156,
                            28,62,126,252,252,126,190,220,
                            28,62,126,252,252,126,62,28,
                            29,62,126,252,252,126,62,28,
                            28,62,126,252,252,126,62,28])

# ---------------------------------------------
# Grass sprites

# Big  16x16
# partial grass 1 frame
bigPartialGrass = bytearray([16,0,0,68,0,0,0,16,0,1,128,0,8,0,66,0,128,2,16,0,128,4,0,0,32,4,0,0,64,8,0,0])
# full grass 1 frame
bigFullGrass = bytearray([57,16,68,238,69,0,16,56,17,131,193,136,28,74,231,82,194,151,58,144,196,142,4,32,116,174,5,64,232,92,8,128])

# Small 8x8
# partialGrass 1 frame
smallPartialGrass = bytearray([0,8,128,0,0,32,2,0])
# fullGrass 1 frame
smallFullGrass = bytearray([8,156,201,128,32,114,39,2])
# ---------------------------------------------
# Explosion sprites

# Big 16x16
# 7 frames
bigExplosionFrames = bytearray([0,0,0,0,0,128,192,224,192,128,0,0,0,0,0,0,0,0,0,0,0,0,1,3,1,0,0,0,0,0,0,0,0,0,0,0,224,240,240,240,240,240,224,0,0,0,0,0,0,0,0,0,3,7,7,7,7,7,3,0,0,0,0,0,0,0,0,224,240,248,248,248,248,248,240,224,0,0,0,0,0,0,0,3,7,15,15,15,15,15,7,3,0,0,0,0,0,0,224,240,248,252,252,252,252,252,248,240,224,0,0,0,0,0,3,7,15,31,31,31,31,31,15,7,3,0,0,0,0,0,0,224,240,248,248,248,248,248,240,224,0,0,0,0,0,0,0,3,7,15,15,15,15,15,7,3,0,0,0,0,0,0,0,0,224,240,240,240,240,240,224,0,0,0,0,0,0,0,0,0,3,7,7,7,7,7,3,0,0,0,0,0,0,0,0,0,0,128,192,224,192,128,0,0,0,0,0,0,0,0,0,0,0,0,1,3,1,0,0,0,0,0,0,0])

# Small 8x8
# 7 frames
smallExplosionFrames = bytearray([0,0,0,24,24,0,0,0,
                                0,0,24,60,60,24,0,0,
                                0,24,60,126,126,60,24,0,
                                24,60,126,255,255,126,60,24,
                                0,24,60,126,126,60,24,0,
                                0,0,24,60,60,24,0,0,
                                0,0,0,24,24,0,0,0])
# ---------------------------------------------
# Ball sprites

# big 16x16
# 1 frames
bigBall = bytearray([0,32,120,252,254,254,254,126,62,30,14,132,192,224,224,0,0,6,28,56,57,121,120,120,124,126,127,63,63,31,7,0])

# small 8x8
# 1 frames
smallBall = bytearray([100,78,206,206,196,224,112,56])
# ---------------------------------------------
# Door sprites
# Big 16x16
# 4 frames
bigDoorFrames = bytearray([192,240,248,244,250,253,255,1,255,255,254,252,248,240,224,0,227,255,127,127,125,125,127,0,127,127,125,125,127,127,255,192,192,48,136,228,242,249,111,111,111,111,254,252,248,240,224,0,227,128,255,125,125,127,0,0,2,6,127,125,125,255,255,224,192,16,136,228,106,109,111,111,111,111,110,108,248,240,224,0,225,128,253,127,126,56,0,0,2,6,14,30,127,253,255,224,192,112,120,100,106,109,111,111,111,111,110,108,104,112,96,0,227,254,254,126,126,56,0,0,2,6,14,30,62,190,254,224])

# Small 8x8
# 4 frames
smallDoorFrames = bytearray([252,254,223,1,255,223,252,0,252,254,223,15,15,223,252,0,252,254,47,15,15,47,252,0,252,110,47,15,15,47,108,0])
# ---------------------------------------------
# Baloon Frames

# big 16x16
# 4 frames
bigBaloonFrames = bytearray([120,252,254,254,255,255,255,255,255,255,254,254,124,0,0,0,0,1,3,7,7,15,175,71,7,3,3,1,0,0,0,0,0,120,252,254,254,255,255,255,255,255,255,254,254,124,0,0,0,0,1,3,7,7,15,79,167,7,3,3,1,0,0,0,0,0,120,252,254,254,255,255,255,255,255,255,254,254,124,0,0,0,0,1,3,7,7,15,175,71,7,3,3,1,0,0,0,120,252,254,254,255,255,255,255,255,255,254,254,124,0,0,0,0,1,3,7,7,15,79,167,7,3,3,1,0,0,0])

# small 8x8
# 4 frames
smallBaloonFrames = bytearray([14,31,63,127,191,31,7,2,
                            0,30,63,127,191,31,14,0,
                            2,7,31,191,127,63,31,14,
                            0,30,63,127,191,31,6,0])
# BITMAP: width: 8, height: 8
# BITMAP: width: 8, height: 8
bitmap6 = bytearray([0,30,63,127,191,31,6,0])
# ---------------------------------------------
# Granade sprites

# big 16x16
# 2 frames
bigGranadeFrames = bytearray([0,224,80,176,81,233,83,187,83,233,81,179,82,64,0,0,0,14,21,59,85,110,85,59,85,110,21,27,5,6,0,0,0,0,2,1,0,200,224,224,224,200,0,0,66,4,0,0,0,2,1,0,0,1,3,3,11,17,0,0,0,8,0,0])

# small 8x8
#2 frames
smallGranadeFrames = bytearray([0,40,85,43,87,43,21,1,
                                2,72,0,153,24,128,2,40])
# ---------------------------------------------
# TODO: redo metal wall to be more distinct from small grenade
# metal wall

# big 16x16
# 16x16 for 1 frames
bigMetalWall = bytearray([255,231,113,57,13,143,199,227,121,29,7,143,195,241,121,0,127,56,28,14,71,99,97,56,28,78,103,107,33,24,12,0])


# small 8x8
# 8x8 for 1 frames
smallMetalWall = bytearray([127,1,37,1,1,37,0,0])

# ---------------------------------------------
# brick wall

# big 16x16
# 16x16 for 1 frames
bigBrickWall = bytearray([7,7,7,7,7,7,3,0,127,127,63,7,7,7,7,7,127,127,63,7,7,7,7,7,7,7,7,7,7,7,3,0])

# small 8x8
# 8x8 for 1 frames
smallBrickWall = bytearray([115,51,49,48,55,51,19,3])

# ---------------------------------------------
# travelator sprites

# big 16x16

# Left
# 8 frames

#first 4 frames are normal. last 4 frames are bump animation for travel
bigLeftTravelatorFrames = bytearray([191,129,1,9,129,129,1,1,129,129,1,9,129,129,1,0,127,2,2,11,3,2,2,3,3,2,2,11,3,2,2,1,
                                    191,1,1,137,129,1,1,129,129,1,1,137,129,1,1,128,126,2,3,11,2,2,3,3,2,2,3,11,2,2,3,1,
                                    63,1,129,137,1,1,129,129,1,1,129,137,1,1,129,128,126,3,3,10,2,3,3,2,2,3,3,10,2,3,3,0,
                                    63,129,129,9,1,129,129,1,1,129,129,9,1,129,129,0,127,3,2,10,3,3,2,2,3,3,2,10,3,3,2,0,
                                    
                                    223,65,1,133,193,65,1,129,193,65,1,133,193,65,1,128,191,129,129,133,129,129,129,129,129,129,129,133,129,129,129,128,
                                    95,1,129,197,65,1,129,193,65,1,129,197,65,1,129,192,191,129,129,133,129,129,129,129,129,129,129,133,129,129,129,128,
                                    31,129,193,69,1,129,193,65,1,129,193,69,1,129,193,64,191,129,129,133,129,129,129,129,129,129,129,133,129,129,129,128,
                                    159,193,65,5,129,193,65,1,129,193,65,5,129,193,65,0,191,129,129,133,129,129,129,129,129,129,129,133,129,129,129,128])

# Right
# 8 frames
bigRightTravelatorFrames = bytearray([63,1,129,137,1,1,129,129,1,1,129,137,1,1,129,128,127,2,2,11,3,2,2,3,3,2,2,11,3,2,2,1,191,1,1,137,129,1,1,129,129,1,1,137,129,1,1,128,127,3,2,10,3,3,2,2,3,3,2,10,3,3,2,0,191,129,1,9,129,129,1,1,129,129,1,9,129,129,1,0,126,3,3,10,2,3,3,2,2,3,3,10,2,3,3,0,63,129,129,9,1,129,129,1,1,129,129,9,1,129,129,0,126,2,3,11,2,2,3,3,2,2,3,11,2,2,3,1,159,1,65,197,129,1,65,193,129,1,65,197,129,1,65,192,191,129,129,133,129,129,129,129,129,129,129,133,129,129,129,128,223,129,1,69,193,129,1,65,193,129,1,69,193,129,1,64,191,129,129,133,129,129,129,129,129,129,129,133,129,129,129,128,95,193,129,5,65,193,129,1,65,193,129,5,65,193,129,0,191,129,129,133,129,129,129,129,129,129,129,133,129,129,129,128,31,65,193,133,1,65,193,129,1,65,193,133,1,65,193,128,191,129,129,133,129,129,129,129,129,129,129,133,129,129,129,128])


# small 8x8
#
# Left 
# 8 frames
smallLeftTravelatorFrames = bytearray([115,57,41,33,49,57,41,0,123,41,33,49,57,41,33,16,107,33,49,57,41,33,49,24,99,49,57,41,33,49,57,8,179,153,153,145,145,153,153,128,187,153,145,145,153,153,145,128,187,145,145,153,153,145,145,136,179,145,153,153,145,145,153,136])

# Right
# 8x8 for 8 frames
smallRightTravelatorFrames = bytearray([99,41,57,49,33,41,57,16,115,33,41,57,49,33,41,24,123,49,33,41,57,49,33,8,107,57,49,33,41,57,49,0,179,153,153,145,145,153,153,128,179,145,153,153,145,145,153,136,187,145,145,153,153,145,145,136,187,153,145,145,153,153,145,128])

# ---------------------------------------------
# empty
# small 8x8
# 1 frames
emptyFrame = bytearray([0,0,0,0,0,0,0,0])

TILE_EMPTY = 0
TILE_GRASS = 1
TILE_ROCK = 2
TILE_HEART = 3  
TILE_WALL = 4
TILE_METAL = 5
TILE_GRENADE = 6
TILE_PLASMA = 7

TILE_BALLOON = 12
TILE_DOOR = 32
TILE_DWARF = 40
TILE_EXPLOSION = 48



# Make a sprite object using bytearray (a path to binary file from 'IMPORT SPRITE' is also valid)
smallElfSpriteLeft = thumby.Sprite(8, 8, smallElfWalkingLeftFrames)
smallElfSpriteRight = thumby.Sprite(8, 8, smallElfWalkingRightFrames)
smallPartialGrassSprite = thumby.Sprite(8, 8, smallPartialGrass)
emptyFrameSprite = thumby.Sprite(8, 8, emptyFrame)
smallBallSprite = thumby.Sprite(8, 8, smallBall)
smallHeartSprite = thumby.Sprite(8, 8, smallHeartFrames)
smallMetalWallSprite = thumby.Sprite(8, 8, smallMetalWall)
smallExplosionSprite = thumby.Sprite(8, 8, smallExplosionFrames)
smallGranadeSprite = thumby.Sprite(8, 8, smallGranadeFrames)
smallBrickWallSprite = thumby.Sprite(8, 8, smallBrickWall)
smallBalloonSprite = thumby.Sprite(8, 8, smallBaloonFrames)


class TileInfo:
    def __init__(self, spriteNum, falling, pushable):
        self.sprite = spriteNum
        self.falling = falling
        self.pushable = pushable

class SpriteInfo:
    def __init__(self, sprite, coordinates):
        self.sprite = sprite
        self.coordinates = coordinates

# TODO: make elements objects instead of numbers to reference with a key. objects will have sprite, and variables like, falling?
level = [[TileInfo(0, False,False), TileInfo(2, False, True), TileInfo(1, False, False), TileInfo(1, False, False), TileInfo(1, False, False), TileInfo(1, False, False), TileInfo(1, False, False), TileInfo(6, False, True), TileInfo(1, False, False)],
         [TileInfo(2, False, False), TileInfo(1, False, False), TileInfo(40, False, False), TileInfo(1, False, False), TileInfo(3, False, False), TileInfo(2, False, True), TileInfo(1, False, False), TileInfo(1, False, False), TileInfo(1, False, False)],
         [TileInfo(1, False, True), TileInfo(1, False, False), TileInfo(1, False, False), TileInfo(6, False, True), TileInfo(1, False, False), TileInfo(1, False, False), TileInfo(1, False, False), TileInfo(1, False, False), TileInfo(1, False, False)],
         [TileInfo(0, False, False), TileInfo(12, False, True), TileInfo(1, False, False), TileInfo(1, False, False), TileInfo(1, False, False), TileInfo(3, False, False), TileInfo(4, False, False), TileInfo(1, False, False), TileInfo(5, False, False)],
         [TileInfo(1, False, False), TileInfo(0, False, False), TileInfo(1, False, False), TileInfo(1, False, False), TileInfo(1, False, False), TileInfo(1, False, False), TileInfo(1, False, False), TileInfo(2, False, True), TileInfo(1, False, False)]]


def restart():
    level = [[TileInfo(1, False, False), TileInfo(1, False, False), TileInfo(1, False, False), TileInfo(1, False, False), TileInfo(1, False, False), TileInfo(1, False, False), TileInfo(1, False, False), TileInfo(1, False, False), TileInfo(1, False, False)],
         [TileInfo(1, False, False), TileInfo(40, False), TileInfo(1, False, False), TileInfo(2, False, True), TileInfo(3, False, True), TileInfo(2, False, True), TileInfo(1, False, False), TileInfo(1, False, False), TileInfo(1, False, False)],
         [TileInfo(1, False, False), TileInfo(1, False, False), TileInfo(1, False, False), TileInfo(1, False, False), TileInfo(1, False, False), TileInfo(1, False, False), TileInfo(1, False, False), TileInfo(1, False, False), TileInfo(1, False, False)],
         [TileInfo(1, False, False), TileInfo(1, False, False), TileInfo(1, False, False), TileInfo(1, False, False), TileInfo(1, False, False), TileInfo(1, False, False), TileInfo(1, False, False), TileInfo(1, False, False), TileInfo(1, False, False)],
         [TileInfo(1, False, False), TileInfo(1, False, False), TileInfo(1, False, False), TileInfo(1, False, False), TileInfo(1, False, False), TileInfo(1, False, False), TileInfo(1, False, False), TileInfo(1, False, False), TileInfo(1, False, False)]]

    return level
# Set the FPS (without this call, the default fps is 30)
thumby.display.setFPS(15)

lastDir = ""
started  = False
dead = False

spriteRate = 0 
heartCount = 0

ABOVE = level[i-1][j]
BELOW = level[i+1][j]
LEFT_OF = level[i][j-1]
RIGHT_OF = level[i][j+1]

while(1):
    
    smallElfSpriteRight.setFrame(smallElfSpriteRight.currentFrame*0)
    smallElfSpriteLeft.setFrame(smallElfSpriteLeft.currentFrame*0)
    #this is used to slow down sprite animation. 
    spriteRate = (spriteRate + 1) % 4
    
    t0 = time.ticks_ms()   # Get time (ms)
    thumby.display.fill(0) # Fill canvas to black
    if started == False:
        positionX = 0
        positionY = 0
        started = True
        dead = False


    #---------------------------------------------
    # DIRECTION MOVEMENT
    # Left


    if (thumby.buttonL.pressed() == True and positionX >= 0 ):

        if (level[int(positionY / 8)][int(positionX / 8) - 1].sprite == TILE_METAL) or (level[int(positionY / 8)][int(positionX / 8) - 1].sprite == TILE_WALL):
            continue
        
        #moving one object left
        elif int(positionX / 8) > 1 and level[int(positionY / 8)][int(positionX / 8) - 1].pushable and level[int(positionY / 8)][int(positionX / 8) - 2].sprite == TILE_EMPTY:
            #move rock
            if level[int(positionY / 8)][int(positionX / 8) - 1].sprite == TILE_ROCK:
                level[int(positionY / 8)][int(positionX / 8) - 2].sprite = TILE_ROCK
                level[int(positionY / 8)][int(positionX / 8) - 2].falling = False
                level[int(positionY / 8)][int(positionX / 8) - 2].pushable = True
                
                level[int(positionY / 8)][int(positionX / 8) - 1].sprite = TILE_DWARF
                level[int(positionY / 8)][int(positionX / 8) - 1].falling = False
                level[int(positionY / 8)][int(positionX / 8) - 1].pushable = False
                
                
                level[int(positionY / 8)][int(positionX / 8)].sprite = TILE_EMPTY
                level[int(positionY / 8)][int(positionX / 8)].falling = False
                level[int(positionY / 8)][int(positionX / 8)].pushable = False
            
                positionX -= 8
                if positionX <= 0:
                    positionX = 0

            #move bomb
            if level[int(positionY / 8)][int(positionX / 8) - 1].sprite == TILE_GRENADE:
                level[int(positionY / 8)][int(positionX / 8) - 2].sprite = TILE_GRENADE
                level[int(positionY / 8)][int(positionX / 8) - 2].falling = False
                level[int(positionY / 8)][int(positionX / 8) - 2].pushable = True
                
                level[int(positionY / 8)][int(positionX / 8) - 1].sprite = TILE_DWARF
                level[int(positionY / 8)][int(positionX / 8) - 1].falling = False
                level[int(positionY / 8)][int(positionX / 8) - 1].pushable = False
                
                level[int(positionY / 8)][int(positionX / 8)].sprite = TILE_EMPTY
                level[int(positionY / 8)][int(positionX / 8)].falling = False
                level[int(positionY / 8)][int(positionX / 8)].pushable = False
            
                positionX -= 8
                if positionX <= 0:
                    positionX = 0

            #move balloon
            if level[int(positionY / 8)][int(positionX / 8) - 1].sprite == TILE_GRASS:
                level[int(positionY / 8)][int(positionX / 8) - 2].sprite = TILE_BALLOON
                level[int(positionY / 8)][int(positionX / 8) - 2].falling = False
                level[int(positionY / 8)][int(positionX / 8) - 2].pushable = True
                
                level[int(positionY / 8)][int(positionX / 8) - 1].sprite = TILE_DWARF
                level[int(positionY / 8)][int(positionX / 8) - 1].falling = False
                level[int(positionY / 8)][int(positionX / 8) - 1].pushable = False
                
                level[int(positionY / 8)][int(positionX / 8)].sprite = TILE_EMPTY
                level[int(positionY / 8)][int(positionX / 8)].falling = False
                level[int(positionY / 8)][int(positionX / 8)].pushable = False
            
                positionX -= 8
                if positionX <= 0:
                    positionX = 0

    
                
        elif level[int(positionY / 8)][int(positionX / 8)-1].sprite == TILE_EMPTY or level[int(positionY / 8)][int(positionX / 8)-1].sprite == TILE_GRASS or level[int(positionY / 8)][int(positionX / 8)-1].sprite == TILE_HEART:
            level[int(positionY / 8)][int(positionX / 8)].sprite = TILE_EMPTY
            positionX -= 8
            if positionX <= 0:
                positionX = 0
            
            level[int(positionY / 8)][int(positionX / 8)].sprite = TILE_DWARF
        lastDir = "left"
        #TODO: move rock left  if rock has empty on other side of rock.

    # Right
    if (thumby.buttonR.pressed() == True and positionX < 64 ):

        if (level[int(positionY / 8)][int(positionX / 8) + 1].sprite == TILE_METAL) or (level[int(positionY / 8)][int(positionX / 8) + 1].sprite == TILE_WALL):
            continue

        elif int(positionX / 8) < 7 and level[int(positionY / 8)][int(positionX / 8) + 1].pushable and level[int(positionY / 8)][int(positionX / 8) + 2].sprite == TILE_EMPTY:
            if level[int(positionY / 8)][int(positionX / 8) + 1].sprite == TILE_ROCK:
                level[int(positionY / 8)][int(positionX / 8) + 2].sprite = TILE_ROCK
                level[int(positionY / 8)][int(positionX / 8) + 2].falling = False
                level[int(positionY / 8)][int(positionX / 8) + 2].pushable = True
                
                level[int(positionY / 8)][int(positionX / 8) + 1].sprite = TILE_DWARF
                level[int(positionY / 8)][int(positionX / 8) + 1].falling = False
                level[int(positionY / 8)][int(positionX / 8) + 1].pushable = False
                
                
                level[int(positionY / 8)][int(positionX / 8)].sprite = TILE_EMPTY
                level[int(positionY / 8)][int(positionX / 8)].falling = False
                level[int(positionY / 8)][int(positionX / 8)].pushable = False
            
                positionX -= 8
                if positionX <= 0:
                    positionX = 0


            if level[int(positionY / 8)][int(positionX / 8) + 1].sprite == TILE_GRENADE:
                level[int(positionY / 8)][int(positionX / 8) + 2].sprite = TILE_GRENADE
                level[int(positionY / 8)][int(positionX / 8) + 2].falling = False
                level[int(positionY / 8)][int(positionX / 8) + 2].pushable = True
                
                level[int(positionY / 8)][int(positionX / 8) + 1].sprite = TILE_DWARF
                level[int(positionY / 8)][int(positionX / 8) + 1].falling = False
                level[int(positionY / 8)][int(positionX / 8) + 1].pushable = False
                
                level[int(positionY / 8)][int(positionX / 8)].sprite = TILE_EMPTY
                level[int(positionY / 8)][int(positionX / 8)].falling = False
                level[int(positionY / 8)][int(positionX / 8)].pushable = False
            
                positionX -= 8
                if positionX <= 0:
                    positionX = 0


            if level[int(positionY / 8)][int(positionX / 8) + 1].sprite == TILE_GRASS2:
                level[int(positionY / 8)][int(positionX / 8) + 2].sprite = TILE_BALLOON
                level[int(positionY / 8)][int(positionX / 8) + 2].falling = False
                level[int(positionY / 8)][int(positionX / 8) + 2].pushable = True
                
                level[int(positionY / 8)][int(positionX / 8) + 1].sprite = TILE_DWARF
                level[int(positionY / 8)][int(positionX / 8) + 1].falling = False
                level[int(positionY / 8)][int(positionX / 8) + 1].pushable = False
                
                level[int(positionY / 8)][int(positionX / 8)].sprite = TILE_EMPTY
                level[int(positionY / 8)][int(positionX / 8)].falling = False
                level[int(positionY / 8)][int(positionX / 8)].pushable = False
            
                positionX -= 8
                if positionX <= 0:
                    positionX = 0

            
            

        elif level[int(positionY / 8)][int(positionX / 8)+1].sprite == TILE_EMPTY or level[int(positionY / 8)][int(positionX / 8)+1].sprite == TILE_GRASS or level[int(positionY / 8)][int(positionX / 8)+1].sprite == TILE_HEART:
            level[int(positionY / 8)][int(positionX / 8)].sprite = TILE_EMPTY
            positionX += 8
            if positionX >= 64:
                positionX = 64
            
            level[int(positionY / 8)][int(positionX / 8)].sprite = TILE_DWARF
        lastDir = "right"


        #TODO: move rock right if rock has empty on other side of rock.
    # Up
    if (thumby.buttonU.pressed() == True and positionY > 0 ):
        if level[int(positionY / 8 - 1)][int(positionX / 8)].pushable or level[int(positionY / 8 - 1)][int(positionX / 8)].sprite == TILE_WALL or level[int(positionY / 8 - 1)][int(positionX / 8)].sprite == TILE_METAL or level[int(positionY / 8 - 1)][int(positionX / 8)].sprite == TILE_GRENADE or level[int(positionY / 8 - 1)][int(positionX / 8)].sprite == TILE_GRASS2:
            continue
        if (thumby.buttonR.pressed() or thumby.buttonL.pressed()):
            continue

        level[int(positionY / 8)][int(positionX / 8)].sprite = TILE_EMPTY
        positionY -= 8
        if positionY <= 0:
            positionY = 0

        smallElfSpriteRight.x = positionX
        smallElfSpriteRight.y = positionY
        level[int(positionY / 8)][int(positionX / 8)].sprite = TILE_DWARF

    # Down
    if (thumby.buttonD.pressed() == True and positionY < 32 ):
        print("level[y]:", positionY / 8 + 1 )
        if level[int(positionY / 8 + 1)][int(positionX / 8)].pushable or level[int(positionY / 8 + 1)][int(positionX / 8)].sprite == TILE_WALL or level[int(positionY / 8 + 1)][int(positionX / 8)].sprite == TILE_METAL or level[int(positionY / 8 + 1)][int(positionX / 8)].sprite == TILE_GRENADE or level[int(positionY / 8 + 1)][int(positionX / 8)].sprite == TILE_GRASS2:
            continue
        if (thumby.buttonR.pressed() or thumby.buttonL.pressed()):
            continue
        level[int(positionY / 8)][int(positionX / 8)].sprite = TILE_EMPTY
        positionY += 8
        if positionY > 32:
            positionY = 32
        
        smallElfSpriteRight.x = positionX
        smallElfSpriteRight.y = positionY
        level[int(positionY / 8)][int(positionX / 8)].sprite = TILE_DWARF




    # DISPLAY SPRITES & UPDATE SCREEN    
    #TODO: set function for each event taking place on grid. eg. falling items, explosions etc.
    
    for i in range(5): 
        for j in range(9):
            if level[i][j].sprite == TILE_EMPTY:
                sprite = emptyFrameSprite
                spriteObj = SpriteInfo(TILE_EMPTY, [i, j])
            if level[i][j].sprite == TILE_GRASS:
                sprite = smallPartialGrassSprite
                spriteObj = SpriteInfo(TILE_GRASS, [i, j])
                
            if level[i][j].sprite == TILE_GRENADE:
                sprite = smallGranadeSprite
                spriteObj = SpriteInfo(6, [i, j])
                
                if i < 4:
                    if level[i+1][j].sprite == TILE_EMPTY: 
                        level[i][j].sprite = TILE_EMPTY
                        level[i][j].falling = False
                        level[i][j].pushable = False
                        
                        level[i+1][j].sprite = TILE_GRENADE
                        level[i+1][j].falling = True
                        level[i+1][j].pushable = True
                        
                        if dead:
                            level = restart()       
                            dead = False
                    #bomb fall left
                    elif level[i][j-1].sprite == TILE_EMPTY:
                        if level[i+1][j].sprite != 1 and level[i+1][j].sprite != 40  and level[i+1][j-1].sprite == TILE_EMPTY:
                            level[i][j].sprite = TILE_EMPTY
                            level[i][j].falling = False
                            level[i][j].pushable = False
                            
                            level[i][j-1].sprite = TILE_GRENADE
                            level[i][j-1].falling = True
                            level[i][j-1].pushable = True
                        
                            
                            
                    #bomb fall right
                    elif level[i][j+1].sprite == TILE_EMPTY:
                        if level[i+1][j].sprite != 1 and level[i+1][j].sprite != 40 and level[i+1][j+1].sprite == TILE_EMPTY:
                            level[i][j].sprite = TILE_EMPTY
                            level[i][j].falling = False
                            level[i][j].pushable = False

                            level[i][j+1].sprite = TILE_GRENADE
                            level[i][j+1].falling = True
                            level[i][j+1].pushable = True
                        

                    elif level[i][j].falling == True:
                        if level[i+1][j].sprite != TILE_GRASS:
                            level[i][j].sprite = TILE_EXPLOSION
                            level[i][j].falling = False
                            
                            if level[i+1][j].sprite != 5: 
                                level[i+1][j].sprite = TILE_EXPLOSION
                            if level[i-1][j].sprite != 5: 
                                level[i-1][j].sprite = TILE_EXPLOSION
                            if level[i][j+1].sprite != 5: 
                                level[i][j+1].sprite = TILE_EXPLOSION 
                            if level[i][j-1].sprite != 5: 
                                level[i][j-1].sprite = TILE_EXPLOSION
                        

                    if level[i-1][j].falling:
                        if level[i+1][j].sprite != 5: 
                            level[i+1][j].sprite = TILE_EXPLOSION
                        if level[i-1][j].sprite != 5: 
                            level[i-1][j].sprite = TILE_EXPLOSION
                        if level[i][j+1].sprite != 5: 
                            level[i][j+1].sprite = TILE_EXPLOSION 
                        if level[i][j-1].sprite != 5: 
                            level[i][j-1].sprite = TILE_EXPLOSION
                            
                    if level[i+1][j].sprite == TILE_GRASS:
                        level[i][j].falling = False
    
            if level[i][j].sprite == TILE_ROCK:
                sprite = smallBallSprite
                spriteObj = SpriteInfo(TILE_ROCK, [i, j])
                
                #stay in screen height range
                if i < 4 and spriteRate == 3: 
                    #if empty below rock, rock falls
                    if level[i+1][j].sprite == TILE_EMPTY: 
                        level[i][j].sprite = TILE_EMPTY
                        level[i][j].falling = False
                        level[i][j].pushable = False
                        
                        level[i+1][j].sprite = TILE_ROCK
                        level[i+1][j].falling = True
                        level[i+1][j].pushable = True
                        if dead:
                            level = restart()       
                            dead = False
                        
                    if level[i][j].falling == True and level[i+1][j].sprite == TILE_WALL0:
                        level[i+1][j].sprite = TILE_EXPLOSION
                        #dead is true
                        
                    if level[i+1][j].sprite != 6 or level[i+1][j].sprite != 0:
                        level[i][j].falling = False
                        
                    #rock fall left
                    elif level[i][j-1].sprite == TILE_EMPTY and level[i+1][j-1].sprite == TILE_EMPTY:
                        if  level[i+1][j].sprite == TILE_ROCK  or level[i+1][j].sprite == TILE_HEART or level[i+1][j].sprite == TILE_GRENADE:
                            level[i][j].sprite = TILE_EMPTY
                            level[i][j].falling = False
                            level[i][j].pushable = False
                            
                            level[i][j-1].sprite = TILE_ROCK
                            level[i][j-1].falling = True
                            level[i][j-1].pushable = True
                        
                    #rock fall right
                    elif level[i][j+1].sprite == TILE_EMPTY and level[i+1][j+1].sprite == TILE_EMPTY:
                        if level[i+1][j].sprite == TILE_ROCK or level[i+1][j].sprite == TILE_HEART or level[i+1][j].sprite == TILE_GRENADE:
                            level[i][j].sprite = TILE_EMPTY
                            level[i][j].falling = False
                            level[i][j].pushable = False
                            
                            level[i][j+1].sprite = TILE_ROCK
                            level[i][j+1].falling = True
                            level[i][j+1].pushable = True
                            
                
                        
                   
            if level[i][j].sprite == TILE_HEART:
                sprite = smallHeartSprite
                spriteObj = SpriteInfo(3, [i, j])
                #if empty below heart, heart falls
                if i < 4 and spriteRate == 3: 
                    #if empty below rock, rock falls
                    if level[i+1][j].sprite == TILE_EMPTY: 
                        level[i][j].sprite = TILE_EMPTY
                        level[i][j].falling = False
                        level[i][j].pushable = False
                        
                        level[i+1][j].sprite = TILE_HEART
                        level[i+1][j].falling = True
                        level[i+1][j].pushable = False
                        
                        if dead:
                            level = restart()       
                            dead = False
                    #heart fall left
                    elif level[i][j-1].sprite == TILE_EMPTY and level[i+1][j-1].sprite == TILE_EMPTY:
                        if  level[i+1][j].sprite == TILE_ROCK  or level[i+1][j].sprite == TILE_HEART or level[i+1][j].sprite == TILE_GRENADE:
                            level[i][j].sprite = TILE_EMPTY
                            level[i][j].falling = False
                            level[i][j].pushable = False
                            
                            level[i][j-1].sprite = TILE_HEART
                            level[i][j-1].falling = True
                            level[i][j-1].pushable = False
                        
                    #heart fall right
                    elif level[i][j+1].sprite == TILE_EMPTY and level[i+1][j+1].sprite == TILE_EMPTY:
                        if level[i+1][j].sprite == TILE_ROCK or level[i+1][j].sprite == TILE_HEART or level[i+1][j].sprite == TILE_GRENADE:
                            level[i][j].sprite = TILE_EMPTY
                            level[i][j].falling = False
                            level[i][j].pushable = False
                            
                            level[i][j+1].sprite = TILE_HEART
                            level[i][j+1].falling = True
                            level[i][j+1].pushable = False
                            
                
                    if level[i][j].falling == True and level[i+1][j].sprite == TILE_WALL0:
                        level[i+1][j].sprite = TILE_EXPLOSION
                        
                    if level[i+1][j].sprite != 0:
                        level[i][j].falling = False


                        
            if level[i][j].sprite == TILE_WALL:
                sprite = smallBrickWallSprite
                spriteObj = SpriteInfo(4, [i, j])
                
            if level[i][j].sprite == TILE_METAL:
                sprite = smallMetalWallSprite
                spriteObj = SpriteInfo(5, [i, j])  
            

            #balloon
            if level[i][j].sprite == TILE_GRASS2:
                sprite = smallBalloonSprite
                if i > 0 and i <= 4:

                    #only one object on balloon. object and balloon both float up
                    
                    if i > 1 and level[i-1][j].pushable and level[i-2][j].sprite == TILE_EMPTY:
                    
                        level[i-2][j] = level[i-1][j]
                        level[i-1][j] = level[i][j]
                        level[i][j] =  TileInfo(0, False, False)
                        
                        
                    #at least 2 objects on balloon? balloon falls
                    elif i > 1 and i < 4 and level[i-1][j].pushable and level[i-2][j].pushable and level[i+1][j].sprite == TILE_EMPTY:
                        print("inside two object on balloon condition")
                        
                        level[i+1][j] = level[i][j]
                        level[i][j] =  level[i-1][j]
                        level[i-1][j] = level[i-2][j]
                        level[i-2][j] = TileInfo(0, False, False)
        
                    
                    #float up with no objects above
                    elif level[i-1][j].sprite == TILE_EMPTY:
                        level[i][j].sprite = TILE_EMPTY
                        level[i][j].falling = False
                        level[i][j].pushable = False
                        
                        level[i-1][j].sprite = TILE_BALLOON
                        level[i-1][j].falling = False
                        level[i-1][j].pushable = True
                        
                        
                
                
            if level[i][j].sprite == TILE_WALL0:
                if (lastDir == "right" or lastDir == ""):
                    sprite = smallElfSpriteRight
                    spriteObj = SpriteInfo(TILE_DWARF, [i, j])
                    positionX = j*8
                    positionY = i*8
                if lastDir == "left":
                    spriteObj = SpriteInfo(TILE_DWARF, [i, j])
                    sprite = smallElfSpriteLeft
                    positionX = j*8
                    positionY = i*8
            if level[i][j].sprite == TILE_WALL:
                sprite = smallExplosionSprite
                spriteObj = SpriteInfo(48, [i, j])

            # Draw the sprite at its x and y coordinates
            
            sprite.x = j*8
            sprite.y = i*8
            spriteObj.coordinates[0] = i
            spriteObj.coordinates[1] = j
            
            #walking animation
            if (sprite == smallElfSpriteRight and thumby.buttonR.justPressed()) or (sprite == smallElfSpriteRight and thumby.buttonU.justPressed()) or (sprite == smallElfSpriteRight and thumby.buttonD.justPressed()):
                smallElfSpriteRight.setFrame(smallElfSpriteRight.currentFrame+1)

            if sprite == smallElfSpriteLeft and thumby.buttonL.justPressed()  or (sprite == smallElfSpriteLeft and thumby.buttonU.justPressed()) or (sprite == smallElfSpriteLeft and thumby.buttonD.justPressed()):
                smallElfSpriteLeft.setFrame(smallElfSpriteLeft.currentFrame+1)
            
            #explosion animation
            if sprite == smallExplosionSprite:
                smallExplosionSprite.setFrame(smallExplosionSprite.currentFrame+1)

                if smallExplosionSprite.currentFrame == 5:
                    level[i][j].sprite = TILE_EMPTY
                    level[i][j].falling = False
                    #dead = True
                
            
            if sprite == smallHeartSprite and spriteRate == 2:
                smallHeartSprite.setFrame(smallHeartSprite.currentFrame+1)
                
            if sprite == smallBalloonSprite and spriteRate == 2:
                smallBalloonSprite.setFrame(smallBalloonSprite.currentFrame+1)
             
            thumby.display.drawSprite(sprite)
            
    smallElfSpriteRight.setFrame(smallElfSpriteRight.currentFrame*0)
    smallElfSpriteLeft.setFrame(smallElfSpriteLeft.currentFrame*0)
    

    
    
    thumby.display.update()
