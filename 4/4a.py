from datetime import datetime

filename = "input.txt"

dates = []
wake_sleep = []
current_guard = ""

sleep_summary = []

current_object = {
    "guard": current_guard,
    "sleep": "",
    "wake": ""
}

def processLine(line):
    global dates
    global current_guard

    date = line.split("]")[0].strip('[').split(' ')[0]
    time = line.split("]")[0].strip('[').split(' ')[1]

    dt_string = date + " " + time
    dt_object = datetime.strptime(dt_string, '%Y-%m-%d %H:%M')

    dates.append((dt_object, line))

def processDate(line_object):
    global current_object
    global current_guard

    dt_object = line_object[0]
    line = line_object[1]


    if "begins shift" in line:
        current_guard = line.split("Guard ")[1].split(" ")[0]
        current_object["guard"] = current_guard
    elif "falls asleep" in line:
        current_object["sleep"] = dt_object
    elif "wakes up" in line:
        current_object["wake"] = dt_object
        wake_sleep.append(current_object)
        current_object = {
            "guard": current_guard,
            "sleep": "",
            "wake": ""
        }

def calc_sleep(e):
    sleep_time = e["wake"] - e["sleep"]
    sleep_time = (sleep_time.seconds/60)
    return sleep_time

def summarize_sleep(e):
    global sleep_summary

    for x in sleep_summary:
        if x["guard"] == e["guard"]:
            x["sleep_time"] += e["sleep_time"]
            return

    sleep_summary.append({
        "guard": e["guard"],
        "sleep_time": e["sleep_time"]
    })

def find_most_sleep_minute(guard):
    minute_array = []
    for i in range(00,60):
        minute_array.append(0)

    for e in wake_sleep:
        if e["guard"] == guard:
            for second in range(e["sleep"].minute, e["wake"].minute):
                minute_array[second] += 1

    most_minute = 0
    sleep_count = 0
    for i, e in enumerate(minute_array):
        if e > sleep_count:
            sleep_count = e
            most_minute = i
    print("Most sleep minute: ", most_minute)
    print("Sleep minute * guard # ", (most_minute * int(guard.strip("#"))) )

with open(filename) as my_file:
    for line in my_file:
        processLine(line.strip())

dates = sorted(dates, key=lambda dt_object: dt_object[0])
for d in dates:
    processDate(d)

for e in wake_sleep:
    e["sleep_time"] = calc_sleep(e)

for e in wake_sleep:
    summarize_sleep(e)

sleep_summary = sorted(sleep_summary, key=lambda dt_object: dt_object["sleep_time"])
most_asleep = sleep_summary[-1]
most_asleep_guard = most_asleep["guard"]
most_asleep_time = most_asleep["sleep_time"]

print(most_asleep_guard)
print(most_asleep_time)

find_most_sleep_minute(most_asleep_guard)
