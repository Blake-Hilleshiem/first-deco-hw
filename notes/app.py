from decorator import convert_to_strings, convert_to_numbers, pass_by_value
from math import fsum

@convert_to_strings
def concat(list_of_items, sep=' '):
    return sep.join(list_of_items)


# item_list = ['Hi','there','.','I','like', 'pie', 'times', 20]

# print(concat(item_list))

@convert_to_numbers
def sum_all(list_of_numbers):
    return fsum(list_of_numbers)

def sum_all_two(*args):
    print(args)
    return sum(args)

# print(sum_all_two(1,2,3,4,5,6,7))

@pass_by_value
def reverse(list_of_values):
    # list_of_values = list_of_values[::-1]
    list_of_values.sort(reverse=True)
    # return list_of_values[::-1]
    return list_of_values

values_list = [1,2,3,4,5,6,7,8,9]
print('before: ', values_list)

new_values_list = reverse(values_list)

print('new after func:', new_values_list)
print('orginal var:', values_list)

# list_of_nums = [1, 2, 3, 4, 5, 6, 7, 9, '10.33']
# print(sum_all(list_of_nums))

# x = '2'

# print(isinstance(x, int))
# print(isinstance(x, float))

# .copy()