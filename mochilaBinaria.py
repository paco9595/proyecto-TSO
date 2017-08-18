archivo = open("datos-mochila.txt","r")
suma=""
aux=[]
datos=[]
for linea in archivo.readlines():
	for x in linea:
		if x!=" " and x!="\n":
			suma+=x
		else:
			if(len(suma)>0):
				aux.append(int(suma))
				suma=""
	if(len(aux)>0):
		datos.append(aux)
		aux=[]
def tablaVerdad(bits): 
    aux=[]
    for i in range(pow(2,bits)): 
        elemento=[0]*bits 
        for j in reversed(range(bits)): 
            if i<=1: 
                elemento[j]=i 
                if i==1: 
                    i=0 
            else: 
                elemento[j]=i%2 
                i=i//2 
        aux.append(elemento)
    return aux
tabla_binaria = tablaVerdad(len(datos))
pesos = []
beneficio = []
aux = 0
aux1 = 0
for x in range(len(tabla_binaria)):
    for y in range(len(tabla_binaria[x])):
        if(tabla_binaria[x][y] ==1):
            aux += datos[y][0]
            aux1 += datos[y][1]
    if(aux<=60 and aux>0): # es el rango de peso
        pesos.append(aux)
        beneficio.append(aux1)
    else:
        pesos.append(0)
        beneficio.append(0)
    aux=0
    aux1=0
maxBen = beneficio.index(max(beneficio))
print 'el beneficio optimo es: ',max(beneficio),' ',tabla_binaria[maxBen]