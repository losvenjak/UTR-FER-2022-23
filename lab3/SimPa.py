import sys
unos = sys.stdin.readlines()
ulazniNizovi = unos[0].strip()
skupStanja = unos[1].strip()
skupUlaznihZnakova = unos[2].strip()
skupZnakovaStoga = unos[3].strip()
skupPrihvatljivihStanja = unos[4].strip()
pocetnoStanje = unos[5].strip()
pocetniZnakStoga = unos[6].strip()
funkcijePrijelaza = unos[7:]
ulazniNizovi = ulazniNizovi.split("|")

def razdvojiZnakove(rijec):
    return [char for char in rijec]

def nadiPrijelaz(funkcijaPronadena, funkcija, printLista, sadrzajStoga):				
	funkcijaPronadena = True				
	desnaStranaFunkcije = funkcija[1].strip()
	desnaStranaFunkcije = desnaStranaFunkcije.split(',')
	novoStanje = desnaStranaFunkcije[0]
	dioNovogStoga = ''.join(desnaStranaFunkcije[1:])										
	noviStog = []
	noviStog.append(dioNovogStoga)			
	noviStog = noviStog + sadrzajStoga				
	listaZaRazdvajanje1 = []
	listaZaRazdvajanje2 = []
	listaZaRazdvajanje1 = razdvojiZnakove(noviStog[0])					
	if len(noviStog) > 1:				
		listaZaRazdvajanje2 = razdvojiZnakove(noviStog[1])
		listaZaRazdvajanje2 = listaZaRazdvajanje2[1:]	
	else:
		listaZaRazdvajanje2 = []			
	noviZnakStoga = listaZaRazdvajanje1[0]	
	noviStog = listaZaRazdvajanje1 + listaZaRazdvajanje2
	if noviZnakStoga == '$' and len(noviStog) > 1:
		listaZaRazdvajanje1 = listaZaRazdvajanje1[1:]
		noviStog = listaZaRazdvajanje1 + listaZaRazdvajanje2
		noviZnakStoga = noviStog[0]
	stogZaPrint = ''.join(noviStog)
	printLista.append(novoStanje)
	printLista.append('#')
	printLista.append(stogZaPrint)
	printLista.append('|')					
	izlaz=''.join(printLista)
	print(izlaz, end='')				
	sadrzajStoga = []
	return [funkcijaPronadena, printLista, sadrzajStoga, novoStanje, noviZnakStoga, noviStog]

for ulazniNiz in ulazniNizovi:
	ulazniNiz = ulazniNiz.split(",")
	sadrzajStoga = []
	pocetak = True;
	i = 0
	for simbol in ulazniNiz:		
		simbolRijesen = False
		while(simbolRijesen == False):
			printLista = []
		
			if pocetak == True:
				stanje = pocetnoStanje
				znakStoga = pocetniZnakStoga
				pocetak = False
				sadrzajStoga.append(pocetniZnakStoga)
				printLista.append(stanje)
				printLista.append('#')			
				printLista.append(znakStoga)
				printLista.append('|')
			
			else:
				stanje = novoStanje
				znakStoga = noviZnakStoga
				stog = ''.join(noviStog)
				sadrzajStoga.append(stog)
		
		
			
		
		
			pomLista = []
			pomLista.append(stanje)
			pomLista.append(',')
			pomLista.append(simbol)
			pomLista.append(',')
			pomLista.append(znakStoga)
			lijevaStranaFunkcije = ''.join(pomLista).strip()
			
			funkcijaPronadena = False
		

			for funkcija in funkcijePrijelaza:
				funkcija = funkcija.strip()
				funkcija = funkcija.split("->")	
									
				if funkcija[0] == lijevaStranaFunkcije:						
					prijelaz = nadiPrijelaz(funkcijaPronadena, funkcija, printLista, sadrzajStoga)
					funkcijaPronadena = prijelaz[0]
					printLista = prijelaz[1]
					sadrzajStoga = prijelaz[2]
					novoStanje = prijelaz[3]
					noviZnakStoga = prijelaz[4]
					noviStog = prijelaz[5]
					simbolRijesen = True							
							
				else:
					epsilonPrijelaz = funkcija[0]
					epsilonPrijelaz = epsilonPrijelaz.split(',')				
					if epsilonPrijelaz[0] == stanje and epsilonPrijelaz[1] == '$' and epsilonPrijelaz[2] == znakStoga:
						prijelaz = nadiPrijelaz(funkcijaPronadena, funkcija, printLista, sadrzajStoga)
						funkcijaPronadena = prijelaz[0]
						printLista = prijelaz[1]
						sadrzajStoga = prijelaz[2]
						novoStanje = prijelaz[3]
						noviZnakStoga = prijelaz[4]
						noviStog = prijelaz[5]			
				if(funkcijaPronadena == True):
					break	

			if funkcijaPronadena == False:
				printLista.append('fail|')			
				printLista.append('0')
				izlaz=''.join(printLista)
				print(izlaz)
				break
		if(funkcijaPronadena == False):
			break
	
	
	if funkcijaPronadena == True:		
			
		if novoStanje in skupPrihvatljivihStanja:
			print(1)
		else:				
			prihvatljivoStanje = False
			while(prihvatljivoStanje == False):
				funkcijePrijelaza = unos[7:]
				printLista = []				
				stog = ''.join(noviStog)
				sadrzajStoga.append(stog)
				funkcijaPronadena = False		
								
				for funkcija in funkcijePrijelaza:
													
					funkcija = funkcija.strip()
					funkcija = funkcija.split("->")												
					epsilonPrijelaz = funkcija[0]
					epsilonPrijelaz = epsilonPrijelaz.split(',')						
								
					if epsilonPrijelaz[0] == novoStanje and epsilonPrijelaz[1] == '$' and epsilonPrijelaz[2] == noviZnakStoga:
						prijelaz = nadiPrijelaz(funkcijaPronadena, funkcija, printLista, sadrzajStoga)
						funkcijaPronadena = prijelaz[0]
						printLista = prijelaz[1]
						sadrzajStoga = prijelaz[2]
						novoStanje = prijelaz[3]
						noviZnakStoga = prijelaz[4]
						noviStog = prijelaz[5]
						if novoStanje in skupPrihvatljivihStanja:
							prihvatljivoStanje = True
						if funkcijaPronadena == True:							
							break	

				if(prihvatljivoStanje == True):
					break
				elif(prihvatljivoStanje == False and funkcijaPronadena == False):
					break
				elif(prihvatljivoStanje == False and funkcijaPronadena == True):
					continue
											
					
			if prihvatljivoStanje == True:
				print(1)
			else:
				print(0)

