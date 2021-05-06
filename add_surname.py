# Author: Samuel Bennett
# Date: 5/5/2021
# Description: Takes a parameter list of first names and uses a list comprehension to return a list that contains only those names that start with a "K" but with the surname "Kardashian" added to each one.

names = ["Kiki", "Krystal", "Pavel", "Sally", "MaryKay", "Annie", "Koala"]

k_names = [first for first in names if first.startswith("K")]

lastname = " Kardadhian"

newlist = [k_names[0] + lastname, k_names[1] + lastname, k_names[2] + lastname]

print(newlist)

