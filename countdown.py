import time 

def count_down(t):
    try: 
       while t:
          mins, sec = divmod(t, 60)
          timer = '{:02d}:{:02d}'.format(mins, sec)
          print(timer, end="\r")
          time.sleep(1)
          t -= 1

          print("Timer Completed!")
    except(t):
       print("Please Enter Number", t)

t = int(input("Enter the Time in Second: "))

count_down(t)