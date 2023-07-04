
#Pizza Shop deliveres 
#Author = Chit Ko Ko


print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")


S =15
M=20
L=25
Bill=0


if size == "S":
    Bill +=S

elif size=="M":
    Bill +=M

elif size=="L":
    Bill +=L

if add_pepperoni == "Y":
    if size == "S":
            Bill += 2

    else :
            Bill +=3

if extra_cheese == "Y":
    Bill += 1

print (f"Your final bill is: ${Bill}")
