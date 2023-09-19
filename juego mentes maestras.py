print ("Bienvenido(a) hoy vamos a probar tu habilidad mental para resolver problemas, para poder escapar del laberinto.Resolviendo acertijos.\n")
print ("Las decisiones que tomes durante el juego te llevaran a acabar o salvar tu vida\n")
nombre = input ("Ingresa tu nombre: ")
print ("\nQue comience el juego!\n")
print ("*REGLA: Recuerda contestar las preguntas en MAYUSCULA y con la palabra indicada en cada opciÃ³n que se encuentra escrita tambiÃ©n en MAYÃšSCULA*\n")
print ("> Parte 1")
print (nombre + ", Un hombre está mirando una foto y una amiga le pregunta quiénes son. Responde: No tengo ni hermanos ni hermanas, pero el padre de ese hombre es el hijo de mi padre.\n")
print ("- 1ra: Debe ser SU PAPÁ.")
print ("- 2da: Debe ser SU HIJO")


intento = 0
while (intento == 0):
    direccion = input ("\n¿Quién es?: ")
    if direccion == ("SU HIJO"):
        print ("\n Que bien" + nombre + "!" + " sigues con vida\n")
        intento = -1


        print ("> CapÃ­tulo 2")
        print (nombre + ", ya te has liberado ahora estas frente a tres puertas, debes elegir una de ellas para emprender tu huida\n")
        print ("- 1ra: ROJA")
        print ("- 2da: AMARILLA")
        print ("- 3ra: AZUL")


        intento = 0
        while (intento == 0):
            color = input ("\nÂ¿QuÃ© color de puerta escoges?: ")
            if color == ("AMARILLA"):
                print ("\nÂ¡Que bien " + nombre + "!" + " sigues con vida\n")
                intento = -1


                print ("> CapÃ­tulo 3")
                print ("Vas por el camino correcto hacia la playa y tu libertad, pero a lo lejos logras identificar dos leopardos. " + nombre + ", debes hallar la forma de quitarlos de tu camino.")
                print ("A escasos pasos de ti se encuentran dos armas:\n")
                print ("- 1ra: RIFLE de caza")
                print ("- 2da: ARCO de caza")


                intento = 0
                while (intento == 0):
                    arma = input ("\nÂ¿QuÃ© arma eliges para acabar con los leopardos?: ")
                    if arma == ("RIFLE"):
                        print ("\nÂ¡Que bien " + nombre + "!" + " sigues con vida, estas a una decisiÃ³n de ser libre\n")
                        intento = -1


                        print ("> CapÃ­tulo Final")
                        print ("Lograste llegar a la playa y ahora estas en la orilla, a lo lejos identificas un bote con tripulantes y mediante una serie de seÃ±as logras persuadirlos.")
                        print ("Los tripulantes te indican que irÃ¡n hacia donde estas, pero sabes que cada minuto cuenta y sientes angustia de ser descubierto(a) por tus captores. AsÃ­ que te planteas dos opciones\n")
                        print ("- 1ra: DeberÃ­a ESPERAR el bote")
                        print ("- 2da: DeberÃ­a NADAR hasta el bote")


                        intento = 0
                        while (intento == 0):
                            accion = input ("\nÂ¿QuÃ© decides hacer?: ")
                            if accion == ("ESPERAR"):
                                print ("\nÂ¡" + nombre + " GANASTE! Ya estas en el bote lejos de la isla\n")
                                intento = -1
                            elif accion == ("NADAR"):
                                print ("\nPERDISTE: " + nombre + ", la tribu de secuestradores identifico un movimiento extraÃ±o en el agua y te atacÃ³ con decenas de flechas causÃ¡ndote la muerte")
                                intento = -2
                            else:
                                print ("\n*Entrada invalida*")


                    elif arma == ("ARCO"):
                        print ("\nPERDISTE: Los leopardos te devoraron completamente ya que no sabÃ­as utilizar un arco de caza y lo Ãºnico que hiciste fue alertarlos " + nombre)
                        intento = -2
                    else:
                        print ("\n*Entrada invalida*")


            elif color == ("ROJA"):
                print ("\nPERDISTE: " + nombre + " has muerto incinerado(a) ya que al abrir la puerta activaste una trampa")
                intento = -2
            elif color == ("AZUL"):
                print ("\nPERDISTE: " + nombre + " has muerto ya que tras esta puesta se encontraba una jaurÃ­a de bestias")
                intento = -3
            else:
                print ("\n*Entrada invalida*")


    elif direccion == ("DERECHA"):
        print ("\nPERDISTE: " + nombre + " has muerto a manos del guardia luego de caer en un agujero y ser descubierto(a)")
        intento = -2
    else:
        print ("\n*Entrada invalida*")