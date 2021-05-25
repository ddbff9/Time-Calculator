def add_time(start, duration, day = False):
#Seperate the start time into hours, minutes, and period(AM/PM)
#**************************************************************
    
    #Splits the start time into a list
    start_pieces = start.split()
    
    #Splits time into a list of hours, minutes, and period(AM/PM)
    time_pieces = start_pieces[0].split(":")
    
    #Defines Start Time's Hours, Minutes, and Period (AM/PM)
    start_hrs = time_pieces[0]
    start_mins = time_pieces[1]
    start_period = start_pieces[1]

    #Sets Start Time Hrs and Minutes as Integers
    start_hrs = int(start_hrs)
    start_mins = int(start_mins)

    #DeBug Printing Statement -    DELETE
    print("\nStart Hours:", start_hrs)
    print("Start Minutes:", str(start_mins).zfill(2))
    print("Start Period:", start_period)

#Split duration into hrs and minutes
#***********************************

    #Splits the duration time hours and minutes
    duration_pieces = duration.split(":")

    #Splits the duration into a list of hours and minutes
    duration_hrs = duration_pieces[0]
    duration_mins = duration_pieces[1]

    #Sets Start Time Hrs and Minutes as Integers
    duration_hrs = int(duration_hrs)
    duration_mins = int(duration_mins)

    #Debug Printing Statement -     DELETE
    print("\nDuration Hours:", duration_hrs)
    print("Duration Minutes:", duration_mins, "\n")

    #If Statement for optional Day parameter
    if day:
        print("Day:", day, "\n")

#Calculate the New Time
#***********************
    
    #Addition of duration hours:
    new_hrs = start_hrs + duration_hrs
    
    #Addtiion of duration minutes:
    new_mins = start_mins + duration_mins

    #If addition of minutes causes hours to increase:
    if new_mins >= 60:
        new_mins = new_mins - 60
        new_hrs +=1
    
    #Determine New Time Period (AM/PM):
    if new_hrs < 12:
        new_period = start_period
    
    if new_hrs >= 12:
        if start_period == "AM":
            new_period = "PM"
        else:
            new_period = "AM"
    
    #If hours rolls over 12...
    if new_hrs >= 13:
        new_hrs -= 12
        


    #Debug Printing Statement -     DELETE
    print("New Hours:", new_hrs)
    print("New Minutes:", str(new_mins).zfill(2))
    print("New Period:", new_period)
    # return new_time

add_time("9:06 PM", "2:54")