"""
Opgave "Animals"

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Alt, hvad du har brug for at vide for at løse denne opgave, finder du i cars_oop-filerne.

Del 1:
    Definer en klasse ved navn Animal.
    Hvert objekt i denne klasse skal have attributterne name (str), sound (str), height (float),
    weight (float), legs (int), female (bool).
    I parentes står data typerne, dette attributterne typisk har.

Del 2:
    Tilføj til klassen meningsfulde metoder __init__ og __repr__.
    Kald disse metoder for at oprette objekter af klassen Animal og for at udskrive dem i hovedprogrammet.

Del 3:
    Skriv en klassemetode ved navn make_noise, som udskriver dyrets lyd i konsollen.
    Kald denne metode i hovedprogrammet.

Del 4:
    Definer en anden klasse Dog, som arver fra Animal.
    Hvert objekt af denne klasse skal have attributterne tail_length (int eller float)
    og hunts_sheep (typisk bool).

Del 5:
    Tilføj til klassen meningsfulde metoder __init__ og __repr__.
    Ved skrivning af konstruktoren for Dog skal du forsøge at genbruge kode fra klassen Animal.
    Kald disse metoder for at oprette objekter af klassen Hund og for at udskrive dem i hovedprogrammet.

Del 6:
    Kald metoden make_noise på Dog-objekter i hovedprogrammet.

Del 7:
    Skriv en klassemetode ved navn wag_tail for Dog.
    Denne metode udskriver i konsollen noget i stil med
    "Hunden Snoopy vifter med sin 32 cm lange hale"
    Kald denne metode i hovedprogrammet.

Del 8:
    Skriv en funktion mate(mother, father). Begge parametre er af typen Dog.
    Denne funktion skal returnere et nyt objekt af typen Dog.
    I denne funktion skal du lave meningsfulde regler for den nye hunds attributter.
    Hvis du har lyst, brug random numbers så mate() producerer tilfældige hunde.
    Sørg for, at denne funktion kun accepterer hunde med det korrekte køn som argumenter.

Del 9:
    I hovedprogrammet kalder du denne metode og udskriver den nye hund.

Del 10:
    Gør det muligt at skrive puppy = daisy + brutus i stedet for puppy = mate(daisy, brutus)
    for at opnå den samme effekt.  Du bliver nok nødt til at google det først.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""

import random

class Animal:
    def __init__(self, name, sound, height, weight, legs, female):
        self.name = str(name)
        self.sound = str(sound)
        self.height = float(height)
        self.weight = float(weight)
        self.legs = int(legs)
        self.female = bool(female)

    def make_noise(self):
        # return f'\n{self.name} makes the noise {self.sound}! What a good {'girl' if self.female else 'boy'}.'
        print(f'\n{self.name} makes the noise {self.sound}! What a good {'girl' if self.female else 'boy'}.')

    def __repr__(self):
        return (
            f'{self.name} is an animal.\n\nName: {self.name}\nSound: {self.sound}\nHeight: {self.height} cm\nWeight: {self.weight} kg\n'
            f'Legs: {self.legs}\nFemale: {self.female}'
        )

class Dog(Animal):
    def __init__(self, name, sound, height, weight, legs, female, tail_length, hunts_sheep):
        super().__init__(name, sound, height, weight, legs, female)
        self.tail_length = float(tail_length)
        self.hunts_sheep = bool(hunts_sheep)

    def __repr__(self):
        return (
            f'{self.name} is a Dog.\n\nName: {self.name}\nSound: {self.sound}\nHeight: {self.height} cm\nWeight: {self.weight} kg\n'
            f'Legs: {self.legs}\nFemale: {self.female}\nTail length: {self.tail_length}\nHunts Sheep: {self.hunts_sheep}'
        )

    def wag_tail(self):
        print(f'\nThe dog, {self.name}, wags {'her' if self.female else 'his'} {self.tail_length} cm long tail.')

    def mate(mother, father):
        minimum = 0
        maximum = 1
        puppy_name = 'Alex'
        puppy_sound = f'{mother.sound}{father.sound}!'
        puppy_height = (mother.height + father.height) / 2
        puppy_weight = (mother.weight + father.weight) / 2
        puppy_legs = (mother.legs + father.legs) // 2
        puppy_female = random.randint(minimum, maximum)
        puppy_tail_length = (mother.tail_length + father.tail_length) / 2
        puppy_hunts_sheep = random.randint(minimum, maximum)
        if mother.female and not father.female:
            print(f'\n{mother.name} and {father.name} mated. It was a {'girl' if puppy_female else 'boy'} named Alex!\n')
            return Dog(puppy_name, puppy_sound, puppy_height, puppy_weight, puppy_legs, puppy_female, puppy_tail_length, puppy_hunts_sheep)
        else:
            print("\nThat's not how this works.. maybe it's time for a talk about the birds and the bees?")

    def __add__(mother, father):
        puppy = Dog.mate(mother, father)
        return puppy

def main():
    jeff = Dog('Jeff', 'brrrrr', 55.4, 32.5, 4, 0, 12.5, 1)
    sophie = Dog('Sophie', 'skrt', 33.5, 27.9, 3, 1, 10.2, 1)
    print(jeff)
    # print(jeff.make_noise())
    jeff.make_noise()
    jeff.wag_tail()
    # puppy = Dog.mate(sophie, jeff)
    puppy = sophie + jeff
    print(puppy)


main()
