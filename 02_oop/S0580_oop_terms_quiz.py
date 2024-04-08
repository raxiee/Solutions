"""
Kør dette program.
Tilføj oop-relaterede kommentarer til denne kode.
    Eksempler:
        class definition / klasse definition
        constructor / konstruktor
        inheritance / nedarvning
        object definition / objekt definition
        attribute / attribut
        method / metode
        polymorphism / polymorfisme
        encapsulation: protected attribute / indkapsling: beskyttet attribut
        encapsulation: protected method / indkapsling: beskyttet metode
"""


class Building:  # Class definition
    def __init__(self, area, floors, value):  # Constructor, magic function hvilket ses ved brug af to underscores før og efter
        self.area = area  # Attribute
        self.floors = floors  # Attribute
        self._value = value  # Attribute

    def renovate(self):  # Method
        print("Installing an extra bathroom...")
        self._adjust_value(10)  # Protected method calles her. Det er helt ok, da det foregår inden for samme class

    def _adjust_value(self, percentage):  # Protected method, _adjust_value bør altså ikke calles uden for class 'Building'
        self._value *= 1 + (percentage / 100)  # Protected attribute, _value bør altså ikke bruges uden for class 'Building'
        print(f'Value has been adjusted by {percentage}% to {self._value:.2f}\n')


class Skyscraper(Building):  # Inheritance, 'Skyscraper' er nu en child class til parent class 'Building'

    def renovate(self):  # Method fra parent class omskrives. Samme method kan calles i fx en list og gøre noget forskelligt alt afhængigt af objektets class (polymorphism)
        print("Installing a faster elevator.")
        self._adjust_value(6)  # Protected method, _adjust_value inherited fra 'Building', 'Skyscraper's parent class


small_house = Building(160, 2, 200000)  # Object definition, 'small_house' er nu et object af class 'Building'
skyscraper = Skyscraper(5000, 25, 10000000)  # Object definition, 'skyscraper' er nu et object af class 'Skyscraper'

for building in [small_house, skyscraper]:  # for-loop, der gør noget for hver ting i listen
    print(f'This building has {building.floors} floors and an area of {building.area} square meters.')  # Virker for begge, da 'Skyscraper' også er en 'Building'
    building.renovate()  # Polymorphism, 'Skyscraper' er også en 'Building', men methoden 'renovate()' er omskrevet for Skyscraper, så det resulterer i et andet output,
    # men begge kan kaldes på samme tid, og metoden, der bliver brugt, er bestemt af classen.
