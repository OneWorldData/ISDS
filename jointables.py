import csv

def makedict(f):
# make dictionary

    newdict = {}
    for row in f:
        ID = row['ID']
        newdict[ID] = row
    return newdict

def iftry(DB,ID,column):

    try:
        if DB[ID][column] != '':
            return DB[ID][column]
        else:
            return ''
    except KeyError:
        return ''
    
def fillin(ID,column):
# fillin missing values
    global F1,F2,GUS,I,OU,DUTCH,C9,C11,C13,U

    tryf1 = iftry(F1,ID,column)
    tryf2 = iftry(F2,ID,column)
    trygus = iftry(GUS,ID,column)
    tryI = iftry(I,ID,column)
    tryou = iftry(OU,ID,column)
    tryu = iftry(U,ID,column)
    trydutch = iftry(DUTCH,ID,column)
    tryc9 = iftry(C9,ID,column)
    tryc11 = iftry(C11,ID,column)
    tryc13 = iftry(C13,ID,column)

    if tryf1 != '':
        return tryf1
    elif tryf2 != '':
        return tryf2
    elif trygus != '':
        return trygus
    elif tryI != '':
        return tryI
    elif tryou != '':
        return tryou
    elif trydutch != '':
        return trydutch
    elif tryc13 != '':
        return tryc13
    elif tryc11 != '':
        return tryc11
    elif tryc9 != '':
        return tryc9
    elif tryu!= '':
        return tryu
    else:
        return 'unknownValue'

c9 = csv.DictReader(open('tables/claims_2009.csv'))
c11 = csv.DictReader(open('tables/claims_2011.csv'))
c13 = csv.DictReader(open('tables/claims_2013_NC.csv'))
f2 = csv.DictReader(open('tables/Frankfillin-2.csv'))
f1 = csv.DictReader(open('tables/Frankfillin.csv'))
gus = csv.DictReader(open('tables/GusDB.csv'))
i = csv.DictReader(open('tables/ICSID.csv'))
ou = csv.DictReader(open('tables/oldUNCTAD.csv'))
dutch = csv.DictReader(open('tables/Dutch_ISDS.csv'))
u = csv.DictReader(open('tables/UNCTAD.csv'))
DB = csv.DictReader(open('tables/DB-master.csv'))

C9 = makedict(c9)
C11 = makedict(c11)
C13 = makedict(c13)
F2 = makedict(f2)
F1 = makedict(f1)
GUS = makedict(gus)
I = makedict(i)
OU = makedict(ou)
U = makedict(u)
DUTCH = makedict(dutch)

newdb = {}
fieldnames = ["ID","CaseTitle","InitiationYear","ResolutionYear","RespondentState","ClaimantCountry","ClaimantName","InvestmentType","ArbitrationRules","LegalInstrument","OutcomeStatus","amountSought","amountSought_cur","amountAwarded","amountAwarded_cur","Arbitrator1","Arbitrator1President","Arbitrator2","Arbitrator2Claimant","Arbitrator3","Arbitrator3Respondent","description","italaw"]

for row in DB:

    ID = row['ID']

    newdb[ID] = {}

    for column in row:
       cell = row[column]
       if cell == '':
            cell = fillin(ID,column)

       newdb[ID][column] = cell

# import pprint
# pprint.pprint(newdb)

with open("isds.csv","w") as out:
    writer = csv.DictWriter(out, fieldnames=fieldnames)
    writer.writeheader()

    for ID in newdb:
        writer.writerow(newdb[ID])    


