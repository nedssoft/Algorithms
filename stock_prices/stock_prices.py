#!/usr/bin/python

import argparse

"""
 - Initialize find max_profit_so_far to the difference of the second and the last arg
 - if there's only two integers, set max_price_so_far to second item minus first item
 - If there are more than 2 integers, loop through the prices and find the max_profit_so_far 
 - Return max_price_so_far 
"""
def find_max_profit(prices):

  # Assume the current min price to be first item
  current_min_price_index = 0
  # Assume the current_max_price to be second item
  current_max_price_index  = 1
  max_profit_so_far = prices[current_max_price_index] - prices[current_min_price_index]
  
  #Loop through the prices, taking one at a time as the current min price
  for i in range(len(prices) -1 ):
    current_min_price_index = i
    # Loop through the RHS of the current min price and find the max_profit
    for j in range(i+1, len(prices)):
      current_max_price_index = j
      current_max_profit = prices[current_max_price_index] - prices[current_min_price_index]
      
      # Let's be sure the max_profit so far is the best possible
      if (current_max_profit > max_profit_so_far):

        max_profit_so_far = current_max_profit
  return max_profit_so_far


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))