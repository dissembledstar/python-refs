def hotel_cost (nights) :
    cost_per_night = 140
    return nights * cost_per_night
    
def plane_ride_cost (city) :
    # I would normally use a dictionary from another module for this, or a DB lookup
    
    cost = None
    
    if city == "Charlotte" :
        cost = 183
    if city == "Tampa" :
        cost = 220
    if city == "Pittsburgh" :
        cost = 222
    if city == "Los Angeles" :
        cost = 475
    
    return cost

def rental_car_cost (days) :
    daily_cost = 40
    
    # some discounts in dollars off total
    discount = 0
    
    if days >= 3 :
        discount = 20
    if days >= 7 :
        discount = 50

    return (days * daily_cost) - discount

def trip_cost(city, days, spending_money) :
    
    # cool list, bro
    costs =  [plane_ride_cost (city), rental_car_cost (days) , hotel_cost (days) , spending_money]
    
    # sum takes an iterable sequence of values, which is the same thing as an array or list 
    return sum (costs)
    
# if __name ==  __main__
print trip_cost ("Los Angeles", 5, 1337)
