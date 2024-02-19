import sys
unos = sys.stdin.readlines()
ulazniNizovi = unos[0].strip()
ulazniNizovi = ulazniNizovi.split("|")
skupStanja = unos[1].strip()
skupUlaznihZnakova = unos[2].strip()
skupPrihvatljivihStanja = unos[3].strip()
skupPocetnihStanja = unos[4].strip()
skupPocetnihStanja = skupPocetnihStanja.split(",")
funkcijePrijelaza = unos[5:]


def nadiPrijelaz(stanje, simbol, funkcijaPronadena):	
	pomLista = []
	pomLista.append(stanje)
	pomLista.append(',')
	pomLista.append(simbol)	
	lijevaStranaFunkcije = ''.join(''.join(i) for i in pomLista).strip()
	
	for funkcija in funkcijePrijelaza:
		funkcija = funkcija.strip()
		funkcija = funkcija.split("->")								
		if funkcija[0] == lijevaStranaFunkcije:
			funkcijaPronadena = True;
			desnaStranaFunkcije = funkcija[1].strip()
			if desnaStranaFunkcije == '#':
				funkcijaPronadena = False
				return [funkcijaPronadena, desnaStranaFunkcije]
			desnaStranaFunkcije = desnaStranaFunkcije.split(",")
			for i in desnaStranaFunkcije:
				if i == '#':
					desnaStranaFunkcije.remove('#')		
			
			return [funkcijaPronadena, desnaStranaFunkcije]
	return[funkcijaPronadena, []]

for ulazniNiz in ulazniNizovi:
	rBrSimbola = 0	
	ulazniNiz = ulazniNiz.split(",")
	
	listaStanja = []

	pocetak	= True	
	izlaz = []
	
	for simbol in ulazniNiz:
		rBrSimbola = rBrSimbola + 1
		postojiPrijelaz = False
		printLista = []			
		if pocetak == True:
			listaStanja = skupPocetnihStanja
			pocetak = False
			count = 0
			for i in listaStanja:
				epsilonPrijelaz = nadiPrijelaz(i,'$',False) 
				epsilonFunkcijaPronadena = epsilonPrijelaz[0]
				if epsilonFunkcijaPronadena == True:		
					desnaStranaFunkcije = epsilonPrijelaz[1]
					if len(desnaStranaFunkcije) > 0:
						for i in desnaStranaFunkcije:
							if not i in listaStanja:
								listaStanja.append(i)
			#for i in printLista:
			#	listaStanja.append(i)
			listaStanja.sort()
			printLista = []	
			for i in listaStanja:
				count = count + 1
				izlaz.append(i)
				if count<len(listaStanja):
					izlaz.append(',')
			izlaz.append('|')		
				
		for stanje in listaStanja:		
			prijelaz = nadiPrijelaz(stanje, simbol, False) 
			funkcijaPronadena = prijelaz[0]			
			if funkcijaPronadena == True:
				postojiPrijelaz = True
				desnaStranaFunkcije = prijelaz[1]
				if len(desnaStranaFunkcije) > 0:
					for i in desnaStranaFunkcije:
						if not i in printLista:
							printLista.append(i)
		listaStanja = printLista
				
		if postojiPrijelaz == False:
			printLista = '#'
			listaStanja = '#'

		for stanje in listaStanja:
			epsilonPrijelaz = nadiPrijelaz(stanje, '$', False) 
			epsilonFunkcijaPronadena = epsilonPrijelaz[0]
			if epsilonFunkcijaPronadena == True:		
				desnaStranaFunkcije = epsilonPrijelaz[1]
				if len(desnaStranaFunkcije) > 0:
					for i in desnaStranaFunkcije:
						if not i in printLista:
							printLista.append(i)
		
		listaStanja = printLista
		if len(listaStanja) > 1:
			listaStanja.sort()
		
		
	
		count = 0	
		for i in listaStanja:
			count = count + 1
			izlaz.append(i)
			if count<len(listaStanja):
				izlaz.append(',')
		if rBrSimbola < len(ulazniNiz):
			izlaz.append('|')		
	izlaz = ''.join(''.join(i) for i in izlaz).strip()
	print(izlaz)
	

		
				