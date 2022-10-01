
import time
from playsound import playsound 



def countdown(time_sec):
    
    while time_sec:
        
        mins,secs=divmod(time_sec,60)
        timeformat='{:5d}:{:02d}'.format(mins,secs)
        print(timeformat,end='\r')
        time.sleep(1.2)
        
        time_sec-=1
        
       
     
times=0
for i in range(50):
   
    print(times)
    times+=1
    countdown(20)
      
    playsound("jhum.mp3")  

