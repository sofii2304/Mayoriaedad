class JuegoLaberinto:
    def __init__(self):
        self.nombre = input("Ingresa tu nombre: ")

    def presentacion(self):
        print("\nBienvenido(a), " + self.nombre + ". Hoy vamos a probar tu habilidad mental para resolver problemas y escapar del laberinto resolviendo acertijos.")
        print("Las decisiones que tomes durante el juego determinarán si logras salvar tu vida.")
        print("\nQue comience el juego!")
        print("*REGLA: Recuerda contestar las preguntas en MAYÚSCULAS y con la palabra indicada en cada opción escrita también en MAYÚSCULAS*\n")

    def parte1(self):
        print("> Parte 1")
        print(self.nombre + ", un hombre está mirando una foto y una amiga le pregunta quiénes son. Responde: No tengo ni hermanos ni hermanas, pero el padre de ese hombre es el hijo de mi padre.")
        print("- 1ra: Debe ser SU PAPÁ.")
        print("- 2da: Debe ser SU HIJO")

        while True:
            familiar = input("\n¿Quién es?: ")
            if familiar == "SU HIJO":
                print("\n¡Que bien, " + self.nombre + "! Sigues con vida\n")
                break
            elif familiar == "SU PAPÁ":
                print("\nPERDISTE: " + self.nombre + ", te estrellaste contra un muro. Vuelve a intentarlo.")
                return
            else:
                print("\n*Entrada inválida*")

    def parte2(self):
        print("> Parte 2")
        print(self.nombre + ", el que me compra no me necesita. El que me hace no me quiere. El que me usa no me aprecia.")
        print("- 1ra: UNA FLOR")
        print("- 2da: UN ATAUD")
        print("- 3ra: UN DADO")

        while True:
            objeto = input("\n¿Qué soy?: ")
            if objeto == "UN ATAUD":
                print("\n¡Que bien, " + self.nombre + "! Sigues con vida\n")
                break
            elif objeto == "UNA FLOR":
                print("\nPERDISTE: " + self.nombre + ", caíste en un agujero lleno de serpientes.")
                return
            elif objeto == "UN DADO":
                print("\nPERDISTE: " + self.nombre + ", caíste en el abismo.")
                return
            else:
                print("\n*Entrada inválida*")

    def parte3(self):
        print("> Parte 3")
        print("En un depósito, hay un nivel de agua muy bajo pero que se duplica todos los días. Tarda 60 días en llenarse.")
        print("- 1ra: CINCUENTA Y NUEVE DIAS")
        print("- 2da: CUARENTA Y DOS DIAS")
        print("- 3ra: NOVENTA Y SEIS DIAS")

        while True:
            tiempo = input("\n¿Cuánto tarda en llegar a la mitad?: ")
            if tiempo == "CINCUENTA Y NUEVE DIAS":
                print("\n¡Que bien, " + self.nombre + "! Sigues con vida\n")
                break
            elif tiempo == "42 DIAS":
                print("\nPERDISTE: Una serpiente te mordió, " + self.nombre + ".")
                return
            elif tiempo == "96 DIAS":
                print("\nPERDISTE: Te atacó un cocodrilo, " + self.nombre + ".")
                return
            else:
                print("\n*Entrada inválida*")

    def parteFinal(self):
        print("> Parte Final")
        print("Resuelve este acertijo y saldrás con vida.")
        print("- 1ra: Debe ser UN SELLO")
        print("- 2da: Debe ser UNA AZAFATA")
        print("- 3ra: Debe ser UN PILOTO")

        while True:
            cosa = input("\n ¿Qué es lo que puede viajar por todo el mundo mientras está en una esquina?: ")
            if cosa == "UN SELLO":
                print("\n¡" + self.nombre + " GANASTE! LOGRASTE PASAR EL NIVEL\n")
                break
            elif cosa == "UNA AZAFATA":
                print("\nPERDISTE: " + self.nombre + ", te atropelló una roca enorme.")
                return
            elif cosa == "UN PILOTO":
                print("\nPERDISTE: Vuelve a empezar, " + self.nombre + ".")
                return
            else:
                print("\n*Entrada inválida*")

if __name__ == "__main__":
    juego = JuegoLaberinto()
    juego.presentacion()
    juego.parte1()
    juego.parte2()
    juego.parte3()
    juego.parteFinal()
