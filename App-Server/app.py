from flask import Flask
from controllers.routes import server

baseurl = '/scanner'


app = Flask(__name__)

app.register_blueprint(server)

qwe = "hrl"


if __name__ == "__main__":
    app.run(debug=True)