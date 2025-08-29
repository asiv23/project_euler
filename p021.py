def divisors(n):
    divs = []
    for i in range(1, n):
        if (n % i == 0):
            divs.append(i)
    return divs

def arrSum(x):
    sum = 0
    for i in range(0, len(x)):
        sum += x[i]
    return sum

def main():
    x = []
    for i in range(1, 10000):
        n = arrSum(divisors(i))
        if (i == arrSum(divisors(n)) and i != n):
            x.append(i)
    print(x)
    # print(arrSum(divisors(n)))
    print(arrSum(x))

if __name__ == "__main__":
    main()