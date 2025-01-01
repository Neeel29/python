# functions
print("Print function")

# methods -> functions of datatypes
print('value'.upper())
print("VALUE".lower())
print('value'.replace('e', '3'))

# New functions
print(abs(-1325))
print(max(1, 2))
print(min(1 , 2))
print(len('test'))

# User defined functions
def print_x_times(parameter, loop_amount = 0):
  counter = 0
  while counter < loop_amount:
    print(counter, parameter)
    counter += 1
  
print_x_times("Neel", 5)