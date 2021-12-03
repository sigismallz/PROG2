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
            faecher_bestanden = request.form["fächer_bestanden"]
            semester = request.form["semester"]
            absolvierte_ECTS = request.form["absolvierte_ECTS"]
            ECTS_sozial = request.form["ECTS_sozial"]
            ECTS_information = request.form["ECTS_information"]
            ECTS_ux = request.form["ECTS_ux"]
            ECTS_innovation = request.form["ECTS_innovation"]

            berechnungen_dict["ECTS_information"] = ECTS_information
            berechnungen_dict["ECT_innovation"] = ECTS_innovation
            berechnungen_dict["ECTS_information"] = ECTS_information
            berechnungen_dict["ECTS_sozial"] = ECTS_sozial
            berechnungen_dict["ECTS_ux"] = ECTS_ux
            berechnungen_dict["ECTS_absolviert"] = absolvierte_ECTS
            berechnungen_dict["semester"] = semester
            berechnungen_dict["faecher_bestanden"] = faecher_bestanden


            with open("Speicher_ECTS.json", "w") as f:
                json.dump(berechnungen_dict, f, indent=4, separators=(",",":"), sort_keys=True)
            if berechnungen_dict["faecher_bestanden"] == "Ja":
                bestanden = "Du kannst das Studium normal beenden"
            else:
                bestanden = "Du kannst das Studium nicht beenden"

            with open("ECTS_ux.json", "w") as f:
                json.dump(berechnungen_dict, f, indent=4, separators=(",",":"), sort_keys=True)
                ux_need = 8-int(ECTS_ux)
                ux_maj = 20 - int(ECTS_ux)
    return render_template("Resultat.html", bestanden=bestanden,ux=berechnungen_dict["ECTS_ux"], ux_maj=ux_maj, ux_need=ux_need)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
