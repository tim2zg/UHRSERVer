import flask
import datetime
import time

app = flask.Flask(__name__)
on = True


@app.route('/get')
def index():
    time2 = datetime.datetime.now()
    if on:
        resp = flask.Response(time2.strftime("%H:%M"))
    else:
        resp = flask.Response("off")
    return resp


@app.route('/get/on')
def on():
    global on
    on = True
    resp = flask.Response("on")
    return resp


@app.route('/get/off')
def off():
    global on
    on = False
    resp = flask.Response("off")
    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=60009)
    flask.session.clear()