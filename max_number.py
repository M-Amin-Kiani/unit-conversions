# written by Mohammad.Amin.Kiani

''' --------------------------------------------------------------------------- '''

list_num = []
cancel = 0

while(True) :
    
    num = eval(input("please Enter a number (for exit Enter 0) : "))
    
    if ( num == 0):
        cancel += 1
        print("finished!")
        break
    
    else:
        cancel = 2
        list_num.append(num) 

if(cancel != 1) :
    max_num = max(list_num)

    print("the MAX of num's list : ", max_num)    
    
else :
     print("you did't make a list...!")    
    
''' --------------------------------------------------------------------------- '''