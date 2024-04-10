"""opgave: Objektorienteret rollespil, afsnit 2 :

Som altid skal du læse hele øvelsesbeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Byg videre på din løsning af afsnit 1.

Del 1:
    Opfind to nye klasser, som arver fra klassen Character. For eksempel Hunter og Magician.
    Dine nye klasser skal have deres egne ekstra metoder og/eller attributter.
    Måske overskriver de også metoder eller attributter fra klassen Character.

Del 2:
    Lad i hovedprogrammet objekter af dine nye klasser (dvs. rollespilfigurer) kæmpe mod hinanden,
    indtil den ene figur er død. Udskriv, hvad der sker under kampen.

I hver omgang bruger en figur en af sine evner (metoder). Derefter er det den anden figurs tur.
Det er op til dig, hvordan dit program i hver tur beslutter, hvilken evne der skal bruges.
Beslutningen kan f.eks. være baseret på tilfældighed eller på en smart strategi

Del 3:
    Hver gang en figur bruger en af sine evner, skal du tilføje noget tilfældighed til den anvendte evne.

Del 4:
    Lad dine figurer kæmpe mod hinanden 100 gange.
    Hold styr på resultaterne.
    Prøv at afbalancere dine figurers evner på en sådan måde, at hver figur vinder ca. halvdelen af kampene.

Hvis du går i stå, kan du spørge google, de andre elever eller læreren (i denne rækkefølge).

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-besked til din lærer: <filename> done
Fortsæt derefter med den næste fil."""

class Character:
    def __init__(self, name, health, attackpower):
        self.name = name
        self.max_health = health
        self._current_health = health
        if self._current_health < 0:
            self._current_health = 0
        self.attackpower = attackpower
        self.attackcooldown = 0
        if self.attackcooldown < 0:
            self.attackcooldown = 0

    def __repr__(self):
        return f'Name: {self.name}\nMax health: {self.max_health}\nCurrent health: {self._current_health}\nAttackpower: {self.attackpower}\n'

    # def hit_without_get_hit(self, target):
    #     if isinstance(target, Character):
    #         target._current_health -= self.attackpower

    def hit(self, target):
        print(f'{self.name} strikes {target.name} for {self.attackpower} damage!\n')
        target.get_hit(self.attackpower)

    def get_hit(self, attackpower):
        self._current_health -= attackpower

    def get_healed(self, healpower):
        self._current_health += healpower

    def polymorphed(self):
        self.attackcooldown += 2


class Healer(Character):
    def __init__(self, name, health, healpower):
        super().__init__(name, health, attackpower=0)
        self.healpower = healpower

    def heal(self, target):
        print(f'{self.name} heals {target.name} for {self.healpower} health!\n')
        target.get_healed(self.healpower)

class Mage(Character):
    def __init__(self, name, health, attackpower):
        super().__init__(name, health, attackpower)

    def polymorph(self, target):
        print(
            f'{self.name} polymorphs {target.name}! {target.name} is unable to perform an action for next two turns! '
            f'Polymorph is now on cooldown for 5 turns.\n'
        )


class Hunter(Character):
    def __init__(self, name, health, attackpower, pet_name):
        super().__init__(name, health, attackpower)
        self.pet_name = pet_name
        self.pet_attackpower = self.attackpower // 2

    def hit(self, target):
        print(
            f"{self.name} strikes {target.name} for {self.attackpower} damage, and their pet, "
            f"{self.pet_name}, strikes {target.name} for {self.pet_attackpower} damage!\n"
        )
        target.get_hit(self.pet_attackpower)
        target.get_hit(self.attackpower)


    def bestial_wrath(self):
        print(
            f"{self.name} and {self.pet_name} are enraged by their inner beast, causing their damage to be doubled this turn!"
            f"Bestial wrath is now on cooldown for 5 turns.\n"
        )


def battle(char1, char2):
    print(f"A battle between the fierce {char1.name} and the ruthless {char2.name} is about to commence...\n")
    turns = 0
    polymorph_cooldown = 0
    if polymorph_cooldown < 0:
        polymorph_cooldown = 0
    bestial_wrath_cooldown = 0
    if bestial_wrath_cooldown < 0:
        bestial_wrath_cooldown = 0
    char1.attackcooldown -= 1
    char2.attackcooldown -= 1
    while char1._current_health and char2._current_health > 0:
        if char1._current_health == 0:
            print(f"{char1.name} has been defeated, and {char2.name} is victorious with "
                  f"{char2._current_health} health remaining after {turns} turns! Are you not entertained?!?"
                  )
            break
        if char2._current_health == 0:
            print(f"{char2.name} has been defeated, and {char1.name} is victorious with "
                  f"{char1._current_health} health remaining after {turns} turns! Are you not entertained?!?"
                  )
            break
        if isinstance(char1, Mage) and polymorph_cooldown == 0 and char1.attackpower == 0:
            char1.polymorph(char2)
            polymorph_cooldown = 5

    turns += 1



def main():
    char1 = Hunter('Timothy', 80, 10, 'Pedro')
    char2 = Mage('Christopher', 80, 10)
    char3 = Healer('Leona', 80, 10)
    print(f"Christopher's current health: {char2._current_health}")
    char1.hit(char2)
    print(f"Christopher's current health: {char2._current_health}")
    char3.heal(char2)
    print(f"Christopher's current health: {char2._current_health}")


main()
