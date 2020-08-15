 # Learning how to handle errors using try and except

while True:
    try:                                      
        num = int(input('Enter number:'))
        den = int(input('Enter number:'))
        if den == 0:
            raise ZeroDivisionError         # custom exception
            #raise NameError                # this will cause error here since NameError isnt 
                                            # called below in exceptions
        print(num/den)
        break                           
    except (ValueError):                        
        print("Numerator and denominator should be integers")
    except ZeroDivisionError:                
        print("Denominator cannot be zero") 
