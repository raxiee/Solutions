"""
Opgave "Mere tips&tricks til pycharm":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe og løs opgaven dér.


1) Debugger:
Se denne video: https://youtu.be/j0Wz_uBaDmo?si=pSeDspIym1BIBHeB&t=61
Brug debuggeren med eksempelkoden nedenfor.
    Sæt fx et breakpoint i begyndelsen af for-løkken og klik på billen for at starte programmet i debuggertilstand.
    Tryk på F8 eller F7 flere gange og se hvad der sker efter hvert enkelt trin.
    Hvad er forskellen mellem F8 og F7?
    Hvis man for eksempel er ved noget kode, der kalder en anden funktion, og man bruger step into (F7), vil man gå direkte til den funktion, der bliver kaldt og se,
    hvad den gør trin for trin, hvorimod step over (F8) vil springe trin inde i selve den kaldte funktion over.


2) Refactoring:
Se denne video: https://www.youtube.com/watch?v=4kzEbqaT2DY&t=56s
Ændr eksempelkoden nedenfor ved at refaktorisere.
    Ændr fx funktionens navn fra eksempel til ny_eksempel.
    Skift fx navnet på funktionsparameteren fra number til some_number.
    Tilføj en anden parameter til funktionen.

3) Shortcuts
Vend tilbage til S0105_pycharm_tips.py og prøv nogle shortcuts i eksempelkoden nedenfor.

"""

# Den følgende kode tjener som legeplads for de ovenstående opgaver.

def ny_eksempel(some_number, anden_parameter):
    res_xxxx_ult = 0
    for n in range(some_number, 2 * some_number, 3):
        res_xxxx_ult += n
    res_xxxx_ult *= 10
    return res_xxxx_ult


print("Start")
print(ny_eksempel(4, 123))
print(ny_eksempel(7, 123))
print("End")
