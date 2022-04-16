'''Functions to data analyst'''

from datetime import time


def hour_format(str_hour):
    '''
    Return:
    '''
    l_hour = str_hour.split(":")
    return time(int(l_hour[0]), int(l_hour[1]))


schedule = []
d_general = {}
d_veces = {}


with open(file='./data/Schedule.txt', mode='r', encoding='utf-8') as file:
    schedule = file.readlines()

for employee_line in schedule:
    info = employee_line.strip().split("=")
    name_employee = info[0]
    week_days_worked = info[1].split(",")
    for day_hours_info in week_days_worked:
        day = day_hours_info[:2]
        hours_worked = day_hours_info[2:]
        d_general[day] = d_general.get(day, {})
        d_general[day][name_employee] = hours_worked

# print(d_general)

for d_user in d_general.values():
    for name_employee, hours in d_user.items():
        l_hours = hours.split("-")
        start_h = hour_format(l_hours[0])
        end_h = hour_format(l_hours[1])
        for name_emplo_friend, hours_friend in d_user.items():
            if name_employee != name_emplo_friend:
                l_hours_friend = hours_friend.split("-")
                start_h_friend = hour_format(l_hours_friend[0])
                end_h_friend = hour_format(l_hours_friend[1])
                if (start_h_friend <= start_h < end_h_friend) or (start_h_friend < end_h <= end_h_friend):
                    d1 = d_veces.get((name_employee, name_emplo_friend))
                    d2 = d_veces.get((name_emplo_friend, name_employee))
                    if d1 is None and d2 is None:
                        d_veces[(name_employee, name_emplo_friend)] = 0

                    else:
                        if d1 is not None:
                            d_veces[(name_employee, name_emplo_friend)] = d_veces.get(
                                (name_employee, name_emplo_friend), 0) + 1
                        if d2 is not None:
                            # d_veces[(name_emplo_friend, name_employee)] = d_veces.get(
                            #     (name_emplo_friend, name_employee), 0) + 1
                            print("hola")

print(d_veces)
