from flask import Flask
from flask import render_template

import urllib


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
        code = urllib.urlopen("http://127.0.0.1:%s" % self.port).getcode()
        if code == 200:
            self.status = True
        else:
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


@app.route('/')
def hello_world():
    #return 'Hello World!'
    hadoopList = ServerList.initialize(hadoop)
    return render_template('hello1.html',
                           hadoop=hadoopList,
                           yarn=yarn)


if __name__ == '__main__':
    # port: 5000
    app.run(host='0.0.0.0')
    #hello_world()
