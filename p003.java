import java.util.Scanner;

public class p003 {//start class
    /* Problem 3 - Largest Prime Factor (Java)
     * 
     * This program finds the largest prime factor of a number greater than 1
     * One is not considered a prime number.
     * Error if enters prime number
     */
    public static void main(String[] args) {//start main
        System.out.println("This program finds the largest prime factor of a number");

        Scanner scanner = new Scanner(System.in);        
        System.out.print("Enter a number: ");
        long userin = scanner.nextLong();

        findPrimeFactors(userin);

        scanner.close();
    }//end main

    public static void findPrimeFactors(long x){//function to find prime factors of input x
        for (long i = (long)Math.sqrt(x); i > 1; i--){//start for
            if (x % i == 0){//check if i is a factor of x 
                if (isPrime(i) == true){//check if i is prime
                    System.out.println("The largest prime factor is " + i);
                    return;
                }//end if
            }//end if
        }//end for
    }//end findPrimeFactors

    public static boolean isPrime(long x){//function to find if number is prime
        if (x <= 1) //base case, if less than or equals 1, not a prime number
            return false;
        
        for (long i = 2; i < Math.sqrt(x); i++){//start for
            if(x % i == 0)//if x divisible by i (any number between 2 and squareroot of x) then not prime
                return false;
        }//end for
        return true;//otherwise is prime

    }//end isPrime

}//end class