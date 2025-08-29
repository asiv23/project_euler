def powerSum(n):
    sum = 0
    while(n > 0):
        sum += (n % 10) ** 5
        n = n // 10
    return sum

def main():
    # n = 1634
    x = 0
    for i in range(2, 1000000):
        if i == powerSum(i):
            print(i)
            x += powerSum(i)
    print("sum:", x)

if __name__ == "__main__":
    main()