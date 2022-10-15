# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import time
import random
species = {'Lorbon': 1, 'Zenith': 2, 'Haeron': 3, 'Kakrei': 4}
alive = dict()
allchosengenes = list()
u = 0
for key in species:
    if key not in alive:
        manygenes = random.randint(1, 3)
        allchosengenes.append(manygenes)
            
    else:
        alive[key] += 1
    chosengenes = list()
    for i in range(manygenes):
        genes = [1, 2, 3]
        whichgenes = random.choice(genes)
        chosengenes.append(whichgenes)
        alive[key] = chosengenes
    
    print('Species:', key, '| Gene Amount:', allchosengenes[u], '| Genes:', alive[key])
    u += 1
print(alive)
u = 0
def alivespecies():
    u = 0
    for key in species:
        print('Species:', key, '| Gene Amount:', allchosengenes[u], '| Genes:', alive[key])
        u += 1
alivespecies()
floor4 = '                                '
floor3 = '                                '
floor2 = '                                '
floor1 = '                                '
floor0 = ['O','O','O','O','O','O',' ',' ','H',' ',' ','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O', 'O']
area = (
    floor4,
    floor3,
    floor2,
    floor1,
    floor0
    )
print(floor4, '\n', floor3, '\n', floor2, '\n', floor1, '\n', floor0)
Lorbon = 'L'
walk1 = 0
walk2 = 32
walk3 = 32
walk4 = 96
print(len(floor0), len(floor1))
error = 0
def step():
    global walk1, walk2, floor0, Lorbon, walk3, walk4, alive, error
    alivespecies()
    if walk1 < 32 and walk3 > 0 and error == 0:
        walk1 += 1
        walk2 += 1
        walk3 -= 1
        walk4 -= 1
    floor0n = floor0[0:32]
    f0 = floor0n.pop(walk1)
    floor0n[walk1] = 'L'
    floor0n[walk1 - 1] = floor0[walk1 - 1]
    delimiter = ''
    floor0nn = delimiter.join(floor0n)
    # floor0n = floor0[walk1: walk2] + Lorbon + floor0[walk3: walk4]
    print(floor4, '\n', floor3, '\n', floor2, '\n', floor1, '\n', floor0nn)
    if floor0nn[30] == 'L':
        error = 1
while True:
    # time.sleep(1.5)
    test = input("Test: ")
    step()

