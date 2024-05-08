def factorial(n):
    """Calculate the factorial of a number."""
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        try:
            number = int(sys.argv[1])
            print(f"The factorial of {number} is {factorial(number)}")
        except ValueError:
            print("Please provide a valid integer.")
    else:
        print("Usage: python main.py <integer>")
