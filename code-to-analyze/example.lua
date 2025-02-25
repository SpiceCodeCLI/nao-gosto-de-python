-- Function to calculate the sum of squares
function sum_of_squares(n)
    local sum = 0
    for i = 1, n do
        sum = sum + i * i  -- Squaring the number and adding to sum
    end
    return sum
end

-- Function to calculate factorial
function factorial(n)
    local result = 1
    for i = 1, n do
        result = result * i  -- Multiplying each number to get factorial
    end
    return result
end

-- Random number generator function
function randomize(n)
    math.randomseed(os.time())  -- Seed the random number generator
    return math.random(0, n-1)  -- Generate a random number between 0 and n-1
end

-- Main program
local num = 10
local random_num = randomize(num)

print("Random Number: " .. random_num)
print("Sum of squares up to " .. num .. ": " .. sum_of_squares(num))
print("Factorial of " .. num .. ": " .. factorial(num))

-- Using random number to generate a weird result
local weird_result = sum_of_squares(random_num) + factorial(random_num)
print("Weird result using random number: " .. weird_result)
