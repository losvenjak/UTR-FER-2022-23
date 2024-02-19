import sys
from collections import deque

unos = sys.stdin.readlines()
skupStanja = unos[0].strip()
skupStanja = skupStanja.split(",")
skupSimbola = unos[1].strip();
skupSimbola = skupSimbola.split(",")
skupPrihvatljivihStanja = unos[2].strip()
skupPrihvatljivihStanja = skupPrihvatljivihStanja.split(",")
pocetnoStanje = unos[3].strip()
funkcijePrijelaza = unos[4:]

glavniDict = {}

for stanje in skupStanja:
	stanjeDict = {}
	for funkcija in funkcijePrijelaza:
		funkcija = funkcija.strip().split("->")
		lijevoStanje0 = funkcija[0].split(",")
		lijevoStanje = lijevoStanje0[0]
		simbol = lijevoStanje0[1]
		desnoStanje = funkcija[1]
		if lijevoStanje == stanje:
			stanjeDict[simbol] = desnoStanje
	glavniDict[stanje] = stanjeDict					#npr {p1: {c:p6, d:p3}}

listaIstih = []								#sadrzi parove istih stanja
listaStanja = []



#trazimo nedohvatljiva stanja

manjeGlavniDict = {key: set(pomDict.values()) for key, pomDict in glavniDict.items()}		#manjeGlavniDict ima oblik {stanje: set stanja u koje prelazi}, nema simbole

rijeseno = set()
dohvatljivo = set()
dohvatljivo.add(pocetnoStanje)
d = deque()
d.append(pocetnoStanje)
while d:
	stanje = d.popleft()		
	if stanje not in rijeseno:
		rijeseno.add(stanje)	
	for desnoStanje in manjeGlavniDict[stanje]:
		if desnoStanje not in rijeseno:
			d.append(desnoStanje)
			dohvatljivo.add(desnoStanje)


listaStanja = list(sorted(dohvatljivo))



#provjeravamo ocitu istovjetnost (dva para su istovjetna ako za svaki simbol idu u ista stanja i ako imaju istu prihvatljivost)

pomocniDict = {}
izadi = 0	
for key, value in glavniDict.items():			
	if value in pomocniDict.values() and key in listaStanja:				#pomocniDict je prepisani glavniDict ali su izbacena stanja koja su proglasena istovjetnima nekom prethodnom 
		izadi = 0	
		for k, v in pomocniDict.items():
			if v == value:
				if (k in skupPrihvatljivihStanja and key in skupPrihvatljivihStanja or k not in skupPrihvatljivihStanja and key not in skupPrihvatljivihStanja):				
					ponovljeniKljuc = k	
					listaIstih.append((key,ponovljeniKljuc))
				else:
					izadi = 1
		if izadi == 1:
			pomocniDict[key] = value
	elif key in listaStanja:
		pomocniDict[key] = value



setStanja = set()

for par in listaIstih:
	setStanja.add(min(par))
for key in pomocniDict.keys():
	setStanja.add(key)


listaStanja = list(sorted(setStanja))					#lista stanja nakon prve provjere

glavniDict = {}								#mijenjamo glavniDict tako da stanja koja se ponavljaju (istovjetna su nekom prethodnom) sada imaju oznaku tog prethodnog stanja
for stanje in listaStanja:	
	stanjeDict = {}
	for funkcija in funkcijePrijelaza:
		funkcija = funkcija.strip().split("->")		
		lijevoStanje0 = funkcija[0].split(",")
		lijevoStanje = lijevoStanje0[0]		
		simbol = lijevoStanje0[1]
		desnoStanje = funkcija[1]
		if lijevoStanje not in listaStanja:
			continue
		if desnoStanje not in listaStanja:				
			for par in listaIstih:
				if desnoStanje in par:	
					if par[0] == desnoStanje:
						desnoStanje = par[1]
					else:
						desnoStanje = par[0]
					break;
		if lijevoStanje == stanje:
			stanjeDict[simbol] = desnoStanje			
	glavniDict[stanje] = stanjeDict	





#provjeravamo istovjetnost za svaki par stanja

istovjetnaStanja = []
def provjeriIstovjetnost(st1, st2):	
	if st1 in skupPrihvatljivihStanja and not st2 in skupPrihvatljivihStanja or not st1 in skupPrihvatljivihStanja and st2 in skupPrihvatljivihStanja:
		return 0
	if (st1,st2) in istovjetnaStanja or (st2,st1) in istovjetnaStanja:
		return 0
	else:		
		rijeseno = set()
		dodano = set()
		dq = deque()
		dq.append((st1,st2))
		while dq:
			stanje1,stanje2 = dq.popleft()		
			if (stanje1,stanje2) not in rijeseno or (stanje2,stanje1) not in rijeseno:
				rijeseno.add((stanje1,stanje2))			
				for simbol in skupSimbola:					
					novoStanje1 = glavniDict[stanje1][simbol]
					novoStanje2 = glavniDict[stanje2][simbol]
					if novoStanje1 in skupPrihvatljivihStanja and not novoStanje2 in skupPrihvatljivihStanja or not novoStanje1 in skupPrihvatljivihStanja and novoStanje2 in skupPrihvatljivihStanja:
						return 0
					elif (novoStanje1,novoStanje2) not in rijeseno and (novoStanje2,novoStanje1) not in rijeseno and novoStanje1 != novoStanje2 and (novoStanje1,novoStanje2) not in dodano and (novoStanje2,novoStanje1) not in dodano:
						dq.append((novoStanje1, novoStanje2))
						dodano.add((novoStanje1, novoStanje2))		
		istovjetnaStanja.extend(list(rijeseno))
		return 1

for i in range(len(listaStanja)):
	for j in range(i+1, len(listaStanja)):		
		provjeriIstovjetnost(listaStanja[i], listaStanja[j])

for par in istovjetnaStanja:
	if max(par) in listaStanja:
		listaStanja.remove(max(par))


result = ','.join(listaStanja)
print(result)
simboli = ','.join(skupSimbola)
print(simboli)
novaPrihvatljivaStanja = []
for stanje in skupPrihvatljivihStanja:
	if stanje in listaStanja:
		novaPrihvatljivaStanja.append(stanje)
novaPrihvatljivaStanja = ','.join(novaPrihvatljivaStanja)
print(novaPrihvatljivaStanja)
if pocetnoStanje not in listaStanja:
	for par in istovjetnaStanja:
		if pocetnoStanje in par:
			if pocetnoStanje == par[0] and par[1] in listaStanja:
				pocetnoStanje = par[1]
				break
			elif pocetnoStanje == par[1] and par[0] in listaStanja:
				pocetnoStanje = par[0]
				break			
print(pocetnoStanje)
pomDict2 = {}
for key, pomDict in glavniDict.items():
	if key in listaStanja:
		for simbol in pomDict.keys():	
			pocStanje = key
			zavrsnoStanje = pomDict[simbol]
			if zavrsnoStanje not in listaStanja:
				for par in istovjetnaStanja:
					if zavrsnoStanje in par:
						if zavrsnoStanje == par[0] and par[1] in listaStanja:
							zavrsnoStanje = par[1]
							break
						elif zavrsnoStanje == par[1] and par[0] in listaStanja:
							zavrsnoStanje = par[0]
							break
			print('{},{}->{}'.format(''.join(pocStanje), (simbol), (zavrsnoStanje)))