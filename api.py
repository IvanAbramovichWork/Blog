from app import app, db, mail, cli
from app.models import User, Post
from flask_mail import Message


def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Message': Message,
            'mail': mail}
