drink = input("how much was your drink: ")
app = input("how much was your appitizer: ")
entree = input("how much was your entree: ")
dessert = input("how much was your dessert")
tip = input("what is the tip percentage in your area: ")

tip2 = float(tip) * 0.01
sub = float(drink) + float(app) + float(entree) + float(dessert)
tip1 = float(tip2) * float(sub)
tip_sub1 = float(tip1) + float(sub)

tip_sub1 = (tip_sub1)

print(f"Bill Summary")
print(f"the subtotal was {sub}$")
print(f"the tip was {tip1}$")
print(f"the total was {tip_sub1}$")
