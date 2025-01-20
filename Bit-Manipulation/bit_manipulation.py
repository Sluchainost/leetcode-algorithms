""" Bit Manipulation """

from typing import List


#  1. Check if a number is even or odd:


def is_even(n: int) -> bool:
    """ Check if the number is even.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if n is even, False if odd.
    """

    return (n & 1) == 0


print(is_even(4))  # True
print(is_even(5))  # False


#  2. Counting the number of 1s in a binary representation (Hamming Weight):


def hamming_weight(n: int) -> int:
    """ Count the number of 1s in the binary representation of n.

    Args:
        n (int): The number to analyze.

    Returns:
        int: The count of 1s in the binary representation.
    """

    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count


print(hamming_weight(11))  # Output: 3 (binary 1011)


#  3. Finding the single number (where every other number appears twice):


def single_number(nums: List) -> int:
    """ Find the number that appears only once in the list.

    Args:
        nums (List[int]): List of integers where every number appears twice
                          except for one.

    Returns:
        int: The number that appears only once.
    """

    result = 0
    for num in nums:
        result ^= num
    return result


print(single_number([4, 1, 2, 1, 2]))  # Output: 4


#  4. Power of Two:


def is_power_of_two(n: int) -> bool:
    """ Check if n is a power of two.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if n is a power of two, False otherwise.
    """

    return n > 0 and (n & (n - 1)) == 0


print(is_power_of_two(16))  # True
print(is_power_of_two(18))  # False


#  5. Reverse bits of a number:


def reverse_bits(n: int) -> int:
    """ Reverse the bits of a 32-bit unsigned integer.

    Args:
        n (int): The number to reverse bits for.

    Returns:
        int: The number with its bits reversed.
    """

    result = 0
    for _ in range(32):  # Assuming 32-bit integer
        result = (result << 1) | (n & 1)
        n >>= 1
    return result


print(reverse_bits(43261596))
# Output: 964176192 (binary: 00000010100101000001111010011100)
