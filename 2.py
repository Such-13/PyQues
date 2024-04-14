import numpy as np

def create_2d_array(a, b):
    # Initialize an empty list to store non-prime numbers
    non_primes = []
    if(a > b):
        a, b = b, a
    # Loop through the range [a, b]
    while a <= b:
        # Check if the number is not a prime number
        if a != 2 and a != 3 and a != 5 and a != 7 and (a % 2 == 0 or a % 3 == 0 or a % 5 == 0 or a % 7 == 0):
            non_primes.append(a)
        a += 1

    # Convert the list to a numpy array and reshape it into a 2D array with 10 columns
    # arr = np.array(non_primes).reshape(-1, 10)
    return non_primes

# Example usage:
try:
    a = int(input("Enter the 1st number: "))
    b = int(input("Enter the 2nd number: "))
    if a < 0 or b < 0:
        raise ValueError("Error")
    res = create_2d_array(a, b)
    for chunk in np.array_split(res, len(res) // 10 + (len(res) % 10 > 0)):
        print(*chunk)

except Exception as e:
    print("Error")
