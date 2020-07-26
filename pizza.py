# Store some information about a pizza being ordered.

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# Sumarize order
print(f"You ordered a {pizza['crust']}-crust pizza "
      "with the following toppins:")

for topping in pizza['toppings']:
    print(f"\t{topping}")
