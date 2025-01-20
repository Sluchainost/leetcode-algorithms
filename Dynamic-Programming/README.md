# Dynamic Programming

## Properties of dynamic programming
**Dynamic programming** (DP) is a powerful algorithmic technique used to solve problems that can be broken down into overlapping **subproblems** and optimal substructure. Here are the key properties and characteristics of **dynamic programming**:

1. `Optimal Substructure`

    - A problem exhibits optimal substructure if an optimal solution to the problem can be constructed from optimal solutions to its **subproblems**. This means that solving the smaller **subproblems** will lead to the optimal solution for the entire problem.

2. `Overlapping Subproblems`

    - **Dynamic programming** is applicable when the problem can be divided into smaller subproblems that are solved independently. If the same **subproblems** are solved multiple times, **DP** can save computation time by storing the results of these subproblems (usually in a table or an array).
3. `Memoization (Top-Down Approach)`

    - This technique involves storing the results of expensive function calls and reusing them when the same inputs occur again. In this approach, the problem is solved **recursively**, and results are **cached** to avoid redundant calculations.
4. `Tabulation (Bottom-Up Approach)`

    - In this approach, the problem is solved **iteratively** by filling out a table (usually an array) based on previously computed values. The idea is to build up the solution from the smallest subproblems to the larger ones.
5. `State and State Transition`

    - The state represents a specific configuration of the problem at a given point in time, often defined by some parameters. The state transition defines how to move from one state to another, usually by making a decision based on the current state.
6. `Complexity Analysis`

    - The time and space complexity of **dynamic programming** algorithms can often be analyzed based on the number of states and the time required for each state transition. The goal is to reduce the complexity compared to naive recursive approaches.
7. `Choice Property`

    - In many **DP** problems, the choices made at each step can lead to different outcomes. The choice property ensures that the best choice at one step leads to the best overall solution.
8. `Problem-Specific Structures`

    - Different problems may have unique structures that can be exploited through **dynamic programming**. For instance, some problems can be solved using a *one-dimensional array*, while others may require *multi-dimensional arrays* or matrices.
9. `Applications`
    - **Dynamic programming** is widely used in various fields such as computer science, operations research, economics, bioinformatics, and more. Common applications include:
        - *Shortest path problems* (e.g., Dijkstra's algorithm, Floyd-Warshall algorithm)
        - *Knapsack problems*
        - *Sequence alignment in bioinformatics*
        - *Fibonacci number calculation*
        - *Dynamic programming on trees* (e.g., finding the longest path)

## Visualization

In the image below, we can see a tree of **subproblems** we need to solve in order to get `F(5)`:

![Fibonacci-sequence](img\Fibonacci-sequence-5.jpg)

One drawback to this approach is that it requires computing the same **Fibonacci** numbers multiple times in order to get our solution.

### Top-Down Approach (Memoization)

The first **dynamic programming** approach we’ll use is the **top-down** approach. The idea here is similar to the recursive approach, but the difference is that we’ll save the solutions to subproblems we encounter.

This way, if we run into the same **subproblem** more than once, we can use our saved solution instead of having to recalculate it. This allows us to compute each subproblem exactly one time.

This **dynamic programming** technique is called **memoization**. We can see how our tree of subproblems shrinks when we use **memoization**:

![Fibonacci-memoization](img\Fibonacci-memoization-(top-down).jpg)

### Bottom-Up Approach (Tabulation)

In the **bottom-up dynamic programming** approach, we’ll reorganize the order in which we solve the **subproblems**.

We’ll compute `F(0)`, then `F(1)`, then `F(2)`, and so on:

![Fibonacci-tabulation](img\Fibonacci-tabulation-(bottom-up).jpg)

This will allow us to compute the solution to each problem only once, and we’ll only need to save two intermediate results at a time.

For example, when we’re trying to find `F(2)`, we only need to have the solutions to `F(1)` and `F(0)` available. Similarly, for `F(3)`, we only need to have the solutions to `F(2)` and `F(1)`.

## Best explanations

YouTube:

1. [Greg Hogg: Dynamic Programming - Top Down Memoization & Bottom Up Tabulation - DSA Course in Python Lecture 15](https://www.youtube.com/watch?v=piAlsJySUGE)
2. ~
3. ~

Leetcode:

1. [Dynamic Programming card](https://leetcode.com/explore/featured/card/dynamic-programming/)

## Litcode Problems

[**Dynamic Programming problem list**](https://leetcode.com/problem-list/dynamic-programming/)

1. [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/description/?envType=problem-list-v2&envId=dynamic-programming)
2. [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/description/?envType=problem-list-v2&envId=dynamic-programming)
3. [198. House Robber](https://leetcode.com/problems/house-robber/solutions/?envType=problem-list-v2&envId=dynamic-programming)
4. [300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/description/?envType=problem-list-v2&envId=dynamic-programming)
5. [322. Coin Change](https://leetcode.com/problems/coin-change/description/?envType=problem-list-v2&envId=dynamic-programming)
