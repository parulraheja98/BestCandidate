from db import db
from models.application import ApplicationModel

class JobModel(db.Model):
    __tablename__ = 'jobs'

    id = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.String(80))
    posted_by = db.Column(db.String(80))
    position = db.relationship('ApplicationModel', backref='jobmodel', lazy=True)


    def __init__(self, description, posted_by):
        self.description = description
        self.posted_by = posted_by

    def json(self):
        return {
            'description': self.description,
            'posted_by': self.posted_by
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id = _id).first()
