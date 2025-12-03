
#GROUP: David Gil, Jonathan Medina, Giovanni Villanueva 
#classroom hall monitor challenge 


#1. Create the hall pass lists: You will start by creating two lists:
students= ["Alice", "Bob", "Charlie", "Alice", "David"] 
minutes_gone = [3, 7, 12, 4, 11]

print("=== HallPass Security Report ===\n")
#2-4
for i in range(len(students)):
    name = students[i]
    minutes = minutes_gone[i]


    # Count how many times this student's name appears
    repeat_count = students.count(name)

    # APPLY HALLWAY RULES 
    if minutes <= 5:
        status = "OK"
    elif 6 <= minutes <= 10:
        status = "WARNING"
    else:                      # minutes > 10
        status = "FLAGGED"

    # SPECIAL FLAG RULE 
    if minutes > 10 or repeat_count > 1:
        status = "FLAGGED"

    # Add note for duplicate names
    if repeat_count > 1:
        note = "(Duplicate name detected!)"


    # 5. PRINT THE REPORT LINE FOR STUDENT
   
    print(f"Student: {name}")
    print(f"Minutes gone: {minutes}")
    print(f"Status: {status} {note}")
    print("------------------------")
 #Their st


