def isPythag(a, b, c):
    if (a**2 + b**2 == c**2):
        return True
    return False

def checkSum(a, b, c):
    if(a + b + c == 1000):
        return True
    return False

def main():
    for i in range(1, 1000):
        for j in range(1, 1000):
            k = (i**2 + j**2)**0.5
            if(checkSum(i, j, k) == True):
                print(i, j, k, i*j*k)
                return 
    # print(isPythag(3, 4, 5))
    # print a*b*c

if __name__ == "__main__":
    main()
