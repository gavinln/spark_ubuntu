from flask import Flask
from flask import render_template
import flask

from yarn_api_client.resource_manager import ResourceManager
import urllib
from collections import namedtuple


app = Flask(__name__)

hadoop = (
    ('NameNode', 50070),
    ('DataNode', 50075),
    ('Secondary NameNode', 50090),
)

yarn = (
    ('Resource manager', 8088),
)


class ServerInfo(object):
    @classmethod
    def initialize(cls, serverData):
        return cls(serverData[0], serverData[1], None)

    def __init__(self, server, port, status):
        self.name = server
        self.port = port
        try:
            code = urllib.urlopen("http://127.0.0.1:%s" % self.port).getcode()
            if code == 200:
                self.status = True
            else:
                self.status = False
        except:
            self.status = False

    def __str__(self):
        names = ['name', 'port', 'status']
        values = [self.name, self.port, self.status]
        return ', '.join('%s: %s' % (
            name, value) for name, value in zip(names, values))


class ServerList(list):
    @classmethod
    def initialize(cls, serverData):
        servers = cls()
        for server in serverData:
            servers.append(ServerInfo.initialize(server))
        return servers

    def __str__(self):
        return '\n'.join(str(server) for server in self)


def getClusterInfo():
    rm = ResourceManager(address='localhost', port=8088)
    data = rm.cluster_information().data
    return data.get('clusterInfo', None)

YarnApp = namedtuple('YarnAppInfo', ['id', 'trackingUrl', 'state'])


def getYarnApps():
    yarnApps = []
    rm = ResourceManager(address='localhost', port=8088)
    data = rm.cluster_applications().data
    apps = data.get('apps', None)
    if apps:
        appList = apps.get('app', None)
        if appList:
            for app in appList:
                yarnApps.append(YarnApp._make((
                    app['id'],
                    app['trackingUrl'],
                    app['state'])))
    return yarnApps


@app.route('/')
def server_list():
    urlHostPort = flask.request.host.split(':')
    url_base = 'http://%s' % urlHostPort[0]

    hadoopList = ServerList.initialize(hadoop)
    yarnList = ServerList.initialize(yarn)
    yarnApps = getYarnApps()
    return render_template('server_list.html',
                           url_base=url_base,
                           hadoop=hadoopList,
                           yarn=yarnList,
                           yarnApps=yarnApps)


if __name__ == '__main__':
    # port: 5000
    app.run(host='0.0.0.0')
