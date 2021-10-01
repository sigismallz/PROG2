
Studium = input("Hast du alle Fächer bestanden? Ja/Nein")
if Studium == ("Nein"):
    Studium = 1

if Studium == 1:
    semester = int(input("in welchem semester bist du?"))
    if semester >= 4:
        print("Das Studium kann nicht in der Vorgeschriebenen Zeit beendet werden")
    else:
        print("Studium kann normal votgesetzt werden, das Fach kan nächstes Jahr wiederholt werden")




ECTS_main = int(60)
ECTS_ux = int(0)
ECTS_inovation = int(4)
ECTS_information = int(4)
ECTS_sozial = int(2)
ECTS_main = ECTS_main + ECTS_ux + ECTS_inovation + ECTS_information + ECTS_sozial

if ECTS_main < int(180):
    main_ausgabe = (180 - ECTS_main)
    print("Dir Fehlen noch ", main_ausgabe , "ECTS")
else:
    print("Gartuliere du hast dein Studium beendet")



