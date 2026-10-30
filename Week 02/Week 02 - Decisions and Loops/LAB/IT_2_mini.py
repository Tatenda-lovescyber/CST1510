"""
RECORD CHECK  -  my version
===========================

Name  :  TATENDA DUBE
Lane  :  IT
Date  :  03/10/2026
"""
#Repeats the condition while still true
#while loop because we do not know how many times someone will run the programme
while True:
    hostname = input("Please enter a hostname: ")
    if hostname == "quit":
        break
    #break to stop the loop after quit has been repated


    occupied_space = float(input("Please enter the amount of GB used: "))
    total_space = float(input("Please enter the total amount of GB: "))
    # float to ensure that computer knows the variable type that is being entered.


   #Do basically the same thing as in the last one for the calulations
    difference = total_space - occupied_space
    percent = (occupied_space/total_space) * 100

    # status to show in the output as well.
    status = 88.4
    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"
  
    #Ensure everything is in alignment by using f to format
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {hostname}")
    print("=" * 34)

    print(f"USED GB  :   {occupied_space:>10.2f}")
    print(f"TOTAL GB :   {total_space:>10.2f}")
    print(f"FREE   :   {difference:>10.2f}")
    print(f"PERCENT:   {percent:>10.2f}")
    print(f"STATUS :   {status:>10}")


    print("=" * 34)


