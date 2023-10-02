item1 = float(str(input("enter price of first item: ")))
item2 = float(str(input("enter price of second item: ")))
item3 = float(str(input("enter price of third item: ")))

total1 = item1 + item2 + item3
total2 = total1 * 0.08
total = total2 + total1

print("total before tax: ", total1)
print("total after tax: ", total)