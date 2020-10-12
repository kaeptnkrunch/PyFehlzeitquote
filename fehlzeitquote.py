# Library import
from datetime import date
                                
# Fehlzeitquotenrechner
print("Willkommen zum Fehlzeitenrechner\n")

# Eigabe
input1 = input("Bitte gebe deine aktuellen Fehlzeiten an: ")
input2 = input("Bitte gebe nun deine aktuellen Arbeitstage an: ")

# Datum
aktuellesDatum = date.today()

# Berechnung
ausgabe = (int(input1))/(int(input2))
ausgabe2 = ausgabe * 100

# Ausgabe
print("Deine aktuelle Fehlzeitquote ist " + (str(ausgabe2)) + " am " + (str(aktuellesDatum)))