from db import db

class RecruiterModel(db.Model):
    __tablename__ = 'recruiter'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    name = db.Column(db.String(80))
    title = db.Column(db.String(80))
    company = db.Column(db.String(80))
    job = db.relationship('JobModel', backref='recruitermodel', lazy=True)


    def __init__(self, username, password, name, title, company):
        self.username = username
        self.password = password
        self.name = name
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

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username = username).first()
