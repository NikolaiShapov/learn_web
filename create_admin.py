from getpass import getpass
import sys
from webapp import create_app
from webapp.db import db
from webapp.news.models import User

app = create_app()

with app.app_context():
    username = input('name:')

    if User.query.filter(User.username == username).count():
        print('Erro user ')
        sys.exit()

    password1 = getpass('Password:')
    password2 = getpass('Password:')

    if not password1 == password2:
        print('Erro pass')
        sys.exit()

    new_user = User(username = username, role='admin')
    new_user.set_password(password1)

    db.session.add(new_user)
    db.session.commit()
    print('Add user and password')
