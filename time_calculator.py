def add_time(start, duration, day="day"):
  # Dict for counting days, if selected.
  hr, minutes, count_days = int, int, int
  days = {
         1: "Monday", 
         2: "Tuesday", 
         3: "Wednesday", 
         4: "Thursday", 
         5: "Friday", 
         6: "Saturday", 
         7: "Sunday"
        }
  # format day input, first make all char lowercase
  # then capitalize first char.
  if bool(day):
    day = day.lower().capitalize() 
  # split start time into hour, minute, and am/pm.
  t = start.split()
  # partition hour and minutes from start.
  shr, sm = t[0].partition(":")[0], t[0].partition(":")[2]
  # partition hour and minutes from duration.
  dhr, dm = duration.partition(":")[0], duration.partition(":")[2]
  
  am_pm = t[1]

  # Convert to 24hr.
  if am_pm == "PM":
    shr = int(shr) + 12

  hr = int(shr) + int(dhr)
  minutes = int(sm) + int(dm)
  # Count days.
  if hour > 24:
    count_days += 1

  if hr > 12:
    hr = hr - 12
    if am_pm == "PM":
      am_pm = "AM"
    else:
      am_pm = "PM"

  # convert back to 12hr clock
  if hr > 12:
    hr -= 12
    am_pm = "AM"
  # the number after the colon in minutes adds the leading zero.
  if bool(day):
    new_time = f'{hr}:{minutes:02} {am_pm}, {d}'
  else: 
    new_time = f'{hr}:{minutes:02} {am_pm}' 

  return new_time

if __name__ == "__main__":
  print(add_time("11:06 PM", "2:02"))