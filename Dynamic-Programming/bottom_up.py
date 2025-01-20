""" Bottom-up (Tabulation) """


from typing import List


# Fibonacci Numbers

def fibonacci_tab(n: int) -> int:
    """Calculate the n-th Fibonacci number using a bottom-up tabulation
    approach.

    Args:
        n (int): The position in the Fibonacci sequence (0-indexed).

    Returns:
        int: The n-th Fibonacci number.

    Raises:
        ValueError: If n is negative.
    """

    if n < 0:
        raise ValueError("Input should be a non-negative integer.")
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


print(fibonacci_tab(10))  # 55


# 0/1 The Knapsack Problem

def knapsack_tab(weights: List, values: List, capacity: int) -> int:
    """Solve the 0/1 Knapsack problem using a bottom-up tabulation approach.

    Args:
        weights (List[int]): A list of weights of the items.
        values (List[int]): A list of values corresponding to the items.
        capacity (int): The maximum weight capacity of the knapsack.

    Returns:
        int: The maximum value that can be obtained within the given capacity.

    Raises:
        ValueError: If the lengths of weights and values
                    are not equal or if capacity is negative.
    """

    if len(weights) != len(values):
        raise ValueError("The lengths of weights and values must be equal.")
    if capacity < 0:
        raise ValueError("Capacity must be a non-negative integer.")

    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i - 1][w],
                    values[i - 1] + dp[i - 1][w - weights[i - 1]]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


W = [1, 2, 3]
V = [10, 15, 40]
C = 6
print(knapsack_tab(W, V, C))  # 65


# Longest common subsequence (LCS)

def lcs_tab(x: str, y: str) -> int:
    """Compute the length of the longest common subsequence (LCS) of two
    strings using a bottom-up tabulation approach.

    Args:
        x (str): The first string.
        y (str): The second string.

    Returns:
        int: The length of the longest common subsequence of the two strings.
    """

    m = len(x)
    n = len(y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif x[i - 1] == y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


A = "AGGTAB"
B = "GXTXAYB"
print(lcs_tab(A, B))  # 4
