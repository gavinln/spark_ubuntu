from __future__ import print_function

from gevent import monkey
monkey.patch_all()

from threading import Thread
import time

import flask
from flask import Flask
from flask import render_template
from flask.ext.socketio import SocketIO, emit

from server_info import getYarnApps
from server_info import getHadoopServers
from server_info import getYarnServers


thread = None
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'


def background_thread():
    count = 0
    #while True:
    #    time.sleep(2)
    #    count += 1
    #    socketio.emit(
    #        'elapsedTime', {'id': 'app_id', 'count': count})

def createSocketIO(app):
    global thread
    thread = Thread(target=background_thread)
    thread.start()
    return SocketIO(app)


socketio = SocketIO(app)


@app.route('/')
def server_list():
    hostUrl = flask.request.host
    ##hostUrl = '192.168.0.132:5000'

    urlHostPort = hostUrl.split(':')
    url_base = 'http://%s' % urlHostPort[0]

    return render_template('server_list.html',
                           url_base=url_base,
                           hadoop=getHadoopServers(),
                           yarn=getYarnServers(),
                           yarnApps=getYarnApps())


@socketio.on('my event', namespace='/test')
def test_message(message):
    emit('my response',
         {'data': 'a', 'count': 1})


if __name__ == '__main__':
    # port: 5000
    #app.run(host='0.0.0.0')
    socketio.run(app, host='0.0.0.0')
