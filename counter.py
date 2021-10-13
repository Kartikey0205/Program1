import time

# countdown timer 
def countdown(t):
    while t: # while t > 0 for clarity 
      mins = t // 60
      secs = t % 60
      timer = '{:02d}:{:02d}'.format(mins, secs)
      print(timer, end="\r") # overwrite previous line 
      time.sleep(1)
      t -= 1
    print('Blast Off!!!')
t = input("Enter the time in seconds: ") 

countdown(int(t))


# pomodoro timer 
def pomodoro(): 
  print("Pomodoro starts now!")
  for i in range(4):
    t = 25*60
    while t: 
      mins = t // 60 
      secs = t % 60
      timer = '{:02d}:{:02d}'.format(mins, secs) 
      print(timer, end="\r") # overwrite previous line 
      time.sleep(1)
      t -= 1 
    print("Break Time!!")

    t = 5*60 
    while t: 
      mins = t // 60 
      secs = t % 60
      timer = '{:02d}:{:02d}'.format(mins, secs) 
      print(timer, end="\r") # overwrite previous line 
      time.sleep(1)
      t -= 1 
    print("Work Time!!")

pomodoro()

