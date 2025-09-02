from .database import db



# MODELS -------------------------------------------------------------------------
class AnonComments(db.Model) :
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    text = db.Column(db.String(300), nullable = False)