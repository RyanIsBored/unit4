#Ryan Jones
#3/22/18
#Monkey Quest 2.0

from ggame import *

#constants
ROWS = 20
COLS = 40
CELL_SIZE = 20

if __name__ == '__main__':
    
    #colors
    green = Color(0x006600,1)
    
    jungleBox = RectangleAsset(CELL_SIZE*COLS,CELL_SIZE*ROWS,LineStyle(1,green),green)
    
    Sprite(jungleBox)
    
    App().run()