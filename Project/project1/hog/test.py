

def free_bacon(score):
    """Return the points scored from rolling 0 dice (Free Bacon).

    score:  The opponent's current score.

    >>> free_bacon(4)
    3
    >>> free_bacon(1)
    2
    >>> free_bacon(20)
    9
    >>> free_bacon(45)
    13
    """
    assert score < 100, 'The game should be over.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    num = 1
    ans = 0
    if score == 1:
        return 2
    else:
        x = score ** 3
        last_digit = x % 10
        first_digit = x
        pre = 0
        while first_digit // 10:
            num += 1
            first_digit = first_digit // 10
        for i in range(1, num + 1):
            t = x // (10 ** (num - i))
            ans += ((-1) ** (i + 1)) * t
            x -= t * (10 ** (num - i))
    return 1 + ans if(ans > 0) else 1 - ans
