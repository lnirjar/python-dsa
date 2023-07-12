# nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
#   1. What was the average temperature in first week of Jan
#   2. What was the maximum temperature in first 10 days of Jan
# Figure out data structure that is best for this problem

import os
file_path = os.path.join(os.path.dirname(__file__), 'nyc_weather.csv')

temperatures = []
with open(file_path, "r") as f:
    for index, line in enumerate(f):
        if index == 0:
            continue # ignore the heading row
        date, temperature = line.split(',')
        temperatures.append(int(temperature))

print(temperatures)

# 1. What was the average temperature in first week of Jan
first_week_temperatures = temperatures[0:7]
first_week_avg = round(sum(first_week_temperatures) / len(first_week_temperatures), 2)
print(first_week_avg)

# 2. What was the maximum temperature in first 10 days of Jan
print(max(temperatures[0:10]))
