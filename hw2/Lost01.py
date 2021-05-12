'''Write a function that returns True if a positive integer n is a prime number and
False otherwise'''
'''Q1'''
def is_prime(n):
    if n <= 2:
        return True
    else:
        i = 2
        while i < n:
            if n % i == 0:
                return False
            i +=1
        return True

'''Q2'''
def ordered_digits(x):
    while x > 0:
        if (x//10)%10 <= x%10:
            x = x // 10
        else:
            return False
    return True

'''Q3 given area and perimeter, obtain the longest the length of side'''
def rect(area, perimeter):
    side = 1
    while side * side <= area:
        other = round(area/side)
        if 2 * side + 2 * other == perimeter and side * other == area:
            return max(side,other)
        side = side + 1
    return False

if __name__ == '__main__':
    print(rect(100,50))