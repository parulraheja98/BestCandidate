from db import db

class ApplicationModel(db.Model):
    __tablename__ = 'applications'

    id = db.Column(db.Integer, primary_key = True)
    job = db.Column(db.Integer, db.ForeignKey('jobs.id'), nullable=False)
    candidate = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
   
    def __init__(self, job, candidate):
        self.job = job
        self.candidate = candidate

    def json(self):
        return {
            'id': self.id,
            'job': self.job,
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
    
    @classmethod
    def find_by_job(cls, job):
        return cls.query.filter_by(job=job)

    @classmethod
    def find_by_job_and_candidate(cls, job, candidate):
        return cls.query.filter_by(job=job,candidate=candidate).first()
    
    @classmethod
    def find_all(cls):
        return cls.query.all()