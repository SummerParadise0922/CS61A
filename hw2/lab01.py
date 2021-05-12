def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    if k == 0:
        return 1
    elif k > n:
        return 0
    else:
        factor = 1
        i = 0
        while i<k:
            factor *= (n-i)
            i += 1
        return factor

def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    sum = 0
    while y > 0:
        sum += y % 10
        y = y//10
        # sum, y = sum + y % 10, y//10
    return sum



def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    # prev_eight = False
    # while n > 0:
    #     last_digit = n % 10
    #     n = n // 10
    #     if last_digit==8 and prev_eight:
    #         return True
    #     elif last_digit == 8:
    #         prev_eight = True
    #     else:
    #         prev_eight = False
    # return False
    count = 0
    while n!=0:
        number = n%10
        n = n//10
        if number == 8:
            count +=1
        else:
            count = 0
        if count == 2:
            return True
    return False


if __name__ == '__main__':
    print(double_eights(80808080))