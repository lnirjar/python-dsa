# poem.txt Contains famous poem "Road not taken" by poet Robert Frost. You have to read this file in python and print every word and its count as show below. Think about the best data structure that you can use to solve this problem and figure out why you selected that specific data structure.
#  'diverged': 2,
#  'in': 3,
#  'I': 8

import os
import re

file_path = os.path.join(os.path.dirname(__file__), 'poem.txt')

content = ''
with open(file_path, 'r') as f:
    content = f.read()

word_count_dict = {}
words = re.split(r'\W+', content)
for word in words:
    key = word.lower()
    word_count_dict[key] = word_count_dict.get(key, 0) + 1

for word in word_count_dict:
    if not word:
        continue # ignore empty string
    print(f'{word}:', word_count_dict[word])
