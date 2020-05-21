class Team():
    dictionaryRunners={}
    nameTeam=" "
    quantityPlayers=0

    def __init__(self):
        count = 1
        self.nameTeam = input("INSERTE EL NOMBRE DEL EQUIPO " + str(count))
        self.dictionaryRunners.update({self.nameTeam: {}})
        self.quantityPlayers = int(input("INSERTE LA CANTIDAD DE JUGADORES: "))
        count = count + 1
    def register(self):
        listInsertRunner = ("INGRESE EL NOMBRE DEL PARTICIPANTE: ", "INGRESE EL APELLIDO DEL PARTICIPANTE: ",
                            "INGRESE A QUE VELOCIDAD VA EL PARTICIPANTE: ")

        for y in range(self.quantityPlayers):
            print("INGRESANDO AL "+str(y+1)+" PARTICIPANTE")
            idRunner = input("INGRESE EL NUMERO DEL PARTICIPANTE: ")
            listInfoRunner = []
            for x in range(len(listInsertRunner)):
                infoRunner= input(listInsertRunner[x])
                listInfoRunner.append(infoRunner)
            self.dictionaryRunners[self.nameTeam].update({idRunner: listInfoRunner})
        return self.dictionaryRunners