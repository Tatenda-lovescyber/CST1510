"""
RECORD CHECK  -  my version
===========================

Name  : TATENDA DUBE
Lane  : IT    
Date  : 25/09/26
"""
#-------------------------------------------------------------------------------------------------
#Input will have the user enter what is being asked for
#Put float when entering the values to let the computer know the type of varaibles to be entered
#Then calculate the difference using the two values, no need to put float since we put it on the input
#And calculte the percentage of the space being occupied in the disk 
hostname = input("Enter a label for the record: ")  
occupied_space = float(input("Enter the first value: "))    
total_space= float(input("Enter the second value: ")) 


# no need to put float on difference
difference = occupied_space - total_space

# a/b = a divided by b, "*" = multiplication
percent = (occupied_space/total_space) * 100     

#-------------------------------------------------------------------------------------------------
#Now we wil print the variables that were input by the user in the form of a report 
#Remember to us the f string to format it and to put you variable names in curly brackets
#The titles you want will be written in the comments and not the curly brackets
print()
print("=" * 34)
# Prints a certain number of "="
print(f"  RECORD CHECK  -  {hostname}")
# write srv-... since in IT
print("=" * 34)
# f is used to format the output in a secific form

print(f"GB USED : {occupied_space:>10.2f}")
print(f"TOTAL GB: {total_space:>10.2f}")
# float print to 2 s.f
print(f"FREE    : {difference:>+10.2f}")
# difference printed as positive or negative sign and to 2 s.f
print(f"PERCENT : {percent:>10.2f}")
#The percent will show as 2 s.f

print("=" * 34)
#Then run the code


