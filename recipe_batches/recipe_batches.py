#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  # Edge case check
  if len(ingredients) is None:
    return 0

  elif len(recipe) > len(ingredients):
    return 0

  # Store batch yield by ingredient
  batches = []
  # Compare recipe quantities with available ingredients
  for key in recipe:
    if ingredients[key] < recipe[key]:
      return 0
    
    elif ingredients[key] // recipe[key] == 0:
      return 0
    
    else:
      batches.append(ingredients[key] // recipe[key])

    return min(batches)




# if __name__ == '__main__':
#   # Change the entries of these dictionaries to test 
#   # your implementation with different inputs
#   recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
#   ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
#   print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))


"""
UNDERSTANDING THE PROBLEM
1. Can I restate the problem in my own words?
  WRITE A FUNCTION THAT DETERMINES THE FOLLOWING:
  -IF YOU CAN MAKE A RECIPE BASED ON THE AVAILABLE INGREDIENTS
  -IF SO HOW MANY BATCHES CAN BE MADE BASED ON THE AVAILABLE INGREDIENTS
2. What are the input(s) that go into the problem?
	- Confirm required data types (string, integers, floats, arrays, objects)
    TWO DICTIONARIES - RECIPES, INGREDIENTS
	- Can negative numbers be included? NO
  - Confirm upper/lowercase enforcement
    KEY NAMES SHOULD ALL BE LOWERCASE - NOTE: CONFIRM WITH INTERVIEWER
	- Confirm whitespace and punctuation N/A
	- Confirm if each argument must be the same length (strings and arrays)
    UNKNOWN - NOTE: CONFIRM WITH INTERVIEWER
	- Confirm upper and lower bound limits of integers and floating points
    lower bound: 0
    upper bound: NO
3. What are the outputs that should come from the solution to the problem? POSITIVE INTEGER
4. Can the outputs be determined from the inputs? YES
5. Any time or space constraints with the solution? 
  UNKNOWN, NOTE: CHECK WITH INTERVIEWERS
6. How should I label the important pieces of data that are part of the problem?
  batches = []
"""

"""
ALGORITHM
1. Edge case check: RETURN 0
  -Empty dictionaries
  -Missing ingredients
2. Initialize an array variable called batches
2. Iterate through both dictionaries and compare keys/value pairs
  if ingredients are less than 0 break and return 0
  floor divide value of ingredients by value of recipes and append t
3. Find and return the lowest number in the batches array
"""
