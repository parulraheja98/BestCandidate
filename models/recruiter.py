from db import db

class RecruiterModel(db.Model):
    __tablename__ = 'recruiter'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(80))
    company = db.Column(db.String(80))
    job = db.relationship('JobModel', backref='jobmodel', lazy=True)


    def __init__(self, title, company):
        self.title = title
        self.company = company

    def json(self):
        return {
            'title': self.title,
            'company': self.company
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id = _id).first()
