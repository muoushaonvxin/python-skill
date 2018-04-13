def get_ip():
	import random

	l = []
	for i in range(0,4):
	n = random.randint(1,255)
	l.append(str(n))
	return ".".join(l)

	ip = get_ip()
print(ip)
