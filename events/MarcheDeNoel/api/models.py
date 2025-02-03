from sqlalchemy.orm import declarative_base
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
Base = declarative_base()
db = SQLAlchemy(model_class=Base)

class Participant(Base):
    __tablename__ = 'participants'
    cookie_id = Column(String(255), primary_key=True)
    Q1 = Column(Integer, nullable=False, default=0)
    Q2 = Column(Integer, nullable=False, default=0)
    Q3 = Column(Integer, nullable=False, default=0)
    Q4 = Column(Integer, nullable=False, default=0)
    Q5 = Column(Integer, nullable=False, default=0)
    Q6 = Column(Integer, nullable=False, default=0)
    Q7 = Column(Integer, nullable=False, default=0)
    Q8 = Column(Integer, nullable=False, default=0)
    Q9 = Column(Integer, nullable=False, default=0)
    Q10 = Column(Integer, nullable=False, default=0)
    Q11 = Column(Integer, nullable=False, default=0)
    Q12 = Column(Integer, nullable=False, default=0)
    Q13 = Column(Integer, nullable=False, default=0)
    Q14 = Column(Integer, nullable=False, default=0)
    Q15 = Column(Integer, nullable=False, default=0)
    Q16 = Column(Integer, nullable=False, default=0)
    Q17 = Column(Integer, nullable=False, default=0)
    Q18 = Column(Integer, nullable=False, default=0)
    Q19 = Column(Integer, nullable=False, default=0)
    Q20 = Column(Integer, nullable=False, default=0)
    Q21 = Column(Integer, nullable=False, default=0)
    Q22 = Column(Integer, nullable=False, default=0)
    Q23 = Column(Integer, nullable=False, default=0)
    Q24 = Column(Integer, nullable=False, default=0)
    Q25 = Column(Integer, nullable=False, default=0)    
    score = Column(Integer, nullable=False, default=0)
    time = Column(Integer, nullable=False)
    name = Column(String(255), nullable=False, default='name')
    email = Column(String(255), nullable=False, default='email')

class Question(Base):
    __tablename__ = 'questions'
    # id de la question
    id = Column(Integer, primary_key=True)
    # code réponse à récupérer sur le stand
    code = Column(Integer, nullable=False)

