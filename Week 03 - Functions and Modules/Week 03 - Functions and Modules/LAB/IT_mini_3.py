"""
RECORD CHECK  -  my version
===========================

Name  : Tatenda Dube
Lane  : IT  
Date  : 10/10/2026
"""

#Each function has its own specific thing that it is calculating so that you don't have to keep repeating the same block of code
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
        
#All functions need a one line docstring which tells us what they will be doing
#return then allows us to get the values that we want when we call the function
#Functions can have more than one input in the parameter
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

#Using a while loop to allow the user to enter the values they want to as many times as they want to
#Break ends the programme once the user has entered quit as the hostname 
while True:
    hostname = input("Please enter a host name: ")   
    if hostname == "quit":
        break

      
#The user is being asked to input the space occupied by the disk
#They also need to print the total disk storage 
    occupied_space = float(input("Please enter the amount of GB used: ")) 
    total_space = float(input("Please enter the total GB: "))  
   
#Calculate the amount of space left in the disk by saying total_space - occupied_space
#Calculate disk space left as a percentage by dividing occupied_space by total_space and multiplying by 100
    difference = total_space - occupied_space
    percentage = (occupied_space/total_space) * 100
#Make a status then using if loop say what should happen
    status = 0
#status uses the answer found in percentage to determine storage levels of a server   
    if percentage >= 100:
        status = "OVER LIMIT"
    elif percentage >= 90:
        status = "WARNING"
    else:
        status = "OK"

    
#Calling the functions so that the output we want can appear
#Call all of them at the end
    print(check(occupied_space, total_space)) 

    print(status_of(percentage))
    print_report(hostname, occupied_space, total_space, difference, percentage, status)


