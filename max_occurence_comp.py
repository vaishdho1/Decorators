''''
This program uses a timer decorator to find the time taken
for each of the functions written to pick the element with maximum
number of occurences.

The input is a random sequence of characters and the output is the time
taken by each of the different implementations.
The functions called are:
a) Counter method
b)Dictionary method
c) Set method

'''

from collections import Counter
from time import perf_counter
import random
import string


def timer(func):
    def wrapper(*args, **kwargs):
        time_start = perf_counter()
        out = func(*args, **kwargs)
        time_end = perf_counter()

        print(f"Total time taken by {func.__name__} is {time_end - time_start}")

        return out

    return wrapper


@timer
def counter_rep(str):
    out1 = Counter(str).most_common()[0]
    print("counter_rep", out1)


@timer
def dict_rep(str):
    v1 = dict.fromkeys(str)
    out2 = max(v1, key=str.count)
    print("dict_rep", out2)


@timer
def set_rep(str):
    out3 = max(set(str), key=str.count)
    print("set_rep", out3)


def main():
    str = "".join([random.choice(string.ascii_uppercase) for _ in range(100)])
    # print("string",str)
    counter_rep(str)
    dict_rep(str)
    set_rep(str)


main()