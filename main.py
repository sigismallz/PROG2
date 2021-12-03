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
            print(berechnungen_dict)
            with open("Speicher_ECTS.json", "w") as f:
                json.dump(berechnungen_dict, f, indent=4, separators=(",",":"), sort_keys=True)
            hurensohn = "SIGI IST EIN HURENSOHN"
    return render_template("Resultat.html",hurensohn=berechnungen_dict["faecher_bestanden"])


if __name__ == "__main__":
    app.run(debug=True, port=5000)
