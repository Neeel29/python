# f-strings
user_name = "Neel"
user_age = 24
user_info = f"{user_name} is {user_age} years old."
bad_approach = user_name + " is " + str(user_age) + " years old."

print(user_info)

# single line if statement
user_status = 'Adult' if user_age >= 18 else 'Child'
print(user_status)

# List comprehension
# for i in range(0, 10, 1):
#   simple_list.append(i)
simple_list = [f'{j}{i}' for i in range(0, 11, 1) for j in ['a', 'b', 'c'] if j == 'a']
print(simple_list)

# Lambda functions
# def double_value(number):
#   return number * 2
double_value = lambda num: num*2
print(double_value(2))

# Some functions want a function as an arguement
random_list = [('Anna', 25), ('Paul', 20), ('Lisa', 46)]
sorted_list = sorted(random_list, key = lambda user_tuple: user_tuple[1])
print(sorted_list)