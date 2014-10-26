"""if <MS $0
if MS $5
if HS $7
else $12

if rainy: sale $2 dollars off each price
if sunny +$2 each price
if hailing: everybody free!
if snowing +1.50 to every price"""

def Movies(age):
    weather = str(input("Is the weather rainy, sunny, hailing, or snowing?:" ))
    if age < 11:
        ticket = 0
        return "The ticket is free"
    elif age >= 11 and age < 14:
        ticket = 5
    elif age >=14 and age <=18:
        ticket = 7
    else:
        ticket = 12
    if weather == "rainy":
        ticket = ticket - 2
    elif weather == "sunny":
        ticket = ticket + 2
    elif weather == "hailing":
        ticket = 0
        return "The ticket is free"
    elif weather == "snowing":
        ticket = ticket + 1.50
    else:
        ticket = ticket
    print ("The ticket costs $" + str(ticket))
