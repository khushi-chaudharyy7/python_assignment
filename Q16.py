# Get input from the user
user_input = input("Enter a string: ")

# Initialize an empty dictionary to store the frequency of each character
frequency = {}

# Iterate over each character in the string
for char in user_input:
   if char in frequency:
      frequency[char] += 1
   else:
      frequency[char] = 1

# Print the frequency of each character
for char, count in frequency.items():
  print(f"'{char}': {count}")

