'''
Problmen 4 - Largest Palindrome Product (Python)

This program finds the largest palindromic (read the same both forward and backwards) number that is a product
of two 3-digit numbers. 
'''

def isPalindrome(num):
    revNum = str(num)[::-1]
    if num == int(revNum):
        return True
    return False

def main():
    x = 0
    for i in range(999, 100, -1):
        for j in range(990, 100, -1):
            if isPalindrome(i*j) == True:
                x = max(x, i*j)

    print(x)       
    
if __name__ == "__main__":
    main()