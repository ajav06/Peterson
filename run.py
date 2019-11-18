from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("algoritmo.html")

@app.route('/_peterson')
def peterson():
    return jsonify(respuesta="ola")

