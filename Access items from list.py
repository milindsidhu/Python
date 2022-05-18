list1 = ["jan", "feb", "mar", "apr", "may"]
# to add value to a list we use .append() "appending adds to the end of list"

def name_month(inputs):
    # here logic is to return the value assigned to index value in the list
    return f"{list1[inputs].title()} is assigned to {inputs} index value.\n"


def checkpoint():
    try:
        user_inputs = int(inputs)
        if user_inputs >= 0 or user_inputs <= 4:
            my_out = name_month(user_inputs)
            print(my_out)

    except:
        print("Error!! Entered value either out of range or invalid!\n")


inputs = ""
while inputs != "exit":
    inputs = input("Enter a number ranging from 0-4:\n")
    print(type(inputs.split()))
    print(inputs.split(", "))
    for inputs in inputs.split(", "):
        checkpoint()
