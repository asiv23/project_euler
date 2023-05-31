'''
Problmen 1 - Multiples of 3 or 5

This program finds the sum of multiples from two numbers until an upper limit.
If a number is a multiple of both inputs they're only counted once.
Originally the program was hardcoded for the numbers given in the problem but it has been modified
so that user will input the two numbers, then an upper limit.
No error checking on user input.
'''

def getMultipleSum(x, y, limit): #get multiples of x (user input) from x to limit
    sum = 0
    for num in range(0, limit): #for loop to find multiples
        if (num % x == 0 or num % y == 0): #if mod of num is 0, add to array of multiples
            sum = sum + num
    
    return sum

def main():
    print("This program finds the sum of multiples from two numbers until an upper limit.")
    firstnum = int(input("Enter your first number: "))# Get user input - number
    secondnum = int(input("Enter your second number: "))# Get user input - number
    limit = int(input("Enter the limit: "))# Get user inpun - limit
    
    totalSum = getMultipleSum(firstnum, secondnum, limit)

    print()
    print("The sum of the multiples of {} and {} is {}" .format(firstnum, secondnum, totalSum))

if __name__ == "__main__":
    main()

