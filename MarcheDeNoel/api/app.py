from flask import Flask, request, make_response, jsonify
from models import Question, Participant, db
import os
from flask_migrate import Migrate

from random import choice, randint
from string import ascii_uppercase, ascii_lowercase
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default_secret_key')

db.init_app(app)
migrate = Migrate(app, db)




# Enregistre un nouveau participant qui démarre le jeu
# None -> None
@app.route('/init', methods=['POST'])
def init():
    cookie_id = ''.join(choice(ascii_uppercase + ascii_lowercase) for _ in range(12))
    participant = Participant(cookie_id=cookie_id, time=datetime.today().strftime('%H%M%S'))
    db.session.add(participant)
    db.session.commit()
    resp = make_response('Participant enregistré', 200)
    resp.set_cookie('cookie_id', cookie_id)
    return resp



# Envoie les questions auxquelles le participant a eu bon
# None -> json{ "questions" : [int] }
@app.route('/', methods=['GET'])
def index(): 

    # Récupération du participant
    cookie_id = request.cookies.get('cookie_id')
    if not cookie_id: 
        return 'Désolé, une erreur est survenue', 400
    participant = db.session.query(Participant).filter(Participant.cookie_id == cookie_id).first()
    if not participant:
        return 'Désolé, une erreur est survenue', 400   
    
    # Envoi des questions
    questions = []
    for i in range(1, 26):
        if participant.__dict__[f'Q{i}'] == 1:
            questions.append(i)
    return { 'questions' : questions } 




# Teste et enregistre les bonnes réponses 
# id, code -> json{ "good_code" : boolean, "all_good" : boolean}
# Premier booléen : si le participant a eu bon à la question
# Second booléen : si le participant a tout bon
@app.route('/submit', methods=['PUT'])
def submit(): 

    # Récupération du participant
    cookie_id = request.cookies.get('cookie_id')
    if not cookie_id: 
        return 'Désolé, une erreur est survenue', 400
    participant = db.session.query(Participant).filter(Participant.cookie_id == cookie_id).first()
    if not participant:
        return 'Désolé, une erreur est survenue', 400   
    
    # Récupération de la question et de la réponse du participant
    question_id = request.args.get('id')
    code = request.args.get('code')
    if not question_id or not code:    
        return 'Désolé, une erreur est survenue', 400
    code = int(code)
    
    # On vérifie qu'il n'a pas déjà eu bon
    if participant.__dict__[f'Q{question_id}'] == 1:
        return {
            "good_code" : True, 
            "all_good" : False
            }
    
    # On vérifie que le code est le bon et on effectue les modifications dans la base de données
    good_code = db.session.query(Question.code).filter(Question.id == question_id).scalar()
    if code == good_code:
        # Mise à jour dans la db
        exec(f"participant.Q{question_id} = 1")
        participant.score += 1
        participant.time = datetime.today().strftime('%H%M%S')
        db.session.commit()
        # Vérification de si le participant a tout bon
        allgood = (participant.score >= 25)    
        return {
            "good_code" : True, 
            "all_good" : allgood
            }
    return {
        "good_code" : False, 
        "all_good" : False
        }




# Une fois que le participant a tout bon, on enregistre ses coordonnées
# name, email -> None
@app.route('/end', methods=['PUT'])
def end():
    cookie_id = request.cookies.get('cookie_id')
    if not cookie_id:    
        return 'Désolé, une erreur est survenue', 400
    participant = db.session.query(Participant).filter(Participant.cookie_id == cookie_id).first()
    if not participant:
        return 'Désolé, une erreur est survenue', 400
    name = request.args.get('name')
    email = request.args.get('email')
    if not name or not email:
        return 'Désolé, une erreur est survenue', 400
    participant.name = name
    participant.email = email
    db.session.commit()
    return 'Données enregistrées', 200




"""
@app.route('/insert', methods=['GET'])
def insert():
    for i in range(1, 26):
        question = Question(id=i,code=randint(1000, 9999))
        db.session.add(question)
        db.session.commit()
    return 'Questions ajoutées', 200
"""




if __name__ == '__main__':
    app.run(debug=True)
