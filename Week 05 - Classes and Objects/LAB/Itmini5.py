"""
RECORD CHECK  -  my version
===========================

Name  : Tatenda Dube
Lane  : IT 
Date  : 25/10/2026
"""
"""The class is like the blueprint where we write everything"""
class Record:

    """__init__ is used to hide self """
    def __init__(self, label, value, limit):
        self.server = label,
        self.space_occupied = value,
        self.total_space = limit,

    def status(self):
        percent = (self.space_occupied/self.total_space) *100
        """When the function is called the status of each object will be called"""
        if percent >= 100:
            return "Over limit"
        elif percent >= 90:
            return "Warning"
        else:
            return "Ok"

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

record = load_records("final_records.txt")

"""This now prints each line and its records"""
for record in record:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.server}")
    print("=" * 34)
    print(f"{"Server Name"}:{record.server:>10}")
    print(f"{"Storage occupied"}:{record.space_occupied:>10.2f}GB")
    print(f"{"Total Storage"}:{record.total_space:>10.2f}")
    print(f"{"Server Name"}:{record.status():>10}")
    print("=" * 34)

def count_r():
    count = 0 
    if record.status() == "Over limit":
        count += 1
    return (count)


