from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False) #nullable=False - данное значение обязательно должно быть
    url = db.Column(db.String, unique=True, nullable=False) #unique - уникальность
    published = db.Column(db.DateTime, nullable=False)
    text = db.Column(db.Text, nullable=True) #nullable=True - данное значение НЕ обязательно должно быть

    def __repr__(self) -> str:
        return f'News {self.title}, {self.url}'
