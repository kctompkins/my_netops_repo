my_dict = {}
print(type(my_dict))
print("# Add to my_dict some keys and values")
my_dict["gigE0"] = "Link to ISP"
my_dict["gigE1"] = "Link to DNS"
my_dict["gigE2"] = "Link to DMZ"
my_dict["gigE3"] = "Link to Servers"
print(my_dict)
print("# Print from my_dict the value of key 'gigE0'")
print(my_dict["gigE0"])
print("# Make nested lists and dictionaries")
my_list = [0,1,2,3]
alt_dict = {}
alt_dict["key1"] = "value1"
my_dict["nested_list"] = my_list
my_dict["nested_dict"] = alt_dict
print("# Print my_dict with my_list and alt_dict added")
print(my_dict) 
print("# Print my_dict['nested_dict']['key1]")
print(my_dict["nested_dict"]["key1"])
