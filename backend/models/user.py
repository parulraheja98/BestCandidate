from db import db


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    role = db.Column(db.String(80))
    application = db.relationship('ApplicationModel', backref='usermodel', lazy=True) 

    def __init__(self, firstname, lastname, username, password, role):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password
        self.role = role

    def json(self):
        return {
            'id': self.id,
            'username': self.username,
            'role': self.role,
            'firstname': self.firstname,
            'lastname': self.lastname
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()
    @classmethod
    def find_by_role(cls, role):
        return cls.query.filter_by(role=role)

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

