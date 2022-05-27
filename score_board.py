import pygame
import text
import main

class ScoreBoard:
    
    def __init__(self, x, y, width, height):
        self.mX = x
        self.mY = y
        self.mWidth = width
        self.mHeight = height
        self.mLeftScore = 0
        self.mRightScore = 0
        self.mServeStatus = 1
        
    def getX(self):
        return self.mX
    
    def getY(self):
        return self.mY
    
    def getWidth(self):
        return self.mWidth
    
    def getHeight(self):
        return self.mHeight
    
    def getLeftScore(self):
        return self.mLeftScore
    
    def getRightScore(self):
        return self.mRightScore
    
    def getServeStatus(self):
        return self.mServeStatus
    
    def isGameOver(self):
        if self.mLeftScore == 9 or self.mServeStatus == 3:
            return True
        elif self.mRightScore == 9 or self.mServeStatus ==  4:
            return True
        return False
    
    def scoreLeft(self):
        if self.mLeftScore > 8:
            self.mServeStatus = 3
        else:
            self.mLeftScore += 1
            if self.mLeftScore > 8 and self.mServeStatus != 4:
                self.mServeStatus = 3
            
    def scoreRight(self):
        if self.mRightScore > 8:
            self.mServeStatus = 4
        else:
            self.mRightScore += 1
            if self.mRightScore > 8 and self.mServeStatus != 3:
                self.mServeStatus = 4
            
    def swapServe(self):
        if self.mServeStatus == 3:
            return
        elif self.mServeStatus == 4:
            return
        elif self.mServeStatus == 1:
            self.mServeStatus = 2
        elif self.mServeStatus == 2:
            self.mServeStatus = 1

    def draw(self, surface):
        winX = 400
        winY = 300
        replayX = 400
        replayY = 400
        leftWinString = "Left player won."
        rightWinString = "Right player won."
        replayString = "Would you like to play again(Y) or (N)"
        scoreString = "           " + str(self.mLeftScore) + "                            " + str(self.mRightScore)
        score = text.Text(scoreString, self.mX, self.mY)
        text.Text.draw(score, surface)
        if self.mServeStatus == 3:
            leftWin = text.Text(leftWinString, winX, winY)
            replay = text.Text(replayString, replayX, replayY)
            text.Text.draw(leftWin, surface)
            text.Text.draw(replay, surface)
            for e in pygame.event.get( ):
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_y:
                        main.main()
                    elif e.key == pygame.K_n:
                        pygame.quit()
        elif self.mServeStatus == 4:
            rightWin = text.Text(rightWinString, winX, winY)
            replay = text.Text(replayString, replayX, replayY)
            text.Text.draw(rightWin, surface)
            text.Text.draw(replay, surface)
            for e in pygame.event.get( ):
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_y:
                        main.main()
                    elif e.key == pygame.K_n:
                        pygame.quit()
            
            
            
            
            
            
            
            