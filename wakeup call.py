import datetime
import time
import winsound 

def set_alarm():
    alarm_time = input("Enter alarm time in HH:MM:SS format: ")
    print(f"Alarm set for {alarm_time}")

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Wake up!")
            for i in range(5):
                winsound.Beep(1000, 1000)
            break
        time.sleep(1)

set_alarm()
