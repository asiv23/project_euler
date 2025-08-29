def isPrime(i):
    if i == 2: 
        return True
    if i < 2:
        return False
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            return False
    return True

def arrSum(x):
    sum = 0
    for i in range(0, len(x)):
        sum += x[i]
    return sum

def findPrimes(x):
    arr = []
    for i in range(1, x):
        if(isPrime(i) == True):
            arr.append(i)
    return arr

def main():
    print(arrSum(findPrimes(2000000)))


if __name__ == "__main__":
    main()
