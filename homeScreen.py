import text
import pong

class HomeScreen:

    def __init__(self):
        return

    def draw(self, surface):
        oneX, oneY = 400, 200
        twoX, twoY = 400, 300
        one = "For 1 player press (1)"
        two = "For 2 players press (2)"
        oneTxt = text.Text(one, oneX, oneY)
        twoTxt = text.Text(two, twoX, twoY)
        text.Text.draw(oneTxt, surface)
        text.Text.draw(twoTxt, surface)
        return