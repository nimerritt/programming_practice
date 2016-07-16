# 1.3 from CtCI
# A bit silly in python

def urlify(s):
    return s.replace(' ', '%20')

tests = [
    ('abc', 'abc'),
    ('a c', 'a%20c'),
    ('   ', '%20%20%20'),
    ]

for test, expected in tests:
    result = urlify(test)
    if (result != expected):
        print('{} FAILED'.format(test, 'FAIL'))
        print('Expected {} on input "{}" but got {}'.format(expected, test, result))
        break
else:
    print('{} tests passed'.format(len(tests)))

