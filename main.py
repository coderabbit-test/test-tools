def nth_fibonacci(n):
  
    # Base case: if n is 0 or 1, return n
    if n <= 1:
        return n
      
    # Recursive case: sum of the two preceding Fibonacci numbers
    return nth_fibonacci(n - 1) + nth_fibonacci(n - 2)

n = 5
result = nth_fibonacci(n)
print(result)


# Function to calculate the nth Fibonacci number using memoization
def nth_fibonacci_util(n, memo):

    # Base case: if n is 0 or 1, return n
    if n <= 1:
        return n

    # Check if the result is already in the memo table
    if memo[n] != -1:
        return memo[n]

    # Recursive case: calculate Fibonacci number
    # and store it in memo
    memo[n] = nth_fibonacci_util(n - 1, memo) + nth_fibonacci_util(n - 2, memo)

    return memo[n]


# Wrapper function that handles both initialization
# and Fibonacci calculation
def nth_fibonacci(n):

    # Create a memoization table and initialize with -1
    memo = [-1] * (n + 1)

    # Call the utility function
    return nth_fibonacci_util(n, memo)


if __name__ == "__main__":
    n = 5
    result = nth_fibonacci(n)
    print(result)



def nth_fibonacci(n):
  
    # Handle the edge cases
    if n <= 1:
        return n

    # Create a list to store Fibonacci numbers
    dp = [0] * (n + 1)

    # Initialize the first two Fibonacci numbers
    dp[0] = 0
    dp[1] = 1

    # Fill the list iteratively
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    # Return the nth Fibonacci number
    return dp[n]

n = 5
result = nth_fibonacci(n)
print(result)

