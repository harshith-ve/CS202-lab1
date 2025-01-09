# Python Program to find the Nth Fibonacci number using
# Matrix Exponentiation
""" Program to find Nth Fibonacci number """

MOD = 10**9 + 7

def multiply(matrix_a, matrix_b):
    """Multiply two 2x2 matrices."""
    # Matrix to store the result
    result = [[0, 0], [0, 0]]

    # Matrix multiplication
    result[0][0] = (matrix_a[0][0] * matrix_b[0][0] + matrix_a[0][1] * matrix_b[1][0]) % MOD
    result[0][1] = (matrix_a[0][0] * matrix_b[0][1] + matrix_a[0][1] * matrix_b[1][1]) % MOD
    result[1][0] = (matrix_a[1][0] * matrix_b[0][0] + matrix_a[1][1] * matrix_b[1][0]) % MOD
    result[1][1] = (matrix_a[1][0] * matrix_b[0][1] + matrix_a[1][1] * matrix_b[1][1]) % MOD

    # Copy the result back to matrix_a
    matrix_a[0][0] = result[0][0]
    matrix_a[0][1] = result[0][1]
    matrix_a[1][0] = result[1][0]
    matrix_a[1][1] = result[1][1]

def power(matrix, exponent):
    """Calculate matrix exponentiation with mod."""
    # Initialize result with the identity matrix
    result = [[1, 0], [0, 1]]

    # Fast exponentiation
    while exponent:
        if exponent & 1:
            multiply(result, matrix)
        multiply(matrix, matrix)
        exponent >>= 1

    return result

def nth_fibonacci(index):
    """Return the Nth Fibonacci number."""
    # Base cases
    if index in (0, 1):
        return 1

    transformation_matrix = [[1, 1], [1, 0]]
    base_matrix = [[1, 0], [0, 0]]

    # Multiply transformation_matrix (index - 1) times
    result_matrix = power(transformation_matrix, index - 1)

    # Multiply result_matrix with base_matrix
    multiply(result_matrix, base_matrix)

    return result_matrix[0][0] % MOD

# Sample Input
NTH_IDX = 3

# Print the nth Fibonacci number
print(nth_fibonacci(NTH_IDX))
