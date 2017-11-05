# Created by: David Wang
# Created on: 31-Oct-2017
# Created for: ICS3U
# Daily Assignment - Unit4-02
# This program displays a rounded decimal, given the rounded decimal place

def decimal(user_input, decimal_roundoff):
    user_input = long(user_input * (10 ** decimal_roundoff) + 0.5) / (10 ** decimal_roundoff)
    print(str(user_input))
    
user_input = raw_input("Enter a decimal: ")
user_input = float(user_input)
decimal_roundoff = raw_input("Enter how many decimal places you would like the number to round to: ")
decimal_roundoff = float(decimal_roundoff)
decimal(user_input, decimal_roundoff)
