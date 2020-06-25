def calu_discount(price, discount):
    discount_value = discount 15 / 100

    discount_amount = price *0.15
    after_discount_price -= discount_amount
    return price

def force_number(message):
        while True:
            try:
                number=float(input(message))
                break
            except VauleError:
                print("Please enter a number!")

                return number

       price = force_number("Please enter the price of the item: ")
       discount = force_number("Please enter the % discount e.g. 10: ")


       new_price, money_saved = calc_discount(price, discount)
       print("The new price after a {: If}% discount on ${:.2f} is: ${:.2f}. You saved ${:.2f}!".format(discount,price, new_price, money_saved))

        price= input(  ""

           

    
