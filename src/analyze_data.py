'''Methods used in main program'''

from datetime import time


class AnalyzeData:
    '''
    A class who reads a list with information from a .txt file and analyze how many times employees have coincided in the office
    '''

    def __init__(self):
        self.msg = "default constructor"

    def hour_format(self, str_hour):
        '''
        Return:
            hour(time): time type variable to compare with other hours
        Args:
            str_hour(str): string for convertion

        '''
        self.str_hour = str_hour
        if not isinstance(self.str_hour, str):
            raise TypeError("The hour must be a String")
        l_hour = self.str_hour.split(":")
        return time(int(l_hour[0]), int(l_hour[1]))

    def generate_schedule(self, schedule):
        '''
        Return:
            d_general(dict): dictionary {day:{name:hours_string}}
        Args:
            schedule(list): string for convertion
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

    def count_concurrencies(self, d_general):
        '''
        Return:
            d_concurrencies(dict): dictionary {(str_name1,str_name2)):int_count}
        Args:
            d_general(list): dictionary with information of the .txt file
        '''
        d_concurrencies = {}
        for d_user in d_general.values():
            for name_employee, hours in d_user.items():
                l_hours = hours.split("-")
                start_h = self.hour_format(l_hours[0])
                end_h = self.hour_format(l_hours[1])
                for name_emplo_friend, hours_friend in d_user.items():
                    if name_employee != name_emplo_friend:
                        l_hours_friend = hours_friend.split("-")
                        start_h_friend = self.hour_format(l_hours_friend[0])
                        end_h_friend = self.hour_format(l_hours_friend[1])
                        condition1 = start_h_friend <= start_h < end_h_friend
                        condition2 = start_h_friend < end_h <= end_h_friend
                        if condition1 or condition2:
                            d_format1 = d_concurrencies.get(
                                (name_employee, name_emplo_friend))
                            d_format2 = d_concurrencies.get(
                                (name_emplo_friend, name_employee))
                            if d_format1 is None and d_format2 is None:
                                d_concurrencies[(
                                    name_employee, name_emplo_friend)] = 1

                            elif d_format1 is not None:
                                d_concurrencies[(name_employee, name_emplo_friend)] = d_concurrencies.get(
                                    (name_employee, name_emplo_friend), 0) + 1
        return d_concurrencies

    def submit_data(self, d_concurrencies):
        '''
        Args:
            d_concurrencies(dict): dictionary {(str_name1,str_name2)):int_count}
        '''
        for names, times in d_concurrencies.items():
            print(f"{names[0]}-{names[1]}:{times}")
