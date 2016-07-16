def is_unique(s):
    counts = dict()
    for c in s:
        if c in counts:
            return False
        counts[c] = 1
    return True

tests = [
    ('abc', True),
    ('abb', False),
    ('', True),
    ('a', True),
    ('aa', False),
    ]

for test, expected in tests:
    print('"{}" {}'.format(test, 'Pass' if is_unique(test) == expected else 'Fail'))
