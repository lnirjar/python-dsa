# nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
#   1. What was the temperature on Jan 9?
#   2. What was the temperature on Jan 4?
# Figure out data structure that is best for this problem

import os

file_path = os.path.join(os.path.dirname(__file__), 'nyc_weather.csv')

temperatures = {}
with open(file_path, 'r') as f:
    f.readline() # ignore heading row
    line = f.readline()
    while line:
        date, temperature = line.split(',')
        temperatures[date] = int(temperature)
        line = f.readline()

print(temperatures)

# 1. What was the temperature on Jan 9?
print(temperatures['Jan 9'])

# 2. What was the temperature on Jan 4?
print(temperatures['Jan 4'])
