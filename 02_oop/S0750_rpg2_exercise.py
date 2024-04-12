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


import random

class Character:
    def __init__(self, name, health, attackpower):
        self.name = name
        self.max_health = health
        self._current_health = health
        self.attackpower = attackpower
        self.attackcooldown = 0

    def __repr__(self):
        return f'Name: {self.name}\nMax health: {self.max_health}\nCurrent health: {self._current_health}\nAttackpower: {self.attackpower}\n'

    # def hit_without_get_hit(self, target):
    #     if isinstance(target, Character):
    #         target._current_health -= self.attackpower

    def hit(self, target):
        damage = self.calculate_damage()
        print(f'{self.name} strikes {target.name} for {damage} damage!\n')
        target.get_hit(damage)

    def get_hit(self, attackpower):
        self._current_health -= attackpower
        if self._current_health < 0:
            self._current_health = 0

    def get_healed(self, healpower):
        self._current_health += healpower

    def update_cooldown(self):
        pass

    def calculate_damage(self):
        minimum = int(self.attackpower * 0.5)
        maximum = int(self.attackpower * 1.5)
        damage = random.randint(minimum, maximum)
        return damage


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
        self.polymorph_cooldown = 0
        if self.polymorph_cooldown < 0:
            self.polymorph_cooldown = 0

    def polymorph(self, target):
        print(f'{self.name} polymorphs {target.name}! {target.name} is unable to perform an action for next two turns! '
              f'Polymorph is now on cooldown for 5 turns.\n')
        target.attackcooldown += 3

    def update_cooldown(self):
        self.polymorph_cooldown = max(0, self.polymorph_cooldown - 1)

class Hunter(Character):
    def __init__(self, name, health, attackpower, pet_name):
        super().__init__(name, health, attackpower)
        self.pet_name = pet_name
        self.pet_attackpower = self.attackpower // 2
        self.bestial_wrath_cooldown = 0
        if self.bestial_wrath_cooldown < 0:
            self.bestial_wrath_cooldown = 0

    def update_cooldown(self):
        self.bestial_wrath_cooldown = max(0, self.bestial_wrath_cooldown - 1)

    def hit(self, target):
        damage, pet_damage = self.calculate_damage()
        print(f"{self.name} strikes {target.name} for {damage} damage, and their pet, "
              f"{self.pet_name}, strikes {target.name} for an additional {pet_damage} damage!\n")
        target.get_hit(pet_damage)
        target.get_hit(damage)

    def calculate_damage(self):
        minimum = int(self.attackpower * 0.5)
        maximum = int(self.attackpower * 1.5)
        minimum_pet = int(self.pet_attackpower * 0.5)
        maximum_pet = int(self.pet_attackpower * 1.5)
        damage = random.randint(minimum, maximum)
        pet_damage = random.randint(minimum_pet, maximum_pet)
        return damage, pet_damage

    def bestial_wrath(self, target):
        damage, pet_damage = self.calculate_damage()
        print(f"{self.name} and {self.pet_name} are enraged by their inner beasts, causing their damage to be doubled this turn! "
              f"Bestial wrath is now on cooldown for 5 turns.\n")
        target.get_hit(damage * 2)
        target.get_hit(pet_damage * 2)
        print(f"{self.name} strikes {target.name} for {damage * 2} damage, and their pet, "
              f"{self.pet_name}, strikes {target.name} for {pet_damage * 2} damage!\n")

def battle(char1, char2):
    print(f"A battle between the fierce {char1.name} and the ruthless {char2.name} is about to commence...\n")
    turns = 0
    while char1._current_health > 0 and char2._current_health > 0:
        if char1.attackcooldown > 0:
            char1.attackcooldown -= 1
        if char2.attackcooldown > 0:
            char2.attackcooldown -= 1
        char1.update_cooldown()
        char2.update_cooldown()
        if isinstance(char1, Mage) and char1.polymorph_cooldown == 0 and char1.attackcooldown == 0:
            char1.polymorph(char2)
            char1.polymorph_cooldown += 6
        elif isinstance(char1, Hunter) and char1.bestial_wrath_cooldown == 0 and char1.attackcooldown == 0:
            char1.bestial_wrath(char2)
            char1.bestial_wrath_cooldown += 6
        elif char1.attackcooldown == 0:
            char1.hit(char2)
        else:
            print(f"{char1.name}'s attack is still on cooldown, so their turn is skipped.\n")

        if isinstance(char2, Hunter) and char2.bestial_wrath_cooldown == 0 and char2.attackcooldown == 0:
            char2.bestial_wrath(char1)
            char2.bestial_wrath_cooldown += 6
        elif isinstance(char2, Mage) and char2.polymorph_cooldown == 0 and char2.attackcooldown == 0:
            char2.polymorph(char1)
            char2.polymorph_cooldown += 6
        elif char2.attackcooldown == 0:
            char2.hit(char1)
        else:
            print(f"{char2.name}'s attack is still on cooldown, so their turn is skipped.\n")
            print(f"Attack cooldown value = {char2.attackcooldown}")

        turns += 1

    print(f"The battle lasted {turns} turns.\n")
    print(f"Final health of {char1.name}: {char1._current_health}")
    print(f"Final health of {char2.name}: {char2._current_health}\n")
    if char1._current_health <= 0 and char2._current_health <= 0:
        print(f'Both gladiators were killed in battle, resulting in a draw. Are you not entertained?!?\n')
    elif char2._current_health <= 0:
        print(f'{char1.name} is victorious! Are you not entertained?!?\n')
    elif char1._current_health <= 0:
        print(f'{char2.name} is victorious! Are you not entertained?!?\n')

def many_battles(battles):
    char_1_wins = 0
    char_2_wins = 0
    draws = 0
    for _ in range(battles):
        char_1 = Hunter('Timothy', 250, 10, 'Pedro')
        char_2 = Mage('Christopher', 239, 16)
        battle(char_1, char_2)
        if char_1._current_health <= 0 and char_2._current_health <= 0:
            draws += 1
        elif char_2._current_health <= 0:
            char_1_wins += 1
        elif char_1._current_health <= 0:
            char_2_wins += 1

    print(f'The {battles} battles between {char_1.name} and {char_2.name} have concluded.\n\nTotal wins\n\n{char_1.name}:'
          f' {char_1_wins}\n{char_2.name}: {char_2_wins}\nDraws: {draws}')


def main():
    many_battles(100)


main()
