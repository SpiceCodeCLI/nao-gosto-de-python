public class example {

    // Function to calculate the sum of squares
    public static int sumOfSquares(int n) {
        int sum = 0;
        for (int i = 1; i <= n; i++) {
            sum += i * i; // Squaring the number and adding to sum
        }
        return sum;
    }

    // Function to calculate factorial
    public static int factorial(int n) {
        int result = 1;
        for (int i = 1; i <= n; i++) {
            result *= i; // Multiplying each number to get factorial
        }
        return result;
    }

    // Random number generator function
    public static int randomize(int n) {
        return (int) (Math.random() * n); // Generate a random number between 0 and n-1
    }

    // Main function
    public static void main(String[] args) {
        int num = 10;
        int randomNum = randomize(num);

        System.out.println("Random Number: " + randomNum);
        System.out.println("Sum of squares up to " + num + ": " + sumOfSquares(num));
        System.out.println("Factorial of " + num + ": " + factorial(num));

        // Using random number to generate a weird result
        int weirdResult = sumOfSquares(randomNum) + factorial(randomNum);
        System.out.println("Weird result using random number: " + weirdResult);
    }
}
