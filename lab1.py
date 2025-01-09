# Python Program to find the Nth fibonacci number using
# Matrix Exponentiation
""" NEW program"""
MOD = 10**9 + 7

# function to multiply two 2x2 Matrices
def multiply(A, B):
    """Multiply two matrices"""
    # Matrix to store the result
    C = [[0, 0], [0, 0]]

    # Matrix Multiply
    C[0][0] = (A[0][0] * B[0][0] + A[0][1] * B[1][0]) % MOD
    C[0][1] = (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % MOD
    C[1][0] = (A[1][0] * B[0][0] + A[1][1] * B[1][0]) % MOD
    C[1][1] = (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % MOD

    # Copy the result back to the first matrix
    A[0][0] = C[0][0]
    A[0][1] = C[0][1]
    A[1][0] = C[1][0]
    A[1][1] = C[1][1]

# Function to find (Matrix M ^ expo)
def power(M, expo):
    """return mod power"""
    # Initialize result with identity matrix
    ans = [[1, 0], [0, 1]]

    # Fast Exponentiation
    while expo:
        if expo & 1:
            multiply(ans, M)
        multiply(M, M)
        expo >>= 1

    return ans


def nthFibonacci(n):
    """return nth fib"""
    # Base case
    if n == 0 or n == 1:
        return 1

    M = [[1, 1], [1, 0]]
    # F(0) = 0, F(1) = 1
    F = [[1, 0], [0, 0]]

    # Multiply matrix M (n - 1) times
    res = power(M, n - 1)

    # Multiply Resultant with Matrix F
    multiply(res, F)

    return res[0][0] % MOD


# Sample Input
n = 3

# Print the nth fibonacci number
print(nthFibonacci(n))