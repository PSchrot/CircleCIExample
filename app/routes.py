from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.models import *

@app.route('/')
@app.route('/startseite', methods=["GET", "POST"])
def index():
    
    return render_template("startseite.html", title="startseite")

@app.route('/edituser/<int:id>', methods=["GET", "POST"])
def edituser(id):
    
    teams = Team.query.all()
    user = User.query.filter_by(id=id).first()
    return render_template("edituser.html", title="edituser", user=user, 
                           id=id, teams=teams)

@app.route('/benutzeransicht', methods=["GET", "POST"])
def benutzeransicht():
    
    user = User.query.all()
    return render_template("benutzeransicht.html", title="benutzeransicht",
                           user=user)

@app.route('/deleteuser/<int:id>', methods=['GET', 'POST'])
def deleteuser(id):
    
    user = User.query.filter_by(id = id).first()
    
    db.session.delete(user)
    db.session.commit()
        
    return redirect(url_for('benutzeransicht'))








