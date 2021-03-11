from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    teamid = db.Column(db.Integer, db.ForeignKey("team.id"))
    
class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bez = db.Column(db.String(64), index=True, unique=True)
    user = db.relationship("User", backref="team", lazy="dynamic")