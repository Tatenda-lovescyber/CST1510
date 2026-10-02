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
label = input("Enter a label for the record: ")   
first = float(input("Enter the first value: "))    
second = float(input("Enter the second value: ")) 

difference = first - second 
percent = (first/second) * 100     


# =================================================================== OUTPUT
# 3. Print the report.
#
#    Threshold : print the three values you were given, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : difference always shows its sign, plus one line of your own

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print(f" First value  :{first:>10.2f}")
print(f" Second value :{second:>10.2f}")
print(f" Difference   :{difference:>+10.2f}")
print(f" Percent      :{percent:>10.2f}")
# : your report lines go here

print("=" * 34)


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and write the error in your journal
#    [ ] Check every variable name says what it holds
#    [ ] Show it to the person next to you
