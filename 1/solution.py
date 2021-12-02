def find_increases(values):
	res = 0
	for first, second in zip(values, values[1:]):
		if first < second:
			res += 1
	return res

# Parse input values
file = open('input.txt')
values = []
for line in file:
	values.append(int(line))

# PART 1 -- Find how many increases there are
res = find_increases(values)
print("Result (part 1): {}".format(res))

# PART 2 -- Consider sliding windows of size 3, find increases
triplets = [(values[x], values[x+1], values[x+2]) for x in range(0, len(values)-2)]
sums = [x[0]+x[1]+x[2] for x in triplets]
res1 = find_increases(sums)
print("Result (part 2): {}".format(res1))
