#!/usr/bin/python3
"""
Maria and Ben are playing a game. Given a set of
consecutive integers starting from 1 up to and including n,
they take turns choosing a prime number from the set and removing
that number and its multiples from the set. The player that cannot
make a move loses the game.
"""


def isWinner(x, nums):
    """
    Determines the winner of the prime number game.

    Args:
        x (int): Number of rounds.
        nums (list): List of integers representing the n values for each round.

    Returns:
        str: Name of the player with the most wins ("Maria" or "Ben").
             If the winner cannot be determined, return None.
    """
    if x < 1 or not nums:
        return None

    # Precompute prime numbers using the Sieve of Eratosthenes
    # up to the maximum n
    max_n = max(nums)
    primes = [True] * (max_n + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not prime

    for i in range(2, int(max_n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_n + 1, i):
                primes[j] = False

    # Precompute the number of primes up to each n
    prime_counts = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_counts[i] = prime_counts[i - 1] + (1 if primes[i] else 0)

    maria_wins = 0
    ben_wins = 0

    # Determine the winner for each round
    for n in nums:
        # Number of primes up to n determines the number of moves
        if prime_counts[n] % 2 == 1:
            # Maria wins if the count of primes is odd
            maria_wins += 1
        else:
            # Ben wins if the count of primes is even
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
