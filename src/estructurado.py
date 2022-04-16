'''Functions to data analyst'''

schedule = []
with open(file='./data/Schedule.txt', mode='r', encoding='utf-8') as file:
    schedule = file.readlines()
d_general = {}

for employee_line in schedule:
    info = employee_line.strip().split("=")
    name_employee = info[0]
    week_days_worked = info[1].split(",")
    for day_hours_info in week_days_worked:
        day = day_hours_info[:2]
        hours_worked = day_hours_info[2:]
        d_general[day] = d_general.get(day, {})
        d_general[day][name_employee] = hours_worked

print(d_general)
