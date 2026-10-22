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
    new_records = []

    """r reads the file line by line"""
    with open ("minifiles.txt", "r") as f:
        for line in f:
            hostname,value,limit = line.strip().split(",")
            value = float(value)
            limit = float(limit)
            parts = line.split()
        
        r_record = {
                "Hostname": hostname,
                "GB used": value,
                    "Total GB": limit,
                }
        """The dictionary is meant to return all the lines instead of just the last one"""
        new_records.append(r_record)
    
    return new_records

   
        
        
my_files = load_records("minifiles.txt") 
print(my_files)

while True:
     print(check(67,120))
     print( print_report("T-013", 67,120, 53, 45, "OVER LIMITS"))
     break


