from enum import unique
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False) #nullable=False - данное значение обязательно должно быть
    url = db.Column(db.String, unique=True, nullable=False) #unique - уникальность
    published = db.Column(db.DateTime, nullable=False)
    text = db.Column(db.Text, nullable=True) #nullable=True - данное значение НЕ обязательно должно быть

    def __repr__(self) -> str:
        return f'News {self.title}, {self.url}'

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index = True, unique=True)
    password = db.Column(db.String(128))
    role = db.Column(db.String(10), index=True)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @property
    def is_admin(self):
        return self.role == 'admin'

    def __repr__(self) -> str:
        return f'<User {self.username}>'
