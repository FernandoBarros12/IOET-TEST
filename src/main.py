from posixpath import split


file = open("Schedule.txt", "r")
schedule= file.readlines()
#l_employees_names=[]

def crear_Diccionario(archive):
    d_general={} #{name:d_schedule}
    d_schedule={} #{day:hours}
    for employee in schedule: #creation of d_general
        info=employee.split("=")
        name=info[0]
        week_days=info[1].split(",")
        for day in week_days:
            d_schedule[day[:2]]=day[2:]
        d_general[name]=d_schedule
    file.close()
    return d_general

d=crear_Diccionario(schedule)

print (d)

