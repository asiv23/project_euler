def factorial(x):
    if(x < 1):
        return 0
    if(x == 1):
        return 1
    return x * factorial(x-1)

def main():
    n = (factorial(100))
    x = 0
    while(n > 0):
        m = n % 10
        x += m 
        n = n // 10
    print(x)

if __name__ == "__main__":
    main()