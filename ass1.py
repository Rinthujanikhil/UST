#1. Write a function to take input from user in days and print it in years, month and days
#input - 397, output - 1 year , 1 month , 1 day.year:-365 days 
def days():
   num=int(input("enter the days"))
   year=num//365
   month=(num-(year*365))//30
   day=(num-(year*365)-(month*30))
   print("year:",year)
   print("months:",month)
   print("days:",day)  
    
days()
