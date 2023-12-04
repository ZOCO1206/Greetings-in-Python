import time
t = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
hour = int(input("Enter ThE hours: "))
print(hour)
if (hour>=0 and hour<12):
  print("Good Morning ")
elif (hour>=12 and hour<17):
  print("Good Evening")
elif (hour>=17 and hour<0):
  print("Good Night ")