'''Concurrencies between employees'''

from analyze_data import AnalyzeData


def main():
    '''
    Main clase that reads a .txt file and output pairs of employees 
    with how many times they have seen each other at work
    '''
    with open(file='./data/Schedule.txt', mode='r', encoding='utf-8') as file:
        schedule = file.readlines()
    employees = AnalyzeData()
    d_schedule = employees.generate_schedule(schedule)
    d_concurrencies = employees.count_concurrencies(d_schedule)
    employees.submit_data(d_concurrencies)


if __name__ == "__main__":
    main()
