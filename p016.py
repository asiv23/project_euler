def main():
    n = 2 ** 1000 
    x = 0
    while(n > 0):
        m = n % 10
        x += m 
        n = n // 10

    print(x)
    
if __name__ == "__main__":
    main()
