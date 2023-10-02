print("when asked about location enter the location based on floor(room) EX: basement(18)")

print("Water fountains: ")
WFN = input("Enter number of water fountains: ")
WFL = input("Where are the water fountains: ")
WFC = input("How well maintained are the bathrooms: ")

print("Bathrooms: ")
BRN = input("How any bathrooms are there: ")
BRL = input("Where are the bath rooms: ")
BRC = input("How are the conditions of the bathroom: ")

print("Classrooms: ")
CRN = input("How many classrooms are there")
CRL = input("Were are the classrooms")

BRD = int(BRN)/int(CRN)
WFD = int(WFN)/int(CRN)

print(" ")

print("Water fountains: ")
print(f"There are {WFN}")
print(f"the water fountains are in {WFL}")
print(f"The conditon of the water fountains are {WFC}")

print("Bathrooms: ")
print(f"There are {BRN} bathrooms")
print(f"the bathrooms are in {BRL}")
print(f"The conditon of the bathrooms are {BRC}")

print("classrooms: ")
print(f"There are {CRN} bathrooms")
print(f"the bathrooms are in {CRL}")
print(f"there are {BRD} bathrooms per classroom and {WFD} water fountains per classroom")