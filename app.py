from flask import Flask, request, render_template
import csv
import os

app = Flask(__name__)

@app.route("/")
def form():
    return '''
        <form method="POST" action="/submit">
            Nama: <input name="nama"><br>
            <input type="submit">
        </form>
    '''


@app.route("/submit", methods=["POST"])
def submit():
    nama = request.form["nama"]
    with open("data.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([nama])
    return f"Halo, {nama}!"


app.run(debug=True)
