'''Functions used in main program'''

from datetime import time
from tokenize import String

def hour_format(str_hour):
    '''
    Return:
        hour(time): time type variable to compare with other hours
    Parameters:
        str_hour(string): hour in string type for convertion
    '''

    if not isinstance(str_hour, str):
        raise TypeError("The hour must be a String")
    
    l_hour = str_hour.split(":")
    return time(int(l_hour[0]), int(l_hour[1]))

def generate_schedule (schedule):
    '''
    Return:
    '''
    d_general={}
    for employee_line in schedule:
        info = employee_line.strip().split("=")
        name_employee = info[0]
        week_days_worked = info[1].split(",")
        for day_hours_info in week_days_worked:
            day = day_hours_info[:2]
            hours_worked = day_hours_info[2:]
            d_general[day] = d_general.get(day, {})
            d_general[day][name_employee] = hours_worked
    return d_general

def count_concurrencies (d_general):
    '''
    Return:
    '''
    d_concurrencies={}
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
                        d_format1 = d_concurrencies.get((name_employee, name_emplo_friend))
                        d_format2 = d_concurrencies.get((name_emplo_friend, name_employee))
                        if d_format1 is None and d_format2 is None:
                            d_concurrencies[(name_employee, name_emplo_friend)] = 1

                        elif d_format1 is not None:
                            d_concurrencies[(name_employee, name_emplo_friend)] = d_concurrencies.get(
                                (name_employee, name_emplo_friend), 0) + 1
    return d_concurrencies

def submit_data(d_concurrencies):
    for names,times in d_concurrencies.items():
        print (f"{names[0]}-{names[1]}:{times}")
