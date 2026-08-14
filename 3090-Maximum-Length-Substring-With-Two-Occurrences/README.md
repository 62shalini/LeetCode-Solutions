# LeetCode 3090 - Maximum Length Substring With Two Occurrences

## Problem

Given a string `s`, find the maximum length of a substring such that each character appears at most two times.

## Approach

This problem is solved using the **Sliding Window** technique with a frequency array.

We maintain a window using two pointers:

- `left` → left boundary of the window
- `right` → right boundary of the window

The `frequency` array stores the number of occurrences of each character inside the current window.

When a character appears more than two times, we move `left` forward until the window becomes valid again.

## Algorithm

1. Initialize `left = 0`.
2. Create a frequency array of size 26.
3. Move `right` through the string.
4. Increase the frequency of `s[right]`.
5. If the current character appears more than twice, move `left` forward.
6. Calculate the current window length.
7. Update the maximum length.

## Example

### Input

```text
s = "bcbbbcba"
