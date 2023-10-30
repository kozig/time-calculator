def add_time(start, duration, d="d"):
  # Dict for counting days, if selected.
  day = {
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
  d = d.lower().capitalize() 
  # split start time into hour, minute, and am/pm.
  t = start.split()
  # partition hour and minutes from start.
  shr = t[0].partition(":")[0]
  sm = t[0].partition(":")[2]
  # partition hour and minutes from duration.
  dhr = d[0].partition(":")[0]
  dm = duration.partition(":")[2]
  
  am_pm = t[1]
  
  hr = int
  minutes = int
  
  hr = shr + dhr
  minutes = sm + dm
  new_time = f'{hr} + ":" + {minutes} + " " + {am_pm}'





  return new_time

if __name__ == "__main__":
  print(add_time("11:06 PM", "2:02"))