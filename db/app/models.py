from app import app, db

class Greetings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    adj  = db.Column(db.String(30), index=True, unique=True)
    noun = db.Column(db.String(30), index=True, unique=True)

    def __repr__(self):
        return '<Greeting: {} {}>'.format(self.adj, self.noun)