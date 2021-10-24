import fractions
from fractions import Fraction as frac


class Basic:  # This is the superclass that will be inherited by other specialised calculators

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

    def indices(self, num, power):
        return num ** power


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
    if ch in (1, 2, 3, 4, 5, 6):

        # first check whether user want to exit
        if ch == 6:
            print('Bye!')
            break

        # If not then ask fo the input and call appropriate methods
        x = input("Enter first number. ")
        if '/' in x:
            k = float(fractions.Fraction(x))

        else:
            k = frac(float(x))

        y = input("Enter second number. ")
        if '/' in y:
            k = float(fractions.Fraction(y))

        else:
            k = frac(float(y))

        # Print the equation and output
        # TODO: fix print statements to not use round function and then rework documentation
        if ch == 1:
            result = my_cl.add(x, y)
            print(frac(str(round(result, 10))))

        elif ch == 2:
            result = my_cl.subtract(x, y)
            print(frac(str(round(result, 10))))

        elif ch == 3:
            result = my_cl.multiply(x, y)
            print(frac(str(round(result, 10))))

        elif ch == 4:
            result = my_cl.divide(x, y)
            print(frac(str(round(result, 10))))

        elif ch == 5:
            result = my_cl.indices(x, y)
            print(frac(str(round(result, 10))))

        # Returns the result as a decimal if the user requests to
        while result is not None:
            i = input('Do you want the answer displayed as a decimal? Y or N').upper()
            if i == 'Y':
                k = int(input('How many decimal places?'))
                print(round(float(result), k))  # TODO: Make the result a decimal.
                break
            elif i == 'N':
                break
            else:
                print('Invalid input')
                break
    else:
        print("Invalid Input")
