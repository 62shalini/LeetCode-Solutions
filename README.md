# LeetCode 2213 - Longest Substring of One Repeating Character

## Approach

This problem is solved using a Segment Tree.

Each node stores:

- First character
- Last character
- Segment length
- Longest repeating prefix
- Longest repeating suffix
- Longest repeating substring

When two segments are merged, if the boundary characters are equal:

`left suffix + right prefix`

can form a longer repeating substring.

## Complexity

- Build: O(n)
- Each update: O(log n)
- Total: O(n + k log n)
- Space: O(n)

## Example

Input:

```text
s = "babacc"
queryCharacters = "bcb"
queryIndices = [1, 3, 3]
