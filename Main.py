my_list = [1,2,3,4,5]
print(my_list[1:4])
print(my_list[::-1])

my_list.append(6)
my_list.extend([7,8])
del my_list[1]

print(my_list)

list1 = [1,2,3]
list2 = [4,5,6]
concatenated_list = list1 + list2
print(concatenated_list)
repeated_list = list1 * 3
print(repeated_list)
print(2 in list1)
print(len(list1))