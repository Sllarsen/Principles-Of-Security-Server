from flask import Blueprint
#set up the blueprints
server = Blueprint('server', __name__)
from app import baseurl 

@server.route(baseurl + '/', methods=['GET'])
@server.route(baseurl + '/helloworld', methods=['GET'])
def helloWorld():
    return "Hello World!!!"




