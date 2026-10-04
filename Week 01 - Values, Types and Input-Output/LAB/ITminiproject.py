"""
RECORD CHECK  -  my version
===========================

Name  : TATENDA DUBE
Lane  : IT      (delete two)
Date  : 25/09/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
# iput will have the user enter what is being asked for
# float to change the variable type
label = input("Enter a label for the record: ")   
first = float(input("Enter the first value: "))    
second = float(input("Enter the second value: ")) 

difference = first - second 
percent = (first/second) * 100     
# a/b = a divided by b, "*" = multiplication

print()
print("=" * 34)
# Prints a certain number of "="
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)
# f is used to format the output in a secific form

print(f" GB USED :{first:>10.2f}")
print(f" TOTAL GB :{second:>10.2f}")
# float print to 2 s.f
print(f" FREE   :{difference:>+10.2f}")
# difference printed as positive or negative sign and to 2 s.f
print(f" PERCENT     :{percent:>10.2f}")


print("=" * 34)


