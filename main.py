from flask import Flask
import json
from flask import render_template
from flask import request

app = Flask("Hello World")


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/berechnungen", methods=["GET", "POST"])
def berechnungen():
    return render_template("Berechnungen.html")


@app.route("/berechnungen_addition", methods=["GET", "POST"])
def berechnungen_addition():
    return render_template("Berechnungen_addition.html")


@app.route("/semester_übersicht", methods=["GET", "POST"])
def semester_übersicht():
    return render_template("semester_übersicht.html")


@app.route("/resultat", methods=["GET", "POST"])
def resultat():
    b = open("Speicher_ECTS.json")
    berechnungen_dict = json.load(b)

    if request.method == "POST":
        if request.form.get("submit_button") == "Senden":
            semester = request.form["semester"]

            faecher_bestanden = request.form["fächer_bestanden"]
            absolvierte_ECTS = request.form["absolvierte_ECTS"]
            ECTS_sozial = request.form["ECTS_sozial"]
            ECTS_information = request.form["ECTS_information"]
            ECTS_ux = request.form["ECTS_ux"]
            ECTS_innovation = request.form["ECTS_innovation"]

            berechnungen_dict[semester]["ECTS_information"] = ECTS_information
            berechnungen_dict[semester]["ECTS_innovation"] = ECTS_innovation
            berechnungen_dict[semester]["ECTS_information"] = ECTS_information
            berechnungen_dict[semester]["ECTS_sozial"] = ECTS_sozial
            berechnungen_dict[semester]["ECTS_ux"] = ECTS_ux
            berechnungen_dict[semester]["ECTS_absolviert"] = absolvierte_ECTS
            berechnungen_dict[semester]["semester"] = semester
            berechnungen_dict[semester]["faecher_bestanden"] = faecher_bestanden

            with open("Speicher_ECTS.json", "w") as f:
                json.dump(berechnungen_dict, f, indent=4, separators=(",", ":"), sort_keys=True)
            if berechnungen_dict[semester]["faecher_bestanden"] == "Ja":
                bestanden = "Du hast die Möglichkeit dein Studium im geplanten Zeitraum Abzuschliessen"
            else:
                bestanden = "Du kannst dein Studium nicht im geplanten Zeitraum Abschliessen"

        # with open("ECTS_ux.json", "w") as f:
        #    json.dump(berechnungen_dict, f, indent=4, separators=(",",":"), sort_keys=True)
        #   ux_need = 8-int(ECTS_ux)
        #  ux_maj = 20 - int(ECTS_ux)




    return render_template("Resultat.html", bestanden=bestanden, ux=berechnungen_dict[semester]["ECTS_ux"],
                           insgesamt=berechnungen_dict[semester]["ECTS_absolviert"],
                           it=berechnungen_dict[semester]["ECTS_information"],
                           di=berechnungen_dict[semester]["ECTS_innovation"],
                           sm=berechnungen_dict[semester]["ECTS_sozial"],
                           lel=int(berechnungen_dict[semester]["ECTS_absolviert"]) - (int(berechnungen_dict[semester]["ECTS_ux"])+ int(berechnungen_dict[semester]["ECTS_information"])+int(berechnungen_dict[semester]["ECTS_innovation"])+int(berechnungen_dict[semester]["ECTS_sozial"]))
)



@app.route("/semesteruebersicht", methods=["GET", "POST"])
def semesteruebersicht():
    b = open("Speicher_ECTS.json")
    berechnungen_dict = json.load(b)
    semester_output1 = ()
    for semester in berechnungen_dict:
        semester_output2 = ((berechnungen_dict[semester]["semester"], berechnungen_dict[semester]["ECTS_information"],
                             berechnungen_dict[semester]["ECTS_sozial"], berechnungen_dict[semester]["ECTS_ux"],
                             berechnungen_dict[semester]["ECTS_innovation"],
                             berechnungen_dict[semester]["ECTS_absolviert"]),)
        semester_output1 = semester_output1 + semester_output2
    return render_template("semester_übersicht.html", daten=semester_output1)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
