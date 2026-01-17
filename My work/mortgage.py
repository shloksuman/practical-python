principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months=0
extra_pay = input('Enter extra pay: ')
newpayment = payment + int(extra_pay)
start_month = int(input('Enter month no. when extra pay starts: '))
end_month = int(input('Enter last extra pay month: '))


while principal > 0:
    months= months+1
    interest = principal * (rate/12)
    principal += interest

    if months >= start_month and months <= end_month and principal > payment:
        payment = newpayment
    else:
        payment = 2684.11
    if payment > principal:
        payment = principal
    principal = principal - payment
    total_paid = total_paid + payment
    print(months, round(total_paid,2), round(principal,2))


print('Total paid', total_paid)
print('Total months', months)
