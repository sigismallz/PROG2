from flask import Flask
import json
from flask import render_template
from flask import request
import plotly.graph_objects as go

app = Flask("Hello World")


@app.route("/", methods=["GET", "POST"])
def hello_world():
    b = open("Speicher_ECTS.json")
    berechnungen_dict = json.load(b)
    if request.method == "POST":
        # ermöglicht das Zurücksetzen des json Dictionary
        if request.form.get("button_name") == "Resultate Zurücksetzen":
            berechnungen_dict["1"]["ECTS_absolviert"] = "0"
            berechnungen_dict["1"]["ECTS_information"] = "0"
            berechnungen_dict["1"]["ECTS_innovation"] = "0"
            berechnungen_dict["1"]["ECTS_sozial"] = "0"
            berechnungen_dict["1"]["ECTS_ux"] = "0"
            berechnungen_dict["1"]["faecher_bestanden"] = "Ja"

            berechnungen_dict["2"]["ECTS_absolviert"] = "0"
            berechnungen_dict["2"]["ECTS_information"] = "0"
            berechnungen_dict["2"]["ECTS_innovation"] = "0"
            berechnungen_dict["2"]["ECTS_sozial"] = "0"
            berechnungen_dict["2"]["ECTS_ux"] = "0"
            berechnungen_dict["2"]["faecher_bestanden"] = "Ja"

            berechnungen_dict["3"]["ECTS_absolviert"] = "0"
            berechnungen_dict["3"]["ECTS_information"] = "0"
            berechnungen_dict["3"]["ECTS_innovation"] = "0"
            berechnungen_dict["3"]["ECTS_sozial"] = "0"
            berechnungen_dict["3"]["ECTS_ux"] = "0"
            berechnungen_dict["3"]["faecher_bestanden"] = "Ja"

            berechnungen_dict["4"]["ECTS_absolviert"] = "0"
            berechnungen_dict["4"]["ECTS_information"] = "0"
            berechnungen_dict["4"]["ECTS_innovation"] = "0"
            berechnungen_dict["4"]["ECTS_sozial"] = "0"
            berechnungen_dict["4"]["ECTS_ux"] = "0"
            berechnungen_dict["4"]["faecher_bestanden"] = "Ja"

            berechnungen_dict["5"]["ECTS_absolviert"] = "0"
            berechnungen_dict["5"]["ECTS_information"] = "0"
            berechnungen_dict["5"]["ECTS_innovation"] = "0"
            berechnungen_dict["5"]["ECTS_sozial"] = "0"
            berechnungen_dict["5"]["ECTS_ux"] = "0"
            berechnungen_dict["5"]["faecher_bestanden"] = "Ja"

            berechnungen_dict["6"]["ECTS_absolviert"] = "0"
            berechnungen_dict["6"]["ECTS_information"] = "0"
            berechnungen_dict["6"]["ECTS_innovation"] = "0"
            berechnungen_dict["6"]["ECTS_sozial"] = "0"
            berechnungen_dict["6"]["ECTS_ux"] = "0"
            berechnungen_dict["6"]["faecher_bestanden"] = "Ja"

    with open("Speicher_ECTS.json", "w") as f:
        json.dump(berechnungen_dict, f, indent=4, separators=(",", ":"), sort_keys=True)
    return render_template("index.html")


@app.route("/berechnungen", methods=["GET", "POST"])
def berechnungen():
    return render_template("Berechnungen.html")


@app.route("/resultat", methods=["GET", "POST"])
def resultat():
    b = open("Speicher_ECTS.json")
    berechnungen_dict = json.load(b)
    # enfängt die Werte von der HTML Datei und sendet die werte in den json Dictionary
    if request.method == "POST" and request.form.get("submit_button") == "Senden":
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

        # Ab dem 5 Semester ist es nicht mehr möglich das Studium im normalen Zeitraum zu Beenden
        with open("Speicher_ECTS.json", "w") as f:
            json.dump(berechnungen_dict, f, indent=4, separators=(",", ":"), sort_keys=True)
        if berechnungen_dict[semester]["faecher_bestanden"] != "Nein":
            bestanden = "Du hast die Möglichkeit dein Studium im geplanten Zeitraum Abzuschliessen"
        elif int(berechnungen_dict[semester]["semester"]) < int(5):
            bestanden = "Du hast die Möglichkeit dein Studium im geplanten Zeitraum Abzuschliessen"
        else:
            bestanden = "Du kannst dein Studium nicht im geplanten Zeitraum Abschliessen"

    return render_template("Resultat.html", bestanden=bestanden, ux=berechnungen_dict[semester]["ECTS_ux"],
                           insgesamt=berechnungen_dict[semester]["ECTS_absolviert"],
                           it=berechnungen_dict[semester]["ECTS_information"],
                           di=berechnungen_dict[semester]["ECTS_innovation"],
                           sm=berechnungen_dict[semester]["ECTS_sozial"],
                           lel=int(berechnungen_dict[semester]["ECTS_absolviert"]) - (
                                   int(berechnungen_dict[semester]["ECTS_ux"]) + int(
                               berechnungen_dict[semester]["ECTS_information"]) + int(
                               berechnungen_dict[semester]["ECTS_innovation"]) + int(
                               berechnungen_dict[semester]["ECTS_sozial"]))
                           )


@app.route("/semesteruebersicht", methods=["GET", "POST"])
def semesteruebersicht():
    b = open("Speicher_ECTS.json")
    berechnungen_dict = json.load(b)
    semester_output1 = ()
    # Berechnungen für die Übersicht
    it = int(20) - (
            int(berechnungen_dict["1"]["ECTS_information"]) + int(berechnungen_dict["2"]["ECTS_information"]) + int(
        berechnungen_dict["3"]["ECTS_information"]) + int(berechnungen_dict["4"]["ECTS_information"]) + int(
        berechnungen_dict["5"]["ECTS_information"]) + int(berechnungen_dict["6"]["ECTS_information"]))
    if it < 0:
        it = 0
    di = int(20) - (
            int(berechnungen_dict["1"]["ECTS_innovation"]) + int(berechnungen_dict["2"]["ECTS_innovation"]) + int(
        berechnungen_dict["3"]["ECTS_innovation"]) + int(berechnungen_dict["4"]["ECTS_innovation"]) + int(
        berechnungen_dict["5"]["ECTS_innovation"]) + int(berechnungen_dict["6"]["ECTS_innovation"]))
    if di < 0:
        di = 0
    ux = int(20) - (int(berechnungen_dict["1"]["ECTS_ux"]) + int(berechnungen_dict["2"]["ECTS_ux"]) + int(
        berechnungen_dict["3"]["ECTS_ux"]) + int(berechnungen_dict["4"]["ECTS_ux"]) + int(
        berechnungen_dict["5"]["ECTS_ux"]) + int(berechnungen_dict["6"]["ECTS_ux"]))
    if ux < 0:
        ux = 0

    it_1 = int(8) - (
            int(berechnungen_dict["1"]["ECTS_information"]) + int(berechnungen_dict["2"]["ECTS_information"]) + int(
        berechnungen_dict["3"]["ECTS_information"]) + int(berechnungen_dict["4"]["ECTS_information"]) + int(
        berechnungen_dict["5"]["ECTS_information"]) + int(berechnungen_dict["6"]["ECTS_information"]))
    if it_1 < 0:
        it_1 = 0
    di_1 = int(8) - (
            int(berechnungen_dict["1"]["ECTS_innovation"]) + int(berechnungen_dict["2"]["ECTS_innovation"]) + int(
        berechnungen_dict["3"]["ECTS_innovation"]) + int(berechnungen_dict["4"]["ECTS_innovation"]) + int(
        berechnungen_dict["5"]["ECTS_innovation"]) + int(berechnungen_dict["6"]["ECTS_innovation"]))
    if di_1 < 0:
        di_1 = 0
    ux_1 = int(8) - (int(berechnungen_dict["1"]["ECTS_ux"]) + int(berechnungen_dict["2"]["ECTS_ux"]) + int(
        berechnungen_dict["3"]["ECTS_ux"]) + int(berechnungen_dict["4"]["ECTS_ux"]) + int(
        berechnungen_dict["5"]["ECTS_ux"]) + int(berechnungen_dict["6"]["ECTS_ux"]))
    if ux_1 < 0:
        ux_1 = 0
    sz = int(4) - (int(berechnungen_dict["1"]["ECTS_sozial"]) + int(berechnungen_dict["2"]["ECTS_sozial"]) + int(
        berechnungen_dict["3"]["ECTS_sozial"]) + int(berechnungen_dict["4"]["ECTS_sozial"]) + int(
        berechnungen_dict["5"]["ECTS_sozial"]) + int(berechnungen_dict["6"]["ECTS_sozial"]))
    if sz < 0:
        sz = 0

    # Methode zur generierung der Daten für die Tabelle
    for semester in berechnungen_dict:
        semester_output2 = ((berechnungen_dict[semester]["semester"], berechnungen_dict[semester]["ECTS_information"],
                             berechnungen_dict[semester]["ECTS_sozial"], berechnungen_dict[semester]["ECTS_ux"],
                             berechnungen_dict[semester]["ECTS_innovation"],
                             berechnungen_dict[semester]["ECTS_absolviert"]),)
        semester_output1 = semester_output1 + semester_output2
    return render_template("semester_übersicht.html", daten=semester_output1,
                           insgesamt=int(180) - (int(berechnungen_dict["1"]["ECTS_absolviert"]) + int(
                               berechnungen_dict["2"]["ECTS_absolviert"]) + int(
                               berechnungen_dict["3"]["ECTS_absolviert"]) + int(
                               berechnungen_dict["4"]["ECTS_absolviert"]) + int(
                               berechnungen_dict["5"]["ECTS_absolviert"]) + int(
                               berechnungen_dict["6"]["ECTS_absolviert"])),
                           it=it,
                           di=di,
                           ux=ux,
                           it_1=it_1,
                           di_1=di_1,
                           ux_1=ux_1,
                           sz=sz,
                           )


@app.route("/plotly", methods=["GET", "POST"])
def plotly():
    # Datenvisualiesierung mit Ploty
    b = open("Speicher_ECTS.json")
    berechnungen_dict = json.load(b)

    graph = go.Figure(data=go.Bar(
        x=[1, 2, 3, 4, 5, 6],
        y=[int(berechnungen_dict["1"]["ECTS_absolviert"]), int(berechnungen_dict["2"]["ECTS_absolviert"]),
           int(berechnungen_dict["3"]["ECTS_absolviert"]), int(berechnungen_dict["4"]["ECTS_absolviert"]),
           int(berechnungen_dict["5"]["ECTS_absolviert"]), int(berechnungen_dict["6"]["ECTS_absolviert"])]
    ),
        layout=go.Layout(
            title=go.layout.Title(text="Visualisierung der absolvierten ECTS")
        )
    )
    graph.write_html("templates/Plotly.html", auto_open=False)

    return render_template("Plotly.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
