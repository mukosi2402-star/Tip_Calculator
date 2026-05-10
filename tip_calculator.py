meal_price =input("What is the meal price? ")
tip_percentage = input("What percentage would you like to tip? ")
meal_price = float(meal_price[1:])
tip_percentage = float(tip_percentage[:-1])
if tip_percentage < 15:
    print("You should tip more than 15%")
else:
    tip_amount = meal_price * (tip_percentage / 100)
    print(f"Leave : ${tip_amount:.2f}")