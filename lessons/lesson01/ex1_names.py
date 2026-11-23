# Example 1: names are stuck on objects
price = 189.5
shares = 100 
symbol = "AAPL"
is_buy = True

print(type(price), type(shares), type(symbol), type(is_buy))

old_price = price
price = 190.25
print(old_price, price)

print(shares*price)
print(7/2, type(7/2))
