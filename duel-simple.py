import random


rollResult= 0


gameCount = 0


roundCount = 0


unit1Wins = 0


unit2Wins = 0


unitNum = 0


unit1 = None
unit2 = None


def rollDice():
    global rollResult
    roll = random.randint(1,100)
    rollResult += roll

def getPercent(first, second, integer = False):
    percent = first / second * 100

    if integer:
        return int(percent)
    return round(percent, 2)


class basicUnit:
    
    def __init__(self, name, maxhitpoints, hitpoints, basedamage, damage,
                 basehitchance, hitchance, basedodgechance, dodgechance,
                 armour, initiative):
        self.name = name
        self.maxhitpoints = maxhitpoints
        self.hitpoints = hitpoints
        self.basedamage = basedamage
        self.damage = damage
        self.basehitchance = basehitchance
        self.hitchance = hitchance
        self.basedodgechance = basedodgechance
        self.dodgechance = dodgechance
        self.armour = armour
        self.initiative = initiative


    @classmethod
    def get_user_input(self):
        while 1:
            try:
                name = input("Enter name: ")
                maxhitpoints = int(input("Enter hitpoints: "))
                hitpoints = maxhitpoints
                basedamage = int(input("Enter base damage: "))
                damage = basedamage
                basehitchance = int(input("Enter base hit chance: "))
                hitchance = basehitchance
                basedodgechance = int(input("Enter base dodge chance: "))
                dodgechance = basedodgechance
                armour = int(input("Enter armour: "))
                initiative = int(input("Enter initiative: "))
                return self(name, maxhitpoints, hitpoints, basedamage, damage,
                            basehitchance, hitchance, basedodgechance, dodgechance,
                            armour, initiative)
            except:
                print("invalid input, please try again.")
                continue

    @classmethod
    def defaultUnit(self):
        name = "unit " + str(unitNum)
        maxhitpoints = 10
        hitpoints = maxhitpoints
        basedamage = 5
        damage = basedamage
        basehitchance = 50
        hitchance = basehitchance
        basedodgechance = 20
        dodgechance = basedodgechance
        armour = 2
        initiative = 50

        return self(name, maxhitpoints, hitpoints, basedamage, damage,
                    basehitchance, hitchance, basedodgechance, dodgechance,
                    armour, initiative)


def combatRound():
    unit1.initiative += random.randint(1,100)
    unit2.initiative += random.randint(1,100)
    if unit1.initiative > unit2.initiative:
        unit1Turn()
        unit2Turn()
        unit1.initiative = 0
        unit2.initiative = 0
    else: 
        unit2Turn()
        unit1Turn()
        unit1.initiative = 0
        unit2.initiative = 0


def mainLoop():
    
    global gameCount
    global roundCount
    global unit1
    global unit2
    global unit1Wins 
    global unit2Wins
    global unit1WinP
    global unit2WinP
    global unitNum
    
    while True:
        unit1Wins = 0
        unit2Wins = 0
        unit1WinP = 0
        unit2WinP = 0
        unitNum = 0
        choice = input("Default unit (1), custom unit (2), or exit program (3)? ")
        print("\n")
        if choice == "1":
            unitNum += 1
            unit1 = basicUnit.defaultUnit()
            unitNum += 1
            unit2 = basicUnit.defaultUnit()
        elif choice == "2":
            unit1 = basicUnit.get_user_input()
            unit2 = basicUnit.get_user_input()
        elif choice == "3":
            break
        else:
            print("Invalid input. Try again.\n")
            continue
        iterations = int(input("How many times should the duel be run? "))
        unit1WinP = unit1Wins / iterations * 100
        unit2WinP = unit2Wins / iterations * 100
        print("\n")
        for i in range (iterations + 1):
            roundCount = 0
            gameCount += 1
            unit1.hitpoints = unit1.maxhitpoints
            unit2.hitpoints = unit2.maxhitpoints  
            while i > 0:
                if unit1.hitpoints <= 0:
                    unit2Wins += 1
                    break
                elif unit2.hitpoints <= 0:
                    unit1Wins += 1
                    break
                else:
                    roundCount += 1
                    combatRound()
        print(f"{unit1.name}'s score = {unit1Wins}, {unit2.name}'s score = {unit2Wins}.\n\n")
        print(f"{unit1.name} won {getPercent(unit1Wins, iterations)}% of games. {unit2.name} won {getPercent(unit2Wins, iterations)}% of games.\n")

def unit1Turn():
    global rollResult
    if unit1.hitpoints <= 0:
        pass
    else:
        rollDice()
        if rollResult > unit1.hitchance:
            rollResult = 0
            return rollResult
        else:
            rollDice()
            if rollResult > unit2.dodgechance:
                unit2.hitpoints -= (unit1.damage - unit2.armour)
                rollResult = 0
                return rollResult
            else:
                pass

def unit2Turn():
    global rollResult
    if unit2.hitpoints <= 0:
        pass
    else:
        rollDice()
        if rollResult > unit2.hitchance:
            rollResult = 0
            return rollResult
        else:
            rollDice()
            if rollResult > unit1.dodgechance:
                unit1.hitpoints -= (unit2.damage - unit1.armour)
                rollResult = 0
                return rollResult
            else:
                pass


mainLoop()


