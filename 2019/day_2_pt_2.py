

result = 0
max = 99*99
i = 0

for i in range(100):
	for j in range(100):
		with open('input_2.txt') as f:
			for line in f:
				array = []
				array= [int(n) for n in line.strip().split(',')]
		if (array[0] != 1):
			print('ou')
		c = 0
		add = False
		x = 0
		y = 0
		noun = i
		array[1] = noun
		verb = j
		array[2] = verb
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
				#print (array[item])
				c = -1
			c = c + 1
			
		if (array[0] == 19690720):
			print(array[0])
			print(100 * noun + verb)