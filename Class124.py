from flask import Flask, jsonify, request
app=Flask(__name__)
task=[
    {"id":1,
    "title":"you buy groceries",
    "description":"milk, pizza, cheese",
    "done":False},
    {"id":2,
    "title":"you learn python",
    "description":"find a good website",
    "done":False}
]
@app.route("/")
def helloworld():
    return "helloworld"
@app.route("/name")
def name():
    return "naman"
@app.route("/naman/age")
def age():
    return("13")
@app.route("/adddata",methods=["POST"])
def data():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide the data"
        },400)

if __name__=="__main__":
    app.run(debug=True)
