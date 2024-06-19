#multiple line input

lines = []

print("Enter your lines (press Enter on an empty line to finish):")
while True:
        line = input()
        if line == "":
            break
        lines.append(line)

print("\nYou entered:")
for line in lines:
 print(line)

