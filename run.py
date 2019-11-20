from flask import Flask, render_template, jsonify, request
from peterson import Peterson
import threading
app = Flask(__name__)
critico_1 = True
critico_2 = False
primera_vez = False
p = Peterson()

@app.route('/')
def index():
    print("ruta")
    return render_template("algoritmo.html")

@app.route('/_peterson')
def peterson():
    print("peterson")
    if request:
        if request.method == 'GET':
            global critico_1, critico_2, primera_vez, p
            if not primera_vez:
                t = threading.Thread(target=p.main())
                t.start()
                primera_vez = True
                return jsonify(critico = 1)
            else:
                if p.proceso1_seccion_critica and not p.proceso2_seccion_critica:
                    return jsonify(critico = 1)
                elif p.proceso2_seccion_critica and not p.proceso1_seccion_critica:
                    return jsonify(critico = 2)
                else:
                    if critico_1:
                        critico_1 = False
                        critico_2 = True
                        return jsonify(critico = 1)
                    else:
                        critico_1 = True
                        critico_2 = False
                        return jsonify(critico = 2)
    return jsonify(respuesta="ola")

@app.route('/check_chofer')
def chequeo():
    return jsonify("proceso_critico",p.p_f)