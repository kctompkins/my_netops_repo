my_list = [1,2,3]
print(my_list)
print(my_list[0])
print(my_list[1])
print(my_list[2])
print("# command: my_list.append('four')")
my_list.append("four")
print(my_list)
print("# command: del my_list[2]")
del my_list[2]
print(my_list)
print("# Add nested_list")
nested_list = []
nested_list.append(123)
nested_list.append(22)
nested_list.append("ntp")
nested_list.append("ssh")
print("# command: my_list.append(nested_list)")
my_list.append(nested_list)
print(my_list)
print(my_list[3])
print(my_list[3][2])
# print(my_list[0][1])
print("# Print the letter 'o' from the list item 'four'")
print("# command: print(my_list[2][1]")
print(my_list[2][1])
# Experiment with Slicing
print("# command: slice = my_list[1:3]")
slice = my_list[1:3]
print(slice)
print("# Slice ip address")
slice_me = "ip address"
sliced = slice_me[:2]
print("# command: sliced = slice_me[:2]")
print(sliced)
print("# slicing functions: [start:end -1] [start: ] [:end]")
