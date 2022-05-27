import pygame

class Paddle:
    
    def __init__(self, x, y, width, height, speed, min_y, max_y):
        self.mX = x
        self.mY = y
        self.mWidth = width
        self.mHeight = height
        self.mSpeed = speed
        self.mMinY = min_y
        self.mMaxY = max_y
        
    def getX(self):
        return self.mX
    
    def getY(self):
        return self.mY
    
    def getWidth(self):
        return self.mWidth
    
    def getHeight(self):
        return self.mHeight
    
    def getSpeed(self):
        return self.mSpeed
    
    def getMinY(self):
        return self.mMinY
    
    def getMaxY(self):
        return self.mMaxY
    
    def getRightX(self):
        rightSide = self.mX + self.mWidth
        return rightSide
    
    def getBottomY(self):
        bottom = self.mY + self.mHeight
        return bottom
    
    def setPosition(self, y):
        bottom = y + self.mHeight
        if bottom > self.mMaxY or y < self.mMinY:
            return
        else:
            self.mY = y
            
    def moveUp(self, dt):
        new_y = self.mY - (self.mSpeed * dt)
        if new_y <= self.mMinY:
            self.mY = self.mMinY
        else:
            self.mY = new_y
            
    def moveDown(self, dt):
        bottom = self.mY + self.mHeight
        new_bottom = bottom + (self.mSpeed * dt)
        if new_bottom >= self.mMaxY:
            self.mY = self.mMaxY - self.mHeight
        else:
            self.mY = new_bottom - self.mHeight
            
    def draw(self, surface):
        color = (145, 187, 255)
        Rect= pygame.Rect(self.mX, self.mY, self.mWidth, self.mHeight)
        pygame.draw.rect(surface, color, Rect)
            
        
        
        
        
        
        
        
        
        
        
        
        
    
    