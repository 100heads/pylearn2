import time
import random
import string
# 32 species so far
species = ['Lorbon', 'Zenith', 'Haeron', 'Kakrei', 'Libbin', 'Isirant', 'Mexeleon', 'Qhelluleon', 'Qharitan', 'Yesaiinae', 'Eshalian', 'Zathulae', 'Gruducean', 'Stirrenian', 'Qatheamon', 'Essego', 'fdh', 'gfhuh', 'fdhd', 'fdbb', 'fgnf', 'sgdf', 'sg', 'efg', 'qwerty', 'uiop', 'asd', 'fghjk', 'lzxc', 'vbnm', 'qscwdv', 'potyu']
alive = dict()
allchosengenes = list()
u = 0
while True:
    howmanyspecies = input('Input the number of creatures preferred for the simulation (32 max): \n')
    try:
        howmanyspecies = int(howmanyspecies)
        break
    except:
        # so.system('clear')
        continue
for key in species[0:howmanyspecies]:
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
    
    #print('Species:', key, '| Gene Amount:', allchosengenes[u], '| Genes:', alive[key])
    u += 1
print(alive)
u = 0
def alivespecies():
    u = 0
    for key in alive:
        print('Species:', key, '| Gene Amount:', allchosengenes[u], '| Genes:', alive[key])
        u += 1
alivespecies()
floor9 = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','M','M',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
floor8 = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','M','M',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
floor7 = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','M','M',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
floor6 = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','M','M',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
floor5 = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','M','M',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
floor4 = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','M','M',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
floor3 = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','M','M',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
floor2 = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','M','M',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
floor1 = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','M','M',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
floor0 = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','M','M',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
area = (
    floor4,
    floor3,
    floor2,
    floor1,
    floor0
    )
print(floor4, '\n', floor3, '\n', floor2, '\n', floor1, '\n', floor0)
Lorbon = random.choice(string.ascii_letters)

walk1 = 16
walk01 = 0
walk2 = 32
walk3 = 32
walk4 = 96
print(len(floor0), len(floor1))
error = 0
error2 = 0
error3 = 0
speciesvals = dict()
# List: x, z, error1, error2, error3, character.
def spoon():
    global species, speciesvals
    for key in species:
        try:
            speciesvals[key] = [random.randint(1, 32), random.randint(0, 9), 0, 0, 0, random. choice(string. ascii_letters)]
        except:
            print('OW')
    #random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u', 'v', 'w', 'x', 'y', 'z'], ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])]
    #speciesvals = {'Lorbon': [random.randint(1, 32), random.randint(0, 9), 0, 0, 0, random.choice(string.ascii_letters)], 'Zenith': [random.randint(1, 32), random.randint(1, 32), 0, 0, 0, random.choice(string.ascii_letters)], 'Haeron': [random.randint(1, 32), random.randint(0, 9), 0, 0, 0, random.choice(string.ascii_letters)], 'Kakrei': [random.randint(1, 32), random.randint(0, 9), 0, 0, 0, random.choice(string.ascii_letters)]}
spoon()
def step():
    global walk1, walk2, floor0, Lorbon, walk3, walk4, alive, error, walk01, error2, error3, speciesvals
    floor0n = floor0[0:32]
    delimiter = ''
    floor0nn = delimiter.join(floor0n)
    
    floor1n = floor1[0:32]
    delimiter = ''
    floor1nn = delimiter.join(floor1n)
    
    floor2n = floor2[0:32]
    delimiter = ''
    floor2nn = delimiter.join(floor2n)
    
    floor3n = floor3[0:32]
    delimiter = ''
    floor3nn = delimiter.join(floor3n)
    
    floor4n = floor4[0:32]
    delimiter = ''
    floor4nn = delimiter.join(floor4n)
    
    floor5n = floor5[0:32]
    delimiter = ''
    floor5nn = delimiter.join(floor5n)
    
    floor6n = floor6[0:32]
    delimiter = ''
    floor6nn = delimiter.join(floor6n)
    
    floor7n = floor7[0:32]
    delimiter = ''
    floor7nn = delimiter.join(floor7n)
    
    floor8n = floor8[0:32]
    delimiter = ''
    floor8nn = delimiter.join(floor8n)
    
    floor9n = floor9[0:32]
    delimiter = ''
    floor9nn = delimiter.join(floor9n)
    alivespecies()
    for key in speciesvals:
        geneval = speciesvals[key]
        if geneval[0] == 31:
            geneval[2] = 1
        if geneval[0] == 0:
            geneval[3] = 1
        if geneval[1] == 9:
            geneval[4] = 1
        if key in alive:
            thegene = alive[key]
            if thegene[0] == 1:
                if geneval[0] < 32 and geneval[2] == 0:
                    geneval[0] += 1
                if geneval[1] == 0:
                    floor0n[geneval[0]] = geneval[5]
                    delimiter = ''
                    floor0nn = delimiter.join(floor0n)
                if geneval[1] == 1:
                    floor1n[geneval[0]] = geneval[5]
                    delimiter = ''
                    floor1nn = delimiter.join(floor1n)
                if geneval[1] == 2:
                    floor2n[geneval[0]] = geneval[5]
                    delimiter = ''
                    floor2nn = delimiter.join(floor2n)
                if geneval[1] == 3:
                    floor3n[geneval[0]] = geneval[5]
                    delimiter = ''
                    floor3nn = delimiter.join(floor3n)
                if geneval[1] == 4:
                    floor4n[geneval[0]] = geneval[5]
                    delimiter = ''
                    floor4nn = delimiter.join(floor4n)
                if geneval[1] == 5:
                    floor5n[geneval[0]] = geneval[5]
                    delimiter = ''
                    floor5nn = delimiter.join(floor5n)
                if geneval[1] == 6:
                    floor6n[geneval[0]] = geneval[5]
                    delimiter = ''
                    floor6nn = delimiter.join(floor6n)
                if geneval[1] == 7:
                    floor7n[geneval[0]] = geneval[5]
                    delimiter = ''
                    floor7nn = delimiter.join(floor7n)
                if geneval[1] == 8:
                    floor8n[geneval[0]] = geneval[5]
                    delimiter = ''
                    floor8nn = delimiter.join(floor8n)
                if geneval[1] == 9:
                    floor9n[geneval[0]] = geneval[5]
                    delimiter = ''
                    floor9nn = delimiter.join(floor9n)
            if thegene[0] == 2:
                if geneval[0] > 0 and geneval[3] == 0:
                    geneval[0] -= 1
                if geneval[1] == 0:
                    floor0n[geneval[0]] = geneval[5]
                    delimiter = ''
                    floor0nn = delimiter.join(floor0n)
                if geneval[1] == 1:
                    floor1n[geneval[0]] = geneval[5]
                    delimiter = ''
                    floor1nn = delimiter.join(floor1n)
                if geneval[1] == 2:
                    floor2n[geneval[0]] = geneval[5]
                    delimiter = ''
                    floor2nn = delimiter.join(floor2n)
                if geneval[1] == 3:
                    floor3n[geneval[0]] = geneval[5]
                    delimiter = ''
                    floor3nn = delimiter.join(floor3n)
                if geneval[1] == 4:
                    floor4n[geneval[0]] = geneval[5]
                    delimiter = ''
                    floor4nn = delimiter.join(floor4n)
                if geneval[1] == 5:
                    floor5n[geneval[0]] = geneval[5]
                    delimiter = ''
                    floor5nn = delimiter.join(floor5n)
                if geneval[1] == 6:
                    floor6n[geneval[0]] = geneval[5]
                    delimiter = ''
                    floor6nn = delimiter.join(floor6n)
                if geneval[1] == 7:
                    floor7n[geneval[0]] = geneval[5]
                    delimiter = ''
                    floor7nn = delimiter.join(floor7n)
                if geneval[1] == 8:
                    floor8n[geneval[0]] = geneval[5]
                    delimiter = ''
                    floor8nn = delimiter.join(floor8n)
                if geneval[1] == 9:
                    floor9n[geneval[0]] = geneval[5]
                    delimiter = ''
                    floor9nn = delimiter.join(floor9n)
            if thegene[0] == 3:
                if geneval[1] < 9 and geneval[4] == 0:
                    geneval[1] += 1
                if geneval[1] == 0:
                    floor0n[geneval[0]] = geneval[5]
                    delimiter = ''
                    floor0nn = delimiter.join(floor0n)
                if geneval[1] == 1:
                    floor1n[geneval[0]] = geneval[5]
                    delimiter = ''
                    floor1nn = delimiter.join(floor1n)
                if geneval[1] == 2:
                    floor2n[geneval[0]] = geneval[5]
                    delimiter = ''
                    floor2nn = delimiter.join(floor2n)
                if geneval[1] == 3:
                    floor3n[geneval[0]] = geneval[5]
                    delimiter = ''
                    floor3nn = delimiter.join(floor3n)
                if geneval[1] == 4:
                    floor4n[geneval[0]] = geneval[5]
                    delimiter = ''
                    floor4nn = delimiter.join(floor4n)
                if geneval[1] == 5:
                    floor5n[geneval[0]] = geneval[5]
                    delimiter = ''
                    floor5nn = delimiter.join(floor5n)
                if geneval[1] == 6:
                    floor6n[geneval[0]] = geneval[5]
                    delimiter = ''
                    floor6nn = delimiter.join(floor6n)
                if geneval[1] == 7:
                    floor7n[geneval[0]] = geneval[5]
                    delimiter = ''
                    floor7nn = delimiter.join(floor7n)
                if geneval[1] == 8:
                    floor8n[geneval[0]] = geneval[5]
                    delimiter = ''
                    floor8nn = delimiter.join(floor8n)
                if geneval[1] == 9:
                    floor9n[geneval[0]] = geneval[5]
                    delimiter = ''
                    floor9nn = delimiter.join(floor9n)
        if geneval[0] == 31:
            geneval[2] = 1
        if geneval[0] == 0:
            geneval[3] = 1
        if geneval[1] == 9:
            geneval[4] = 1
    print('\n', '\n', '\n', '\n', '\n', floor9nn, '\n', floor8nn, '\n', floor7nn, '\n', floor6nn, '\n', floor5nn, '\n', floor4nn, '\n', floor3nn, '\n', floor2nn, '\n', floor1nn, '\n', floor0nn)
while True:
    # time.sleep(2)
    test = input("Test: ")
    try:
        step()
    except:
        print('A bug has occurred. The loop will be retried.')
        spoon()
