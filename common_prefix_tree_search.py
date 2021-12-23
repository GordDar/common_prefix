from typing import List


# O(log n)

def solution(values_array: List[str]):
    if not len(values_array):
        return ''

    current_level_queue = values_array
    next_level_queue = []

    while len(current_level_queue) != 1:
        for i in range(0, len(current_level_queue), 2):
            if len(current_level_queue) - 1 == i:
                next_level_queue.append(current_level_queue[i])
                break

            common_prefix = ''
            for index, letter in enumerate(current_level_queue[i]):
                if len(current_level_queue[i + 1]) - 1 < index or current_level_queue[i + 1][index] != letter:
                    break
                common_prefix += letter

            next_level_queue.append(common_prefix)

        current_level_queue = next_level_queue
        next_level_queue = []

    return current_level_queue[0]


assert solution(['ab', 'abc', 'abcd', 'abcde']) == 'ab'
assert solution(['aba', 'abb', 'abcd', 'abcd']) == 'ab'
assert solution(['', 'abb', 'abcd', 'abcd']) == ''
assert solution(['aba', 'abb', 'abcd', 'a']) == 'a'
assert solution(['aba', 'abab', 'ababc', 'abae']) == 'aba'
assert solution([]) == ''
assert solution(['abcde']) == 'abcde'
assert solution(['a', 'b', 'c', 'b']) == ''
assert solution(['flower', 'flow', 'flight']) == 'fl'

print(solution(['aba', 'abab', 'ababc', 'abae']))