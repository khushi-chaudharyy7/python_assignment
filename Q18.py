def are_anagrams(str1, str2):
 # Remove any spaces and convert both strings to lowercase
 str1 = str1.replace(" ", "").lower()
 str2 = str2.replace(" ", "").lower()

# Check if sorted characters of both strings are the same
 return sorted(str1) == sorted(str2)



# Get input from the user for both strings
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Check if the strings are anagrams
if are_anagrams(string1, string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")