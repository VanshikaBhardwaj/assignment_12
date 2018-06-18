#1
a=3
try:
    if(a<4):
        a=a/(a-3)
        print(a)
except ZeroDivisionError:
    print("Invalid division")
#2
l=[1,2,3]
try:
    print(l[3])
except IndexError:
    print("Index value does not exist.")
  
#3
'''
==============================================================================
OUTPUT:
    we get a NameError: Hi there
    
==============================================================================
'''

#4
'''
==============================================================================
OUTPUT:
    
-5.0
a/b result in 0

==============================================================================

'''

#5
try:
    #import adfs
    n=int("two")
    print(n/2)
    a=[2,12,3,5]
    print(a[10])
except ImportError:
    print("Module can't be imported")
except ValueError:
    print("Invalid value for data type")
except IndexError:
    print("Index out of bound error!")

#6
class Error(Exception):
    pass
class AgeTooSmallError(Error):
    
    pass

while True: 
   try: 
       i_num=int(input("Enter a number")) 
       if i_num < 18: 
           raise AgeTooSmallError 
       elif i_num >= 18: 
           break 
   except AgeTooSmallError: 
       print("Under-aged!")
print("Congratulations!")   