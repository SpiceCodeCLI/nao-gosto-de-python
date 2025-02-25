// Function to calculate the sum of squares
fn sum_of_squares(n: i32) -> i32 {
    let mut sum = 0;
    for i in 1..=n {
        sum += i * i; // Squaring the number and adding to sum
    }
    sum
}

// Function to calculate factorial
fn factorial(n: i32) -> i32 {
    let mut result = 1;
    for i in 1..=n {
        result *= i; // Multiplying each number to get factorial
    }
    result
}

// Random number generator function
fn randomize(n: i32) -> i32 {
    use rand::Rng;
    let mut rng = rand::thread_rng();
    rng.gen_range(0..n) // Generate a random number between 0 and n-1
}

fn main() {
    let num = 10;
    let random_num = randomize(num);

    println!("Random Number: {}", random_num);
    println!("Sum of squares up to {}: {}", num, sum_of_squares(num));
    println!("Factorial of {}: {}", num, factorial(num));

    // Using random number to generate a weird result
    let weird_result = sum_of_squares(random_num) + factorial(random_num);
    println!("Weird result using random number: {}", weird_result);
}
