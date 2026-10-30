"""
RECORD CHECK  -  my version
===========================

Name  : Tatenda Dube
Lane  : IT  
Date  : 10/10/2026
"""

#Functions to make things easier
def status_of(percentage):
    status = 0 
    """This function will return the status of the percent given."""
    if percentage >= 100:
        status = "OVER LIMIT"
    elif percentage >= 90:
        status = "WARNING"
    else:
        status = "OK"
        return status 

def check(occupied_space,total_space):
    """This function will calculate the difference and percentage, then return both values."""
    difference = total_space - occupied_space
    percentage = (occupied_space/total_space) * 100
    return difference, percentage 

def print_report(hostname, occupied_space, total_space, difference, percentage, status):
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {hostname}")
    print("=" * 34)
    print(f"USED GB  :   {occupied_space:>10.2f}")
    print(f"TOTAL GB :   {total_space:>10.2f}")
    print(f"FREE   :   {difference:>+10.2f}")
    print(f"PERCENT:   {percentage:>10.2f}")
    print(f"STATUS :   {status:>10}")
    print("=" * 34)

#Using a while loop because I do not know how many times it will be repeated
while True:
    hostname = input("Please enter a host name: ")   
    if hostname == "quit":
        break
    """Break basically stops the code loop"""
      

    occupied_space = float(input("Please enter the amount of GB used: ")) 
    total_space = float(input("Please enter the total GB: "))  
   
    
    difference = total_space - occupied_space
    percentage = (occupied_space/total_space) * 100
    status = 0
#status uses the answer found in percentage to determine storage levels of a server   
    if percentage >= 100:
        status = "OVER LIMIT"
    elif percentage >= 90:
        status = "WARNING"
    else:
        status = "OK"

    
#Calling the functions so that the output we want can appear

    print(check(occupied_space, total_space)) 

    print(status_of(percentage))
    print_report(hostname, occupied_space, total_space, difference, percentage, status)


