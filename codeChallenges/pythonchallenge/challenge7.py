a = [1, 2, 3, 4, 5, 6]
b = [34, 2, 9, 91, 19, 401, 0]

def print_odd_numbers(array):

    for i in array:
        if i % 2 != 0:
            print("These is an odd number of the array:", i)

print_odd_numbers(a)

print_odd_numbers(b)