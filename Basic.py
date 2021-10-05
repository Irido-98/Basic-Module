class Basic:

    def add(self, x, y):  # Add method
        return x + y

    def subtract(self, x, y):  # Subtract method
        return x - y

    def multiply(self, x, y):  # Multiplication method
        return x * y

    def divide(self, x, y):  # Division method
        return x / y

    def indices(self, num,power): # Indices method
        return num**power


# create a calculator object
my_cl = Basic()

while True:
    # Gives user option of what function they want to do
    print("1: Add")
    print("2: Subtract")
    print("3: Multiply")
    print("4: Divide")
    print("5. Indices")
    print("6: Exit")

    ch = int(input("Select operation: "))

    # Make sure the user have entered the valid choice
    if ch in (1, 2, 3, 4, 5,6):

        # first check whether user want to exit
        if (ch == 6):
            print('Bye!')
            break

        # If not then ask fo the input and call appropriate methods
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))

        # Print the equation and output
        if ch == 1:
            print(x, "+", y, "=", my_cl.add(x, y))
        elif ch == 2:
            print(x, "-", y, "=", my_cl.subtract(x, y))
        elif ch == 3:
            print(x, "*", y, "=", my_cl.multiply(x, y))
        elif ch == 4:
            print(x, "/", y, "=", my_cl.divide(x, y))
        elif ch == 5:
            print(x, "**", y, "=", my_cl.indices(x, y))

    else:
        print("Invalid Input")
