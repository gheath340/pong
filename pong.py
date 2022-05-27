import pygame
import ball, wall, paddle, score_board, ai
import homeScreen
import text
import random

LEFT = 1
RIGHT = 2
LEFT_WIN = 3
RIGHT_WIN = 4

class Pong:

    def __init__( self, width, height ):
        self.mWidth = width
        self.mHeight = height
        self.mScreen = 0
        score_width = 120
        score_height = 80
        score_x = self.mWidth / 2 - score_width / 2
        score_y = 40
        self.mScoreBoard = score_board.ScoreBoard( score_x, score_y, score_width, score_height )
        self.mHomeScreen = homeScreen.HomeScreen()

        wall_size = 10
        self.mLeftWall = wall.Wall( 0, 0, wall_size, self.mHeight )
        self.mRightWall = wall.Wall( self.mWidth-wall_size, 0, wall_size, self.mHeight )
        self.mTopWall = wall.Wall( 0, 0, self.mWidth, wall_size )
        self.mBottomWall = wall.Wall( 0, self.mHeight-wall_size, self.mWidth, wall_size )

        paddle_margin = 20
        paddle_width = 20
        paddle_height = 100
        paddle_speed = self.mHeight / 1.25
        self.mLeftPaddle = paddle.Paddle( self.mLeftWall.getRightX( ) + paddle_margin,
                                          self.mHeight / 2 - paddle_height / 2,
                                          paddle_width, paddle_height,
                                          paddle_speed,
                                          self.mTopWall.getBottomY( ),
                                          self.mBottomWall.getY( ) )

        self.mRightPaddle = ai.Ai( self.mRightWall.getX( ) - paddle_margin - paddle_width,
                                           self.mHeight / 2 - paddle_height / 2,
                                           paddle_width, paddle_height,
                                           paddle_speed,
                                           self.mTopWall.getBottomY( ),
                                           self.mBottomWall.getY( ) )

        size = 20
        self.mBall = ball.Ball( size,
                                self.mLeftWall.getRightX( ),
                                self.mRightWall.getX( ),
                                self.mTopWall.getBottomY( ),
                                self.mBottomWall.getY( ),
                                self.mLeftPaddle.getRightX( ),
                                self.mRightPaddle.getX( ) )
        self.serveBall( )

        self.mBall.setLeftPaddleY( self.mLeftPaddle.getY( ), self.mLeftPaddle.getBottomY( ) )
        self.mBall.setRightPaddleY( self.mRightPaddle.getY( ), self.mRightPaddle.getBottomY( ) )

        return

    def serveBall( self ):
        min_dx = self.mWidth / 1
        max_dx = min_dx
        max = random.uniform(self.mHeight / 1, self.mHeight / 1.3)
        min = random.uniform(-self.mHeight / 1, -self.mHeight / 1.3)
        max_dy = max
        min_dy = min
        if self.mScoreBoard.getServeStatus( ) == LEFT:
            self.mBall.serveLeft( self.mLeftPaddle.getRightX( ) + self.mBall.getSize( ),
                                  self.mLeftPaddle.getY( ),
                                  self.mLeftPaddle.getBottomY( ),
                                  min_dx, max_dx, min_dy, max_dy )
            self.mScoreBoard.swapServe( )
            self.mBallMoving = True
        elif self.mScoreBoard.getServeStatus( ) == RIGHT:
            self.mBall.serveRight( self.mRightPaddle.getX( ) - self.mBall.getSize( ),
                                   self.mRightPaddle.getY( ),
                                   self.mRightPaddle.getBottomY( ),
                                   min_dx, max_dx, min_dy, max_dy )
            self.mScoreBoard.swapServe( )
            self.mBallMoving = True
        return

    def update( self, dt, keys ):
        paddleTop = self.mRightPaddle.getY()
        paddleBottom = self.mRightPaddle.getY() + self.mRightPaddle.getHeight()

        if self.mBall.getDX( ) != 0:
            self.mBall.move( dt )

            if pygame.K_w in keys:
                self.mLeftPaddle.moveUp( dt )
                self.mBall.setLeftPaddleY( self.mLeftPaddle.getY( ), self.mLeftPaddle.getBottomY( ) )
            elif pygame.K_s in keys:
                self.mLeftPaddle.moveDown( dt )
                self.mBall.setLeftPaddleY( self.mLeftPaddle.getY( ), self.mLeftPaddle.getBottomY( ) )

            if self.mRightPaddle.ballCrossingY(self.mBall) < paddleTop:
                self.mRightPaddle.moveUp( dt )
                self.mBall.setRightPaddleY( self.mRightPaddle.getY( ), self.mRightPaddle.getBottomY( ) )
            elif self.mRightPaddle.ballCrossingY(self.mBall) > paddleBottom:
                self.mRightPaddle.moveDown( dt )
                self.mBall.setRightPaddleY( self.mRightPaddle.getY( ), self.mRightPaddle.getBottomY( ) )

        else:
            if self.mBallMoving:
                self.mBallMoving = False
                if self.mBall.getX( ) < self.mWidth / 2:
                    self.mScoreBoard.scoreRight( )
                else:
                    self.mScoreBoard.scoreLeft( )

            if( ( self.mScoreBoard.getServeStatus( ) == LEFT and
                  pygame.K_d in keys ) or
                ( self.mScoreBoard.getServeStatus( ) == RIGHT and
                  pygame.K_LEFT in keys ) ):
                self.serveBall( )



        return

    def draw( self, surface ):
        # if self.mScreen == 0:
            #self.mHomeScreen.draw(surface)
        #else:
            color = ( 0, 0, 0 )
            surface.fill( color )
            self.mTopWall.draw( surface )
            self.mBottomWall.draw( surface )
            self.mLeftWall.draw( surface )
            self.mRightWall.draw( surface )
            self.mScoreBoard.draw( surface )
            self.mLeftPaddle.draw( surface )
            self.mRightPaddle.draw( surface )
            self.mBall.draw( surface )

    
    