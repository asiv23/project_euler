def fibbonacci(x):
    a, b = 0, 1
    for _ in range(x):
        a, b = b, a + b
    return b

def countDigit(n):
    count = 0
    while(n > 0):
        count += 1 
        n = n // 10
    return count
        
def main():
    length = 0
    i = 1
    while length < 1000:
        length = countDigit(fibbonacci(i))
        i += 1
    # print(countDigit(fibbonacci(8)))
    print (i)
if __name__ == "__main__":
    main()