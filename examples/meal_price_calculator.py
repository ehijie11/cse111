
#these are the USer inputs
child_price = float(input("What's the price of a child's meal? "))
adult_meal =float(input("What's the price of an adult's meal? "))
num_children = int(input("How many number of children? "))
num_adults = int(input("The number of adults? "))
sales_rate = float(input("What's the sales tax rate? "))

#getting the subTotal
adult_total = adult_meal * num_adults
child_total = child_price * num_children
rate_total1 = sales_rate/100 
rate_total2 = (adult_total + child_total) * rate_total1
rate_total3 = rate_total2 + adult_total + child_total
sub_total = f' SUBTOTAL = {rate_total3}'
print(sub_total)