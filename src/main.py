'''Main File'''

from functions import generate_schedule, count_concurrencies

schedule = []

with open(file='./data/Schedule.txt', mode='r', encoding='utf-8') as file:
    schedule = file.readlines()

d_schedule=generate_schedule(schedule)
d_concurrencies=count_concurrencies(d_schedule)

for names,times in d_concurrencies.items():
    print (f"{names[0]}-{names[1]}:{times}")
