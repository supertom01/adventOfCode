file = open('input1.txt', 'r')
depths = []
for depth in file.readlines():
    depths.append(int(depth))
file.close()

####################################################################
# Calculate the number of times the depth difference has increased #
####################################################################

counter = 0
for i in range(len(depths) - 1):
    if depths[i] < depths[i + 1]:
        counter += 1

print(f'Number of times the depth has increased is: {counter}')

####################################################################
# Calculate the number of times the depth difference has increased #
# However, in order to improve accuracy take the depths as groups  #
# of size 3.                                                       #
####################################################################

counter = 0
for i in range(len(depths) - 3):
    group1 = depths[i] + depths[i + 1] + depths[i + 2]
    group2 = depths[i + 1] + depths[i + 2] + depths[i + 3]
    if group1 < group2:
        counter += 1

print(f'Number of times the depth has increased for groups is: {counter}')