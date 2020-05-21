from Team import Team
from Runner import Runner
totalRunner=[]
speedRunners = {}
dictionaryRunners = {}
team1 = Team()
team2 = Team()
equip1 = team1.register()
equip2 = team2.register()
runners1 = Runner(equip1)
runners2 = Runner(equip2)
speedRunners.update(runners1.getSpeedRunners())
speedRunners.update(runners2.getSpeedRunners())

for runner in speedRunners:
        totalRunner.append(runners1.racerRunners(runner,speedRunners[runner]))
print("")
count = 1
for finish in totalRunner:
    print("INTEGRANTE(S) DEL GRUPO " + str(count))
    print(finish)
    count = count+1