 # Learning how to handle errors using try and except

class ZeroDenominatorError(Exception):      # Inheriting Exception which is an in-built python module
    pass
while True:
    try:                                      
        num = int(input('Enter number:'))
        den = int(input('Enter number:'))
        if den == 0:
            raise ZeroDenominatorError("Zero Denominator error raised")    # raising custom  error     
            # raise ZeroDenominatorError()      # will work without argument too
        print(num/den)
        break                           
    except (ValueError):                        
        print("Numerator and denominator should be integers")
    except ZeroDivisionError:                
        print("Denominator cannot be zero") 
    except ZeroDenominatorError:                                            # using exception to handle 
                                                                            # the custom made error
        print('Zero as denominator is not defined')
