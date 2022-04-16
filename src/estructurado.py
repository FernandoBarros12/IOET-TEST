'''Test'''


schedule = []
# l_employees_names=[]
with open('Schedule.txt', 'r', encoding='utf-8') as file:
    schedule=file.readlines()

d_general = {}  # {name:d_schedule}

for employee in schedule:  # creation of d_general
    info = employee.strip().split("=")
    week_days = info[1].split(",")
    d_schedule = {}  # {day:hours}
    for day in week_days:
        d_schedule[day[:2]] = day[2:]
    d_general[info[0]] = d_schedule
file.close()
print(d_general)

# for name, dic in d_general.items():
#     print(dic)
