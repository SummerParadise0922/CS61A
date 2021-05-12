from operator import add, mul, sub
square = lambda x: x * x
identity = lambda x: x
triple = lambda x: 3 * x
increment = lambda x: x + 1

def product(n, term):
    """Return the product of the first n terms in a sequence.
    n -- a positive integer
    term -- a function that takes one argument to produce the term

    # >>> product(3, identity)  # 1 * 2 * 3
    # 6
    # >>> product(5, identity)  # 1 * 2 * 3 * 4 * 5
    # 120
    # >>> product(3, square)    # 1^2 * 2^2 * 3^2
    # 36
    # >>> product(5, square)    # 1^2 * 2^2 * 3^2 * 4^2 * 5^2
    # 14400
    # >>> product(3, increment) # (1+1) * (2+1) * (3+1)
    # 24
    # >>> product(3, triple)    # 1*3 * 2*3 * 3*3
    # 162
    """
    "*** YOUR CODE HERE ***"
    i = 1
    product = 1
    while i <= n:
        product  *= term(i)
        i += 1
    return product


def square(x):
    return x * x


def accumulate(combiner, base, n, term):
    """Return the result of combining the first n terms in a sequence and base.
    The terms to be combined are term(1), term(2), ..., term(n).  combiner is a
    two-argument commutative function.

    # >>> accumulate(add, 0, 5, identity)  # 0 + 1 + 2 + 3 + 4 + 5
    # 15
    # >>> accumulate(add, 11, 5, identity) # 11 + 1 + 2 + 3 + 4 + 5
    # 26
    # >>> accumulate(add, 11, 0, identity) # 11
    # 11
    # >>> accumulate(add, 11, 3, square)   # 11 + 1^2 + 2^2 + 3^2
    # 25
    # >>> accumulate(mul, 2, 3, square)    # 2 * 1^2 * 2^2 * 3^2
    # 72
    # >>> accumulate(lambda x, y: x + y + 1, 2, 3, square)
    # 19
    # >>> accumulate(lambda x, y: 2 * (x + y), 2, 3, square)
    # 58
    # >>> accumulate(lambda x, y: (x + y) % 17, 19, 20, square)
    # 16
    """
    "*** YOUR CODE HERE ***"
    i = 1
    while i <= n:
        base = combiner(term(i), base)
        i += 1
    return base


def summation_using_accumulate(n, term):
    """Returns the sum of term(1) + ... + term(n). The implementation
    uses accumulate.

    # >>> summation_using_accumulate(5, square)
    # 55
    # >>> summation_using_accumulate(5, triple)
    # 45
    # >>> from construct_check import check
    # >>> # ban iteration and recursion
    # >>> check(HW_SOURCE_FILE, 'summation_using_accumulate',
    # ...       ['Recursion', 'For', 'While'])
    True
    """
    "*** YOUR CODE HERE ***"
    sum, i = 0, 1
    while i <= n:
        sum += term(i)
    return sum

def product_using_accumulate(n, term):
    """An implementation of product using accumulate.

    # >>> product_using_accumulate(4, square)
    # 576
    # >>> product_using_accumulate(6, triple)
    # 524880
    # >>> from construct_check import check
    # >>> # ban iteration and recursion
    # >>> check(HW_SOURCE_FILE, 'product_using_accumulate',
    # ...       ['Recursion', 'For', 'While'])
    True
    """
    "*** YOUR CODE HERE ***"
    product, i = 1, 1
    while i <= n:
        product *= term(i)
    return product


def compose1(func1, func2):
    """Return a function f, such that f(x) = func1(func2(x))."""
    def f(x):
        return func1(func2(x))
    return f


def make_repeater(func, n):
    """Return the function that computes the nth application of func.

    # >>> add_three = make_repeater(increment, 3)
    # >>> add_three(5)
    # 8
    # >>> make_repeater(triple, 5)(1) # 3 * 3 * 3 * 3 * 3 * 1
    # 243
    # >>> make_repeater(square, 2)(5) # square(square(5))
    # 625
    # >>> make_repeater(square, 4)(5) # square(square(square(square(5))))
    # 152587890625
    # >>> make_repeater(square, 0)(5) # Yes, it makes sense to apply the function zero times!
    # 5
    """
    "*** YOUR CODE HERE ***"
    # try use compose1 and acculumate to state
    def f(x):
        i = 1
        while i <= n:
            x = func(x)
            i += 1
        return x
    return f

def make_repeater_oneline(func,n):
    return accumulate(compose1, lambda x: x, n, lambda k: func)


if __name__ == "__main__":
    print(make_repeater_oneline(triple, 5)(1))