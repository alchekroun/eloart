import requests
from ..helpElo import newelo
from flask import Blueprint, render_template, request, redirect, url_for
from sqlalchemy.sql.expression import func

from application import db
from application.models import Piece

main_bp = Blueprint('main_bp', __name__, template_folder='templates', static_folder='static')


@main_bp.route('/')
def index():
    return render_template('index.html')


@main_bp.route('/ranks/')
def ranks():
    allrank = Piece.query.order_by(Piece.elo.desc())

    return render_template('ranks.html', allrank=allrank)


@main_bp.route('/about/')
def about():
    return render_template('about.html')


@main_bp.route('/score/<idPiece1>/<idPiece2>/', methods=['PUT'])
def score(idPiece1, idPiece2):
    winner = Piece.query.get(idPiece1)
    loser = Piece.query.get(idPiece2)
    winner.elo = newelo(winner.elo, loser.elo, 1)
    loser.elo = newelo(loser.elo, winner.elo, 0)
    db.session.commit()
    return redirect(url_for('main_bp.fight'))


@main_bp.route('/piece/<idPiece>')
def showpiece(idPiece):
    piece = Piece.query.get(idPiece)
    if piece:
        return render_template('oeuvre.html', piece=piece)
    return render_template('error.html')


@main_bp.route('/init_db/')
def init_db():
    """
    try:
        response = requests.get("https://collectionapi.metmuseum.org/public/collection/v1/search?departmentId=11"
                                "&hasImages=true&isHighlight=true&q=french")
        response.raise_for_status()
    except requests.RequestException:
        return redirect(url_for('main_bp.error'))

    allobjectids = response.json()

    for piece in allobjectids["objectIDs"]:
        req = "https://collectionapi.metmuseum.org/public/collection/v1/objects/" + str(piece)
        reqON = requests.get(req)
        pieceJson = reqON.json()
        id = pieceJson["objectID"]
        nom = pieceJson["title"]
        linkImage = pieceJson["primaryImage"]
        autheur = pieceJson["artistDisplayName"]
        date = pieceJson["objectDate"]
        pieceDBtoAdd = Piece(id=id, nom=nom, linkImage=linkImage, autheur=autheur, date=date)
        db.session.add(pieceDBtoAdd)
        print('ok')
    """
    req = "https://collectionapi.metmuseum.org/public/collection/v1/objects/438822"
    reqON = requests.get(req)
    pieceJson = reqON.json()
    id = pieceJson["objectID"]
    nom = pieceJson["title"]
    linkImage = pieceJson["primaryImage"]
    autheur = pieceJson["artistDisplayName"]
    date = pieceJson["objectDate"]
    wikiAutheur = pieceJson["artistWikidata_URL"]
    pieceDBtoAdd = Piece(id=id, nom=nom, linkImage=linkImage, autheur=autheur, date=date, wikiAutheur=wikiAutheur)
    db.session.add(pieceDBtoAdd)
    print('ok')
    db.session.commit()

    return redirect(url_for('main_bp.index'))


@main_bp.route('/error/')
def error():
    return render_template('error.html')
