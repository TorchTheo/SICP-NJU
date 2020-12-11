from lab06 import *

s = Link(1, Link(Link(2, Link(3)), Link(4)))
print(deep_map(lambda x: x * x, s))
print(s)
print(deep_map(lambda x: 2 * x, Link(s, Link(Link(Link(5))))))