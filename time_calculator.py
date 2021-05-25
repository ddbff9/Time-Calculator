def add_time(start, duration, day = False):

#Seperate the start time into hours, minutes, and period(AM/PM)
#**************************************************************
    #Days of the week list:
    weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    weekdays_lower = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]

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

#Calculate how many additional Days and Hours should be added to start time
#***************************************************************************

    add_days = int(duration_hrs)//24
    add_hrs = int(duration_hrs)%24

#Calculate how many additional minutes should be added to start time
#***************************************************************************

    new_mins = start_mins + duration_mins

    #If addition of minutes causes hours to increase:
    if new_mins >= 60:
        new_mins = new_mins - 60
        add_hrs +=1

#Calculate the New Time
#***********************
    
    #Step 01: Convert to 24 hour clock:
    if start_period == "PM":
        start_hrs +=12    

    #Step 02: Make sure additional hours is less than 24.
    if add_hrs > 24:
        add_hrs -= 24
        add_days +=1

    #Step 03: Make sure new hours is less than 24.
    new_hrs = start_hrs + add_hrs
    if new_hrs >= 24:
        new_hrs -= 24
        add_days +=1

    #Step 04: Convert time back to standard time.
    if new_hrs == 12:
        new_period = "PM"
    
    if new_hrs == 0:
        new_hrs +=12
        new_period = "AM"
        
    if new_hrs < 12:
        new_period = "AM"

    if new_hrs > 12:
        new_hrs -= 12
        new_period = "PM"
    
    #Step 04: Concatenate hrs and mins into time string.
    new_time = str(new_hrs) + ":" + str(new_mins).zfill(2) + " " + new_period

    #Step 05: Determine if time went into future days.
    if day == False and add_days == 1:
        new_time = new_time + " (next day)"
    
    if day == False and add_days >1:
        new_time = new_time + f" ({add_days} days later)"

#Calculate Day of the Week
#**************************
    
    #Step 01: Find Day of week in list.
    if day:
        weekday_index = weekdays_lower.index(str(day).lower())
    
    #Step 02: Determine new day of the week.
        day_index = weekday_index + int(add_days)%7

    #Step 03: Ensure index for day of week is between 0 and 6.
        if day_index > 6:
            day_index -= 7
    
    #Step 04: Concatenate day information to the new time.
        if add_days <1:
            new_time = new_time + f", {weekdays[day_index]}"
        if add_days ==1:
            new_time = new_time + f", {weekdays[day_index]} (next day)"
        if add_days > 1:
            new_time = new_time + f", {weekdays[day_index]} ({add_days} days later)"    

    return new_time