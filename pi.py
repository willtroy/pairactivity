sum = 0
for i in range(1, 1000):
	sum += (-((-1)**i)/(2*i - 1))
sum *= 4
print(sum)
