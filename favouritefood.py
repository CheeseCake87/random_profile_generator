import random

def favouritefood():
  favfood = ["apples","bananas","oranges","peanuts", "chickpeas", "peas", "potatoes", "tomatoes", "cheese", "shrimp", "kiwis", "rice","fish", "sushi","pizza", "chips", "fries", "pancakes", "waffles" ]

  

  random_foodnum = random.randint(0, 19)

  favfood1 = (''.join((favfood[random_foodnum])))

  favfood = (f"Your favourite food is: {favfood1}")


  return favfood