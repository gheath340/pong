import ball
import paddle

class Ai(paddle.Paddle):

    def __init__(self, x, y, width, height, speed, min_y, max_y):
        super().__init__(x, y, width, height, speed, min_y, max_y)

        return

    def checkBottomBall(self, other, new_y):
        maxY = self.mMaxY - other.mSize
        if new_y < maxY:
            return new_y
        else:
            distance = maxY - new_y
            new_y = maxY + distance
            return new_y

    def checkTopBall(self, other, new_y):
        if new_y > self.mMinY:
            return new_y
        else:
            distance = self.mMinY - new_y
            new_y = self.mMinY + distance
            return new_y

    def ballCrossingY(self, other):
        if other.mDX != 0:
            time = (self.mX - other.mX) / other.mDX
        else:
            time = 0
        new_y = other.mY + (other.mDY * time)
        new_y = self.checkBottomBall(other, new_y)
        new_y = self.checkTopBall(other, new_y)
        return new_y