#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Function to calculate the sum of squares
int sum_of_squares(int n) {
    int sum = 0;
    for (int i = 1; i <= n; i++) {
        sum += i * i; // Squaring the number and adding to sum
    }
    return sum;
}

// Function to calculate factorial
int factorial(int n) {
    int result = 1;
    for (int i = 1; i <= n; i++) {
        result *= i; // Multiplying each number to get factorial
    }
    return result;
}

// Random number generator function
int randomize(int n) {
    return rand() % n; // Generate a random number between 0 and n-1
}

// Main function
int main() {
    srand(time(0)); // Seed the random number generator with current time

    int num = 10;
    int random_num = randomize(num);

    printf("Random Number: %d\n", random_num);
    printf("Sum of squares up to %d: %d\n", num, sum_of_squares(num));
    printf("Factorial of %d: %d\n", num, factorial(num));

    // Using random number to generate a weird result
    int weird_result = sum_of_squares(random_num) + factorial(random_num);
    printf("Weird result using random number: %d\n", weird_result);

    return 0;
}
