def implementation():
    global x
    command_line = input()
    if "++" in command_line:
        x += 1
    else:
        x -=1

x = 0
number_of_lines = int(input())
for i in range(number_of_lines):
    implementation()
print(x)