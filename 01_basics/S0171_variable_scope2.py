"""
Opgave "Variable Scope 2":

Hvis du har en funktion, der kalder en anden funktion, og den kaldte funktion skal bruge variabler fra den kaldende funktion, så er det bedst, hvis du sender disse variabler som parametre.

Kør programmet og find ud af, hvad der skete.
Hvorfor fremkalder print(x) forskellige resultater?
Læs kommentarerne i koden.
"""

def some_function():
  x = "This is a local variable inside the function some_function"  # x is local here and shadows the global variable x in outer scope
  print(x)
  another_function(x)


def another_function(x):
  print(x)  # uses the parameter x


def main():
  x = "This is a local variable inside the function main"
  some_function()
  another_function(x)
  print(x)


main()  # det er god programmeringsskik, at undgå globale variabler og at hovedprogrammet bare indeholderen en enkel linje, som kalder funktionen main.

# Q: 'Hvorfor fremkalder print(x) forskellige resultater?'
# A: Den første, some_function(), giver et andet output, da den bruger sin lokale værdi for x. De to andre bruger værdien for x i main, da andet ikke er specificeret
# i another_function(x), og print(x) printer bare værdien af x i funktionen, altså main(). Jeg har tilføjet another_function(x) i funktionen some_function(), og den
# bruger nu værdien af x i some_function() i stedet for main().