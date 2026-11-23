total_shares = 1250
lot_size = 100

full_lots = total_shares//lot_size
leftover = total_shares % lot_size
print(f"{total_shares} shares = {full_lots} lots + {leftover} odd shares")

print(-7//2, -7%2)

cost = 1250 * 189.537
print(f"Cost: ${cost:,.2f}")
print(f"Price: {189.537:.2f} Pct: {0.0425:.1%}")
