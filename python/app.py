from __future__ import print_function

import flask
from flask import Flask
from flask import render_template

from server_info import getYarnApps
from server_info import getHadoopServers
from server_info import getYarnServers


app = Flask(__name__)


@app.route('/')
def server_list():
    hostUrl = flask.request.host
    #hostUrl = '192.168.0.132:5000'

    urlHostPort = hostUrl.split(':')
    url_base = 'http://%s' % urlHostPort[0]

    return render_template('server_list.html',
                           url_base=url_base,
                           hadoop=getHadoopServers(),
                           yarn=getYarnServers(),
                           yarnApps=getYarnApps())


if __name__ == '__main__':
    # port: 5000
    app.run(host='0.0.0.0')
    #server_list()
