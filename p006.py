def main():
    sum = 0
    for i in range(1, 101):
        sum = sum + i
    sum = sum**2

    square = 0
    for i in range(1, 101):
        square = square + i**2 

    dif = sum - square
    print(dif)


if __name__ == "__main__":
    main()
