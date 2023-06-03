print("Hi")
numberofdiscount = float(input("Please Enter number of discount "))
bdiscount = float(input("Please Enter a b of discount "))
print("Wait.....")
b = numberofdiscount / 100
b2 = b * bdiscount
mdis = numberofdiscount - b2
pdis = numberofdiscount + b2
print(f"The number of discount is {b2}")
print(f"The number m discount is {mdis}")
print(f"The number p discount is {pdis}")
print("Wait.....")
maldis = numberofdiscount * b2
divdis = numberofdiscount / b2
print(f"The number mal discount is {maldis}")
print(f"The number div discount is {divdis}")