from . import db


class Piece(db.Model):
    __tablename__ = "piece"

    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String, nullable=False)
    linkImage = db.Column(db.String, nullable=False)
    autheur = db.Column(db.String, nullable=False)
    date = db.Column(db.String, nullable=False)
    elo = db.Column(db.Integer, nullable=False, default=1500)

    def __repr__(self):
        return self.nom