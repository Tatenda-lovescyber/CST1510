"""
RECORD CHECK  -  my version
===========================

Name  :  Tatenda Dube
Lane  :  IT 
Date  :  18/10/2026

"""
def check(value,limit):
    """This function will calculate the difference, percentage and status."""
    #All calculations happen within this function
    available_space = limit - value
    percentage = (value/limit) * 100
    status = "Over limit" if percentage >= 100 else "OK"
    return available_space, percentage, status 

def print_report(hostname, value, limit, available_space, percentage, status):
    """Returns a report of the different records"""
    print("=" * 34)
    print(f"  RECORD CHECK  -  {hostname}")
    print("=" * 34)
    print(f"  {"GB USED":<9} :  {value:>10.2f}")
    print(f"  {"TOTAL GB":<9} :  {limit:>10.2f}")
    print(f"  {"FREE":<9} :  {available_space:>10.2f}")
    print(f"  {"PERCENTAGE":<9} :  {percentage:>10.2f}")
    print(f"  {"STATUS":<9} :  {status:>10}")
    print("=" * 34) 


with open("minifiles.txt", "w") as f:
        f.write("T-021, 35, 120\n"),
        f.write("T-009,47, 120\n"),
        f.write("T-013, 67, 120\n"),
    

def load_records(path):
    """returns the list using the file path"""
    with open ("minifiles.txt") as f:
        for line in f:
            hostname,value,limit = line.strip().split(",")
            value = float(value)
            limit = float(limit)
    return({
                "Hostname": hostname,
                "GB used": value,
                    "Total GB": limit,
                })
   
        
        
my_files = load_records("minifiles.txt") 
  
print(my_files)
print(check(value,limit))
print(print_report(hostname, value, limit, available_space, percentage, status))



    

       

    

    


     



# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.
#
#    Excellent : also keep a running count of how many were OVER LIMIT, and
#                print that once, after the loop ends.

# your loop goes here

# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
