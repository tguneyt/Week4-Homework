# Tayyip Güney 21.02.2022

# Calculator

# General Information:
# I want to use a program which can calculate basic mathematical operations.

# Acceptance Criteria:
# * The calculator must support the Addition, Subtraction, Multiplication and Division operations.
# * All operations must be in a different module as method.
# * Operations must define with two float numbers as parametres.
# * Use math.ceil() for all results.
# * Create a menu to choose an operation.
# * User can choose invalid options, so you must handle all possible error. (Use try except :))
# * Inform user what type of error occured (TypError, ValueError etc.)
# * This process must continue until user want to quit from calculator.

import CalculatorModul_TG
import math
import sys

print("\nCALCULATOR\n")

while True:
   
    try:
        sel=(int(input(
"""
Choose an operasyon

1-Addition
2-Subtraction
3-Multiplication
4-Division
5-Exit

""")))
        
    except:
        err_text=str(sys.exc_info()[0])
        print("\nOops !!! ", err_text.split("'")[1])
        print("Try again")
        continue
    
    if sel<1 or sel>5:
        print("\nInvalid Value")
        continue
         
    if sel == 5 :
        break
    
    try:
        x=float(input("first  number : "))
        y=float(input("second number : "))
    except:    
        err_text=str(sys.exc_info()[0])
        print("\nOops !!! ", err_text.split("'")[1])
        print("Try again")
        continue
        
    try:   
        if sel == 1 :
            result = CalculatorModul_TG.Addition(x,y)
            print(f"\n{x} + {y} = {math.ceil(result)}")
            continue

        if sel == 2 :
            result = CalculatorModul_TG.Subtraction(x,y)
            print(f"\n{x} - {y} = {math.ceil(result)}")
            continue

        if sel == 3 :
            result = CalculatorModul_TG.Multiplication(x,y)
            print(f"\n{x} * {y} = {math.ceil(result)}")
            continue
        if sel == 4 :
            result = CalculatorModul_TG.Division(x,y)
            print(f"\n{x} / {y} = {math.ceil(result)}")
            continue
        
    except:
                
        err_text=str(sys.exc_info()[0])
        print("\nOops !!! ", err_text.split("'")[1])
        print("Try again")
        continue