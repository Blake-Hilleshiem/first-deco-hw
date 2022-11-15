import functools

def convert_to_strings(func):
    @functools.wraps(func)
    def wrapper_func(*args,**kwargs):

        item_list = args[0]
        for i in range(len(item_list)):
            item_list[i] = str(item_list[i])

        return (
          func( *args, **kwargs)
        )
    return wrapper_func

def convert_to_numbers(func):
    @functools.wraps(func)
    def wrapper_func(*args, **kwargs):
        lst = args[0]
        for i in range(len(lst)):
            # if str(lst[i]).isdigit() == False:
            #     return "List contains non numbers"

            try:
                lst[i] = int(lst[i])
                
            except:
                lst[i] = float(lst[i])


        return (func(*args, **kwargs)
        )
    return wrapper_func

def pass_by_value(func):
    @functools.wraps(func)
    def wrapper_func(*args,**kwargs):

        new_args = []
        
        for i in range(len(args)):
            copy_of_arg = args[i].copy()
            new_args.append(copy_of_arg)

        args = tuple(new_args)

        return (
            func(*args, **kwargs)
        )
    return wrapper_func








# -------------
# decorator will be looking for the next instance of a funcation definition

# args is a tuple, it is immutable
# Note for pass by reference:

#  args[0] is a reference to a list in memory
#  item_list is also a reference to the same list in the same position in memory

# vs. pass by value

# shallow vs deep copy
# shallow copies at top level and as it comes across an object
