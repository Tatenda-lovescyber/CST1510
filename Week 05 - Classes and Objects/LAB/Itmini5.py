"""
RECORD CHECK  -  my version
===========================

Name  : Tatenda Dube
Lane  : IT 
Date  : 25/10/2026
"""
"""The class is like the blueprint where we write everything"""
class Record:

#If you put the commas after label, value and limit pyrhon will consider the variables as tuples and will not print them.
    """__init__ is used to hide self """
    def __init__(self, label, value, limit):
        self.server = label
        self.space_occupied = float(value)
        self.total_space = float(limit)
#Put float in the initialize function as well otherwise it will be seen as a stringa nd won't be printed
    
    """Function to print the statuses of each server"""
    def status(self):
        percent = float(self.space_occupied)/float(self.total_space) *100
        """When the function is called the status of each object will be called"""
        if percent >= 100:
            return "Over limit"
        elif percent >= 90:
            return "Warning"
        else:
            return "Ok"

#Making a file, don't forget w for write 
with open("final_records.txt", "w") as f:
    f.write("T-006, 89.0, 100.0\n"),
    f.write("T-009, 40.0, 100.0\n"),
    f.write("T-011, 140.0, 100.0\n"),

"""to write the file into a list"""
def load_records(path):
    record = []

    """if you want record to be read don't forget to include r"""
    with open(path, "r") as f:
        for line in f:
                hostname,used,total  = line.strip().split(",")
                recs = Record(hostname, used, total)
                record.append(recs)
        return record

#Make a word equal to the function to mKE IT EASIER TO PRINT
all_records = load_records("final_records.txt")

"""This now prints each line and its records"""
for record in all_records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.server}")
    print("=" * 34)
    print(f"{"Server Name"}:{record.server:>10}")
    print(f"{"Storage occupied"}:{record.space_occupied:>10.2f}GB")
    print(f"{"Total Storage"}:{record.total_space:>10.2f}")
    print(f"{"Server Name"}:{record.status():>10}")
    print("=" * 34)
#The format seems to not be working the same way as the others were

"""The function has a loop that should count the number of servers whose status is over limit"""
def count_r(records_list):
#Remember to make count = 0 outside of the loop otherwise the computer won't register it
    count = 0 
    for record in records_list:
        if record.status == "Over Limit":
            count += 1
    return count

over_l = count_r(all_records)
print(f"This is the number of servers that are over limit: {over_l}")
#Make sure your loops and variables have different words for all_records otherwise over_l won't be printed


