"""Assignment 1

Fill in the following function skeletons - descriptions are provided in 
the docstring (the triple quote thing at the top of each function)

Some assert statements have been provided - write more of them to test your code!

The `raise NotImplementedError(...)`s are placeholders to help you not skip implementing
a function. They should be removed and replaced with your solution.

This portion of the assignment will not be graded, but this gives you some problems to 
check, if you do not complete the generative AI portion of the assignment.
"""

from typing import List, TypeVar


def absolute(n: int) -> int:
    if n >= 0:
        n = n+n-n
    else:
        n = n-n-n
    return n
print(absolute(-3))
"""Gives the absolute value of the passed in number. Cannot use the built in
    function `abs`.

    Args:
        n - the number to take the absolute value of

    Returns:
        the absolute value of the passed in number
    """
    # raise NotImplementedError("absolute")


def factorial(n: int) -> int:
    for x in range(n-1,0,-1):
        n = n*x
    return n
print(factorial(4))
"""Takes a number n, and computes the factorial n! You can assume the passed in
    number will be positive

    Args:
        n - the number to compute factorial of

    Returns:
        factorial of the passed in number
    """
# #     raise NotImplementedError("factorial")


T = TypeVar("T")
my_list = ["a", "b", "c", "d"]
def every_other(lst: List[T]) -> List[T]:
    y = int(len(my_list))/2
    if y != int:
        for x in range(0,len(my_list),2):
            print(my_list[x])
    else:
        for x in range(0,len(my_list)-1,2):
            print(my_list[x])
every_other(my_list)
"""Takes a list and returns a list of every other element in the list, starting with
    the first.

    Args:
        lst - a list of any (constrained by type T to be the same type as the returned
            list)

    Returns:
        a list of every of other item in the original list starting with the first
    """
#     raise NotImplementedError("every_other")

int_list = [1,2,3,4]
def sum_list(lst: List[int]) -> int:
    sum = 0
    for x in range(0,len(int_list)):
        sum = sum + int(int_list[x])
    print(sum)
sum_list(int_list)
"""Takes a list of numbers, and returns the sum of the numbers in that list. Cannot
    use the built in function `sum`.

    Args:
        lst - a list of numbers

    Returns:
        the sum of the passed in list
    """
#     raise NotImplementedError("sum_list")

math_list = [1,2,3,4,5]
def mean(lst: List[int]) -> float:
    sum = 0
    count = 0
    for x in range(0,len(math_list)):
        sum = sum + int(math_list[x])
        count = count + 1
    mean = sum/count
    print(mean)
mean(math_list)
"""Takes a list of numbers, and returns the mean of the numbers.

    Args:
        lst - a list of numbers

    Returns:
        the mean of the passed in list
    """
#     raise NotImplementedError("mean")

median_list = [0,2,4,6,8]
def median(lst: List[int]) -> float:
    sum = 0
    count = 0
    for x in range(0,len(median_list)-1):
        sum = sum + int(median_list[x])
        count = count + 1
    if count%2 != 0:
        y = count//2
        print(median_list[y],",",median_list[y+1])
    else:
        y = count//2
        print(median_list[y])
median(median_list)
"""Takes an ordered list of numbers, and returns the median of the numbers.

    If the list has an even number of values, it computes the mean of the two center
    values.

    Args:
        lst - an ordered list of numbers

    Returns:
        the median of the passed in list
    """
#     raise NotImplementedError("median")

duck_list = ['Nathan', 'Sasha', 'Sara', 'Jennie']
def duck_duck_goose(lst: List[str]) -> List[str]:
    quit()
#     """Given an list of names (strings), play 'duck duck goose' with it, knocking out
#     every third name (wrapping around) until only two names are left.

#     In other words, when you hit the end of the list, wrap around and keep counting from
#     where you were.

#     For example, if given this list ['Nathan', 'Sasha', 'Sara', 'Jennie'], you'd first
#     knock out Sara. Then first 'duck' on Jennie, wrap around to 'duck' on Nathan and
#     'goose' on Sasha - knocking him out and leaving only Nathan and Jennie.

#     You may assume the list has 3+ names to start

#     Args:
#         lst - a list of names (strings)

#     Returns:
#         the resulting list after playing duck duck goose
#     """
#     raise NotImplementedError("duck_duck_goose")


# # this line causes the nested code to be skipped if the file is imported instead of run
# if __name__ == "__main__":
#     assert absolute(-1) == 1, "absolute of -1 failed"
#     assert factorial(4) == 24, "factorial of 4 failed"
#     assert every_other([1, 2, 3, 4, 5]) == [
#         1,
#         3,
#         5,
#     ], "every_other of [1,2,3,4,5] failed"
#     assert sum_list([1, 2, 3]) == 6, "sum_list of [1,2,3] failed"
#     assert mean([1, 2, 3, 4, 5]) == 3, "mean of [1,2,3,4,5] failed"
#     assert median([1, 2, 3, 4, 5]) == 3, "median of [1,2,3,4,5] failed"

#     names = ["roscoe", "kim", "woz", "solin", "law", "remess"]
#     assert duck_duck_goose(names) == ["roscoe", "law"]

    # print("All tests passed!")