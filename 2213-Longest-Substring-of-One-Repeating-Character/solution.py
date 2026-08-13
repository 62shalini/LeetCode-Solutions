from typing import List


class Solution:
    def longestRepeating(
        self,
        s: str,
        queryCharacters: str,
        queryIndices: List[int]
    ) -> List[int]:

        n = len(s)
        segment_tree = [None] * (4 * n)

        def merge(left_node, right_node):
            if left_node is None:
                return right_node

            if right_node is None:
                return left_node

            left_char = left_node[0]
            left_right_char = left_node[1]
            left_length = left_node[2]
            left_prefix = left_node[3]
            left_suffix = left_node[4]
            left_best = left_node[5]

            right_left_char = right_node[0]
            right_char = right_node[1]
            right_length = right_node[2]
            right_prefix = right_node[3]
            right_suffix = right_node[4]
            right_best = right_node[5]

            total_length = left_length + right_length

            prefix = left_prefix

            if left_right_char == right_left_char:
                if left_prefix == left_length:
                    prefix = left_length + right_prefix

            suffix = right_suffix

            if left_right_char == right_left_char:
                if right_suffix == right_length:
                    suffix = right_length + left_suffix

            best = max(left_best, right_best)

            if left_right_char == right_left_char:
                best = max(best, left_suffix + right_prefix)

            return [
                left_char,
                right_char,
                total_length,
                prefix,
                suffix,
                best
            ]

        def build(tree_node, start, end):
            if start == end:
                segment_tree[tree_node] = [
                    s[start], s[start], 1, 1, 1, 1
                ]
                return

            middle = (start + end) // 2

            build(tree_node * 2, start, middle)
            build(tree_node * 2 + 1, middle + 1, end)

            segment_tree[tree_node] = merge(
                segment_tree[tree_node * 2],
                segment_tree[tree_node * 2 + 1]
            )

        def update(tree_node, start, end, index, new_char):
            if start == end:
                segment_tree[tree_node] = [
                    new_char, new_char, 1, 1, 1, 1
                ]
                return

            middle = (start + end) // 2

            if index <= middle:
                update(
                    tree_node * 2,
                    start,
                    middle,
                    index,
                    new_char
                )
            else:
                update(
                    tree_node * 2 + 1,
                    middle + 1,
                    end,
                    index,
                    new_char
                )

            segment_tree[tree_node] = merge(
                segment_tree[tree_node * 2],
                segment_tree[tree_node * 2 + 1]
            )

        build(1, 0, n - 1)

        answer = []

        for new_char, index in zip(
            queryCharacters,
            queryIndices
        ):
            update(
                1,
                0,
                n - 1,
                index,
                new_char
            )

            answer.append(segment_tree[1][5])

        return answer
