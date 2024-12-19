# If condition
if 1 > 1:
    print("In if condition!")
elif 3 == 3 and 2 > 1:
    print("This is else if condition")
else:
    print("Else part!")

# While loop
count = 0
while count <= 5:
    print(count)
    if(count == 5): 
        print("Count is 5!")
    count += 1

# For loop
test_list = [1, 2, 3, 4, 5]
test_dict = {7: '1', 8: '2', 9: '3'}
for x in test_list:
    print(x, '->')
for key, value in test_dict.items(): # dict.key(), dict.values(), dict.items()
    print(key, value, '=>')

# Truthy or falsy
if 0: # [], {}, () falsy because empty containers
    print('0')
else: 
    print('1')
