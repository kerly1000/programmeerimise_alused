"""Close far."""


def close_far(a: int, b: int, c: int) -> bool:
    """
    Return if one value is "close" and other is "far".

    Given three ints, a b c, return true if one of b or c is "close" (differing from a by at most 1),
    while the other is "far", differing from both other values by 2 or more.

    close_far(1, 2, 10) => True
    close_far(1, 2, 3) => False
    close_far(4, 1, 3) => True
    """

    b_close = abs(b - a) <= 1
    c_far = abs(c - a) >= 2 and abs(c - b) >= 2
    return b_close and c_far

def close_far(a: int, b: int, c: int) -> bool:
    b_close = abs(b - a) <= 1
    c_close = abs(c - a) <= 1

    b_far = abs(b - a) >= 2 and abs(b - c) >= 2
    c_far = abs(c - a) >= 2 and abs(c - b) >= 2

    if (b_close and c_far) or (c_close and b_far):
        return True
    else:
        return False
