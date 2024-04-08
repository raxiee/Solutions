"""
Opgave "Morris The Miner" (denne gang objekt orienteret)

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Genbrug din oprindelige Morris-kode og omskriv den til en objektorienteret version.

Definer en klasse Miner med attributter som sleepiness, thirst osv.
og metoder som sleep, drink osv.
Opret Morris og initialiser hans attributter ved at kalde konstruktoren for Miner:
morris = Miner()

Hvis du går i stå, så spørg google, de andre elever eller læreren (i denne rækkefølge).

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""

class Miner:
    def __init__(self, sleepiness=0, thirst=0, hunger=0, whiskey=0, gold=0):
        self.sleepiness = sleepiness
        self.thirst = thirst
        self.hunger = hunger
        self.whiskey = whiskey
        self.gold = gold

    def drink(self):
        self.sleepiness += 5
        self.thirst -= 15
        if self.thirst < 0:
            self.thirst = 0
        self.hunger -= 1
        if self.hunger < 0:
            self.hunger = 0
        self.whiskey -= 1

    def buy_whiskey(self):
        self.sleepiness += 5
        self.thirst += 1
        self.hunger += 1
        self.whiskey += 1
        self.gold -= 1

    def sleep(self):
        self.sleepiness -= 10
        if self.sleepiness < 0:
            self.sleepiness = 0
        self.thirst += 1
        self.hunger += 1

    def mine(self):
        self.sleepiness += 5
        self.thirst += 5
        self.hunger += 5
        self.gold += 5

    def eat(self):
        self.sleepiness += 5
        self.thirst -= 5
        if self.thirst < 0:
            self.thirst = 0
        self.hunger -= 20
        if self.hunger < 0:
            self.hunger = 0
        self.gold -= 2

def print_attributes(miner):
    print('sleepiness =', miner.sleepiness)
    print('thirst =', miner.thirst)
    print('hunger =', miner.hunger)
    print('whiskey =', miner.whiskey)

def morris_functional_alcoholic(turns, miner):
    turns_done = 0
    for i in range(turns):
        turns_done = i + 1
        if miner.sleepiness > 100:
            print('Oh no, you killed poor Morris! When he passed away from sleep deprivation after', i, '/', turns, 'turns, he had', miner.gold, 'gold\n\n' 'His attributes were at the following levels:')
            break
        elif miner.thirst > 100:
            print('Oh no, you killed poor Morris! When he died of thirst after', i, '/', turns, 'turns, he had', miner.gold, 'gold\n\n' 'His attributes were at the following levels:')
            break
        elif miner.hunger > 100:
            print('Oh no, you killed poor Morris! When he died of starvation after', i, '/', turns, 'turns, he had', miner.gold, 'gold\n\n' 'His attributes were at the following levels:')
            break
        elif miner.gold < 0:
            print('Oh no, you bankrupted poor Morris! When you caused him to go broke after', i, '/', turns, 'turns, he had', miner.gold, 'gold\n\n' 'His attributes were at the following levels:')
            break
        elif miner.sleepiness >= 90:
            miner.sleep()
        elif miner.thirst >= 90:
            if miner.whiskey < 1:
                miner.buy_whiskey()
            miner.drink()
        elif miner.hunger >= 90:
            miner.eat()
        else:
            miner.mine()

    return miner.sleepiness, miner.thirst, miner.hunger, miner.whiskey, miner.gold, turns, turns_done


def main():
    morris = Miner()
    sleepiness, thirst, hunger, whiskey, gold, turns, turns_done = morris_functional_alcoholic(1000, morris)
    print('Morris ended the game with', gold, 'gold after', turns_done, 'turns.\n\n' 'His attributes were at the following levels:')
    print_attributes(morris)


main()
