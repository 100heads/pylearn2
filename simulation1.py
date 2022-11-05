import time
import random
import string
from blessed import Terminal

class Speciesobj:
    x = 0
    z = 0
    right = 0
    left = 0
    up = 0
    down = 0
    ranletter = "+"
    def __init__(self, x, z, right, left, up, down, ranletter):
        self.x = x
        self.z = z
        self.right = right
        self.left = left
        self.up = up
        self.down = down
        self.ranletter = ranletter


term = Terminal()


species = list()

floorcount = 22
floors = ["██████████████████████████████████████████████████████████████████████████"] * floorcount

for namenum in range(100000):
    species.append(str(namenum+1))

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
floors[21] = "██████████████████████████████████████████████████████████████████████████"
floors[20] = "█                                              ==                        █"
floors[19] = "█                                              ==                        █"
floors[18] = "█                                              ==                        █"
floors[17] = "█                                              ==                        █"
floors[16] = "█                                              ==                        █"
floors[15] = "█                                              ==                        █"
floors[14] = "█                                              ==                        █"
floors[13] = "█                                              ==                        █"
floors[12] = "█                                              ==                        █"
floors[11] = "█                                              ==                        █"
floors[10] = "█                                              ==                        █"
floors[9]  = "█                                              ==                        █"
floors[8]  = "█                                              ==                        █"
floors[7]  = "█                                              ==                        █"
floors[6]  = "█                                              ==                        █"
floors[5]  = "█                                              ==                        █"
floors[4]  = "█                                              ==                        █"
floors[3]  = "█                                              ==                        █"
floors[2]  = "█                                              ==                        █"
floors[1]  = "█                                              ==                        █"
floors[0]  = "██████████████████████████████████████████████████████████████████████████"
print('Floor 0 length: ',len(floors[0]))
print('Floor 21 length: ',len(floors[21]))
for index, floor in enumerate(reversed(floors)):
    print(floor)

area2n = ["X"] * floorcount
for index, floor in enumerate(reversed(floors)):
    area2n[index] = floors[index][:]


#print(floors[4], '\n', floors[3], '\n', floors[2], '\n', floors[1], '\n', floors[0])
Lorbon = random.choice(string.ascii_letters)

walk1 = 0
walk2 = 74
walk3 = 22
walk4 = 96
print(len(floors[0]), len(floors[1]))
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
        ranletter = random.choice(string.ascii_letters)
       # try:
            #speciesvals[key] = [xval, zval, 0, 0, 0, random.choice(string. ascii_letters), 0]
        speciesvals[key] = Speciesobj(xval, zval, 0, 0, 0, 0, ranletter)
       # except:
        #    print('OW')
    #random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u', 'v', 'w', 'x', 'y', 'z'], ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])]
    #speciesvals = {'Lorbon': [random.randint(1, 32), random.randint(0, 9), 0, 0, 0, random.choice(string.ascii_letters)], 'Zenith': [random.randint(1, 32), random.randint(1, 32), 0, 0, 0, random.choice(string.ascii_letters)], 'Haeron': [random.randint(1, 32), random.randint(0, 9), 0, 0, 0, random.choice(string.ascii_letters)], 'Kakrei': [random.randint(1, 32), random.randint(0, 9), 0, 0, 0, random.choice(string.ascii_letters)]}
spoon()
walk1 = 0
walk2 = 74
def step():
    global area2n, walk1, walk2, floors, Lorbon, walk3, walk4, alive, error, walk01, error2, error3, speciesvals, floorcount
    delimiter = ''
    print(f"{term.home}{term.white_on_black}{term.clear}")
    # copy floors to area2 and area2n

   
    #alivespecies()
  
    for key in speciesvals:
        geneval = speciesvals[key]
        if key in alive:
            thegene = alive[key]
            #check if there is no error
            #get the floor they are on
            r = area2n[geneval.z]

            # clear out position they are at
            area2n[geneval.z] = area2n[geneval.z][:geneval.x] + " " + area2n[geneval.z][geneval.x + 1:]
            # check for invalid moving, return to zero if invalid
            if r[geneval.x + 1] == ' ' or r[geneval.x + 1] == '=':
                geneval.right = 0
            if r[geneval.x - 1] == ' ' or r[geneval.x - 1] == '=':
                geneval.left = 0
            if area2n[geneval.z + 1][geneval.x] == ' ' or area2n[geneval.z + 1][geneval.x] == '=':
                geneval.up = 0
            if area2n[geneval.z - 1][geneval.x] == ' ' or area2n[geneval.z - 1][geneval.x] == '=':
                geneval.down = 0
            
            #check if there is an error
            r = area2n[geneval.z]
            if r[geneval.x + 1] != ' ' and r[geneval.x + 1] != '=':
                geneval.right = 1
            if r[geneval.x - 1] != ' ' and r[geneval.x - 1] != '=':
                geneval.left = 1
            if area2n[geneval.z + 1][geneval.x] != ' ' and area2n[geneval.z + 1][geneval.x] != '=':
                geneval.up = 1
            if area2n[geneval.z - 1][geneval.x] != ' ' and area2n[geneval.z - 1][geneval.x] != '=':
                geneval.down = 1
            #GENES AND MOVEMENT
            if thegene[0] == 1 and geneval.right == 0:
                if geneval.x < 76 and geneval.right == 0:
                    geneval.x += 1
            if thegene[0] == 2 and geneval.left == 0:
                if geneval.x > 0 and geneval.left == 0:
                    geneval.x -= 1
            if thegene[0] == 3 and geneval.up == 0:
                if geneval.z < 21 and geneval.up == 0:
                    geneval.z += 1
            if thegene[0] == 4 and geneval.up == 0:
                if geneval.z > 0 and geneval.down == 0:
                    geneval.z -= 1
            #map updating
            #r = area2[geneval.z]
            #r2 = area2n[geneval.z]
            #r[geneval.x] = geneval.ranletter
            #area2n[geneval.z] = delimiter.join(r)

            #print species to map at their new assigned position
            area2n[geneval.z] = area2n[geneval.z][:geneval.x] + geneval.ranletter + area2n[geneval.z][geneval.x + 1:]
    remainder = 0
    if test == 's':
        if walk3 > 19:
            walk3 -= 1
    if test == 'w':
        if walk3 < floorcount:
            walk3 += 1
    floornum = 21
    for i in range(floorcount): #range is 1 more than max floornum
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
    print(f"{term.home}{term.white_on_black}{term.clear}")
    # so.system('clear')
    step()
    #except:
        #print('A bug has occurred. The loop will be retried.')
        #speciesvals = dict()
        #spoon()

