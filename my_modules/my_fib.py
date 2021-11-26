from functools import lru_cache

@lru_cache
def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    print(fib(5))
    print(fib(10))
    print(fib(15))
    print(fib(33))
    print(fib(53))
    print(fib(73))

