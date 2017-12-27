
import time, sys

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        sys.stdout.write('\r' + str(timeformat))
        sys.stdout.flush() # important
        time.sleep(1)
        t -= 1
    print
    print("Time's Up!")