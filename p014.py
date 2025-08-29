def collatz(n):
    x = []
    x.append(n)
    while(n != 1):
        if (n%2 == 0):
            n //= 2
        else:
            n = 3 * n + 1
        x.append(n)
    return x

def main():
    max = 0
    n = 0
    for i in range (1, 1000000):
        if max < len(collatz(i)):
            max = len(collatz(i))
            n = i
    print(n, max)

if __name__ == "__main__":
    main()