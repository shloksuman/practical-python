# A list of stock data: (Ticker, Shares, Price)
# Notice the third item has "N/A" instead of a number—this will cause the error!
portfolio = [
    ('AAPL', 50, 150.25),
    ('IBM', 100, 91.10),
    ('MSFT', 'N/A', 310.50),  # This is our "Dirty Data"
    ('CAT', 20, 83.44)
]

total_cost = 0.0

print("--- Starting Portfolio Calculation ---")

for name, shares, price in portfolio:
    try:
        # We try to multiply shares by price
        # int() or float() will fail if they hit a string like 'N/A'
        cost = int(shares) * float(price)
        total_cost += cost
        print(f"Success: {name} calculated. Subtotal: ₹{total_cost:,.2f}")
        
    except ValueError:
        # This block catches the error and keeps the program alive
        print(f"Warning: Could not calculate {name}. Invalid data: '{shares}'")

print("--- Calculation Finished ---")
print(f"Final Total Cost: ₹{total_cost:,.2f}")