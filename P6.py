import random
import time

# Deterministic Quick Sort
def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)

# Randomized Quick Sort
def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)

# Analysis Function
def analyze_quick_sort():
    sizes = [100, 1000, 5000, 10000]
    print(f"{'Size':<10}{'Deterministic Time':<20}{'Randomized Time':<20}")
    print("-" * 50)
    for size in sizes:
        arr = [random.randint(1, 10000) for _ in range(size)]
        
        # Deterministic Quick Sort
        start_time = time.time()
        deterministic_quick_sort(arr)
        deterministic_time = time.time() - start_time
        
        # Randomized Quick Sort
        start_time = time.time()
        randomized_quick_sort(arr)
        randomized_time = time.time() - start_time
        
        print(f"{size:<10}{deterministic_time:<20.6f}{randomized_time:<20.6f}")

if __name__ == "__main__":
    analyze_quick_sort()