#Ryan Jones
#3/26/18

def prime(n):
    for i in range(2,n):
        if n%i == 0:
            return False
        return True
        

print(prime(9))
print(prime(11))
