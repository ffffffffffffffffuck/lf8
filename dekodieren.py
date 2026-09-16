kodierterstring = input("Geben Sie den String ein:")
eingabeverschoben = input(
    "Geben Sie die Anzahl ein, um wieviel der Kodierte String verschoben wurde."
)

text = kodierterstring.lower()
step = int(eingabeverschoben)
text_neu = ""


for buchstabe in text:
    if buchstabe.isalpha():
        stelle = ord(buchstabe)
        stelle_neu = (stelle - step - 97) % 26 + 97
        buchstabe = chr(stelle_neu)
    text_neu = text_neu + buchstabe

print(text_neu)
