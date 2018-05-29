nums = []
for num in range(1000000):
	nums.append('0'*(6-len(str(num))) + str(num))

with open('pi.txt','r') as f:
	pi = f.read()

postion = []
for num in nums:
	try:
		postion.append([num, pi.index(num)-1])
	except:
		pass

with open('postion.txt','w') as f:
	for pos in postion:
		f.write(pos[0] + ':' + str(pos[1]) + '\n')

print('Done!')

