
with open('input_2.txt') as f:
    for line in f:
        array= [int(n) for n in line.strip().split(',')]
print(array[0])
c = 0
add = False
x = 0
y = 0
array[1] = 12
array[2] = 2
for item in array:
	if (c == 0):
		if (item == 1):
			add = True
		elif (item == 2):
			add = False
		elif( item == 99):
			break;
	elif (c == 1):
		x = array[item]
	elif (c == 2):
		y = array[item]
	elif (c == 3):
		if(add):
			array[item] = x + y
		else:
			array[item] = x * y
		print (array[item])
		c = -1
	c = c + 1
print(array[0])	