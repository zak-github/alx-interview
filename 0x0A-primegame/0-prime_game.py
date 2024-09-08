#!/usr/bin/python3
"""
Prime Game
"""


def get_prime_numbers(n):
    """
    Generates prime numbers less than or equal to n using the Sieve of
    Eratosthenes
    """
    sieve = [True] * (n + 1)
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    return [i for i in range(2, n + 1) if sieve[i]]


def isWinner(x, nums):
    """
    runs the game for the specified rounds in nums array
    """
    invalid_nums = type(nums) is not list or len(nums) == 0 or any(
        type(n) is not int or n < 0 for n in nums)
    invalid_x = type(x) is not int or x != len(nums)
    if invalid_nums or invalid_x:
        return None

    if x == 1 and nums[0] == 1:
        return 'Ben'

    primes = get_prime_numbers(max(nums))
    if len(primes) == 0:
        return None

    stats = [len(list(filter(lambda x: x <= n, primes))) % 2 for n in nums]
    maria_wins = sum(stats)
    if maria_wins == len(stats) / 2:
        return None
    if maria_wins > len(stats) / 2:
        return 'Maria'
    else:
        return 'Ben'
