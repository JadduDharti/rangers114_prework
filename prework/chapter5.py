cars = ['bmw', 'Audi', 'honda', 'toyato', 'Hyundai']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())


topping = 'mashrooms'

if topping != 'anchovies':
    print("Hold the anchovies")

answer = 18

if answer != 42:
    print("That is the wrong answer. Please try again..!")


banned_user = ['Adi', 'Shah', 'Arjun', 'Patel']
user = 'Arjun'

if user not in banned_user:
    print(user.title()+ ", you can post if you wish")


p_age = 12

if p_age < 4:
    print("Your admission fees is $0")
elif p_age < 18:
    print("Your admission fees is $5")
else:
    print("Your admission fees is $10")


requested_toppings = ['mashrooms', 'onion', 'green paper', 'extra cheese']

for requested_topping in requested_toppings:

    if requested_topping == 'green paper':
        print("Sorry, we are out of green paper right now.")
    else:
        print("Adding " + requested_topping + ".")


availabe_toppings = ['mashrooms', 'onion', 'olives', 'green paper','extra cheese', 'pepperoni', 'pineapple']

for req_topping in requested_toppings:
    if req_topping in availabe_toppings:
        print("Adding " + req_topping + ".")
    else:
        print("Sorry, we don't have " + req_topping + ".")

print("\n Finish making your pizza")
