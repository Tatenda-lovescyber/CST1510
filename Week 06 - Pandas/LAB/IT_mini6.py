"""
RECORD CHECK  -  my version
===========================

Name  : Tatenda Thokozile Dube
Lane  : IT      
Date  : 08/11/2026
"""
#Pandas is like the excel of python where we will storeour unprocessed data
import pandas as pd
#-------------------------------------------------------------------------------------------------------------------------------------------
#Make a dictionary
#The number of values in each array has to be similar otherwise you will get an error
#A dataframe is a table built from series or in our case a list of dicts
#we then turn our information into an actual file
#The file is being read by df (don't forget to save it as .csv)
myfinal = {
    'Hostname': ['srv-090', 'srv-001', 'srv-004', 'srv-023', "srv-011", "srv-029", "srve-006"],
    'GB_Used' : [130, 47, 110, 94, 69, 92, 89],
    'Total_GB' : [100, 100, 100, 100, 100, 100, 100],
}

df = pd.DataFrame(myfinal)
csv_file_path = "myfinal.csv"
df.to_csv(csv_file_path, index=False)

df = pd.read_csv("myfinal.csv") 

#-------------------------------------------------------------------------------------------------------------------------------------------
#Adding a new column called percent
#Adding status using .apply in to add the condition f the lambda to it
#Lambda is used in place of where we would normally use a function
df["percent"] = (df["GB_Used"]/df["Total_GB"])*100
df["status"] = df["percent"].apply( 
    lambda p: "OVER LIMIT" if p >= 100 else "WARNING" if p >= 90 else "OK"
)

#----------------------------------------------------------------------------------------------------------------------------------------------
#Print the dataframe as it is
#Sort it by only printing the statuses that are not equal to "OK"
#Then print it again alongside a count per group
#Write your data frame to a new file using df.to_csv
#matplotlib.pyplot as plt is imported to make a bar graph
#Then give it a title and save it as .png

print(df)

state_n = df[df["status"] != "OK"]
print(state_n)

count_s = df["status"].value_counts()
print(count_s)

df.to_csv("final.csv", index=False)

import matplotlib.pyplot as plt

count_s.plot(kind="bar", title = "Serve counts per status")
plt.savefig("statuschart.png")

