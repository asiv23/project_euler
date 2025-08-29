'''
Problem 2 - Even Fibonacci Numbers (Python)

This program finds the sum of the even or odd numbers of the Fibonacci sequence starting from 1,2 until an upper limit.
Originally the program was hardcoded to print the sum of even numbers under 4 million
but has been updated to accomidate any limit as well as summing odd or even numbers.
Error checking implemented on user input of parrity, must enter 1 for odd or 2 for even, repeats until recieves valid answer
'''
def Fibonacci(limit): #finds number in Fibonacci sequence until limit inputted by user
    fib = [1, 2] #starting squence
    x = 0 #variable for next number in sequence
    num = 2 #counter

    while(x <= limit):
        if (num == 2):
            x = fib[0] + fib[1]#base case
        else:
            x = fib[num-2] + fib[num-1]
        
        if x > limit:
            break

        fib.append(x)
        num = num + 1
    
    return fib

def findEvenSum(list):
    listSum = 0
    for num in range(len(list)):
        if (list[num] % 2 == 0):
            listSum = listSum + list[num]
    
    return listSum

def findOddSum(list):
    listSum = 0
    for num in range(len(list)):
        if (list[num] % 2 != 0):
            listSum = listSum + list[num]
    
    return listSum

def main():
    print("This program finds the sum of the even or odd numbers of the Fibonacci sequence starting from 1,2 until an upper limit.")
    limit = int(input("Enter the limit: "))# Get user input - limit
    fib = Fibonacci(limit)

    error = True
    while (error == True):
        paritynum = int(input("Enter the parity, 1 for odd or 2 for even: "))# Get user input
        if paritynum == 1:
            parity = "even"
            totalsum = findEvenSum(fib)
            break
        elif paritynum == 2:
            parity = "odd"
            totalsum = findOddSum(fib)
            break
        print("The answer you've inputted is invalid, please try again")
    
    print("The total sum of the {} numbers in the Fibonacci sequence under {} is {}" .format(parity, limit, totalsum))

if __name__ == "__main__":
    main()
