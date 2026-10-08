"""FibonacciRecursion"""
memo = {0:0, 1:1}
def fibonacci_memo(n):
    """fibonacci calculate"""
    if n in memo:
        return memo[n]
    result = fibonacci_memo(n - 1) + fibonacci_memo(n - 2)
    memo.update({n: result})
    return result

x, limit = int(input()), 900
while True:
    try:
        print(fibonacci_memo(x))
        break
    except RecursionError:
        fibonacci_memo(limit)
        limit += 900
        continue
