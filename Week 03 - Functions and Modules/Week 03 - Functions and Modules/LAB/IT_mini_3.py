"""
RECORD CHECK  -  my version
===========================

Name  : Tatenda Dube
Lane  : IT  
Date  : 10/10/2026
"""

#-------------------------------------------------------------------------------------------------------------------------------------------
#Create functions
#Each function will have its own specific function 
#This will make it easier because you will not have to continue writing the same piece of code over again throughout your programme
#Then you can just call on your function to execute it
#The return function gives us back a piece of information that we want from within the function
#One function that gets the inputs, one that calculates status, one calculates the differnce and percentage then another prints a report
def get_val():
    """This function lets the user input the variables they need to"""
    hostname = input("Please enter your hostname: ")
    if hostname == "quit":
        return None 

    occupied_space = float(input("Please enter the amount of GB used: "))
    total_space = float(input("Please enter the total amount of GB: "))

    return hostname,occupied_space,total_space
#if statement to tell us that when we type quit as hostname that nothing is being given back to us
    
def status_of(percentage):
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

#To fix the formatting problem make sure the ":" are all lined up ina uniform manner
def print_report(hostname, occupied_space, total_space, difference, percentage, status):
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {hostname}")
    print("=" * 34)
    print(f"USED GB  :   {occupied_space:>10.2f}")
    print(f"TOTAL GB :   {total_space:>10.2f}")
    print(f"FREE     :   {difference:>10.2f}")
    print(f"PERCENT  :   {percentage:>10.2f}")
    print(f"STATUS   :   {status:>10}")
    print("=" * 34)

#----------------------------------------------------------------------------------------------------------------------------------------
#Using a while loop because I do not know how many times it will be repeated
#equating the variable values to a fanction that provides us with the hostname, space occupied and total space available
#This will make sure the function gets called
#if statement to let us know that if the function does not return any values to us then the loop will end
#equate the other functions to the things that they are supposed to return as well 
#Then print the report
while True:
    values = get_val()
    if values == None:
        break

    hostname,occupied_space,total_space = values
    difference, percentage = check(occupied_space,total_space)
    status = status_of(percentage)
    print_report(hostname, occupied_space, total_space, difference, percentage, status)



