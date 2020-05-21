import time

class Runner:
    __speedRunners = {}
    def __init__(self, dictionaryTeam):
        for equip in dictionaryTeam:
            for runner in dictionaryTeam[equip]:
                self.__speedRunners.update({(dictionaryTeam[equip][runner][0] + " " + dictionaryTeam[equip][runner][1]) : float(dictionaryTeam[equip][runner][2])})
    def getSpeedRunners(self):
        return self.__speedRunners
    def racerRunners(self, nameRunner, speedRunner):
        run= 10000; bike=20000; swim=1000
        counterRun = 0; counterBike = 0; counterSwim = 0
        metersRun=0; metersBike=0; metersSwim=0;
        print("COMIENZA LA ETAPA CORRIENDO")
        while metersRun < run:
            metersRun += speedRunner
            counterRun += 1
            time.sleep(0.25)
            if metersRun > run:
                metersRun=run
            print(str(nameRunner)+" LLEVA UN TOTAL DE: " +str(metersRun)+" METROS")
        print("COMIENZA LA ETAPA BICICLETEANDO")
        while metersBike < bike:
            metersBike += speedRunner
            counterBike += 1
            time.sleep(0.25)
            if metersBike > bike:
                metersBike=bike
            print(str(nameRunner) + " LLEVA UN TOTAL DE: " + str(metersBike)+ " METROS")
        print("COMIENZA LA ETAPA NADANDO")
        while metersSwim < swim:
            metersSwim += speedRunner
            counterSwim += 1
            time.sleep(0.25)
            if metersSwim > swim:
                metersSwim=swim
            print(str(nameRunner) + " LLEVA UN TOTAL DE: " + str(metersSwim)+" METROS")
        totalCounter = counterSwim + counterRun + counterBike
        totalRunner= nameRunner + " REALIZO UN TOTAL DE: " + str(totalCounter) + " MINUTOS"
        return totalRunner