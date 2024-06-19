#counting occurrence of an element

my_list = [1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5]
element_to_count = 2
occurrences = len([i for i in my_list if i == element_to_count])
print(f"The element {element_to_count} occurs {occurrences} times")