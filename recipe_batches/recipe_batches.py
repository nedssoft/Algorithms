#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):

  #  Initialize batches to zero
  batches = 0

  while True:
    # Loop through recipe
    for key in recipe:
      # Check if the recipe is in the ingredients
        if key in ingredients:
          # If the recipe is in ingredient, check if the ingredient makes up to a batch
          if (ingredients[key] < recipe[key]):
            return batches
          else:
            # Remove a batch quantity from ingredients
            ingredients[key] -= recipe[key]
        else:
          return batches
    batches += 1
  
if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))

  
 
