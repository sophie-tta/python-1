"""
Munch Truck App MVP
v0.1
By Alice
The purpose of Munch is to produce a dinner menu from favourite dishes,
and produce a shopping list of ingredients if required. 
"""

# ---------- Imports ---------------

from random import choice

# ---------- A. Functions ----------
# A1. Choose dishes

def chooseDishes(days):
    while len(myMenu) < int(days):
        chosenDish = choice(foodWeLike)
        if chosenDish not in myMenu:
            myMenu.append(chosenDish)

    print("Done! Here's your menu...")
    print()
    for dish in myMenu:
        print(dish)
    print()
    print("Out of all these dishes my favourite has to be... " + choice(myMenu))
    

# A2. Build shopping list

def buildShoppingList():
    myShoppingList = []
    if "Pizza" in myMenu:
        myShoppingList.append(pizza)
    if "BBQ Chicken" in myMenu:
        myShoppingList.append(bbqChicken)
    if "Beef Burgers" in myMenu:
        myShoppingList.append(beefBurgers)
    if "Beef Fajitas" in myMenu:
        myShoppingList.append(beefFajitas)
    if "Bolognese" in myMenu:
        myShoppingList.append(bolognese)
    if "Chicken Stir Fry" in myMenu:
        myShoppingList.append(chickenStirFry)
    if "Chilli" in myMenu:
        myShoppingList.append(chilli)
    if "Chinese Curry" in myMenu:
        myShoppingList.append(chineseCurry)
    if "Crispy Chicken Wrap" in myMenu:
        myShoppingList.append(crispyChickenWraps)
    if "Fish Finger Sandwich" in myMenu:
        myShoppingList.append(fishFingerSandwich)
    if "Lamb Curry" in myMenu:
        myShoppingList.append(lambCurry)
    if "Thai Chicken" in myMenu:
        myShoppingList.append(thaiChicken)
    print()
    for dish in myShoppingList:
        for ingredient in dish:
            print(ingredient)
    print()
    print("Voila! Bon appetit!")

        

# ---------- B. Lists --------------


# B1 Dishes to choose from
foodWeLike = ["Pizza", "BBQ Chicken", "Beef Burgers", "Beef Fajitas", "Bolognese", "Chicken Stir Fry", "Chilli", "Chinese Curry", "Crispy Chicken Wrap", "Fish Finger Sandwich", "Lamb Curry", "Thai Chicken"]


# B2 Ingredients in dishes

pizza = ["pre made pizza", "side salad"]
bbqChicken = ["chicken", "mushrooms", "peppers", "onion", "bbq powder", "wraps", "sweetcorn"]
beefBurgers = ["beef burgers", "burger buns", "mustard", "onions", "cheese", "pickles", "fries"]
beefFajitas = ["minced beef", "wraps", "onion", "peppers", "fajita powder", "cheese", "nachos"]
bolognese = ["minced beef", "onion", "garlic", "peppers", "mushrooms", "bolognese sauce", "pasta"]
chickenStirFry = ["chicken", "teriyaki sauce", "soy sauce", "stir fry veg", "sesame oil", "noodles"]
chilli = ["minced beef", "onion", "peppers", "mushrooms", "kidney beans", "chilli powder", "tinned tomatoes"]
chineseCurry = ["chicken", "green peppers", "onion", "peas", "curry sauce", "mushrooms"]
crispyChickenWraps = ["crispy chicken", "wraps", "lettuce", "onion", "cheese", "honey mustard", "side salad"]
fishFingerSandwich = ["bread", "mayo", "fish fingers", "side salad"]
lambCurry = ["lamb", "raisins", "mushrooms", "tinned tomatoes", "ras el hanout", "harissa", "rice"]
thaiChicken = ["chicken", "thai curry paste", "coconut milk", "green peppers", "mangetout", "mushrooms", "onion"]

myMenu = []

# 1. How many days to plan?

print("Hello, I'm the Munch Truck! I'll help you to plan your dinner menu...")

answer = input("How many days would you like me to plan? ")

print("Ok, I'm going to plan " + answer + " dinner(s) from your list")


# 2. Choose dishes

chooseDishes(answer)


# 3. Build shopping list?

answer = input("Would you like a shopping list for this menu? ")

if answer == 'y' or 'yes':
     buildShoppingList()
else:
    print()
    print("Fine. bye")
