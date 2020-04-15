#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  # creating a new array to put in how many batches you can make with ingredients you have(the second array)
  batches = [] 
  # looping through the recipe list
  for i in recipe:
    # if the item is not in the ingredients array
    if i not in ingredients:
      # you can't make recipes, so return 0
      return 0
    # dividing ingredient amount by recipe amount, and as long as it is greater than 1
    elif ingredients[i] // recipe[i] >= 1:
      # the batches I can make is equal to the ingredients // recipe amount
      batch_i_can_make = ingredients[i] // recipe[i]
      # appending the 'batches i can make' to the batches array
      batches.append(batch_i_can_make)
    else:
      return 0

  return min(batches)


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))