def monitor_externo(oceano,tamañoOceano):


	for fila in range(tamañoOceano):
		oceano.append([])
		for columna in range(tamañoOceano):
			oceano[fila].append('~')

	return oceano, tamañoOceano

#---------------------------------------------------------------

def impresion_del_oceano(oceano,tamañoOceano):
	filas=["A","B","C","D","E","F","G","H","I","J","K","L","LL","M","N","Ñ","O","P","Q","R","S","T","V","W","X","Z",]
	columnas=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]

	for coordenada in oceano:
		#print(*columnas) los intercala, no me sirve
		print(" ".join("".join(coordenada)))


#--------------------------------------------------------------------------------------

def monitor_interno(oceano,tamañoOceano):

	oceano = [["~" for columna in range(tamañoOceano)] for fila in range(tamañoOceano)]

	return oceano, tamañoOceano
#-------------------------------------------------------------------------------------
def batalla_naval():

	oceano = []

	tamañoOceano=int(input("ingrese el tamaño del oceano : "))

	monitor_externo(oceano,tamañoOceano)
	impresion_del_oceano(oceano,tamañoOceano)
	monitor_interno(oceano,tamañoOceano)
	impresion_del_oceano(oceano,tamañoOceano)

#PPal--------------------------------------------------------------------------------

batalla_naval()


