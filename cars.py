# Instructions
# Create an empty set named showroom.
showroom = set()

# Add four of your favorite car model names to the set.
showroom.add("Mustang")
showroom.add("Model 3")
showroom.add("Tucson")
showroom.add("Bug")
# Print the length of your set.
print("number of cars in showroom:",len(showroom))
# Pick one of the items in your show room and add it to the set again. Print your showroom. Notice how there's still only one instance of that model in there.
showroom.add("Mustang")
print("Attempting to add repeat to set:",showroom)

# Using update(), add two more car models to your showroom with another set.
showroom.update({"LS460", "A6", "Sonata"})
print("update method:",showroom)
# You've sold one of your cars. Remove it from the set with the discard() method.
showroom.discard("A6")
print("Discard method:",showroom)

# Now create another set of cars in a variable junkyard. Someone who owns a junkyard full of old cars has approached you about buying the entire inventory. In the new set, add some different cars, but also add a few that are the same as in the showroom set.
junkyard = {"LS430", "Model 3", "Bug", "Honda", "A3"}
# Use the intersection method to see which cars exist in both the showroom and that junkyard.
print("intersection between junkyard and showroom:",showroom.intersection(junkyard))
acquired_cars = junkyard.difference(showroom)
print("cars available in the junkyard that you do not currently have in your showroom:",acquired_cars)
# Now you're ready to buy the cars in the junkyard. Use the union method to combine the junkyard into your showroom.
print("updated showroom inventory:",showroom.union(junkyard))
# Use the discard() method to remove any cars that you acquired from the junkyard that you want in your showroom.
for car in acquired_cars:
  junkyard.discard(car)

print("final junkyard inventory:",junkyard)