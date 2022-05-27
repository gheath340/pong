import pygame
import random


class Ball:
    
    def __init__(self, size, min_x, max_x, min_y, max_y, left_paddle_x, right_paddle_x):
        self.mX = min_x
        self.mY = min_y
        self.mSize = size
        self.mDX = 0
        self.mDY = 0
        self.mMinX = min_x
        self.mMaxX = max_x
        self.mMinY = min_y
        self.mMaxY = max_y
        self.mLeftPaddleX = left_paddle_x
        self.mLeftPaddleMinY = min_y
        self.mLeftPaddleMaxY = max_y
        self.mRightPaddleX = right_paddle_x
        self.mRightPaddleMinY = min_y
        self.mRightPaddleMaxY = max_y
        
        
    def getX(self):
        return self.mX
    
    def getY(self):
        return self.mY
    
    def getSize(self):
        return self.mSize
    
    def getDX(self):
        return self.mDX
    
    def getDY(self):
        return self.mDY
    
    def getMinX(self):
        return self.mMinX
    
    def getMaxX(self):
        return self.mMaxX
    
    def getMinY(self):
        return self.mMinY
    
    def getMaxY(self):
        return self.mMaxY
    
    def getLeftPaddleX(self):
        return self.mLeftPaddleX
    
    def getLeftPaddleMinY(self):
        return self.mLeftPaddleMinY
    
    def getLeftPaddleMaxY(self):
        return self.mLeftPaddleMaxY
    
    def getRightPaddleX(self):
        return self.mRightPaddleX
    
    def getRightPaddleMinY(self):
        return self.mRightPaddleMinY
    
    def getRightPaddleMaxY(self):
        return self.mRightPaddleMaxY
    
    def setPosition(self, x, y):
        maxX = self.mMaxX - self.mSize
        maxY = self.mMaxY - self.mSize
        if x > self.mMinX and x < maxX and y > self.mMinY and y < maxY:
            self.mX = x
            self.mY = y
        
    def setSpeed(self, dx, dy):
        self.mDX = dx
        self.mDY = dy
        
    def setLeftPaddleY(self, paddle_min_y, paddle_max_y):
        if paddle_min_y >= self.mMinY and paddle_max_y <= self.mMaxY:
            if paddle_min_y < paddle_max_y:
                self.mLeftPaddleMinY = paddle_min_y
                self.mLeftPaddleMaxY = paddle_max_y
        
    def setRightPaddleY(self, paddle_min_y, paddle_max_y):
        if paddle_min_y < paddle_max_y:
            if paddle_min_y >= self.mMinY and paddle_max_y <= self.mMaxY:
                self.mRightPaddleMinY = paddle_min_y
                self.mRightPaddleMaxY = paddle_max_y
        
    def checkTop(self, new_y):
        if new_y > self.mMinY:
            return new_y
        else:
            self.mDY = self.mDY * -1
            distance = self.mMinY - new_y
            new_y = self.mMinY + distance
            return new_y
            
        
    def checkBottom(self, new_y):
        maxY = self.mMaxY - self.mSize
        if new_y < maxY:
            return new_y
        else:
            self.mDY = self.mDY * -1
            distance = maxY - new_y
            new_y = maxY + distance
            return new_y
        
    def checkLeft(self, new_x):
        if new_x > self.mMinX:
            return new_x
        else:
            self.mDX = 0
            self.mDY = 0
            new_x = self.mMinX
            return new_x
        
    def checkRight(self, new_x):
        maxX = self.mMaxX - self.mSize
        if new_x < maxX:
            return new_x
        else:
            self.mDX = 0
            self.mDY = 0
            new_x = maxX
            return new_x
        
    def checkLeftPaddle(self, new_x, new_y):
        if new_y > self.mLeftPaddleMinY and new_y < self.mLeftPaddleMaxY:
            if new_x <= self.mLeftPaddleX:
                xDistance = self.mLeftPaddleX - new_x
                new_x = self.mLeftPaddleX + xDistance
                self.mDX = self.mDX * -1
                return new_x
        return new_x
            
    def checkRightPaddle(self, new_x, new_y):
        maxX = self.mRightPaddleX - self.mSize
        rightSide = self.mX + self.mSize
        newRight = new_x + self.mSize
        if new_y > self.mRightPaddleMinY and new_y < self.mRightPaddleMaxY:
            if newRight >= self.mRightPaddleX:
                self.mDX = self.mDX * -1
                xDistance = maxX - new_x
                new_x = maxX + xDistance
                return new_x
        return new_x

    def move(self, dt):
        new_x = self.mX + (self.mDX * dt)
        new_y = self.mY + (self.mDY * dt)
        new_y = self.checkTop(new_y)
        new_y = self.checkBottom(new_y)
        new_x = self.checkLeft(new_x)
        new_x = self.checkRight(new_x)
        new_x = self.checkLeftPaddle(new_x, new_y)
        new_x = self.checkRightPaddle(new_x, new_y)
        self.mX = new_x
        self.mY = new_y
        
    def serveLeft(self, x, min_y, max_y, min_dx, max_dx, min_dy, max_dy):
        self.mX = x
        self.mY = random.uniform(min_y, max_y)
        self.mDX = random.uniform(min_dx, max_dx)
        self.mDY = random.choice([min_dy, max_dy])
        
    def serveRight(self, x, min_y, max_y, min_dx, max_dx, min_dy, max_dy):
        self.mX = x
        self.mY = random.uniform(min_y, max_y)
        self.mDX = random.uniform(-min_dx, -max_dx)
        self.mDY = random.choice([min_dy, max_dy])
        
    def draw(self, surface):
        rect = pygame.Rect(self.mX, self.mY, self.mSize, self.mSize)
        color = (145, 187, 255)
        pygame.draw.rect(surface, color, rect)



    # def checkLeftPaddle(self, new_x, new_y):
    #     midY = (self.mY + new_y) / 2
    #     if midY < self.mLeftPaddleMinY or midY > self.mLeftPaddleMaxY or new_x > self.mLeftPaddleX or self.mX < self.mLeftPaddleX:
    #         return new_x
    #     xDistance = self.mLeftPaddleX - new_x
    #     new_x = self.mLeftPaddleX + xDistance
    #     self.mDX = self.mDX * -1
    #     return new_x
            
    # def checkRightPaddle(self, new_x, new_y):
    #     maxX = self.mRightPaddleX - self.mSize
    #     midY = (self.mY + new_y) / 2
    #     rightSide = self.mX + self.mSize
    #     newRightSide = new_x + self.mSize
    #     if midY < self.mRightPaddleMinY or midY > self.mRightPaddleMaxY or newRightSide < self.mRightPaddleX or rightSide > self.mRightPaddleX:
    #         return new_x
    #     self.mDX = self.mDX * -1
    #     xDistance = maxX - new_x
    #     new_x = maxX + xDistance
    #     return new_x