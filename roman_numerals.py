# week 6 task 1

# take user input of a digital number to convert into a Roman number
# conver string into an integer
number = int(input("Enter a number (1 to 4999) in decimal form: "))

# define a function


def int2roman(number):

    # create a libraty with digital and Roman numbers to iterate over
    numerals = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL",
                50: "L", 90: "XC", 100: "C", 400: "CD",
                500: "D", 900: "CM", 1000: "M"}

    # returns dictionaties key and value as a tuple pair
    # which also makes it iterable for the for loop
    numerals1 = numerals.items()
    # we need to iterate numerals in a reverse order
    # so we can compare our input number with the highest number in numerals
    # otherwise the input number will not reach any number higher
    # than 1 in the numerlas dictionary
    numerals2 = sorted(numerals1, reverse=True)

    # capping the converter to 4999 and anything above this number
    # won't be converted
    if number >= 5000:
        print("This number is too high to be converted into a Roman number.")

    # a variable with a space to attach the first roman number to in the loop
    # the result variable will change as the loop is executed
    result = " "

    # for loop to iterate over the dictionarie's key and value
    # to compare with our input number to find the roman number equivalent
    for digital, roman in numerals2:

        # while the input number is higher than  the digital number
        # and less than 5000
        while number >= digital and number < 5000:
            # we combine the result variable with the roman equevalent
            # of the digital number we stopped at in the numerals dictionary
            result = result + roman
            # if the input numer is not equal to digital number
            # we subtract the digital number from the input nuber
            number = number - digital
            # the citcle is repeated until we come to number = 0

    # return the answer
    return result


# call the function
print(int2roman(number))
