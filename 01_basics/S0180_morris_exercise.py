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
def morris(turns, sleepiness, thirst, hunger, whiskey, gold):
    sleepiness = 0
    thirst = 0
    hunger = 0
    whiskey = 0
    gold = 0
    sleep(0, 0, 0, 0, 0,)
    print('Morris ended the game with', gold, 'gold after', turns, 'turns.\n\n' 'His attributes were at the following levels:')
    print('sleepiness =', sleepiness)
    print('thirst =',thirst)
    print('hunger =',hunger)
    print('whiskey =',whiskey)

def sleep(sleepiness, thirst, hunger, whiskey, gold):
    sleepiness -= 10
    thirst += 1
    hunger += 1
    whiskey += 0
    gold += 0
    return sleepiness, thirst, hunger, whiskey, gold

def mine(sleepiness, thirst, hunger, whiskey, gold):
    sleepiness += 5
    thirst += 5
    hunger += 5
    whiskey += 0
    gold += 5
    return sleepiness, thirst, hunger, whiskey, gold

def eat(sleepiness, thirst, hunger, whiskey, gold):
    sleepiness += 5
    thirst -= 5
    hunger -= 20
    whiskey += 0
    gold -= 2
    return sleepiness, thirst, hunger, whiskey, gold

def buy_whiskey(sleepiness, thirst, hunger, whiskey, gold):
    sleepiness += 5
    thirst += 1
    hunger += 1
    whiskey += 1
    gold -= 1
    return sleepiness, thirst, hunger, whiskey, gold

def drink(sleepiness, thirst, hunger, whiskey, gold):
    sleepiness += 5
    thirst -= 15
    hunger -= 1
    whiskey -= 1
    gold += 0
    return sleepiness, thirst, hunger, whiskey, gold


def main():
    sleepiness = 0
    thirst = 0
    hunger = 0
    whisky = 0
    gold = 0
    morris(5, sleepiness, thirst, hunger, whisky, gold)

main()

# Morris skal mine så meget som muligt, så medmindre han dør, så vil det være første prioritet i min funktion.