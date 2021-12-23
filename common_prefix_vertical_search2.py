from typing import List


def solution(values_array: List[str]):
    i = 0
    common_prefix = ''

    while True:
        if len(values_array) == 0 or len(values_array[0]) - 1 < i:
            return common_prefix

        test_letter = values_array[0][i]

        for value in values_array:
            if len(value) - 1 < i or value[i] != test_letter:
                return common_prefix

        common_prefix += test_letter
        i += 1

assert solution(['ab', 'abc', 'abcd', 'abcde']) == 'ab'
assert solution(['aba', 'abb', 'abcd', 'abcd']) == 'ab'
assert solution(['', 'abb', 'abcd', 'abcd']) == ''
assert solution(['aba', 'abb', 'abcd', 'a']) == 'a'
assert solution(['aba', 'abab', 'ababc', 'abae']) == 'aba'
assert solution([]) == ''
assert solution(['abcde']) == 'abcde'
assert solution(['a', 'b', 'c', 'b']) == ''