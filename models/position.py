from db import db

class PositionModel(db.Model):
    __tablename__ = 'positions'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80))
    jobs = db.Column(db.Integer, db.ForeignKey('jobs.id'), nullable=False)
    candidate = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
   
    def __init__(self, name, jobs, candidate):
        self.name = name
        self.jobs = jobs
        self.candidate = candidate

    def json(self):
        return {
            'name': self.name,
            'jobs': self.jobs,
            'candidate': self.candidate
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
    
    @classmethod
    def find_by_candidate(cls, candidate):
        return cls.query.filter_by(candidate=candidate)