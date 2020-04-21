import requests
from flask import Blueprint, render_template, request, redirect, url_for

from application import db
from application.models import Piece

main_bp = Blueprint('main_bp', __name__, template_folder='templates', static_folder='static')


@main_bp.route('/')
def index():
    return render_template('index.html')


@main_bp.route('/a')
def a():
    ok = Piece.query.all()
    return render_template('index.html', ok=ok[0])


@main_bp.route('/ranks')
def ranks():
    return render_template('ranks.html')


@main_bp.route('/fight')
def fight():
    return render_template('fight.html')


@main_bp.route('/init_db')
def init_db():
    try:
        response = requests.get("https://collectionapi.metmuseum.org/public/collection/v1/search?departmentId=11"
                                "&hasImages=true&isHighlight=true&q=french")
        response.raise_for_status()
    except requests.RequestException:
        return None

    allobjectids = response.json()
    ''''
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
    '''
    req = "https://collectionapi.metmuseum.org/public/collection/v1/objects/435641"
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
    db.session.commit()

    return redirect(url_for('main_bp.a'))
