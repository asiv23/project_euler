def arrSum(x):
    sum = 0
    for i in range(0, len(x)):
        sum += x[i]
    return sum

def main():
    n = 2 ** 1000 
    x = []
    while(n > 0):
        m = n % 10
        x.append(m)
        n = n // 10

    print(arrSum(x))    
    
if __name__ == "__main__":
    main()
