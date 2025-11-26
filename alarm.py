import datetime
import os
import time
import random
import webbrowser

VIDEO_FILE = "youtube_alarm_videos.txt"
MESSAGE_FILE = "alarm_messages.txt"

# Ensure video file exists
if not os.path.isfile(VIDEO_FILE):
    print(f'Creating "{VIDEO_FILE}"...')
    with open(VIDEO_FILE, "w") as f:
        f.write("https://youtu.be/tXChZFcnsBE?si=QEZ0dMKFGgHVbZsR")
# Ensure messages file exists
if not os.path.isfile(MESSAGE_FILE):
    print(f'Creating "{MESSAGE_FILE}"...')
    with open(MESSAGE_FILE, "w") as f:
        f.write("hey baka!\nwake up baka!\nur a baka")

def check_alarm_input(alarm_time):
    if len(alarm_time) == 1:
        return 0 <= alarm_time[0] < 24
    if len(alarm_time) == 2:
        return 0 <= alarm_time[0] < 24 and 0 <= alarm_time[1] < 60
    if len(alarm_time) == 3:
        return 0 <= alarm_time[0] < 24 and 0 <= alarm_time[1] < 60 and 0 <= alarm_time[2] < 60
    return False

# Input: Multiple alarms
print("if u have multiple nter the times and seperate them by commas (e.g., 06:30, 18:45:00):")
while True:
    alarm_input = input(">> ")
    try:
        alarm_times = []
        for t in alarm_input.split(","):
            parts = [int(n) for n in t.strip().split(":")]
            if check_alarm_input(parts):
                alarm_times.append(parts)
            else:
                raise ValueError
        break
    except ValueError:
        print("ERROR")

# Convert to seconds
seconds_hms = [3600, 60, 1]
now = datetime.datetime.now()
current_seconds = sum([a * b for a, b in zip(seconds_hms, [now.hour, now.minute, now.second])])

alarm_seconds_list = []
for alarm_time in alarm_times:
    alarm_sec = sum([a * b for a, b in zip(seconds_hms[:len(alarm_time)], alarm_time)])
    if alarm_sec < current_seconds:
        alarm_sec += 86400  # next day
    alarm_seconds_list.append(alarm_sec - current_seconds)

for i, wait_time in enumerate(sorted(alarm_seconds_list)):
    print(f"Alarm {i+1} set to go off in {datetime.timedelta(seconds=wait_time)}")

# Run alarms 
for wait_time in sorted(alarm_seconds_list):
    time.sleep(wait_time)
    print("Wakey wakey eggs and bakey baka")

    # msg
    with open(MESSAGE_FILE, "r") as f:
        messages = f.readlines()
    print(random.choice(messages).strip())

    # Vid
    with open(VIDEO_FILE, "r") as f:
        videos = f.readlines()
    webbrowser.open(random.choice(videos))

    # Snooze
    snooze = input("js get up bro, but like if ur still tired answer y or n to if u want to sleep like 5 more min ok (y/n): ").strip().lower()
    if snooze == "y":
        print("slepy time")
        time.sleep(300)  # 5 minutes
        print("ok like actually stop sleping now")
        webbrowser.open(random.choice(videos))
    print("finna done :).\n")
