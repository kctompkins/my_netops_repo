my_integer = 443
if my_integer > 0:
    print("Hey, looks like that's a positive number!")

my_integer = -443
if my_integer > 0:
    print("Hey, looks like that's a positive number!")

# my_integer = 'mmm tacos!'
# if my_integer > 0:
#     print("Hey, looks like that's a positive number!")

no_str = "That's not a string"
yes_question = "Yep, there's a ? in that string."
question = "You call that a "

if "?" in question:
    print(yes_question)
if ":" in question:
    print("There is a : in that string")
else:
    print("There is no : in that string")
if "string" in question:
    print("That string contains the word 'string'")

print("# Refactor code to use elseif instead of multiple ifs")
if "?" in question:
    print(yes_question)
elif ":" in question:
    print("There is a : in that string")
elif "string" in question:
    print("That string contains the word 'string'")
else:
    print("Catch-all rule if no conditions are true")
