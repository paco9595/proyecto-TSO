archivo = open("datos-vecinosMasCercanos.txt","r")
suma=""
aux=[]
datos=[]
ceros=1
aux1=[]
for linea in archivo.readlines():
    for n in range(ceros):
        aux.append(0)
        pass
	for x in linea:
		if x!=" " and x!="-" and x!="\n":
			suma+=x
		else:
			if(len(suma)>0):
				aux.append(int(suma))
				suma=""
	if(len(aux)>0): 
		datos.append(aux)
		aux=[]
    ceros+=1
print datos,aux
