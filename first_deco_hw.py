from decorator import pass_by_value

@pass_by_value
def reverse(list_of_values, another_list=[], yet_another_list=[]):
    list_of_values.sort(reverse=True)
    return list_of_values


values_list = [1,2,3,4,5,6,7,8,9]

print(values_list)
new_values_list = reverse(values_list)
print(new_values_list)
print(values_list)