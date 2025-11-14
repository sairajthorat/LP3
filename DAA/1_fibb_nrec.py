import time

# ---------- Non-Recursive Fibonacci ----------
def fib_non_recursive(n):
    n1, n2 = 0, 1
    print(n1, n2, end=" ")
    for i in range(2, n):
        n3 = n1 + n2
        print(n3, end=" ")
        n1, n2 = n2, n3
    print()



# ---------- Main Function ----------
def main():
    n = int(input("Enter the number of elements: "))
    print("\n\nFibonacci Sequence (Non-Recursive): ", end="")
    start2 = time.time()
    fib_non_recursive(n)
    end2 = time.time()
    time_nonrecursive = (end2 - start2) * 1_000_000  # microseconds

 # ---------- Time & Space Complexity ----------

    print(f"Non-Recursive Time Taken: {time_nonrecursive:.2f} microseconds")
    print("Non-Recursive Time Complexity: O(n)")
    print("Non-Recursive Space Complexity: O(1)")

if __name__ == "__main__":
    main()