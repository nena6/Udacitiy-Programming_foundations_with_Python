import webbrowser
import time

break_count=0
total_breaks=3
break_duration=10

while (break_count < total_breaks):
    time.sleep(break_duration)
    webbrowser.open("https://www.google.com")
    break_count+=1

