from flask import Flask
from flask import render_template


app = Flask(__name__)

hadoop = (
    ('NameNode', 50070),
    ('DataNode', 50075),
    ('Secondary NameNode', 50090),
)

yarn = (
    ('Resource manager', 8088),
)

@app.route('/')
def hello_world():
    #return 'Hello World!'
    return render_template('hello1.html',
                           hadoop=hadoop,
                           yarn=yarn)


if __name__ == '__main__':
    # port: 5000
    app.run(host='0.0.0.0')
