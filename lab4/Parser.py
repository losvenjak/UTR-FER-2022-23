import sys
unos = sys.stdin.readlines()
ulaz = unos[0].strip()
ulazniNiz = []

def razdvojiZnakove(rijec):
	return [char for char in rijec]

ulazniNiz = razdvojiZnakove(ulaz)
kraj = len(ulazniNiz)

def C(i):
	print("C", end='')
	i = A(i)
	i = A(i)
	return i

def B(i):
	print("B", end='')
	if(i<=kraj-2 and ulazniNiz[i] == 'c'):		
		if(ulazniNiz[i+1] == 'c'):
			i = i+2
			i = S(i)
			if(i<=kraj-2 and ulazniNiz[i] == 'b' and ulazniNiz[i+1] == 'c'):
				i = i+2
			else:
				print("\nNE")
				exit()
		else:
			print("\nNE")
			exit()
	return i
	
def A(i):
	print("A", end='')
	if(i<kraj and ulazniNiz[i] == 'b'):
		i = i+1
		i = C(i)
	elif(i<kraj and ulazniNiz[i] == 'a'):
		i = i+1
	else:
		print("\nNE")
		exit()
	return i
	
def S(i):
	print("S", end='')
	if(i<kraj and ulazniNiz[i] == 'a'):
		i = i+1
		i = A(i)
		i = B(i)
	elif(i<kraj and ulazniNiz[i] == 'b'):
		i = i+1
		i = B(i)
		i = A(i)
	else:
		print("\nNE")
		exit()
	return i
	
def main():
	
	i = S(0)
	
	if(i==kraj):
		print("\nDA")
	else:
		
		print("\nNE")



main()