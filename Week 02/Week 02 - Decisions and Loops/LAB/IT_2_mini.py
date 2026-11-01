"""
RECORD CHECK  -  my version
===========================

Name  :  TATENDA DUBE
Lane  :  IT
Date  :  03/10/2026
"""
#-----------------------------------------------------------------------------------------------------------------------
#We start with a while loop and in the while loop will be the variables we need to enter and calculations to be made
#The loop will ensure that the computer will continuously ask the user for values that need to be input in the comouter
#Repeats the condition while still true
#The loop will only end if the user types quit as the hostname
while True:
    hostname = input("Please enter a hostname: ")
    if hostname == "quit":
        break
    #break to stop the loop

    occupied_space = float(input("Please enter the amount of GB used: "))
    total_space = float(input("Please enter the total amount of GB: "))
    # float toensure that computer knows the variable type that is bein entere.

   #Do basically the same thing as in the last one for the calulations
    difference = total_space - occupied_space
    percent = (occupied_space/total_space) * 100

#-----------------------------------------------------------------------------------------------------------------------
#Include a status now in the loop 
#The status will involve the use of if, elif, else 
#The status is dependant on the perecentage, OVER LIMIT if percent >=100, WARNING if percent>=90 and ok otherwise
    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

#----------------------------------------------------------------------------------------------------------------------
#Finally print out the report for the server(s)  
#Ensure everything is in alignment
#Include status in the report
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {hostname}")
    print("=" * 34)

    print(f"USED GB  :   {occupied_space:>10.2f}")
    print(f"TOTAL GB :   {total_space:>10.2f}")
    print(f"FREE     :   {difference:>10.2f}")
    print(f"PERCENT  :   {percent:>10.2f}")
    print(f"STATUS   :   {status:>10}")


    print("=" * 34)


