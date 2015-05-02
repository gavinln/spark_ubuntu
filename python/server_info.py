from __future__ import print_function

import urllib
from collections import namedtuple

from yarn_api_client.resource_manager import ResourceManager

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


YarnApp = namedtuple('YarnAppInfo', ['id', 'name', 'port_path', 'state',
                                     'elapsedTime'])


def getYarnApplicationsData(resourceManager):
    try:
        apps = resourceManager.cluster_applications()
    except Exception:
        return None
    return apps.data


def getAppElapsedTime():
    appTimes = []
    rm = ResourceManager(address='localhost', port=8088)
    data = getYarnApplicationsData(rm)
    if data:
        try:
            apps = data['apps']
            if apps:
                appList = apps['app']
                for app in appList:
                    appTimes.append((
                        app['id'],
                        app['elapsedTime']))
        except KeyError:
            pass

    return appTimes


def getYarnApps():
    yarnApps = []
    rm = ResourceManager(address='localhost', port=8088)
    data = getYarnApplicationsData(rm)
    if data:
        try:
            apps = data['apps']
            if apps:
                appList = apps['app']
                for app in appList:
                    url = app['trackingUrl']
                    port_path = url.split(':')[2]
                    yarnApps.append(YarnApp._make((
                        app['id'],
                        app['name'],
                        port_path,
                        app['state'],
                        app['elapsedTime'])))
        except KeyError:
            pass

    return yarnApps


def getHadoopServers():
    return ServerList.initialize(hadoop)


def getYarnServers():
    return ServerList.initialize(yarn)


def test_hadoopServers():
    print(getHadoopServers())
    assert True


def test_yarnServers():
    print(getYarnServers())
    assert True


def test_yarnApps():
    print(getYarnApps())
    assert False


if __name__ == '__main__':
    getYarnApps()
