#!/usr/bin/python

import argparse

def find_max_profit(prices):
  current_min_price = prices[0]
  max_profit = 0 - prices[0]
  
  for i in range(1, len(prices)):
    for j in range(i-1, 0, -1):
      print(f"compare {prices[j]} with {current_min_price}")
      if prices[j] < current_min_price:
        print(f"lower price at: {prices[j]}")
        current_min_price = prices[j]
    print(f"current max_profit {max_profit} at stock price {prices[i]} low price {current_min_price}")
    if max_profit < (prices[i] - current_min_price):
      max_profit = prices[i] - current_min_price
      print(f"updated max_profit: {max_profit}")

  return max_profit


stock_prices = [1050, 270, 1540, 3800, 2]
#stock_prices = [100, 90, 80, 50, 20, 10]
print(find_max_profit(stock_prices))

# if __name__ == '__main__':
#   # This is just some code to accept inputs from the command line
#   parser = argparse.ArgumentParser(description='Find max profit from prices.')
#   parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#   args = parser.parse_args()

#   print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))

"""
UNDERSTANDING THE PROBLEM
1. Can I restate the problem in my own words?
  Find the largest difference between a given stock price and its previous stock prices, RETURN THAT DIFFERENCE
2. What are the input that go into the problem?
	- Confirm required data types (string, integers, floats, arrays, objects)
    ARRAY OF INTEGERS
	- Can negative numbers be included? 
    STOCK PRICES CAN'T BE NEGATIVE BUT PROFIT CAN BE
  - Confirm upper/lowercase enforcement N/A
	- Confirm whitespace and punctuation N/A
	- Confirm if each argument must be the same length (strings and arrays) NO
	- Confirm upper and lower bound limits of integers and floating points
    lower bound: 0
    upper bound: NO
3. What are the outputs that should come from the solution to the problem? INTEGER
4. Can the outputs be determined from the inputs? YES
5. Any time or space constraints with the solution? UNKNOWN, NOTE: CHECK WITH INTERVIEWERS
6. How should I label the important pieces of data that are part of the problem?
  current_min_price = first element in the array, max_profit_so_far = 0
"""

"""
ALGORITHM
1. Initialize variables
2. Address edge cases empty or single element arrays
3. Iterate through the array for i starting at 1
    4. If arr[i] < current_min_price:
      current_min_price = arr[i]
      
    5. If max_profit < (arr[i] - current_min_price):
      max_profit = arr[i] - current_min_price
4. return max_profit
"""
