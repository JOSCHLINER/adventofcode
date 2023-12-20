import re
from collections import defaultdict


# function for checking if the workflow is rejected or accepted
def check_status(statement: str):
    # checking if we are at the end of the road
    if statement == 'A':
        return True
    elif statement == 'R':
        return False

    return None


# opening the file
FILE_PATH = "../input.txt"
with open(FILE_PATH, 'r') as file:
    lines = file.readlines()

lines = [line.rstrip() for line in lines]

# getting the different rating criteria given by the elves
workflows, row = defaultdict(list), 0
while lines[row] != '':
    name, inst_chain = lines[row].split('{')
    inst_chain = inst_chain[:-1]

    # preparing the instructions
    for inst in inst_chain.split(','):

        if '>' in inst:
            greater = True
        elif '<' in inst:
            greater = False

        inst = re.split(r'[<>]', inst)

        if len(inst) > 1:
            inst[1] = inst[1].split(':')
            inst[1][0] = int(inst[1][0])
            inst.append(greater)

        workflows[name].append(inst)

    row += 1

# going over the given stunts
ans = 0
for l in range(row + 1, len(lines)):
    line = lines[l][1:-1]
    line = line.split(',')

    # getting the variables into a dict
    variables = {}
    for variable in line:
        variable = (variable.split('='))
        variables[variable[0]] = int(variable[1])

    # going over each of the workflow given by the elves
    workflow = workflows['in']
    done = None
    while True:

        # going over each statement, check in each workflow
        for check in workflow:

            # if we only have a new workflow
            if len(check) == 1:

                # checking if the workflow is rejected, accepted or moved further
                done = check_status(check[0])
                if done is not None:
                    break

                # assigning a new workflow
                workflow = workflows[check[0]]
                break

            # checking if the given statement is True
            if (variables[check[0]] > check[1][0]) == check[2]:

                # checking if the item is A or R
                done = check_status(check[1][1])
                if done is not None:
                    break

                # going to the next workflow
                workflow = workflows[check[1][1]]
                break

        # if the workflow is righter rejected or accepted
        if done is not None:
            if done:
                ans += sum(variables[key] for key in variables)
            break

# printing the answer
print("The answer is: ", ans)
