# creating booking a movie ticket
Base_price = 30
seat_type = input('Enter seat type (Gold, Silver, Premium, Regular): ')
age = 21
show_time = '7:00 PM'

if age > 18:
    print('You are eligible to book a movie ticket.') 

if age >= 21:
    print(f'You are eligible to book a movie ticket at {show_time} with alcohol.')


# membership and weekend discounts

is_member = True
is_weekend = False

discount = 0
if is_member:
    discount = 5
    print(f'You get a discount of {discount}% for being a member.')


else:
     print('No additional discount on weekdays.')

if is_weekend and is_member:
    discount += 5
    print(f'You get additional discount of 5% on weekends.')

else:
     print('No additional discount on weekdays.')

print('Total discount:', discount)

if age < 18 and show_time == '7:00 PM':
    print('You are not eligible to book a movie ticket at 7:00 PM due to age restrictions.')
    
else:
    print('You are eligible to book a movie ticket at 7:00 PM.')

is_alcohol_served = False

if age >= 21 and is_member:
    is_alcohol_served = True
    print('Alcohol will be served at the showtime.')

else:
     print('Alcohol will not be served at the showtime due to age or membership restrictions.')

if is_member or is_weekend:
    print('You are eligible for special offers on movie tickets.')

else:
    print('You are not eligible for special offers on movie tickets.')



# seat_type and service charge

service_charge = 0
if seat_type == 'Gold':
    service_charge = 10
    print('You have selected Gold seat. Enjoy your movie!')

elif seat_type == 'Silver':
    service_charge = 5
    print('You have selected Silver seat. Enjoy your movie!')

elif seat_type == 'Premium':
    service_charge = 7
    print('You have selected Premium seat. Enjoy your movie!')

elif seat_type == 'Regular':
    service_charge = 3
    print('You have selected Regular seat. Enjoy your movie!')

else:
    print('Invalid seat type selected.')
print('Service charge:', service_charge)

# additional services

services = 0
extra = input('Enter additional services (Popcorn, Soda, None): ')

if extra == 'Popcorn':
     services = 5
     print('You have selected Popcorn. Enjoy your popcorn!')

elif extra == 'Soda':
     services = 5
     print('You have selected Soda. Enjoy your soda!')

elif extra == '':
     
     services = 0
     print('You have selected no additional services.')

     
else:
    print('Invalid selection for additional services.')
print('Additional services charge:', services) 
    

sub_total = Base_price + service_charge + services
discount_amount = sub_total * (discount / 100)
total_price = sub_total - discount_amount

print(f'Subtotal: ${sub_total}')
print(f'Discount Amount: ${discount_amount}')
print(f'Total price for your movie ticket is: ${total_price}. Enjoy your movie!')