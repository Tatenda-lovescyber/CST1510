"""
RECORD CHECK  -  my version
===========================

Name  :  TATENDA DUBE
Lane  :  IT      (delete two)
Date  :  03/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

while True:
    label = input("Please enter a hostname: ")
    if label == "quit":
        break
    #break to stop the loop
    value = float(input("Please enter the amount of GB used: "))
    limit = float(input("Please enter the total amount of GB: "))
    # float toensure that computer knows the variable type that is bein entere.
   #Do basically the same thing as in the last one
    difference = limit - value  
    percent = (value/limit) * 100

    # status to show in the output as well.
    status = 88.4

    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"
  
    #Ensure everything is in alignment
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)

    print(f"USED   :   {value:>10.2f}")
    print(f"TOTAL  :   {limit:>10.2f}")
    print(f"FREE   :   {difference:>10.2f}")
    print(f"PERCENT:   {percent:>10.2f}")
    print(f"STATUS :   {status:>10}")


    print("=" * 34)


