lines = [line.rstrip('\n') for line in open('input_1.txt')]
v = 0
for line in lines:
	v = v + int(line)//3 - 2
print(v)