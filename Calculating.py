gewicht = float(input("Wieviel wiegst Du? (in kg): "))
groeße = float(input("Wie groß bist Du? (in m z.B. 1.70): "))

bmi = gewicht / (groeße ** 2)

# Funktion für Berechnung BMI
def bmi_kategorie(bmi):
    if bmi < 18.5:
        return "Untergwicht"

    elif 18.5 <= bmi < 24.9:
        return "Normalgewicht"

    elif 25 <= bmi < 29.9:
        return "Übergewicht"
    else:
        return "ERROR ERROR ERROR"

# Ausgabe der berechneten Werte
print("Dein BMI beträgt: ", round(bmi, 2))
print("Deine BMI-Kategorie ist: ", bmi_kategorie(bmi))