#Ryan Jones
#4/3/18
#quiz4.py

def count(num):
    i=1
    while i<num+1:
        print(i)
        i=i+1
count(7)

def excitedPrint(string):
    print(string.upper(),'!!!')
    

excitedPrint('ok')

def firstLetter(phrase):
    for ch in phrase:
        print(ch)
        
firstLetter('wow')

def repeats(a,b,c):
    if a==b or a==c or b==c:
        return True
    else:
        return False

repeats(4,3,4)