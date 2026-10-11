"""
RECORD CHECK  -  my version
===========================

Name  : Tatenda Dube
Lane  : IT  
Date  : 10/10/2026

"""

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

def check(value, limit):
    """This function will calculate the difference and percentage, then return both values."""
    difference = limit - value
    percentage = (value/limit) * 100
    return difference, percentage 

def print_report(hostname, value, limit, difference, percentage, status):
    print("=" * 34)
    print(f"  RECORD CHECK  -  {hostname}")
    print("=" * 34)
    print(f"  {"GB USED":<9} :  {value:>10.2f}")
    print(f"  {"TOTAL GB":<9} :  {limit:>10.2f}")
    print(f"  {"FREE":<9} :  {difference:>10.2f}")
    print(f"  {"PERCENTAGE":<9} :  {percentage:>10.2f}")
    print(f"  {"STATUS":<9} :  {status:>10}")
    print("=" * 34) 

while True:
    hostname = input("Please enter a host name: ")   
    if hostname == "quit":
        break
      

    value = float(input("Please enter the amount of GB used: ")) 
    limit = float(input("Please enter the total GB: "))  
   
    
    difference = limit - value 
    percentage = (value/limit) * 100
    status = 0

    if percentage >= 100:
        status = "OVER LIMIT"
    elif percentage >= 90:
        status = "WARNING"
    else:
        status = "OK"

    
#Calling the functions so that the output we want can appear

    print(check(value, limit)) 

    print(status_of(percentage))
    print_report(hostname, value, limit, difference, percentage, status)


