#Ryan Jones
#4/4/18

from random import randint

a=1
b=2
c=3
d=4
e=5
f=6
g=7
h=8
i=9

def printBoard():
    print('      |   |     ')
    print('  ',a,' |',b,'|',c,'')
    print('   -----------')
    print('      |   |     ')
    print('  ',d,' |',e,'|',f,'')
    print('   -----------')
    print('      |   |     ')
    print('  ',g,' |',h,'|',i,'')

if __name__ == '__main__':
    printBoard()
    while True:    
        choice = int(input("Choose a square: "))
        if choice==1:
            a='x'
        if choice==2:
            b='x'
        if choice==3:
            c='x'
        if choice==4:
            d='x'
        if choice==5:
            e='x'
        if choice==6:
            f='x'
        if choice==7:
            g='x'
        if choice==8:
            h='x'
        if choice==9:
            i='x'
        printBoard()
    
