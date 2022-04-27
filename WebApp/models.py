from WebApp import db


class User(db.Model):
    fname = db.Column(db.String(16), nullable=False)
    username = db.Column(db.String(16), unique=True, nullable=False, primary_key=True)
    phone = db.Column(db.String(10), nullable=False)

    def __repr__(self) -> str:
        return f"User('{self.fname}', '{self.username}', '{self.phone}')"
