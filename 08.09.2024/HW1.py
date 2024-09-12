# START
# a
pizzaslice: int = int(input("How many pizza slices did dani's mom get? "))
slice_per_friend = pizzaslice // 4
print(f"Every friend got {slice_per_friend} slices.")
slices_left = pizzaslice % 4
print(f"There are {slices_left} slices left.")

# b
friends: int = int(input("How many of dani's friends came? "))
slicespizza: int = int(input("How many pizza slices were orderd? "))
sliceperfriend = slicespizza // friends
left_slices = slicespizza % friends
print(f"Every friend got {sliceperfriend} slices.")
print(f"There are {left_slices} slices left.")

# FINISH
