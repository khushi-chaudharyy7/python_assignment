#convert string to a list of its characters

def string_to_list(input_string):
    return [char for char in input_string]

my_string = input("Enter a string: ")
char_list = string_to_list(my_string)
print(char_list)