from flask import Flask, render_template, jsonify, request
from flask_socketio import SocketIO, send

from filosofos import Filosofo, main, app, socketio
from peterson import Peterson

import threading

critico_1 = True
critico_2 = False
primera_vez = False
p = Peterson()


@app.route('/')
def index():
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
                return jsonify(critico=1)
            else:
                if p.proceso1_seccion_critica and not p.proceso2_seccion_critica:
                    return jsonify(critico=1)
                elif p.proceso2_seccion_critica and not p.proceso1_seccion_critica:
                    return jsonify(critico=2)
                else:
                    if critico_1:
                        critico_1 = False
                        critico_2 = True
                        return jsonify(critico=1)
                    else:
                        critico_1 = True
                        critico_2 = False
                        return jsonify(critico=2)
    return jsonify(respuesta="ola")


@app.route('/check_chofer')
def chequeo():
    return jsonify("proceso_critico", p.p_f)


@app.route('/filosofos')
def filosofos():
    main(5)
    return render_template("problema.html")

# @socketio.on('message')
# def handleMessage(msg):
#     msg = 'PENSANDO'
#     return send(msg, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)
