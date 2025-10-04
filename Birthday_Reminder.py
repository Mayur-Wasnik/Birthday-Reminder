import datetime
current_date = datetime.date.today()
bday_log = [
   ('Ayushi', datetime.date(1999, 10, 19)),
   ('Yash', datetime.date(1999, 4, 21)),
]
add = input('To add birthday type y:').strip().lower()

if add[:1] == 'y':
   while True:
      new = input('Add birthday in format yyyy-mm-dd:')
      try:
         bday_date = datetime.datetime.strptime(new, '%Y-%m-%d').date()
         break
      except ValueError:
         print('Invalid date format. Please use yyyy-mm-dd.')
   name = input('Whose bday?')
   bday_log.append((name, bday_date))
   # Log the new entry to a file
   with open('birthday_log.txt', 'a') as log_file:
      log_file.write(f"{name},{bday_date}\n")

for birthday in bday_log:
   # Check if today is the person's birthday
   if (current_date.month, current_date.day) == (birthday[1].month, birthday[1].day):
      age = current_date.year - birthday[1].year
      # Handle ordinal suffix
      if 10 < age % 100 < 14:
         ordinal_suffix = 'th'
      else:
         ordinal_suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(age % 10, 'th')
      print(f" It's {birthday[0]}'s {age}{ordinal_suffix} Birthday")