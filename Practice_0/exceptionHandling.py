 # Learning how to handle errors using try and except

while True:
    try:                                      
        num = int(input('Enter number:'))
        den = int(input('Enter number:'))
        print(num/den)
        break                           # correct inputs will break the while loop
    except:                        
        print("Numerator and denominator should be integers")
