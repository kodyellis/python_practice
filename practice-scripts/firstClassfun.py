#!/usr/bin/python
# def square(x):
#     return x * x

# f= square #Assign function as variable
#
# print(square)
# print(f(5))#uses variable as function
# def cube(x):
#     return x * x * x
#
# def my_map(func, arg_list):
#     result = []
#     for i in arg_list:
#         result.append(func(i))
#     return result
# # squares = my_map(square, [1,2,3,4,5])
# cubes = my_map(cube, [1,2,3,4,5])
#
# # print(squares)
# print(cubes)

# def logger(msg):
#
#     def log_message():
#         print('Log:', msg)
#     return log_message
#
# log_hi = logger('hi!!!')
# log_hi()#uses variable as function also clojures

def html_tag(tag):
#
    def wrapper_text(msg):
         print('<{0}>{1}</{0}>'.format(tag, msg))

    return wrapper_text

print_h1 = html_tag('h1')
print_h1('Test headline')
# log_hi()#uses variable as function also closures
