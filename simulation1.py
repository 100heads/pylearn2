import time
import random
import string
namenum = 1
species = list()
for i in range(100000):
    str(namenum)
    species.append(namenum)
    int(namenum)
    namenum += 1
# 224 species so far, 160 work
specie = ['Lorbon', 'Zenith', 'Haeron', 'Kakrei', 'Libbin', 'Isirant', 'Mexeleon', 'Qhelluleon', 'Qharitan', 'Yesaiinae', 'Eshalian', 'Zathulae', 'Gruducean', 'Stirrenian', 'Qatheamon', 'Essego', 'Fardenh', 'Gejihuh', 'Vwydiher', 'Fudbble', 'Fygnif', 'Scrigduf', 'Sogoul', 'Efrilig', 'Qwertyt', 'Uiopil', 'Asrid', 'Faghij', 'Lyzxc', 'Vubnmi', 'qscwdv', 'potyu', 'Borbon', 'Benith', 'Baeron', 'Bakrei', 'Bibbin', 'Bsirant', 'Bexeleon', 'Bhelluleon', 'Bharitan', 'Besaiinae', 'Bshalian', 'Bathulae', 'Bruducean', 'Btirrenian', 'Batheamon', 'Bssego', 'Bdh', 'Bfhuh', 'Bdhd', 'Bdbb', 'Bgnf', 'Bgdf', 'Bg', 'Bfg', 'Bwerty', 'Biop', 'Bsd', 'Bghjk', 'Bzxc', 'Bbnm', 'Bscwdv', 'Botyu','borbon', 'benith', 'baeron', 'bakrei', 'bibbin', 'bsirant', 'bexeleon', 'bhelluleon', 'bharitan', 'besaiinae', 'bshalian', 'bathulae', 'bruducean', 'btirrenian', 'batheamon', 'bssego', 'bdh', 'bfhuh', 'bdhd', 'bdbb', 'bgnf', 'bgdf', 'bg', 'bfg', 'bwerty', 'biop', 'bsd', 'bghjk', 'bzxc', 'bbnm', 'bscwdv', 'botyu','97', '98', '99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116', '117', '118', '119', '120', '121', '122', '123', '124', '125', '126', '127', '128','129', '130', '131', '132', '133', '134', '135', '136', '137', '138', '139', '140', '141', '142', '143', '144', '145', '146', '147', '148', '149', '150', '151', '152', '153', '154', '155', '156', '157', '158', '159', '160','Lorbon', 'Zenith', 'Haeron', 'Kakrei', 'Libbin', 'Isirant', 'Mexeleon', 'Qhelluleon', 'Qharitan', 'Yesaiinae', 'Eshalian', 'Zathulae', 'Gruducean', 'Stirrenian', 'Qatheamon', 'Essego', 'fdh', 'gfhuh', 'fdhd', 'fdbb', 'fgnf', 'sgdf', 'sg', 'efg', 'qwerty', 'uiop', 'asd', 'fghjk', 'lzxc', 'vbnm', 'qscwdv', 'potyu','Lorbon', 'Zenith', 'Haeron', 'Kakrei', 'Libbin', 'Isirant', 'Mexeleon', 'Qhelluleon', 'Qharitan', 'Yesaiinae', 'Eshalian', 'Zathulae', 'Gruducean', 'Stirrenian', 'Qatheamon', 'Essego', 'fdh', 'gfhuh', 'fdhd', 'fdbb', 'fgnf', 'sgdf', 'sg', 'efg', 'qwerty', 'uiop', 'asd', 'fghjk', 'lzxc', 'vbnm', 'qscwdv', 'potyu']
alive = dict()
allchosengenes = list()
u = 0
while True:
    howmanyspecies = input('Input the number of creatures preferred for the simulation (160 max): \n')
    try:
        howmanyspecies = int(howmanyspecies)
        break
    except:
        # so.system('clear')
        continue
for key in species[0:howmanyspecies]:
    manygenes = random.randint(1, 3)
    allchosengenes.append(manygenes)
    chosengenes = list()
    for i in range(manygenes):
        genes = [1, 2, 3, 4]
        whichgenes = random.choice(genes)
        chosengenes.append(whichgenes)
        alive[key] = chosengenes

#print(alive)
#print(allchosengenes)
u = 0
def alivespecies():
    u = 0
    for key in alive:
        print('Species:', key, '| Gene Amount:', allchosengenes[u], '| Genes:', alive[key])
        u += 1
alivespecies()
floor21 = ['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█']
floor20 = ['█',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','=','=',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','█']
floor19 = ['█',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','=','=',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','█']
floor18 = ['█',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','=','=',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','█']
floor17 = ['█',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','=','=',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','█']
floor16 = ['█',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','=','=',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','█']
floor15 = ['█',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','=','=',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','█']
floor14 = ['█',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','=','=',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','█']
floor13 = ['█',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','=','=',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','█']
floor12 = ['█',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','=','=',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','█']
floor11 = ['█',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','=','=',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','█']
floor10 = ['█',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','=','=',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','█']
floor9 = ['█',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','=','=',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','█']
floor8 = ['█',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','=','=',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','█']
floor7 = ['█',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','=','=',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','█']
floor6 = ['█',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','=','=',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','█']
floor5 = ['█',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','=','=',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','█']
floor4 = ['█',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','=','=',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','█']
floor3 = ['█',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','=','=',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','█']
floor2 = ['█',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','=','=',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','█']
floor1 = ['█',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','=','=',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','█']
floor0 = ['█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█','█']
print('Floor 0 length: ',len(floor0))
print('Floor 21 length: ',len(floor21))
area = (
    floor4,
    floor3,
    floor2,
    floor1,
    floor0
    )
print(floor4, '\n', floor3, '\n', floor2, '\n', floor1, '\n', floor0)
Lorbon = random.choice(string.ascii_letters)

walk1 = 0
walk2 = 74
walk3 = 22
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
        xval = random.randint(1, 72)
        zval = random.randint(1, 20)
        try:
            speciesvals[key] = [xval, zval, 0, 0, 0, random. choice(string. ascii_letters), 0]
        except:
            print('OW')
    #random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u', 'v', 'w', 'x', 'y', 'z'], ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])]
    #speciesvals = {'Lorbon': [random.randint(1, 32), random.randint(0, 9), 0, 0, 0, random.choice(string.ascii_letters)], 'Zenith': [random.randint(1, 32), random.randint(1, 32), 0, 0, 0, random.choice(string.ascii_letters)], 'Haeron': [random.randint(1, 32), random.randint(0, 9), 0, 0, 0, random.choice(string.ascii_letters)], 'Kakrei': [random.randint(1, 32), random.randint(0, 9), 0, 0, 0, random.choice(string.ascii_letters)]}
spoon()
walk1 = 0
walk2 = 74
def step():
    global walk1, walk2, floor0, Lorbon, walk3, walk4, alive, error, walk01, error2, error3, speciesvals
    delimiter = ''
    floor0n = floor0[0:81]
    floor0nn = delimiter.join(floor0n)
    floor1n = floor1[0:81]
    floor1nn = delimiter.join(floor1n)
    floor2n = floor2[0:81]
    floor2nn = delimiter.join(floor2n)
    floor3n = floor3[0:81]
    floor3nn = delimiter.join(floor3n)
    floor4n = floor4[0:81]
    floor4nn = delimiter.join(floor4n)
    floor5n = floor5[0:81]
    floor5nn = delimiter.join(floor5n)
    floor6n = floor6[0:81]
    floor6nn = delimiter.join(floor6n)
    floor7n = floor7[0:81]
    floor7nn = delimiter.join(floor7n)
    floor8n = floor8[0:81]
    floor8nn = delimiter.join(floor8n)
    floor9n = floor9[0:81]
    floor9nn = delimiter.join(floor9n)
    floor10n = floor10[0:81]
    floor10nn = delimiter.join(floor10n)
    floor11n = floor11[0:81]
    floor11nn = delimiter.join(floor11n)
    floor12n = floor12[0:81]
    floor12nn = delimiter.join(floor12n)
    floor13n = floor13[0:81]
    floor13nn = delimiter.join(floor13n)
    floor14n = floor14[0:81]
    floor14nn = delimiter.join(floor14n)
    floor15n = floor15[0:81]
    floor15nn = delimiter.join(floor15n)
    floor16n = floor16[0:81]
    floor16nn = delimiter.join(floor16n)
    floor17n = floor17[0:81]
    floor17nn = delimiter.join(floor17n)
    floor18n = floor18[0:81]
    floor18nn = delimiter.join(floor18n)
    floor19n = floor19[0:81]
    floor19nn = delimiter.join(floor19n)
    floor20n = floor20[0:81]
    floor20nn = delimiter.join(floor20n)
    floor21n = floor21[0:81]
    floor21nn = delimiter.join(floor21n)
    #alivespecies()
    area2 = [
        floor0n,
        floor1n,
        floor2n,
        floor3n,
        floor4n,
        floor5n,
        floor6n,
        floor7n,
        floor8n,
        floor9n,
        floor10n,
        floor11n,
        floor12n,
        floor13n,
        floor14n,
        floor15n,
        floor16n,
        floor17n,
        floor18n,
        floor19n,
        floor20n,
        floor21n
        ]
    area2n = [
        floor0nn,
        floor1nn,
        floor2nn,
        floor3nn,
        floor4nn,
        floor5nn,
        floor6nn,
        floor7nn,
        floor8nn,
        floor9nn,
        floor10nn,
        floor11nn,
        floor12nn,
        floor13nn,
        floor14nn,
        floor15nn,
        floor16nn,
        floor17nn,
        floor18nn,
        floor19nn,
        floor20nn,
        floor21nn
        ]
    for key in speciesvals:
        geneval = speciesvals[key]
        if key in alive:
            thegene = alive[key]
            #check if there is no error
            r = area2[geneval[1]]
            if r[geneval[0] + 1] == ' ' or r[geneval[0] + 1] == '=':
                geneval[2] = 0
            if r[geneval[0] - 1] == ' ' or r[geneval[0] - 1] == '=':
                geneval[3] = 0
            if area2[geneval[1] + 1][geneval[0]] == ' ' or area2[geneval[1] + 1][geneval[0]] == '=':
                geneval[4] = 0
            if area2[geneval[1] - 1][geneval[0]] == ' ' or area2[geneval[1] - 1][geneval[0]] == '=':
                geneval[6] = 0
            
            #check if there is an error
            r = area2[geneval[1]]
            if r[geneval[0] + 1] != ' ' and r[geneval[0] + 1] != '=':
                geneval[2] = 1
            if r[geneval[0] - 1] != ' ' and r[geneval[0] - 1] != '=':
                geneval[3] = 1
            if area2[geneval[1] + 1][geneval[0]] != ' ' and area2[geneval[1] + 1][geneval[0]] != '=':
                geneval[4] = 1
            if area2[geneval[1] - 1][geneval[0]] != ' ' and area2[geneval[1] - 1][geneval[0]] != '=':
                geneval[6] = 1
            #GENES AND MOVEMENT
            if thegene[0] == 1 and geneval[2] == 0:
                if geneval[0] < 76 and geneval[2] == 0:
                    geneval[0] += 1
            if thegene[0] == 2 and geneval[3] == 0:
                if geneval[0] > 0 and geneval[3] == 0:
                    geneval[0] -= 1
            if thegene[0] == 3 and geneval[4] == 0:
                if geneval[1] < 21 and geneval[4] == 0:
                    geneval[1] += 1
            if thegene[0] == 4 and geneval[4] == 0:
                if geneval[1] > 0 and geneval[6] == 0:
                    geneval[1] -= 1
            #map updating
            r = area2[geneval[1]]
            r2 = area2n[geneval[1]]
            r[geneval[0]] = geneval[5]
            area2n[geneval[1]] = delimiter.join(r)
    remainder = 0
    if test == 's':
        if walk3 > 19:
            walk3 -= 1
    if test == 'w':
        if walk3 < 22:
            walk3 += 1
    floornum = 21
    for i in range(19): #range is 1 more than max floornum
        if walk3 > floornum:
            print(area2n[floornum][walk1:walk2])
        else:
            remainder += 1
        floornum -= 1
    #print the remainder
    for i in range(remainder):
        print(area2n[floornum][walk1:walk2])
        if floornum == 0:
            break
        floornum -= 1
    #print('\n', '\n', '\n', '\n', '\n', area2n[9], '\n', area2n[8], '\n', area2n[7], '\n', area2n[6], '\n', area2n[5], '\n', area2n[4], '\n', area2n[3], '\n', area2n[2], '\n', area2n[1], '\n', area2n[0][walk1:walk2]
while True:
    # time.sleep(2)
    test = input("Test: ")
    #try:
    # so.system('clear')
    step()
    #except:
        #print('A bug has occurred. The loop will be retried.')
        #speciesvals = dict()
        #spoon()

