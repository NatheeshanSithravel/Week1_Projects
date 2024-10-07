#Author Natheeshan
#Date Oct-07-2024
#Temperature Conversion

"""
Get Unit Of Temprature
Get Value of Temp
"""

unit = input("Enter the Final Unit You Want To Change (F or C)")

value = int(input("Enter Temprature"))

if unit=="F":
    f1_value = value * (9/5) + 32
    print(f1_value,"°F" )
else:
    f2_value =(value - 32) * 5/9
    print(f2_value, "°C")
    
    
