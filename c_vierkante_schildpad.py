# Schrijf een programma dat een vierkant tekent met de turtle - module.
# - import turtle
# - maak een functie teken_lijn(lengte)
# - maak een functie draai_rechts(graden)
# - maak een functie teken_vierkant()
#     - gebruik een lus om vier zijdes te tekenen
# - gebruik turtle.done() zodat je jouw tekening kan zien.

import turtle
for _ in range(4):
    turtle.forward(100)
    turtle.right(90)
    var = turtle.done
