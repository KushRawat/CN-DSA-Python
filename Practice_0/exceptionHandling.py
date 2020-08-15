 # Learning how to handle errors using try and except

while True:
    try:                                      
        num = int(input('Enter number:'))
        den = int(input('Enter number:'))
        print(num/den)
        break                           
    except (ValueError,ZeroDivisionError):                        # common exception
        print("Numerator and denominator should be integers")
   # except ZeroDivisionError:                   # adding multiple exceptions
    #    print("Denominator cannot be zero")