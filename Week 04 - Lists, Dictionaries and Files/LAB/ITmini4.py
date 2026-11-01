"""
RECORD CHECK  -  my version
===========================

Name  :  Tatenda Dube
Lane  :  IT 
Date  :  18/10/2026

"""
#----------------------------------------------------------------------------------------------------------
#The functions from the previous mini project
#Each function has its own specific role 
#One function is for calculations of the space available(difference), percentage and status
#The other function is responsible for printing the report
def check(occupied_space,total_space):
    """This function will calculate the difference, percentage and status."""
    available_space = total_space - occupied_space
    percentage = (occupied_space/total_space) * 100
    status = "Over limit" if percentage >= 100 else "OK"
    return available_space, percentage, status 

def print_report(hostname, occupied_space, total_space, available_space, percentage, status):
    """Returns a report of the different records"""
    print("=" * 34)
    print(f"  RECORD CHECK  -  {hostname}")
    print("=" * 34)
    print(f"  {"GB USED":<9}    :  {occupied_space:>10.2f}")
    print(f"  {"TOTAL GB":<9}   :  {total_space:>10.2f}")
    print(f"  {"FREE":<9}       :  {available_space:>10.2f}")
    print(f"  {"PERCENTAGE":<9} :  {percentage:>10.2f}")
    print(f"  {"STATUS":<9}     :  {status:>10}")
    print("=" * 34) 

#------------------------------------------------------------------------------------------------------------------
#We are creating a file using with open("......txt", "w") as f
#Remember to save the file immediately after writing the lines otherwise they may not appear
#"w" is what allows us to write to the file 
#Make a function that puts your records int a dictionary 
#The function will return the lines from the file as a list of dicts
with open("minifiles.txt", "w") as f:
        f.write("T-021, 35, 120\n"),
        f.write("T-009,47, 120\n"),
        f.write("T-013, 67, 120\n"),
    

def load_records(path):
    """returns the list using the file path"""
    new_records = []

    """r reads the file line by line"""
    with open (path, "r") as f:
        for line in f:
            hostname,occupied_space,total_space = line.strip().split(",")
            occupied_space = float(occupied_space)
            total_space = float(total_space)
            
#Indentation is important because when the append and return were in the same line the function wasn't working properly
            r_record = {
                "Hostname": hostname,
                "GB used": occupied_space,
                "Total GB": total_space,
                }
#Don't forget to append the new record             
            new_records.append(r_record)
    """The dictionary is meant to return all the lines instead of just the last one"""
    return new_records

   
#--------------------------------------------------------------------------------------------------------------------      
#Make name and give its value as the function to make it easier to call 
#In order to call a function without writing the variables inside it, make them equal to the objects 
# The for loop is being used because we have a specific set of values we want returned
# Rememeber to equate the functions to something in order to call them     
my_files = load_records("minifiles.txt") 
print(my_files)


for record in my_files:
    hostname, occupied_space, total_space = record.values()

    available_space, percentage, status = check(occupied_space, total_space)
    print_report(hostname, occupied_space, total_space, available_space, percentage, status)
    
#Finally it prints the report  


 