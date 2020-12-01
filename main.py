from flask import Flask, render_template, request, redirect
import requests
import json
app=Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html")

student_info = {}
@app.route("/form", methods=["POST", "GET"])
def form():
    if request.method == "POST":
        student_info["name"]=request.form.get("name")
        student_info["year"]=request.form.get("year")
        student_info["major"]=request.form.get("major")
        return redirect(request.url)
    return render_template("form.html")

@app.route("/recommendations", methods=["POST", "GET"])
def recommendations():

    data_from_api=requests.get('https://berkeleytime.com/api/catalog/catalog_json/')
    courses=json.loads(data_from_api.content)
    classes_to_take=[]
    for course in courses["courses"]:
        if course["abbreviation"]==student_info["major"]:
            classes_to_take.append(course)

    return render_template("classes.html", data=classes_to_take)



@app.route("/resources", methods=["GET"])
def resources():
    return render_template("resources.html")

if __name__ == "__main__":
    app.run(port=5000, debug=True)
