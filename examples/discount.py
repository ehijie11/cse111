#Ehijie Omijie

import datetime

DISCOUNT_RATE = 0.10
SALES_TAX_RATE = 0.06

def main():
    subtotal = 0.0
    
    while True:
        price = float(input("Enter the price of the item (or 0 to finish): $"))
        if price == 0:
            break
        quantity = int(input("Enter the quantity of the item: "))
        subtotal += price * quantity
    
    # Current day of the week
    current_day = datetime.datetime.now().strftime('%A')
    
    # Determine if a discount applies
    if subtotal >= 50 and (current_day == 'Tuesday' or current_day == 'Wednesday'):
        discount = subtotal * DISCOUNT_RATE
    else:
        discount = 0
    
    # Calculate the new subtotal after discount
    discounted_subtotal = subtotal - discount
    
    # Calculate the sales tax
    sales_tax = discounted_subtotal * SALES_TAX_RATE
    
    # Calculate the total amount due
    total_due = discounted_subtotal + sales_tax
    
    # Print the results
    if discount > 0:
        print(f"Discount amount: ${discount:.2f}")
    else:
        print("No discount applied.")
    
    print(f"Sales tax amount: ${sales_tax:.2f}")
    print(f"Total amount due: ${total_due:.2f}")

if __name__ == "__main__":
    main()
