from functools import reduce
from typing import List


def solution(values_array: List[str]):
    def reduce_handler(acc, value):
        common_prefix = ''

        for index, letter in enumerate(acc):
            if len(value) - 1 < index or letter != value[index]:
                return common_prefix
            common_prefix += letter

        return common_prefix

    return reduce(reduce_handler, values_array, values_array[0] if len(values_array) else '')

assert solution(['ab', 'abc', 'abcd', 'abcde']) == 'ab'
assert solution(['aba', 'abb', 'abcd', 'abcd']) == 'ab'
assert solution(['', 'abb', 'abcd', 'abcd']) == ''
assert solution(['aba', 'abb', 'abcd', 'a']) == 'a'
assert solution(['aba', 'abab', 'ababc', 'abae']) == 'aba'
assert solution([]) == ''
assert solution(['abcde']) == 'abcde'
assert solution(['a', 'b', 'c', 'b']) == ''

print(solution(['aba', 'abab', 'ababc', 'abae']))