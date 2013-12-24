# -- coding: utf-8 --

GLOBAL_A = 1

def adder(param_b):
    local_c = GLOBAL_A + param_b
    return local_c

print adder(2)


# enclosing function scope
#
# def adder(param_b):
#     local_c = GLOBAL_A + param_b

#     def nested_func(local_c):
#         local_c = local_c + 1

#     return local_c

# print adder(2)


# similarly
#
# def nested_func(local_c):
#     local_c = local_c + 1

# def adder(param_b):
#     local_c = GLOBAL_A + param_b
#     nested_func(local_c)
#     return local_c

# print adder(2)