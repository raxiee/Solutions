"""
Opgave "Morris the Miner":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Udgangssituation:
Morris har egenskaberne sleepiness, thirst, hunger, whisky, gold.
Alle attributter har startværdien 0.

Regler:
Hvis sleepiness, thirst eller hunger kommer over 100, dør Morris.
Morris kan ikke opbevare mere end 10 flasker whisky.
Ingen attribut kan gå under 0.

Ved hver omgang kan Morris udføre præcis én af disse aktiviteter:
sleep:      sleepiness-=10, thirst+=1,  hunger+=1,  whisky+=0, gold+=0
mine:       sleepiness+=5,  thirst+=5,  hunger+=5,  whisky+=0, gold+=5
eat:        sleepiness+=5,  thirst-=5,  hunger-=20, whisky+=0, gold-=2
buy_whisky: sleepiness+=5,  thirst+=1,  hunger+=1,  whisky+=1, gold-=1
drink:      sleepiness+=5,  thirst-=15, hunger-=1,  whisky-=1, gold+=0

Din opgave:
Skriv et program, der giver Morris så meget guld som muligt på 1000 omgange.

Hvis du ikke har nogen idé om hvordan du skal begynde, så åbn S0185_morris_help.py og start derfra.
Hvis du går i stå, så spørg google, de andre elever eller læreren (i denne rækkefølge).

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil.
"""

def sleep(sleepiness=0, thirst=0, hunger=0, whiskey=0, gold=0):
    sleepiness -= 10 if sleepiness >= 10 else sleepiness
    thirst += 1
    hunger += 1
    whiskey += 0
    gold += 0
    return sleepiness, thirst, hunger, whiskey, gold


def mine(sleepiness=0, thirst=0, hunger=0, whiskey=0, gold=0):
    sleepiness += 5
    thirst += 5
    hunger += 5
    whiskey += 0
    gold += 5
    return sleepiness, thirst, hunger, whiskey, gold


def eat(sleepiness=0, thirst=0, hunger=0, whiskey=0, gold=0):
    sleepiness += 5 if sleepiness >= 5 else sleepiness
    thirst -= 5 if thirst >= 5 else thirst
    hunger -= 20 if hunger >= 20 else hunger
    whiskey += 0 if whiskey >= 0 else whiskey
    gold -= 2
    return sleepiness, thirst, hunger, whiskey, gold


def buy_whiskey(sleepiness=0, thirst=0, hunger=0, whiskey=0, gold=0):
    sleepiness += 5
    thirst += 1
    hunger += 1
    whiskey += 1
    gold -= 1
    return sleepiness, thirst, hunger, whiskey, gold


def drink(sleepiness=0, thirst=0, hunger=0, whiskey=0, gold=0):
    sleepiness += 5
    thirst -= 15
    hunger -= 1
    whiskey -= 1
    gold += 0
    return sleepiness, thirst, hunger, whiskey, gold

def print_attributes(sleepiness, thirst, hunger, whiskey, gold):
    print('sleepiness =', sleepiness)
    print('thirst =', thirst)
    print('hunger =', hunger)
    print('whiskey =', whiskey)

def morris_in_recovery(turns, sleepiness=0, thirst=0, hunger=0, whiskey=0, gold=0):
    turns_done = 0
    for i in range(turns):
        turns_done = i
        if sleepiness > 100:
            print('Oh no, you killed poor Morris! When he passed away from sleep deprivation after', turns, 'turns, he had', gold, 'gold\n\n' 'His attributes were at the following levels:')
            break
        elif thirst > 100:
            print('Oh no, you killed poor Morris! When he died of thirst after', turns, 'turns, he had', gold, 'gold\n\n' 'His attributes were at the following levels:')
            break
        elif hunger > 100:
            print('Oh no, you killed poor Morris! When he died of starvation after', turns, 'turns, he had', gold, 'gold\n\n' 'His attributes were at the following levels:')
            break
        elif gold < 0:
            print('Oh no, you bankrupted poor Morris! When you caused him to go broke after', turns, 'turns, he had', gold, 'gold\n\n' 'His attributes were at the following levels:')
            break
        elif sleepiness >= 95:
            sleepiness, thirst, hunger, whiskey, gold = sleep(sleepiness, thirst, hunger, whiskey, gold)
        elif thirst >= 95:
            sleepiness, thirst, hunger, whiskey, gold = eat(sleepiness, thirst, hunger, whiskey, gold)
        else:
            sleepiness, thirst, hunger, whiskey, gold = mine(sleepiness, thirst, hunger, whiskey, gold)

    return sleepiness, thirst, hunger, whiskey, gold, turns, turns_done


def morris_functional_alcoholic(turns, sleepiness=0, thirst=0, hunger=0, whiskey=0, gold=0):
    turns_done = 0
    for i in range(turns):
        turns_done = i
        if sleepiness > 100:
            print('Oh no, you killed poor Morris! When he passed away from sleep deprivation after', i, '/', turns, 'turns, he had', gold, 'gold\n\n' 'His attributes were at the following levels:')
            break
        elif thirst > 100:
            print('Oh no, you killed poor Morris! When he died of thirst after', i, '/', turns, 'turns, he had', gold, 'gold\n\n' 'His attributes were at the following levels:')
            break
        elif hunger > 100:
            print('Oh no, you killed poor Morris! When he died of starvation after', i, '/', turns, 'turns, he had', gold, 'gold\n\n' 'His attributes were at the following levels:')
            break
        elif gold < 0:
            print('Oh no, you bankrupted poor Morris! When you caused him to go broke after', i, '/', turns, 'turns, he had', gold, 'gold\n\n' 'His attributes were at the following levels:')
            break
        elif sleepiness >= 95:
            sleepiness, thirst, hunger, whiskey, gold = sleep(sleepiness, thirst, hunger, whiskey, gold)
        elif thirst >= 95:
            if whiskey < 1:
                sleepiness, thirst, hunger, whiskey, gold = buy_whiskey(sleepiness, thirst, hunger, whiskey, gold)
            sleepiness, thirst, hunger, whiskey, gold = drink(sleepiness, thirst, hunger, whiskey, gold)
        elif hunger >= 95:
            sleepiness, thirst, hunger, whiskey, gold = eat(sleepiness, thirst, hunger, whiskey, gold)
        else:
            sleepiness, thirst, hunger, whiskey, gold = mine(sleepiness, thirst, hunger, whiskey, gold)

    return sleepiness, thirst, hunger, whiskey, gold, turns, turns_done

def main():
    sleepiness, thirst, hunger, whiskey, gold, turns, turns_done = morris_in_recovery(1000)
    print('Morris ended the game with', gold, 'gold after', turns_done, 'turns.\n\n' 'His attributes were at the following levels:')
    print_attributes(sleepiness, thirst, hunger, whiskey, gold)


main()