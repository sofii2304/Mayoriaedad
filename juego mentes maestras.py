print ("Bienvenido(a) hoy vamos a probar tu habilidad mental para resolver problemas, para poder escapar del laberinto.Resolviendo acertijos.\n")
print ("Las decisiones que tomes durante el juego te llevarán a acabar o salvar tu vida\n")
nombre = input ("Ingresa tu nombre: ")
print ("\nQue comience el juego!\n")
print ("*REGLA: Recuerda contestar las preguntas en MAYÚSCULA y con la palabra indicada en cada opción que se encuentra escrita también en MAYÚSCULA*\n")

print ("> Parte 1")
print (nombre + ", Un hombre está mirando una foto y una amiga le pregunta quiénes son. Responde: No tengo ni hermanos ni hermanas, pero el padre de ese hombre es el hijo de mi padre.\n")
print ("- 1ra: Debe ser SU PAPÁ")
print ("- 2da: Debe ser SU HIJO")

intento = 0
while (intento == 0):
    familiar = input ("\n¿Quién es?: ")
    if familiar == "SU HIJO":
        print ("\n ¡Que bien, " + nombre + "!" + " sigues con vida\n")

        print ("> Parte 2")
        print (nombre + ", El que me compra no me necesita. El que me hace no me quiere. El que me usa no me aprecia.\n")
        print ("- 1ra: UN ATAUD")
        print ("- 2da: UNA FLOR")
        print ("- 3ra: UN DADO")

        intento = 0
        while (intento == 0):
            objeto = input ("\n¿Qué soy?: ")
            if objeto == "UN ATAUD":
                print ("\n¡Que bien " + nombre + "!" + " sigues con vida\n")

                print ("> Parte 3")
                print ("En un depósito, hay un nivel de agua muy bajo pero que se duplica todos los días. Tarda 60 días en llenarse.")
                print ("- 1ra: 59 DIAS")
                print ("- 2da: 42 DIAS")
                print ("- 3ra: 96 DIAS")

                intento = 0
                while (intento == 0):
                    tiempo = input ("\n¿Cuánto tarda en llegar a la mitad?: ")
                    if tiempo == "59 DIAS":
                        print ("\n¡Que bien " + nombre + "!" + " sigues con vida\n")

                        print ("> Parte Final")
                        print ("Resuelve este acertijo y saldrás con vida")
                        print ("- 1ra: Debe ser UN SELLO")
                        print ("- 2da: Debe ser UNA AZAFATA")
                        print ("- 3ra: Debe ser UN PILOTO")

                        intento = 0
                        while (intento == 0):
                            cosa = input ("\n ¿Qué es lo que puede viajar por todo el mundo mientras está en una esquina?: ")
                            if cosa == "UN SELLO":
                                print ("\n¡" + nombre + " GANASTE! LOGRASTE PASAR EL NIVEL\n")
                                intento = -1
                            elif cosa == "UNA AZAFATA":
                                print ("\nPERDISTE: " + nombre + ", Te atropelló una roca enorme")
                                intento = -2
                            elif cosa == "UN PILOTO":
                                print ("\nPERDISTE: Vuelve a empezar")
                                intento = -2
                            else:
                                print ("\n*Entrada inválida*")
                    elif tiempo == "42 DIAS":
                        print ("\nPERDISTE: Una serpiente te mordió, " + nombre)
                        intento = -2
                    elif tiempo == "96 DIAS":
                        print ("\nPERDISTE: Te atacó un cocodrilo")
                        intento = -2
                    else:
                        print ("\n*Entrada inválida*")
            elif objeto == "UNA FLOR":
                print ("\nPERDISTE: " + nombre + " Caíste en un agujero lleno de serpientes.")
                intento = -2
            elif objeto == "UN DADO":
                print ("\nPERDISTE: " + nombre + " Caíste en el abismo")
                intento = -2
            else:
                print ("\n*Entrada inválida*")
    elif familiar == "SU PAPÁ":
        print ("\nPERDISTE: " + nombre + " Te estrellaste contra un muro, vuelve a intentarlo")
        intento = -2
    else:
        print ("\n*Entrada inválida*")
