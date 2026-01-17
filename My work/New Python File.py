# mortgage.py

principal = 500000.0
rate = 0.05
total_paid = 0.0
months = 0

while principal > 0:
    months = months + 1
    
    # Increase the payment for the first 12 months
    if months <= 12:
        payment = 3684.11
    else:
        payment = 2684.11
        
    # Add interest and subtract payment
    principal = principal * (1 + rate / 12) - payment
    total_paid = total_paid + payment

print('Total paid:', round(total_paid, 2))
print('Total months:', months)
print('Years:', round(months / 12, 1))
