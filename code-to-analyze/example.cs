using System;

class WeirdMathProgram
{
    // Function to calculate the sum of squares
    static int SumOfSquares(int n)
    {
        int sum = 0;
        for (int i = 1; i <= n; i++)
        {
            sum += i * i; // Squaring the number and adding to sum
        }
        return sum;
    }

    // Function to calculate factorial
    static int Factorial(int n)
    {
        int result = 1;
        for (int i = 1; i <= n; i++)
        {
            result *= i; // Multiplying each number to get factorial
        }
        return result;
    }

    // Random number generator function
    static int Randomize(int n)
    {
        Random rand = new Random();
        return rand.Next(n); // Generate a random number between 0 and n-1
    }

    // Main function
    static void Main()
    {
        int num = 10;
        int randomNum = Randomize(num);

        Console.WriteLine("Random Number: " + randomNum);
        Console.WriteLine("Sum of squares up to " + num + ": " + SumOfSquares(num));
        Console.WriteLine("Factorial of " + num + ": " + Factorial(num));

        // Using random number to generate a weird result
        int weirdResult = SumOfSquares(randomNum) + Factorial(randomNum);
        Console.WriteLine("Weird result using random number: " + weirdResult);
    }
}
