import time
import webbrowser

total_breaks = 3
breake_count = 0

print("This prigram started on " + time.ctime())
while(breake_count < total_breaks):
    time.sleep(2*60*60)
    webbrowser.open("http://google.com")
    breake_count = breake_count + 1
