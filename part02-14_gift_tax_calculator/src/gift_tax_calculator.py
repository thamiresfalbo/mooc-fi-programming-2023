# Write your solution here

gift_value = int(input("Value of gift:"))

if gift_value < 25_000:
    tax_lower_limit = 100
    tax_rate = 0.08
    lower_limit = 5_000
elif gift_value < 55_000:
    tax_lower_limit = 1_700
    tax_rate = 0.10
    lower_limit = 25_000
elif gift_value < 200_000:
    tax_lower_limit = 4_700
    tax_rate = 0.12
    lower_limit = 55_000
elif gift_value < 1_000_000:
    tax_lower_limit = 22_100
    tax_rate = 0.15
    lower_limit = 200_000
elif gift_value > 1_000_000:
    tax_lower_limit = 142_100
    tax_rate = 0.17
    lower_limit = 1_000_000


total = float(tax_lower_limit + (gift_value - lower_limit) * tax_rate)

if gift_value > 5000:
    print(f"Amount of tax: {total}")
else:
    print("No tax!")
