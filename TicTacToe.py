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

def fullBoard():
    if (a=='x' or a=='o') and (b=='x' or b=='o') and (c=='x' or c=='o') and (d=='x' or d=='o') and (e=='x' or e=='o') and (f=='x' or f=='o') and (g=='x' or g=='o') and (h=='x' or h=='o') and (i=='x' or i=='o'):
        return True
    return False

def Winner():
    if a=='x' and b=='x' and c=='x':
        return True
    if d=='x' and e=='x' and f=='x':
        return True
    if g=='x' and h=='x' and i=='x':
        return True
    if a=='o' and b=='o' and c=='o':
        return True
    if d=='o' and e=='o' and f=='o':
        return True
    if g=='o' and h=='o' and i=='o':
        return True
    return False

def isEmpty(square):
    if square==1 and a==1:
        return True
    if square==2 and b==2:
        return True
    if square==3 and c==3:
        return True
    if square==4 and d==4:
        return True
    if square==5 and e==5:
        return True
    if square==6 and f==6:
        return True
    if square==7 and g==7:
        return True
    if square==8 and h==8:
        return True
    if square==9 and i==9:
        return True
    return False
        
        
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
        while isEmpty(choice)==False:
            choice = int(input("Choose a different square: "))
            
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
        if Winner():
            print("You win!")
            break
        if fullBoard():
            print('Tie')
            break
        
        choice2 = randint(1,9)
        while isEmpty(choice2)==False:
            choice2 = randint(1,9)
            
        if choice2==1:
            a='o'
        if choice2==2:
            b='o'
        if choice2==3:
            c='o'
        if choice2==4:
            d='o'
        if choice2==5:
            e='o'
        if choice2==6:
            f='o'
        if choice2==7:
            g='o'
        if choice2==8:
            h='o'
        if choice2==9:
            i='o'
        printBoard()
        if Winner():
            print("You lose")
            break
        
