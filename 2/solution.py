def move_submarine(values):
	horizontal, depth = 0, 0
	
	for value in values:
		if value[0] == 'forward':
			horizontal += value[1]
		elif value[0] == 'up':
			depth -= value[1]
		elif value[0] == 'down':
			depth += value[1]

	return horizontal * depth


def move_submarine_aim(values):
	horizontal, depth, aim = 0, 0, 0
	
	for value in values:
		if value[0] == 'forward':
			horizontal += value[1]
			depth += aim * value[1]
		elif value[0] == 'up':
			aim -= value[1]
		elif value[0] == 'down':
			aim += value[1]

	return horizontal * depth


# Parse input values
file = open('input.txt')
values = []
for line in file:
	(command, size) = line.strip().split(" ")
	values.append((command, int(size)))

# PART 1 -- Move submarine
res = move_submarine(values)
print("Result (part 1): {}".format(res))

# PART 2 -- Move submarine 2
res1 = move_submarine_aim(values)
print("Result (part 2): {}".format(res1))

