# Self-Assessment 1:
# The first bug I found was a missing colon in the for loop.
# I found it by reading the traceback.
# This showed me that the traceback can help me find syntax errors quickly.

# Self-Assessment 2:
# The apply_discount function takes a price and a customer tier.
# It checks the tier and gives the correct discount.
# It returns the new price after the discount.
# Someone could use it by giving it a price and a tier.

# Self-Assessment 3:
# I used AI to help explain some error messages during the lab.
# It helped me understand the errors, and I made the fixes myself.

# Exercise 1:
def calculate_tax(price, rate):
    return price * rate
print(f"Tax on $100 at 7%: ${calculate_tax(100, 0.07):.2f}")
print(f"Tax on $250 at 8%: ${calculate_tax(250, 0.08):.2f}")

# Exercise 2:
def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price
print(f"gold:   ${apply_discount(200, 'gold'):.2f}")
print(f"silver: ${apply_discount(200, 'silver'):.2f}")
print(f"bronze: ${apply_discount(200, 'bronze'):.2f}")
print(f"none:   ${apply_discount(200, 'none'):.2f}")

# Exercise 3:
discounted = apply_discount(200, "gold")
print(f"After gold discount: ${discounted:.2f}")
tax = calculate_tax(discounted, 0.07)
total = discounted + tax
print(f"After tax: ${total:.2f}")
def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax
print(f'final_price(200, "gold", 0.07) = ${final_price(200, "gold", 0.07):.2f}')

# Exercise 4:
orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]
for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")

    # Exercise 5:
sales = [120, 80, 250, 175, 90]
# Bug 3: total was being replaced each time instead of adding each sale.
total = 0
for sale in sales:
    total += sale
print(f"Total: ${total}")
count = 0
# Bug 1: The for loop was missing a colon at the end.
for sale in sales:
    count += 1
print(f"Count: {count}")
# Bug 2: The while loop went one index too far because it used <=.
i = 0
while i < len(sales):
    print(sales[i])
    i += 1

    # Exercise 6:
x = 100
def double_it():
    x = 999
    return x * 2
print(x)
print(double_it())
print(x)
# Scope means a variable inside a function only exists inside that function.
# The local x does not change the global x.