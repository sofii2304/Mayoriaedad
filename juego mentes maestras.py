print ("Bienvenido(a) hoy vamos a probar tu habilidad mental para resolver problemas, para poder escapar del laberinto.Resolviendo acertijos.\n")
print ("Las decisiones que tomes durante el juego te llevaran a acabar o salvar tu vida\n")
nombre = input ("Ingresa tu nombre: ")
print ("\nQue comience el juego!\n")
print ("*REGLA: Recuerda contestar las preguntas en MAYUSCULA y con la palabra indicada en cada opcion que se encuentra escrita tambien en MAYUSCULA*\n")
print ("> Parte 1")
print (nombre + ", Un hombre está mirando una foto y una amiga le pregunta quiénes son. Responde: No tengo ni hermanos ni hermanas, pero el padre de ese hombre es el hijo de mi padre.\n")
print ("- 1ra: Debe ser SU PAPÁ.")
print ("- 2da: Debe ser SU HIJO")


intento = 0
while (intento == 0):
    familiar = input ("\n¿Quién es?: ")
    if familiar  == ("SU HIJO"):
        print ("\n ¡Que bien" + nombre + "!" + " sigues con vida\n")
        intento = -1


        print ("> Parte 2")
        print (nombre + ", El que me compra no me necesita. El que me hace no me quiere. El que me usa no me aprecia.\n")
        print ("- 1ra: UNA FLOR")
        print ("- 2da: UN ATAUD")
        print ("- 3ra: UN DADO")


        intento = 0
        while (intento == 0):
            objeto = input ("\n¿Qué soy?: ")
            if objeto == ("UN ATAUD"):
                print ("\n¡Que bien " + nombre + "!" + " sigues con vida\n")
                intento = -1


                print ("> Parte 3")
                print ("En un depósito, hay un nivel de agua muy bajo pero que se duplica todos los días. Tarda 60 días en llenarse.")
                print ("- 1ra: 59 DIAS")
                print ("- 2da: 42 DIAS")
                print ("- 3ra: 96 DIAS")


                intento = 0
                while (intento == 0):
                    tiempo = input ("\n¿Cuánto tarda en llegar a la mitad?: ")
                    if tiempo == ("59 DIAS"):
                        print ("\n¡Que bien " + nombre + "!" + " sigues con vida\n")
                        intento = -1


                        print ("> Parte Final")
                        print ("Resuelve este acertijo y saldras con vida")
                        print ("- 1ra: Debe ser UN SELLO ")
                        print ("- 2da: Debe ser UNA AZAFATA")
                        print ("- 3ra: Debe ser UN PILOTO")


                        intento = 0
                        while (intento == 0):
                            cosa = input ("\n ¿Qué es lo que puede viajar por todo el mundo mientras está en una esquina?: ")
                            if cosa == ("UN SELLO"):
                                print ("\n¡" + nombre + " GANASTE! LOGRASTE PASAR EL NIVEL\n")
                                intento = -1
                            elif cosa == ("UNA AZAFATA"):
                                print ("\nPERDISTE: " + nombre + ", Te atropello una roca enorme")
                                intento = -2
                            elif cosa == ("UN PILOTO"):
                                print ("\nPERDISTE:Vuelve a empezar")
                            else:
                                print ("\n*Entrada invalida*")


                    elif tiempo == ("42 DIAS"):
                        print ("\nPERDISTE: Una serpiente te mordio " + nombre)
                        intento = -2
                    elif tiempo == ("96 DIAS"):
                        print ("\nPERDISTE:Te ataco un cocodrilo ")
                    else:
                        print ("\n*Entrada invalida*")


            elif objeto == ("UNA FLOR"):
                print ("\nPERDISTE: " + nombre + "Caiste en un agujero lleno de serpientes.")
                intento = -2
            elif objeto == ("UN DADO"):
                print ("\nPERDISTE: " + nombre + " Caiste en el abismo")
                intento = -3
            else:
                print ("\n*Entrada invalida*")


    elif familiar == ("SU PAPÁ"):
        print ("\nPERDISTE: " + nombre + " Te estrellaste contra un muro, vuelve a intentarlo")
        intento = -2
    else:
        print ("\n*Entrada invalida*")