# container setup
a_tuple = (1, 2, 3, 'a string')
# tuple.append('another word') Not valid becasue immutable

a_list = [1, 2, 2, 3, 3, 'a string']
a_list.append('another word')
a_set = {1, 2, 3, 4, 4}
print(a_set)
print(set(a_list))

a_dict = {'key': 'value', 123: [1, 2, 3]}
print(a_dict)
