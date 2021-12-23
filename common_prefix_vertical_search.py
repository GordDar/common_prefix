from typing import List


def solution(values_array: List[str]):
    prefix = []

    for x in zip(*values_array):
        if len(set(x)) == 1:
            prefix.append(x[0])
        else:
            break
    return "".join(prefix)


assert solution(['ab', 'abc', 'abcd', 'abcde']) == 'ab'
assert solution(['aba', 'abb', 'abcd', 'abcd']) == 'ab'
assert solution(['', 'abb', 'abcd', 'abcd']) == ''
assert solution(['aba', 'abb', 'abcd', 'a']) == 'a'
assert solution(['aba', 'abab', 'ababc', 'abae']) == 'aba'
assert solution([]) == ''
assert solution(['abcde']) == 'abcde'
assert solution(['a', 'b', 'c', 'b']) == ''

print(solution(['aba', 'abab', 'ababc', 'abae']))