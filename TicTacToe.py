#Ryan Jones
#4/4/18

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
    choice = int(input("Choose a square: "))
    if choice==1:
        a='x'

printBoard()