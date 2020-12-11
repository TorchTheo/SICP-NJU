""" Homework 3: Recursion and Tree Recursion"""

HW_SOURCE_FILE = 'hw03.py'


#####################
# Required Problems #
#####################
def num_sevens(x):
    """Returns the number of times 7 appears as a digit of x.

    >>> num_sevens(3)
    0
    >>> num_sevens(7)
    1
    >>> num_sevens(7777777)
    7
    >>> num_sevens(2637)
    1
    >>> num_sevens(76370)
    2
    >>> num_sevens(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_sevens',
    ...       ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"

    def s(n, ans):
        if n == 0:
            return ans
        elif n % 10 == 7:
            return s(n // 10, ans + 1)
        else:
            return s(n // 10, ans)

    return s(x, 0)


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"

    def other(who):
        return 1 - who

    def s(x, who, num):
        if x == n:
            return num
        if num_sevens(x) or x % 7 == 0:
            if who == 1:
                return s(x + 1, other(who), num - 1)
            else:
                return s(x + 1, other(who), num + 1)
        else:
            if who == 1:
                return s(x + 1, who, num + 1)
            else:
                return s(x + 1, who, num - 1)

    return s(1, 1, 1)


def count_change(total):
    """Return the number of ways to make change for total.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_change', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    if total == 1:
        return 1
    if total % 2 != 0:
        total -= 1
    return count_change(total / 2) + count_change(total - 1)
    # if total % 2:
    #     total = total - 1
    #
    # def s(t):
    #     if t < 0:
    #         return 0
    #     else:
    #         return 2 ** (total // 4 - t // 4) + s(t - 2)
    # if (total // 2) % 2 != 0:
    #     return s(total)
    # else:
    #     total -= 2
    #     return s(total) + (total + 2) // 4 + 1
    # 2 ** (((total + 2) // 4) - 1) + 1


def missing_digits(n):
    """Given a number a that is in sorted, increasing order,
    return the number of missing digits in n. A missing digit is
    a number between the first and last digit of a that is not in n.
    >>> missing_digits(1248) # 3, 5, 6, 7
    4
    >>> missing_digits(1122) # No missing numbers
    0
    >>> missing_digits(123456) # No missing numbers
    0
    >>> missing_digits(3558) # 4, 6, 7
    3
    >>> missing_digits(4) # No missing numbers between 4 and 4
    0
    >>> from construct_check import check
    >>> # ban while or for loops
    >>> check(HW_SOURCE_FILE, 'missing_digits', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"

    def s(first, last, index, now, ans):  # now为当前数字
        if now == last:
            return ans
        else:
            if now != int(str(n)[index]):
                return s(first, last, index, now + 1, ans + 1)
            else:
                if int(str(n)[index]) == int(str(n)[index + 1]):
                    return s(first, last, index + 1, now, ans)
                else:
                    return s(first, last, index + 1, now + 1, ans)
    # if n < 10:
    #     return 0
    # else:
    return s(int(str(n)[0]), int(str(n)[len(str(n)) - 1]), 0, int(str(n)[0]), 0)


###################
# Just for fun Questions #
###################

def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)


def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"

from operator import sub, mul


def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> make_anonymous_factorial()(6)
    720
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    return lambda x: x if x == 1 else mul(x, (lambda: make_anonymous_factorial)()()(x - 1))






