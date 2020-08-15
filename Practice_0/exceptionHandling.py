 # Learning how to handle errors using try and except

class ZeroDenominatorError(ZeroDivisionError):      # Inheriting ZeroDivisionError which makes it 
                                                    # the parent class here
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
    except ZeroDivisionError:                      # this will run since ZeroDivisionError's all 
                                                # properties has been inherited by our class
        print("Denominator cannot be zero") 
    except ZeroDenominatorError:                # this will run if it comes before in order                           
        print('Zero as denominator is not defined')

    except:
        print('Unknown error occured')           # defualt except needs to be in the last since the block runs
                                             # in order and checks all specified excepts first, if none found 
                                             # defualt except runs 