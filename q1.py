# Write a function that takes three positive numbers and returns the sum of the squares of the two largest numbers. Use only a single line for the body of the function.
def two_of_three(a, b, c):
    """Return x*x + y*y, where x and y are the two largest members of the
    positive numbers a, b, and c.

    """
    return a*a + b*b + c*c - min(a,b,c)*min(a,b,c)


print(
    two_of_three(1,2,3)
)

# 9+4 = 13....