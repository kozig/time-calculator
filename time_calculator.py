def add_time(start, duration, day=None):
  
  # format day input, first make all char lowercase
  # then capitalize first char.
  if bool(day):
    day = day.lower().capitalize()
    # Dict for counting days, if selected.
    days = {
         1: "Monday", 
         2: "Tuesday", 
         3: "Wednesday", 
         4: "Thursday", 
         5: "Friday", 
         6: "Saturday", 
         7: "Sunday"
        }
    
  # get day number from dict to use later
  if bool(day):
    for key in days:
      if day == days[key]:
        day_number = int(key)
 
  # split start time into hour, minute, and am/pm.
  start_time = start.split()

  # partition hour and minutes from start.
  start_hr, start_min = int(start_time[0].partition(":")[0]), int(start_time[0].partition(":")[2])
  am_pm = start_time[1]

  # partition hour and minutes from duration.
  duration_hr, duration_min = int(duration.partition(":")[0]), int(duration.partition(":")[2])
  
  day_count = 0

  total_hours = start_hr + duration_hr
  total_minutes = start_min + duration_min

  while total_minutes >= 60:
    total_minutes -= 60
    total_hours += 1

  if am_pm == "PM" and total_hours >= 12:
    day_count += 1

  while total_hours >= 24:
    total_hours -= 24
    day_count += 1
      

  if bool(day):
    final_day = (day_number + day_count)
    while final_day > 7:
      final_day -= 7

  if total_hours >= 12:
    total_hours -= 12
    if am_pm == "AM":
      am_pm = "PM"
    elif am_pm == "PM":
      am_pm = "AM"
  
  if total_hours == 0:
    total_hours = 12
      
  
  if bool(day):
    if day_count > 0:
      if day_count == 1:
        return f"{total_hours}:{total_minutes:02} {am_pm}, {days[final_day]} (next day)"
      else :
        return f"{total_hours}:{total_minutes:02} {am_pm}, {days[final_day]} ({day_count} days later)"
    else:
      return f"{total_hours}:{total_minutes:02} {am_pm}, {days[final_day]}"
  else:
    if day_count > 0:
        if day_count == 1:
          return f"{total_hours}:{total_minutes:02} {am_pm} (next day)"
        else :
          return f"{total_hours}:{total_minutes:02} {am_pm} ({day_count} days later)"
    else:
      return f"{total_hours}:{total_minutes:02} {am_pm}"
if __name__ == "__main__":
  print(add_time("11:06 PM", "12:02", "friday"))