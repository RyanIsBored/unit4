#Ryan Jones
#3/22/18
#Monkey Quest 2.0

from ggame import *

if __name__ == '__main__':
    
    #colors
    green = Color(0x006600,1)
    
    jungleBox = RectangleAsset(800,500,LineStyle(1,green),green)
    
    Sprite(jungleBox)
    
    App().run()