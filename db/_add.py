from app import app, db
from app.models import Greetings

g = Greetings(adj='yellow', noun='snow')
db.session.add(g)
db.session.commit()

g = Greetings(adj='orange', noun='pillow')
db.session.add(g)
db.session.commit()

g = Greetings(adj='pink', noun='elephant')
db.session.add(g)
db.session.commit()

g = Greetings(adj='red', noun='carpet')
db.session.add(g)
db.session.commit()

g = Greetings(adj='green', noun='lantern')
db.session.add(g)
db.session.commit()

g = Greetings(adj='blue', noun='icechips')
db.session.add(g)
db.session.commit()

g = Greetings(adj='brown', noun='bear')
db.session.add(g)
db.session.commit()

g = Greetings(adj='gray', noun='wolf')
db.session.add(g)
db.session.commit()

g = Greetings(adj='black', noun='cloak')
db.session.add(g)
db.session.commit()
