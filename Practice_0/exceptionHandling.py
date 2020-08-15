 # Learning how to handle errors using try and except

try:                                      # makes the code run normally
    num = int(input('Enter number:'))
    den = int(input('Enter number:'))
    print(num/den)
except:                        # handles all errors when no error mentioned
    print("Numerator and denominator should be integers")
