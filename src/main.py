'''Main File'''

from functions import generate_schedule, count_concurrencies, submit_data

schedule = []

with open(file='./data/Schedule.txt', mode='r', encoding='utf-8') as file:
    schedule = file.readlines()

d_schedule=generate_schedule(schedule)
d_concurrencies=count_concurrencies(d_schedule)
submit_data(d_concurrencies)

