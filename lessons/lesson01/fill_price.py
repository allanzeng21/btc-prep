from decimal import Decimal, ROUND_HALF_UP

shares = 1000
price = "0.1"
fee_per_share = "0.2"

CENT = Decimal("0.01")

# TODO 1: convert price and fee_per_share to Decimal
price = Decimal(price)
fee_per_share = Decimal(fee_per_share)

# TODO 2: compute cost, fee, total, avg
cost = shares * price
fee = fee_per_share * shares
total = cost + fee
avg = total/shares

# TODO 3: write a way to round a Decimal to the cent, half-up
print(f"Cost: ${cost:,.2f}")
# TODO 4: print the five lines in the exact format below
print(f"Shares: {shares}")
print(f"Cost:   ${cost:,.2f}")
print(f"Fee:    ${fee:,.2f}")
print(f"Total:  ${total:,.2f}")
print(f"Avg px: ${avg:,.2f}")
