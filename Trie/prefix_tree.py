""" Trie (prefix_tree) """
from typing import List


# Basic example with root as empty dictionary
class BasicTrie:
    """ Basic example of a Trie data structure. """

    def __init__(self):
        """Initialize the root node of a Trie as an empty dictionary."""

        self.trie = {}

    def insert(self, word: str) -> None:
        """Inserts a word into the Trie.

        Args:
            word (str): The word to insert into the Trie.
        """

        d = self.trie

        for c in word:
            if c not in d:
                d[c] = {}
            d = d[c]

        # Use None to indicate the end of a word
        d[None] = None

    def search(self, word: str) -> bool:
        """Searches for a word in the Trie.

        Args:
            word (str): The word to search for.

        Returns:
            bool: True if the word is found, False otherwise.
        """

        d = self.trie

        for c in word:
            if c not in d:
                return False
            d = d[c]

        # Checking that the word is actually complete
        return None in d

    def starts_with(self, prefix: str) -> bool:
        """Checks if a prefix exists in the Trie.

        Args:
            prefix (str): The prefix to check for.

        Returns:
            bool: True if the prefix exists, False otherwise.
        """

        d = self.trie

        for c in prefix:
            if c not in d:
                return False
            d = d[c]

        return True


# Example of use
trie = BasicTrie()
trie.insert("hello")
trie.insert("world")

print(f'trie.search("hello") = {trie.search("hello")}')  # True
print(f'trie.search("hell") = {trie.search("hell")}')   # False
print(f'trie.starts_with("hell") = {trie.starts_with("hell")}')  # True
print(f'trie.starts_with("wor") = {trie.starts_with("wor")}')    # True
print(f'trie.starts_with("worl") = {trie.starts_with("worl")}')   # True
print(f'trie.starts_with("python") = {trie.starts_with("python")}')  # False


# LeetCode - 3042 Count Prefix and Suffix Pairs I
class Node:
    """Represents a single node in the Trie structure.

    Each node contains an array of links to its children nodes corresponding
    to each letter of the English alphabet (a-z).
    """

    def __init__(self):
        """Initialize a node with links to its children."""

        self.links = [None] * 26

    # Check if the character is present in the current node
    def contains(self, c: str) -> bool:
        """Checks if the character is in the current node's links.

        Args:
            c (str): The character to check for.

        Returns:
            bool: True if the character is present, False otherwise.
        """

        return self.links[ord(c) - ord("a")] is not None

    # Insert a new node for the character
    def put(self, c: str, node: "Node") -> None:
        """Links a new node for the given character.

        Args:
            c (str): The character to insert.
            node (Node): The node to link to the character.
        """

        self.links[ord(c) - ord("a")] = node

    # Get the next node for the character
    def next(self, c: str) -> "Node":
        """Retrieves the next node corresponding to the given character.

        Args:
            c (str): The character for which to get the next node.

        Returns:
            Node: The next node linked to the character.
        """

        return self.links[ord(c) - ord("a")]


class Trie:
    """Represents a Trie for efficient string storage and retrieval.

    This implementation supports insertion of words and checking for prefixes.
    """

    def __init__(self):
        """Initialize the Trie with a root node."""

        self.root = Node()

    # Insert a word into the Trie
    def insert(self, word: str) -> None:
        """Inserts the given word into the Trie.

        Args:
            word (str): The word to insert.
        """

        node = self.root
        for c in word:
            if not node.contains(c):
                node.put(c, Node())
            node = node.next(c)

    # Check if the Trie contains a given prefix
    def starts_with(self, prefix: str) -> bool:
        """Checks if any word in the Trie starts with the given prefix.

        Args:
            prefix (str): The prefix to check for.

        Returns:
            bool:
            True if there is a word with the given prefix, False otherwise.
        """

        node = self.root
        for c in prefix:
            if not node.contains(c):
                return False
            node = node.next(c)
        return True


class Solution:
    """Provides a solution to count prefix and suffix pairs."""

    def count_prefix_suffix_pairs(self, words: List[str]) -> int:
        """Counts valid prefix-suffix pairs in the list of words.

        Args:
            words (List[str]): The list of words to analyze.

        Returns:
            int: The total count of valid prefix-suffix pairs.
        """

        n = len(words)
        count = 0

        # Step 1: Iterate over each word
        for i in range(n):
            prefix_trie = Trie()
            suffix_trie = Trie()

            # Step 2: Insert the current word into the prefix Trie
            prefix_trie.insert(words[i])

            # Step 3: Reverse the word and insert it into the suffix Trie
            rev_word = words[i][::-1]
            suffix_trie.insert(rev_word)

            # Step 4: Iterate over all previous words
            for j in range(i):
                # Step 5: Skip words[j] if it is longer than words[i]
                if len(words[j]) > len(words[i]):
                    continue

                # Step 6: Extract the prefix and reversed prefix of words[j]
                prefix_word = words[j]
                rev_prefix_word = prefix_word[::-1]

                # Step 7:
                # Check if words[j] is both a prefix and suffix of words[i]
                if prefix_trie.starts_with(
                    prefix_word
                ) and suffix_trie.starts_with(rev_prefix_word):
                    count += 1

        # Step 8: Return the total count of valid pairs
        return count


# Example of use
words1 = ["a", "aba", "ababa", "aa"]
words2 = ["pa", "papa", "ma", "mama"]
words3 = ["abab", "ab"]
words4 = ["mmm", "smmm", "hmmm", "hs",
          "s", "h", "s", "h", "hhmm",
          "smm", "hhh", "shh", "sh", "smmm"]

example = Solution()

print(f'words1 = {example.count_prefix_suffix_pairs(words1)}')  # 4
print(f'words2 = {example.count_prefix_suffix_pairs(words2)}')  # 2
print(f'words3 = {example.count_prefix_suffix_pairs(words3)}')  # 0
print(f'words4 = {example.count_prefix_suffix_pairs(words4)}')  # 5
