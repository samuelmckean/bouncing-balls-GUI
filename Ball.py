# defines Ball class and getRandomColor function which uses toHexChar to
# generate a random color when creating a Ball instance

from random import randint # imports all definitions from random module

class Ball:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.dx = 2
        self.dy = 2
        self.color = getRandomColor()
        self.radius = 3

def getRandomColor():
    color = "#"
    for j in range(6):
        # add a random digit to #RRGGBB
        color += toHexChar(randint(0,15))
    return color

# convert an int to a single hex digit in a character
def toHexChar(hexValue):
    if 0 <= hexValue <= 9:
        return chr(hexValue + ord('0'))
    else: # 10 <= hexValue <= 15
        return chr(hexValue - 10 + ord('A'))
            
