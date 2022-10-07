def computepay(hour,rate):

    pay=(hour*rate)+((hour%40)*(rate*1/2))

    return pay
hour=int(input("Enter hour:"))

rate=int(input("Enter rate:"))

print("Total pay: ",computepay(hour,rate))

def hotel_cost(night):

    return 140*night

def plane_ride_cost(city):

    price_list={"Charlotte": 183,"Tampa": 220,"Pittsburgh": 222,"Los Angeles": 475}

    return price_list[city]

def rental_car_cost(days):

    cost=40*days

    if (days>=7):

        cost-=50

    elif (days>=3):

        cost-=20

    return cost
def trip_cost(city,days):

    return rental_car_cost(days)+ hotel_cost(days)+ plane_ride_cost(city)



def trip_cost(city,days,spend_money=None):

    if(spend_money!=None):

        return rental_car_cost(days)+ hotel_cost(days)+ plane_ride_cost(city)+spend_money

    else:

        return rental_car_cost(days)+ hotel_cost(days)+ plane_ride_cost(city)





days=int(input("Enter the trip days: "))

print("enter the city name you going to visit:")

city=input("Charlotte , Tampa , Pittsburgh , Los Angeles:  ")

print("Total cost: ",trip_cost(city,days))

spend_money= int(input("Enter the spending cost:"))

print("Total cost: ",trip_cost(city,days,spend_money))
