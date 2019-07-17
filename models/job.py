from db import db
from sqlalchemy import DateTime
from models.application import ApplicationModel

class JobModel(db.Model):
    __tablename__ = 'jobs'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(80))
    description = db.Column(db.String(80))
    posted_by = db.Column(db.Integer, db.ForeignKey('recruiters.id'), nullable=False)
    status = db.Column(db.String(80))
    date_posted = db.Column(DateTime)
    deadline = db.Column(DateTime)
    
    
    position = db.relationship('ApplicationModel', backref='jobmodel', lazy=True)


    def __init__(self, title, description, posted_by, status, date_posted, deadline):
        self.title = title
        self.description = description
        self.posted_by = posted_by
        self.status = status
        self.date_posted = date_posted
        self.deadline = deadline

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
