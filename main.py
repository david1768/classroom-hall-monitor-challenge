#GROUP: David Gil, Jonathan Medina, Giovanni Villanueva 


#classroom hall monitor challenge 

print("HALL PASS REPORT")
print("----------------------")
#1. Create the hall pass lists: You will start by creating two lists:
# One list that holds the names of students currently out on a hall pass.
student_names = ["Alice", "Bob", "Charlie", "Alice", "David"] 



# A second list that holds how many minutes each student has been gone.
minutes_gone = [3, 7, 12, 4, 11]

# Each name in the first list should match the same position in the minutes list.
# (Example: the first student in the list corresponds to the first number of minutes.)
# Your job: Create both lists so that the positions (indexes) match.


# 2. Loop through the list and do the following for each student: Next, you will go through each student one-by-one and decide if they are:
# OK

# WARNING

# FLAGGED

#To do this, you will use:
#Comparison operators  (such as checking if minutes are less than, greater than, or equal to certain values)
#Logical operators (such as using and/or to combine conditions)

#Your job:  Create conditions that examine the number of minutes each student has been gone and decide which category they belong in.
#Notes: how to work with loops and how to work with while loops

# 3. Classify each student
#Follow these hallway rules in your logic:
print("HALL PASS REPORT")
print("----------------------")
# Loop through every student
for i in range(len(student_names)):
    name = student_names[i]
        minutes = minutes_gone[i]

        # Count how many times the student's name shows up
        repeats = student_names.count(name)

         # Figure out the status
          # Special rule: if they have been gone over 10 min OR have a duplicate name
          if minutes > 10 or repeats > 1:
                  status = "FLAGGED"
                          notes = ""

                          if minutes > 10:
                              notes += "Over 10 minutes. "

                              if repeats > 1:
                                   notes += "Name appears more than once."
                                       
                                       else:
                                           if minutes <= 5:
                                                status = "OK"
                                                     not:
                                                                     if notes: ""
                                                                  else:
                                                                   status = "FLAGGED"
                                                                   notes = "Over 10 minutes."

                                                                           # Print the results
                                                                           print("Student:", name)
                                                                                                     print("Status:", status)
                                                                                       print("Notes:", notes)
                                                                                   print("----------------------")

                                                                                   #4. Add an additional rule using logical operators. Add the Special Flag Rule (Using Logical Operators) A student must be automatically flagged if either of these are true:They have been out longer than 10 minutes


                                                                                   #Their name appears more than once in the list (meaning they left the room more than once)


                                                                                   # You will need to check how many times a name appears in the list.
                                                                                   # Your job: Create a condition that checks both of these possibilities and marks a student as flagged if either condition is true.


                                                                                   # 5. Create and print a report Create a Report With Your Results: Once you have categorized each student, you will produce a summary report.
                                                                                   #Your report should list:
                                                                                   #The student’s name


                                                                                   #Their status (OK
 WARNING, 



         Your job: Create both lists so that the positions (indexes) match.


# 2. Loop through the list and do the following for each student: Next, you will go through each student one-by-one and decide if they are:
# OK

# WARNING

# FLAGGED

#To do this, you will use:
#Comparison operators  (such as checking if minutes are less than, greater than, or equal to certain values)
#Logical operators (such as using and/or to combine conditions)

#Your job:  Create conditions that examine the number of minutes each student has been gone and decide which category they belong in.
#Notes: how to work with loops and how to work with while loops

# 3. Classify each student
#Follow these hallway rules in your logic:
print("HALL PASS REPORT")
print("----------------------")
# Loop through every student
for i in range(len(student_names)):
    name = student_names[i]
    minutes = minutes_gone[i]

# Count how many times the student's name shows up
repeats = student_names.couny have been gone over 10 min OR# have a duplicate name
if minutes > 10 or repeats > 1:
        status = "FLAGGED"
        notes = ""

if minutes > 10:
    notes += "Over 10 minutes. "

if repeats > 1:
     notes += "Name appears more than once."
    
else:
    if minutes <= 5:
     status = "OK"
     notes = ""
    elif minutes <= 10:
         status = "WARNING"
if notes: ""
else:
 status = "FLAGGED"
notes = "Over 10 minutes."

        # Print the results
print("Student:", name)
print("Minutes gone:", minutes)
print("Status:", status)
if notes != "":
    print("Notes:", notes)
    print("----------------------")

#4. Add an additional rule using logical operators. Add the Special Flag Rule (Using Logical Operators) A student must be automatically flagged if either of these are true:They have been out longer than 10 minutes


#Their name appears more than once in the list (meaning they left the room more than once)


# You will need to check how many times a name appears in the list.
# Your job: Create a condition that checks both of these possibilities and marks a student as flagged if either condition is true.


# 5. Create and print a report Create a Report With Your Results: Once you have categorized each student, you will produce a summary report.
#Your report should list:
#The student’s name


#Their status (OK, WARNING, or FLAGGED)


#Any special notes (such as “duplicate name detected”)


#Your job: Print a clean, readable report showing the results for each student




