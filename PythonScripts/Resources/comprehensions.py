# -*- coding: UTF-8 -*-
"""Comprehensions"""

price_strings = ["24", "13", "16000", "1400"]
price_nums = [int(price) for price in price_strings]

fish = "halibut"

# Comprehensions give handles on each element of a collection
letters = [letter for letter in fish]

print(f"We iterate over a string, containing the world: '{fish}'")
print(f"This turns our string into a list: {letters}.")

# We can manipulate each element as we go
capital_letters = [letter.upper() for letter in letters]

print(f"This capitalizes the letters in our list: {capital_letters}.")

# We can remove elements with a boolean test
no_h = [letter for letter in letters if letter != "h"]
dysfunctional_fish = "".join(no_h)

no_h_or_b = [letter for letter in letters if letter != "h" and letter != "b"]
dysfunctional_fish = "".join(no_h_or_b)

print(f"And our filtered string is: {dysfunctional_fish}.")
print("=" * 72)

june_temperatures = [72, 65, 59, 87]
july_temperatures = [87, 85, 92, 79]
august_temperatures = [87, 77, 68, 72]
summer_temperatures = [june_temperatures, july_temperatures, august_temperatures]

# We can use functions inside of list comprehensions
lowest_summer_temperatures = [min(temps) for temps in summer_temperatures]

print(f"The lowest temperature in June was: {lowest_summer_temperatures[0]}.")
print(f"The lowest temperature in July was: {lowest_summer_temperatures[1]}.")
print(f"The lowest temperature in August was: {lowest_summer_temperatures[-1]}.")
