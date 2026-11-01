# Reflection:
# 1. I was surprised by how easy it is to add, remove, and change items in a list.
#  I thought it would be more complicated, but Python makes it simple to manage many items together.

# 2. When I worked in logistics in the army, I had to manage equipment and keep track of inventory.
# Using Python lists could have helped me organize the equipment, update the inventory,
# and save time compared to doing everything manually in Excel.

# Exercise 1 
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

# Exercise 2 
print(inventory[0])
print(inventory[-1])
print(inventory[len(inventory) // 2])

# Exercise 3 
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])

# Exercise 4 
inventory.append("envelope")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort()
print(inventory)

# Exercise 5 
coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError:
    print("Tuples cannot be changed after they are created.")
    print("This is useful for coordinates because it keeps them safe from changes.")
print(coords)

# Exercise 6 
sales = [100, 250, 75, 480, 200]

total = sum(sales)
count = len(sales)
average = total / count
best = max(sales)
worst = min(sales)

print("Total:", total)
print("Count:", count)
print("Average:", average)
print("Best:", best)
print("Worst:", worst)

# Exercise 7 
prices = [9.99, 14.99, 4.99, 24.99, 1.99]

discounted = []

for price in prices:
    new_price = round(price * 0.90, 2)
    discounted.append(new_price)
print("Original prices:", prices)
print("Discounted prices:", discounted)

# Exercise 8 
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []

for sale in sales:
    if sale > 300:
        high_sales.append(sale)

count = len(high_sales)
average = sum(high_sales) / count

print("High sales:", high_sales)
print("Count:", count)
print("Average:", round(average, 2))