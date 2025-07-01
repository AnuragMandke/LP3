import time

def fibonacci_non_recursive(num):
    """
    Time Complexity: O(n) - Iterates through the range of numbers.
    Space Complexity: O(n) - Stores the Fibonacci sequence in a list.
    """
    fib = [1, 1]
    count = 2
    if num == 0:
        return [], 0
    elif num == 1:
        return [1], 1
    elif num == 2:
        return [1, 1], 2
    else:
        for i in range(2, num):
            fib.append(fib[-1] + fib[-2])
            count += 1
    return fib, count

def fibonacci_recursive(num):
    """
    Time Complexity: O(n) - Each recursive call processes one number.
    Space Complexity: O(n) - Recursive stack and list storage.
    """
    fib = [1, 1]
    count = 2
    if num == 0:
        return [], 0
    elif num == 1:
        return [1], 1
    elif num == 2:
        return [1, 1], 2
    
    def calc(n):
        if n == len(fib):  # Base case: stop when the desired length is reached
            return fib
        fib.append(fib[-1] + fib[-2])
        nonlocal count
        count += 1
        return calc(n)  # Continue recursion until the base case is met
    
    return calc(num), count

while True:
    try:
        num = int(input("Enter a number: "))
        if num < 0:
            print("Please enter a non-negative integer.")
            continue
        choice = input("Choose method (1 for non-recursive, 2 for recursive): ")
        
        start_time = time.time()  # Start timing
        if choice == '1':
            res, steps = fibonacci_non_recursive(num)
            method = "Non-Recursive"
        elif choice == '2':
            res, steps = fibonacci_recursive(num)
            method = "Recursive"
        end_time = time.time()  # End timing
        
        print(f"Method: {method}")
        print(f"Fibonacci Sequence: {res[-1] if res else '[]'}")
        print(f"Number of Steps: {steps}")
        print(f"Execution Time: {end_time - start_time:.6f} seconds")
        print(f"Space Complexity: O(n) - List storage")
        print(f"Time Complexity: O(n) - Iterative or recursive processing")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
    except KeyboardInterrupt:
        print("\nExiting the program.")
        break