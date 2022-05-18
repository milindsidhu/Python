myset = ["Jan", "Feb", "Mar"]

inpu = input("Enter month\n")
# TO ADD value to a set we use .add()
# and TO ADD value to a list we use .append() "appending adds to the end of list"
# TO REMOVE value we use .remove() in sets
myset.append(inpu)
for months in myset:
    print(months)
# the new set becomes
print(myset)
