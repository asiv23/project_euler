'''
Problmen 5 - Smallest Multiple (Python)

This program finds the smallest number that is divisible by all numbers between 1 and 20 (inclusive).
The current version of this program is inefficient and can probably be made to run faster. 
'''
def evenDiv(num):
    for i in range(1, 20):
        if num % i != 0:
            return False
    return True

def main():
    ans = False
    x = 7759750
    while ans == False:
        x = x+20 # can probably find a better number than 20 to add at every interval
        ans = evenDiv(x)
    
    print(x)         

if __name__ == "__main__":
    main()
