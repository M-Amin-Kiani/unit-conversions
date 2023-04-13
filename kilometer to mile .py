
#! Written by Mohammad.Amin.Kiani

'''------------------------------------------------------------------------'''
try:
    
    kilometer = eval(input("please enter a valid distance ... :"))

    if type(kilometer) is float or int:
    
        km_to_mile = 0.621371   # mile => km : 10/6  | km => mile : 6/10
    
        mile = kilometer * km_to_mile
    
        print(f"{kilometer} kilometers is equal to {mile} miles")
        
except (NameError, SyntaxError):
    print("invaild input...try again!")

'''------------------------------------------------------------------------'''
