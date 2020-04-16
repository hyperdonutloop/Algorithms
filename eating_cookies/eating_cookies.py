#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution

# count the number of ways there are to eat 'n' number of cookies
# can only eat 0, 1, 2, or 3 cookies at a time

# 1 cookie - 1 way
# 2 cookies - 1 cookie, 1 cookie | 2 cookies
# 3 - 111, 21,12, 3
# 4 - 1111, 1211, 112, 13, 211, 22, 31
# 5 - 11111, 1112, 1121, 1211, 2111, 113, 131, 311, 122, 221, 212, 23, 32, THIS IS 13 ways
# 11111
# 1112
# 1121
# 113
# 1211
# 122
# 131
# 2111
# 212
# 221
# 23
# 311
# 32
# to get all the 5's add four + 3 + 2

def eating_cookies(n, cache=None):
  # anytime you are doing a calculation more than once you can CACHE it, cache the results once you calculate it. 
  if cache is None:
    cache = {}
  # base cases
  # if cookies is 0
  if n == 0:
    # return 1 bc there is only 1 way to eat zero cookies
    return 1

  # if cookies = 1
  elif n == 1:
    # return 1  there is one way to eat 1 cookie
    return 1

  # if cookies = 2
  elif n == 2:
    # return 2 because there is 2 ways to eat 2 cookies
    return 2

  # if cookies = 3
  elif n == 3:
    # return 4 because there is only 4 ways to eat three cookies
    return 4

  elif cache and cache[n]:
    return cache[n]
    # this is in the case of FOUR COOKIES IN THE JAR
    # n-1 is 4 - 1, which is 3. And the CACHE value for n = 3 is 4
    # n-2 is 4 -2, which is 2, and the CACHE value for n = 2, is 2
    # n-3 is 4-3, which is 1, and the CACHE value for n = 1, is 1
    # total ways to eat FOUR cookies would be SEVEN
  else:
    cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
  
  return cache[n]

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')