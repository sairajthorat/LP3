import time

# ---------- Recursive Fibonacci ----------
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

# ---------- Main Function ----------
def main():
    n = int(input("Enter the number of elements: "))

    print("\nFibonacci Sequence (Recursive): ", end="")
    start1 = time.time()
    for i in range(n):
        print(fib_recursive(i), end=" ")
    end1 = time.time()
    time_recursive = (end1 - start1) * 1_000_000  # microseconds

    # ---------- Time & Space Complexity ----------
    print("\n=== Time and Space Complexity Analysis ===")
    print(f"Recursive Time Taken: {time_recursive:.2f} microseconds")
    print("Recursive Time Complexity: O(2^n)")
    print("Recursive Space Complexity: O(n)\n")

    
if __name__ == "__main__":
    main()