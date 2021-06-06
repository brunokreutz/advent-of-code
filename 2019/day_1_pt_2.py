lines = [line.rstrip('\n') for line in open('input_1.txt')]
v = 0
for line in lines:
	v_tmp = int(line)//3 - 2
	v = v + v_tmp
	f = v_tmp
	while f > 0:
		f = f //3 - 2
		if( f> 0):
			v = v + f
			
print(v)