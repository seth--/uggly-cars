import pygame, os

def loadSliced(image, coords):
    sprites = []
    for i in coords:
        iWidth =  i["right"] - i["left"]
        iHeight = i["bottom"] - i["top"]
        sprites.append(pygame.transform.scale(image.subsurface(i["left"], i["top"], iWidth, iHeight), (iWidth * 2, iHeight * 2)))
    return sprites
