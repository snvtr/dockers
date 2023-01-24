from flask import Response
from app import app, db
from app.models import Greetings
from random import randrange


@app.route('/')
def index():
    x = Greetings.query.get(randrange(1,10))
    return Response(','.join([str(x.id), x.adj, x.noun]), mimetype='text/plain')