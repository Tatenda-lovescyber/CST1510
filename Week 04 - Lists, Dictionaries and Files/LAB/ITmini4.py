"""
RECORD CHECK  -  my version
===========================

Name  :  Tatenda Dube
Lane  :  IT 
Date  :  18/10/2026

"""

# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.

# your function(s) go here
def check(value,limit):
    """This function will calculate the difference, percentage and status."""
    #All calculations happen within this function
    available_space = limit - value
    percentage = (value/limit) * 100
    status = "Over limit" if percentage >= 100 else "OK"
    return available_space, percentage, status 

def print_report(hostname, value, limit, available_space, percentage, status):
    print("=" * 34)
    print(f"  RECORD CHECK  -  {hostname}")
    print("=" * 34)
    print(f"  {"GB USED":<9} :  {value:>10.2f}")
    print(f"  {"TOTAL GB":<9} :  {limit:>10.2f}")
    print(f"  {"FREE":<9} :  {available_space:>10.2f}")
    print(f"  {"PERCENTAGE":<9} :  {percentage:>10.2f}")
    print(f"  {"STATUS":<9} :  {status:>10}")
    print("=" * 34) 



# ====================================================================== STORE
# 2. Get your records into a list of dicts, each shaped like:
#        {"label": ..., "value": ..., "limit": ...}
#
#    Threshold : write the list directly in the code - at least 3 records.
#    Typical   : instead, write a function load_records(path) that reads
#                label,value,limit lines from a file and returns the list.
#                Make your own data file, one record per line.
#    Excellent : also write the results out to a new file (one line per
#                record: label, status), as well as printing them.


    with open("minifile.txt", "w") as f:
        f.write("T-007","25", "120\n")
        f.write("T-006","89", "120\n")
        f.write("T-005","73", "120\n")
        f.write("T-012","67", "120\n")
        f.write("T-036","31", "120\n")
        f.write("T-002","4", "120\n")
        f.write("T-134","99", "120\n")

def load_records(path):
    """Return each line as a list"""
    files =[]
    """prints them out as a list"""

    with open(path) as f:
            for line in f:
                label, value, limit = line.strip().split(",")
                files.append({"label": label, "value": float(value), "limit": float(limit)})
                return files

print(load_records("minifile.txt"))
        
    
    


     



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
