""" Top-down (Memoization) """


from typing import List


# Fibonacci Numbers

def fibonacci_memo(n: int, memo=None) -> int:
    """Memoization (Recursive approach with caching).

    Args:
        n (int): The position in the Fibonacci sequence (0-indexed).
        memo (dict, optional): A dictionary to store previously computed
            Fibonacci numbers.

    Returns:
        int: The n-th Fibonacci number.
    """

    if memo is None:
        memo = {}  # Dangerous default value {} as argument

    if n in memo:
        return memo[n]
    if n <= 1:
        return n

    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)

    return memo[n]


print(fibonacci_memo(10))  # 55


# 0/1 The Knapsack Problem

def knapsack_memo(weights: List,
                  values: List,
                  capacity: int,
                  n: int, memo=None) -> int:
    """Memoization (Recursive approach with caching).

    Args:
        weights (List[int]): A list of weights of the items.
        values (List[int]): A list of values corresponding to the items.
        capacity (int): The maximum weight capacity of the knapsack.
        n (int): The number of items.
        memo (dict, optional): A dictionary to store previously computed
            results for the given (n, capacity) tuple

    Returns:
        int: The maximum value that can be obtained within the given
            capacity.
    """

    if memo is None:
        memo = {}  # Dangerous default value {} as argument

    if n == 0 or capacity == 0:
        return 0

    if (n, capacity) in memo:
        return memo[(n, capacity)]

    if weights[n - 1] > capacity:
        result = knapsack_memo(weights, values, capacity, n - 1, memo)
    else:
        result = max(
            values[n - 1] + knapsack_memo(weights,
                                          values,
                                          capacity - weights[n - 1],
                                          n - 1, memo),
            knapsack_memo(weights, values, capacity, n - 1, memo)
        )

    memo[(n, capacity)] = result

    return result


W = [1, 2, 3]
V = [10, 15, 40]
C = 6
N = len(V)
print(knapsack_memo(W, V, C, N))  # 65


# Longest common subsequence (LCS)

def lcs_memo(x: str, y: str, m: int, n: int, memo=None):
    """Memoization (Recursive approach with caching).

    Args:
        x (str): The first string.
        y (str): The second string.
        m (int): The length of the first string.
        n (int): The length of the second string.
        memo (dict, optional): A dictionary to store previously computed
            LCS values.

    Returns:
        int: The length of the longest common subsequence of the two
            strings.
    """

    if memo is None:
        memo = {}  # Dangerous default value {} as argument

    if m == 0 or n == 0:
        return 0

    if (m, n) in memo:
        return memo[(m, n)]

    if x[m - 1] == y[n - 1]:
        memo[(m, n)] = 1 + lcs_memo(x, y, m - 1, n - 1, memo)
    else:
        memo[(m, n)] = max(
            lcs_memo(x, y, m, n - 1, memo),
            lcs_memo(x, y, m - 1, n, memo)
            )

    return memo[(m, n)]


A = "AGGTAB"
B = "GXTXAYB"
print(lcs_memo(A, B, len(A), len(B)))  # 4
