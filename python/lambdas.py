from functools import reduce

multiply = lambda x, y: x * y
print(multiply(3, 6))

is_pos = lambda x: 'pos' if x >= 0 else 'neg'
is_positive = lambda x: True if x >= 0 else False
print(is_positive(4))
print(is_positive(-23))
print(is_pos(4))
print(is_pos(-23))

fruits = ["apple", "mango", "pawpaw", "banana", "pineapple", "watermelon"]
fruits.sort(key=lambda f: len(f) > 5, reverse=True)
print(fruits)

numbers = [23, -16, 34, -87, 22, 1]
print(*map(str, numbers))
print(*map(lambda *x: sum(x), [0, 1, 2], [10, 12, 13], [20, 21, 22]))

def to_dict(d, key):
    d[key] = key * key
    return d

result = reduce(to_dict, [{}] + list(range(10)))
print(result)
print(dict((x, x * x) for x in range(11)))
print(*({x: x*x for x in range(12)}))

print(*map(lambda x: x*x, numbers))

print(reduce(lambda x, y: x if x > y else y, numbers))

xc = filter(lambda z: z > 0, numbers)
xcc = reduce(lambda x, y: x if  x < y else y, xc)
print(xcc)

xcc_py = max((x for x in numbers if x < 0), default=None)
print(xcc_py)

zx = [[x+1 for x in range((row_num*3), (row_num*3)+3)] for row_num in range(3)]
print(zx)

# Capitalize the words in a string,
 # e.g. " aBc dEf "-> "Abc Def".
def capwords(s, sep=None):
    """capwords(s [,sep])-> string Split the argument into words using
    split, capitalize each word using capitalize, and join the capitalized
    words using join. If the optional second argument sep is absent or None,
    runs of whitespace characters are replaced by a single space and leading
    and trailing whitespace are removed, otherwise sep is used to split and
    join the words.
    """
    return (sep or ’ ’).join(x.capitalize() for x in s.split(sep))