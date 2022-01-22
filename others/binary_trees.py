# From a BDD and one of his state, return the boolean formula from the state
def bddToBooleans(bdd, sommet):
    res = []
    # --- Find all sucessful end state (lo or hi == 1)--- #
    for row in bdd:
        if(row[2] == 1):
            res.append(["!"])
            res[len(res)-1].append((row[0], row[1]))
        elif(row[3] == 1):
            res.append([(row[0], row[1])])

    # --- Search all previous states --- #
    search = True
    found = False
    while search:
        search = False
        tempRes = res.copy()
        for formula in tempRes:
            currentSearch = formula[len(formula)-1][0]
            for row in bdd:
                if(row[2] == currentSearch):
                    newRow = formula.copy()
                    newRow.append("!")
                    newRow.append((row[0], row[1]))
                    res.append(newRow)
                    found = True
                if(row[3] == currentSearch):
                    newRow = formula.copy()
                    newRow.append((row[0], row[1]))
                    res.append(newRow)
                    found = True
                if(sommet == currentSearch): # Don't search after the specific state
                    break
            if found:
                res.remove(formula)
                found = False
                search = True

    # --- Remove formulas where is not the parameter "sommet" --- #
    resTemp = res.copy()
    for formula in resTemp:
        found = False
        for item in formula:
            if item[0] == sommet:
                found = True
        if found == False:
            res.remove(formula)

    # --- Formate to boolean string formula --- #
    finalStr = ""
    for i in range(len(res)):
        if i == 0 : finalStr += "("
        else : finalStr += " ∨ ("
        skipNext = False
        for j in range(len(res[i])):
            if skipNext:
                skipNext = False
            elif j == 0:
                if res[i][j] == '!': 
                    finalStr += "¬"+str(res[i][j+1][1])
                    skipNext = True
                else:
                    finalStr += str(res[i][j][1])
            else:
                if res[i][j] == '!': 
                    finalStr += " Λ ¬"+str(res[i][j+1][1])
                    skipNext = True
                else:
                    finalStr += " Λ "+str(res[i][j][1])
        finalStr += ")"
    return finalStr

# Inverse les 0 et 1 sur tout le BDD, créé les sommets voulus si necessaire
def revertFormula(bdd, sommet):
    if(sommet == 0):
        return 1
    if(sommet == 1):
        return 0

    exist = False
    lo = revertFormula(bdd, bdd[sommet][2])
    hi = revertFormula(bdd, bdd[sommet][3])
    for state in bdd:
        if(bdd[sommet][1] == state[1] and lo == state[2] and hi == state[3]):
            exist = True
            return state[0]
        if (not exist):
            newState = [len(bdd),bdd[sommet][1],lo,hi]
            bdd.append(newState)
            return newState[0]

def minWay(bdd, sommet):
    if(sommet == 1):
        return []
    elif(bdd[sommet][2] == 0):
        dic = minWay(bdd, bdd[sommet][3])
        dic.append(1)
        return dic
    else:
        dic = minWay(bdd, bdd[sommet][2])
        dic.append(0)
        return dic

# Prend en entré le tableau de bit comme il ressort de minWay (à l'envers)
# En sortie : Le nombre entier correspondant aux bits d'entré
def binaryToInt(tab):
    val = 0
    for i in range(len(tab)-1, -1, -1):
        if(i == 0 and tab[i] == 1):
            val += 1
        else:
            val += tab[i] * i * 2
    return val 

BDD1 = [
    [0,"X","-","-"],
    [1,"X","-","-"],
    [2,"X3",0,1],
    [3,"X2",1,2],
    [4,"X2",1,0],
    [5,"X1",4,3]
]

BDD2 = [
    [0,"X","-","-"],
    [1,"X","-","-"],
    [2,"X2",1,0],
    [3,"X2",0,1],
    [4,"X1",2,3]
]

BDD3 = [
    [0,"X","-","-"],
    [1,"X","-","-"],
    [2,"X4",0,1],
    [3,"X4",0,1],
    [4,"X3",1,2],
    [5,"X3",0,3],
    [6,"X2",5,4],
    [7,"X2",0,5],
    [8,"X1",7,6]
]

BDD = BDD3
sommet = 8

# print(bddToBooleans(BDD, sommet))
# res = revertFormula(BDD, sommet)
# print(res)
# print(bddToBooleans(BDD, res))
# print(BDD)

tab = minWay(BDD, sommet)
print(tab)
print(binaryToInt(tab))