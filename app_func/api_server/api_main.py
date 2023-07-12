import logging

from flask import Flask
from gevent import pywsgi

from api_list import bp as api_bp

app = Flask(__name__)

log = logging.getLogger()

LISTEN_PORT = 22999


def create_server():
    global app
    app.url_map.strict_slashes = False  # 这样可以把“http://xxx/”当作“http://xxx”接受
    app.register_blueprint(api_bp)
    return app, pywsgi.WSGIServer(("0.0.0.0", LISTEN_PORT), app, log=log)  # WSGIServer可以为每个请求创建一个新实例


if __name__ == "__main__":
    app, server = create_server()
    server.serve_forever()
