# opening file
FILE_PATH = "../input.txt"
with open(FILE_PATH, 'r') as file:
    lines = file.readlines()

inputs = []
for line in lines:
    values = line.rstrip().split(' ')
    inputs.append(list(map(int, values)))

# going over the inputs
ans = 0
for inp in inputs:

    # creating a list of all the rows until the difference between numbers is 0
    temp = [inp]
    while set(temp[-1]) != {0}:
        if not temp:
            print("Error occurred")
            break

        # calculating the difference between neighboring numbers
        row = []
        for i in range(1, len(temp[-1])):
            row.append(temp[-1][i] - temp[-1][i - 1])

        temp.append(row)

    print("IN: ", temp)
    # calculating the value before in the pattern
    for i in range(len(temp) - 1, 0, -1):
        temp[i - 1].insert(0, temp[i - 1][0] - temp[i][0])

    print("OUT:", temp)

    # adding the previous value in the patter to the answer
    ans += temp[0][0]

print("The answer is: ", ans)
