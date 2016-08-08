from app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class GroupMembership(db.Model):
    __tablename__ = 'group_memberships'
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'), primary_key=True)


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    given_name = db.Column(db.String(64), index=True)
    surname = db.Column(db.String(64), index=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    groups = db.relationship('GroupMembership',
                                foreign_keys=[GroupMembership.group_id],
                                backref=db.backref('member', lazy='joined'),
                                lazy='dynamic',
                                cascade='all, delete-orphan')

    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return 'User: {} {}'.format(self.given_name, self.surname)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Group(db.Model):
    __tablename__ = 'groups'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)
    members = db.relationship('GroupMembership',
                                foreign_keys=[GroupMembership.user_id],
                                backref=db.backref('group', lazy='joined'),
                                lazy='dynamic',
                                cascade='all, delete-orphan')



