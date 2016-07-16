def count_chars(s):
    counts = dict()
    for c in s:
        counts[c] = counts.get(c, 0) + 1
    return counts

def is_permutation(first, second):
    first_counts = count_chars(first)
    second_counts = count_chars(second)

    return first_counts == second_counts

tests = [
    ('abc', 'abc', True),
    ('abc', 'aba', False),
    ('abc', 'acb', True),
    ('abc', 'cba', True),
    ('abc', 'cab', True),
    ('abc', '', False),
    ('', '', True),
    ('aaa', 'aa', False),
    ('abba', 'bbaa', True),
]

for first, second, expected in tests:
    if (is_permutation(first, second) == expected):
        print('PASS')
    else:
        print('FAIL')


