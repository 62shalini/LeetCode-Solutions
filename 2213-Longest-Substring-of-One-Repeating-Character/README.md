# LeetCode 2213 - Longest Substring of One Repeating Character

## Problem

Given a string `s`, each query changes one character in the string.

After every update, find the length of the longest substring consisting of only one repeating character.

## Approach

This problem can be solved efficiently using a **Segment Tree**.

Each segment tree node stores:

- First character of the segment
- Last character of the segment
- Length of the segment
- Longest repeating prefix
- Longest repeating suffix
- Longest repeating substring inside the segment

When two nodes are merged, if the last character of the left segment is equal to the first character of the right segment, their suffix and prefix can be combined.

```text
crossing_length = left_suffix + right_prefix
```
The maximum answer is:

max(left_best, right_best, crossing_length)
Complexity
Build: O(n)
Each update: O(log n)
Total: O(n + k log n)
Space: O(n)
Example

Input:

s = "babacc"
queryCharacters = "bcb"
queryIndices = [1, 3, 3]

Output:

[3, 3, 4]

Data Stored in Each Node
[first_character,
 last_character,
 length,
 prefix,
 suffix,
 best]
