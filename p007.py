import math

def isPrime(i):
    if i == 2: 
        return True
    
    if i < 2:
        return False
    
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            return False
        
    return True

def findPrime(x):
    i = 1
    numPrime = 0
    while (numPrime < x):
        i = i+1
        if isPrime(i) == True:
            numPrime = numPrime + 1
            #print(i)
        
    print(i)

def main():
    findPrime(10001)

if __name__ == "__main__":
    main()
