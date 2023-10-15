#!/usr/bin/env python3

""" In a text file, there is a single character H. Your text editor can\
 execute only two operations in this file: Copy All and Paste. Given a \
 number n, write a method that calculates the fewest number of operations\
 needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    """ return an integer"""
    if n <= 1:
        return 0

    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        dp[i] = i
        for j in range(i - 1, 1, -1):
            if i % j == 0:
                dp[i] = dp[j] + (i // j)
                break

    return dp[n]
