from typing import List


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:

        max_length = 0
        frequency = [0] * 26

        left = 0

        for right in range(len(s)):

            frequency[ord(s[right]) - ord('a')] += 1

            while frequency[ord(s[right]) - ord('a')] > 2:

                frequency[ord(s[left]) - ord('a')] -= 1
                left += 1

            current_length = right - left + 1
            max_length = max(max_length, current_length)

        return max_length
