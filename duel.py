import random


rollResult= 0


gameCount = 0


roundCount = 0


unit1Wins = 0


unit2Wins = 0


nameList = ["Erkki", "Pertti", "Masi", "Jorma", "Petteri", "Matti", "Gulliveri", "Mikko", "Matomies"]


unit1 = None
unit2 = None


def rollDice():
    global rollResult
    roll = random.randint(1,100)
    rollResult += roll


class basicUnit:
    
    def __init__(self, name, maxhitpoints, hitpoints, basedamage, damage,
                 basehitchance, hitchance, basedodgechance, dodgechance,
                 armour, initiative, aggressive, defensive, panicked):
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
        self.aggressive = aggressive
        self.defensive = defensive
        self.panicked = panicked

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
                aggressive = 0
                defensive = 0
                panicked = 0
                return self(name, maxhitpoints, hitpoints, basedamage, damage,
                            basehitchance, hitchance, basedodgechance, dodgechance,
                            armour, initiative, aggressive, defensive, panicked)
            except:
                print("invalid input, please try again.")
                continue

    @classmethod
    def defaultUnit(self):
        name = random.choice(nameList)
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
        aggressive = 0
        defensive = 0
        panicked = 0
        return self(name, maxhitpoints, hitpoints, basedamage, damage,
                    basehitchance, hitchance, basedodgechance, dodgechance,
                    armour, initiative, aggressive, defensive, panicked)


    def unitBehavior(self):
        if self.hitpoints <= (self.maxhitpoints/4):
            self.hitchance = self.basehitchance - 10
            self.dodgechance = self.basedodgechance + 20
            self.damage = self.basedamage - 1
            print(f"{self.name} is panicked!")
        elif self.hitpoints <= (self.maxhitpoints/2):
            self.hitchance = self.basehitchance
            self.dodgechance = self.basedodgechance + 10
            self.damage = self.basedamage - 1
            print(f"{self.name} is defensive!")
        else:
            self.damage = self.basedamage + 1
            self.dodgechance = self.basedodgechance + 10
            self.hitchance = self.basehitchance
            print(f"{self.name} is aggressive!")


def combatRound():
    unit1.initiative += random.randint(1,100)
    unit2.initiative += random.randint(1,100)
    unit1.unitBehavior()
    unit2.unitBehavior()
    if unit1.initiative > unit2.initiative:
        print(f"{unit1.name} won the initiative for this round.")
        if unit1.hitpoints <= 0:
            print(f"{unit1.name} can't act because they are dead.")
        else:
            unit1Turn()
            unit2Turn()
            unit1.initiative = 0
            unit2.initiative = 0
    elif unit2.initiative > unit1.initiative:
        print(f"{unit2.name} won the initiative for this round.")
        if unit2.hitpoints <= 0:
            print(f"{unit2.name} can't act because they are dead.")
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
    
    while True:
        unit1Wins = 0
        unit2Wins = 0
        gameCount = 0
        roundCount = 0
        choice = int(input("Default unit (1), custom unit (2), or exit program (3)? "))
        print("\n")
        if choice == 1:
            unit1 = basicUnit.defaultUnit()
            unit2 = basicUnit.defaultUnit()
        elif choice == 2:
            unit1 = basicUnit.get_user_input()
            unit2 = basicUnit.get_user_input()
        elif choice == 3:
            break
        else:
            print("Invalid input. Try again.")
            continue
        iterations = int(input("How many times should the duel be run? "))
        print("\n")
        for i in range (iterations):
            roundCount = 0
            gameCount += 1
            print(f"Game #{gameCount}\n")
            unit1.hitpoints = unit1.maxhitpoints
            unit2.hitpoints = unit2.maxhitpoints  
            while True:
                if unit1.hitpoints <= 0:
                    print(f"{unit1.name} lost.\n")
                    unit2Wins += 1
                    print(f"{unit1.name}'s score = {unit1Wins}, {unit2.name}'s score = {unit2Wins}.\n\n")

                    break
                elif unit2.hitpoints <= 0:
                    print(f"{unit2.name} lost\n")
                    unit1Wins += 1
                    print(f"{unit1.name}'s score = {unit1Wins}, {unit2.name}'s score = {unit2Wins}.\n\n")
                    break
                else:
                    roundCount += 1
                    print(f"\nRound {roundCount}, Game {gameCount}\n")
                    combatRound()


def unit1Turn():
    global rollResult
    if unit1.hitpoints <= 0:
        pass
    else:
        print(f"{unit1.name} attacks!")
        rollDice()
        if rollResult > unit1.hitchance:
            print(f"{unit1.name}'s attack missed.")
            rollResult = 0
            return rollResult
        else:
            print(f"{unit1.name}'s attack succeeded.")
            rollDice()
            if rollResult > unit2.dodgechance:
                print(f"{unit2.name} failed to dodge the attack.")
                unit2.hitpoints -= (unit1.damage - unit2.armour)
                print(f"{unit2.name} took {unit1.damage - unit2.armour} damage and has {unit2.hitpoints} hitpoints left.")
            else:
                print(f"{unit2.name} dodged the attack.")


def unit2Turn():
    global rollResult
    if unit2.hitpoints <= 0:
        pass
    else:
        print(f"{unit2.name} attacks!")
        rollDice()
        if rollResult > unit2.hitchance:
            print(f"{unit2.name}'s attack missed.")
            rollResult = 0
            return rollResult
        else:
            print(f"{unit2.name}'s attack succeeded.")
            rollDice()
            if rollResult > unit1.dodgechance:
                print(f"{unit1.name} failed to dodge the attack")
                unit1.hitpoints -= (unit2.damage - unit1.armour)
                print(f"{unit1.name} took {unit2.damage - unit1.armour} damage and has {unit1.hitpoints} hitpoints left.")
            else:
                print(f"{unit1.name} dodged the attack.")


mainLoop()


