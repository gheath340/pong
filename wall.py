import pygame

class Wall:
    
    def __init__(self, x, y, width, height):
        self.mX = x
        self.mY = y
        self.mWidth = width
        self.mHeight = height
        
    def getX(self):
        return self.mX
    
    def getY(self):
        return self.mY
    
    def getWidth(self):
        return self.mWidth
    
    def getHeight(self):
        return self.mHeight
    
    def getRightX(self):
        rightSide = self.mX + self.mWidth
        return rightSide
    
    def getBottomY(self):
        bottom = self.mY + self.mHeight
        return bottom
    
    def draw(self, surface):
        color = (145, 187, 255)
        Rect= pygame.Rect(self.mX, self.mY, self.mWidth, self.mHeight)
        pygame.draw.rect(surface, color, Rect)
            
    
    