# Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function

max_number = int(input('Enter the max number: '))

odd_numbers = list(range(1, max_number + 1, 2))
print(odd_numbers)
