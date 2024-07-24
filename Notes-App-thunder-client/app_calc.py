from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route("/calc/sum/<a>/<b>",methods=["GET"])
def calc_sum(a,b):
    s = int(a) + int(b)
    res = {'sum' : s,'a':a,'b':b}
    return jsonify(res)

@app.route("/calc/square",methods=["POST"])
def calc_square():
    body = request.get_json()
    num = int(body['num'])
    square = num ** 2
    res = {'square' : square,'num':num}
    return jsonify(res)