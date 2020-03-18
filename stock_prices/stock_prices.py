#!/usr/bin/python

import argparse

def find_max_profit(prices):
  #setting max profit to -infinity
  max_profit = float('-inf')
  # for every item (from 0 to however many items there are)
  for i in range(0, len(prices)-1):
    # setting purchase amount to prices list at every index
    purchase = prices[i]
    # setting j to the purchase amount to the right of the index
    for j in range(i+1, len(prices)-1):
      #setting profit to j subtract i
      profit = prices[j] - purchase
      #if the profit is greater than max_profit then set max_profit equal to profit
      if profit > max_profit:
        max_profit = profit

  return max_profit 


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))