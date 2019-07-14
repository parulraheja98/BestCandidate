from db import db

class PositionModel(db.Model):
    __tablename__ = 'positions'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80))
    jobs = db.Column(db.Integer, db.ForeignKey('jobs.id'), nullable=False)
   
    def __init__(self, name, jobs):
        self.name = name
        self.jobs = jobs

    def json(self):
        return {
            'name': self.name,
            'jobs': self.jobs
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()