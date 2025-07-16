#!/usr/bin/env python3
"""
Schnelle Reparatur - Minimale Version des Klassenbuch-Systems
"""

from flask import Flask, render_template, request, redirect, url_for, jsonify, abort, send_file, session, flash
import datetime
import json
import os
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from collections import defaultdict
from flask_moment import Moment
from flask_migrate import Migrate
from sqlalchemy import func

# App erstellen
app = Flask(__name__)
app.secret_key = 'dein_geheimer_schlüssel_12345'

# Flask-Moment initialisieren
moment = Moment(app)

# Datenbank konfigurieren (nur SQLite)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///local.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
UPLOAD_PATH = os.path.join('static', 'Uploads')
os.makedirs(UPLOAD_PATH, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_PATH

# Datenbankinstanz initialisieren
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# MODELS - In der richtigen Reihenfolge definiert
class User(db.Model):
    """Benutzer-Modell - MUSS als erstes definiert werden"""
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    is_teacher = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

class Klasse(db.Model):
    """Klassen-Modell"""
    __tablename__ = 'klasse'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    schuljahr = db.Column(db.String(9), nullable=False)
    schueler = db.relationship('Schueler', backref='klasse', lazy=True)
    unterrichtseinheiten = db.relationship('Unterrichtseinheit', backref='klasse', lazy=True)

class Familie(db.Model):
    """Familien-Modell"""
    __tablename__ = 'familie'
    id = db.Column(db.Integer, primary_key=True)
    familienname = db.Column(db.String(50), nullable=False)
    kontaktperson = db.Column(db.String(100))
    telefon = db.Column(db.String(20))
    email = db.Column(db.String(100))
    adresse = db.Column(db.Text)
    kinder = db.relationship('Schueler', backref='familie', lazy=True)

class Schueler(db.Model):
    """Schüler-Modell"""
    __tablename__ = 'schueler'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    nachname = db.Column(db.String(50), nullable=False)
    geburtsdatum = db.Column(db.Date)
    geschlecht = db.Column(db.String(1))
    notfallkontakt = db.Column(db.String(100))
    familie_id = db.Column(db.Integer, db.ForeignKey('familie.id'), nullable=True)
    klasse_id = db.Column(db.Integer, db.ForeignKey('klasse.id'), nullable=False)
    
    # Relationships
    anwesenheiten = db.relationship('Anwesenheit', backref='schueler', lazy=True)
    noten = db.relationship('Note', backref='schueler', lazy=True)

class Unterrichtseinheit(db.Model):
    """Unterrichtseinheit-Modell"""
    __tablename__ = 'unterrichtseinheit'
    id = db.Column(db.Integer, primary_key=True)
    datum = db.Column(db.Date, nullable=False)
    stunden = db.Column(db.String(10), nullable=False)
    thema = db.Column(db.String(100), nullable=False)
    inhalte = db.Column(db.Text)
    bemerkung = db.Column(db.Text)
    hausaufgaben = db.Column(db.Text)
    klasse_id = db.Column(db.Integer, db.ForeignKey('klasse.id'), nullable=False)
    lehrer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    
    # Relationships
    lehrer = db.relationship('User', backref='unterrichtseinheiten')
    materialien = db.relationship('UnterrichtsMaterial', backref='unterrichtseinheit', lazy=True)

class Anwesenheit(db.Model):
    """Anwesenheit-Modell"""
    __tablename__ = 'anwesenheit'
    id = db.Column(db.Integer, primary_key=True)
    schueler_id = db.Column(db.Integer, db.ForeignKey('schueler.id'), nullable=False)
    unterrichtseinheit_id = db.Column(db.Integer, db.ForeignKey('unterrichtseinheit.id'), nullable=False)
    status = db.Column(db.String(20), default='anwesend')  # anwesend, abwesend, verspätet, entschuldigt
    verspätung_minuten = db.Column(db.Integer, default=0)
    bemerkung = db.Column(db.Text)
    eingetragen_am = db.Column(db.DateTime, default=datetime.datetime.utcnow)

class Bewertungskategorie(db.Model):
    """Bewertungskategorie-Modell"""
    __tablename__ = 'bewertungskategorie'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)  # z.B. "Koranlesen", "Religiöses Wissen", "Verhalten"
    beschreibung = db.Column(db.Text)
    max_punkte = db.Column(db.Integer, default=5)
    kriterien = db.relationship('Bewertungskriterium', backref='kategorie', lazy=True)

class Bewertungskriterium(db.Model):
    """Bewertungskriterium-Modell"""
    __tablename__ = 'bewertungskriterium'
    id = db.Column(db.Integer, primary_key=True)
    kategorie_id = db.Column(db.Integer, db.ForeignKey('bewertungskategorie.id'), nullable=False)
    kriterium = db.Column(db.String(100), nullable=False)  # z.B. "Tajwid beachtet", "Aussprache korrekt"
    gewichtung = db.Column(db.Float, default=1.0)

class Note(db.Model):
    """Note-Modell"""
    __tablename__ = 'note'
    id = db.Column(db.Integer, primary_key=True)
    schueler_id = db.Column(db.Integer, db.ForeignKey('schueler.id'), nullable=False)
    kategorie_id = db.Column(db.Integer, db.ForeignKey('bewertungskategorie.id'), nullable=False)
    unterrichtseinheit_id = db.Column(db.Integer, db.ForeignKey('unterrichtseinheit.id'), nullable=True)
    bewertung = db.Column(db.Integer, nullable=False)  # 1-5 Sterne
    bemerkung = db.Column(db.Text)
    datum = db.Column(db.Date, default=datetime.date.today)
    
    # Relationships
    kategorie = db.relationship('Bewertungskategorie', backref='noten')
    checkliste_items = db.relationship('ChecklisteItem', backref='note', lazy=True)

class ChecklisteItem(db.Model):
    """Checkliste-Item-Modell"""
    __tablename__ = 'checkliste_item'
    id = db.Column(db.Integer, primary_key=True)
    note_id = db.Column(db.Integer, db.ForeignKey('note.id'), nullable=False)
    kriterium_id = db.Column(db.Integer, db.ForeignKey('bewertungskriterium.id'), nullable=False)
    erfuellt = db.Column(db.Boolean, default=False)
    
    # Relationships
    kriterium = db.relationship('Bewertungskriterium', backref='checkliste_items')

class Spende(db.Model):
    """Spende-Modell"""
    __tablename__ = 'spende'
    id = db.Column(db.Integer, primary_key=True)
    familie_id = db.Column(db.Integer, db.ForeignKey('familie.id'), nullable=False)
    betrag = db.Column(db.Float, nullable=False)
    zweck = db.Column(db.String(100))  # z.B. "Klassenmaterialien", "Bücher", "Ausflug"
    datum = db.Column(db.Date, default=datetime.date.today)
    status = db.Column(db.String(20), default='erhalten')  # erhalten, ausstehend, storniert

class Wettbewerb(db.Model):
    """Wettbewerb-Modell"""
    __tablename__ = 'wettbewerb'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    typ = db.Column(db.String(50), nullable=False)  # "Koran", "Wissen", "Verhalten"
    beschreibung = db.Column(db.Text)
    datum = db.Column(db.Date, nullable=False)
    anmeldeschluss = db.Column(db.Date)
    ist_aktiv = db.Column(db.Boolean, default=True)
    teilnahmen = db.relationship('WettbewerbTeilnahme', backref='wettbewerb', lazy=True)

class WettbewerbTeilnahme(db.Model):
    """Wettbewerb-Teilnahme-Modell"""
    __tablename__ = 'wettbewerb_teilnahme'
    id = db.Column(db.Integer, primary_key=True)
    wettbewerb_id = db.Column(db.Integer, db.ForeignKey('wettbewerb.id'), nullable=False)
    schueler_id = db.Column(db.Integer, db.ForeignKey('schueler.id'), nullable=False)
    anmeldedatum = db.Column(db.Date, default=datetime.date.today)
    platzierung = db.Column(db.Integer, nullable=True)
    punkte = db.Column(db.Integer, nullable=True)
    bemerkung = db.Column(db.Text)

class LehrerKlassenZuordnung(db.Model):
    """Lehrer-Klassen-Zuordnung-Modell"""
    __tablename__ = 'lehrer_klassen_zuordnung'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    klasse_id = db.Column(db.Integer, db.ForeignKey('klasse.id'), nullable=False)
    
    # Relationships
    user = db.relationship('User', backref='klassen_zuordnungen')
    klasse = db.relationship('Klasse', backref='lehrer_zuordnungen')

class UnterrichtsMaterial(db.Model):
    """Unterrichtsmaterial-Modell"""
    __tablename__ = 'unterrichts_material'
    id = db.Column(db.Integer, primary_key=True)
    unterrichtseinheit_id = db.Column(db.Integer, db.ForeignKey('unterrichtseinheit.id'), nullable=False)
    titel = db.Column(db.String(100), nullable=False)
    dateiname = db.Column(db.String(255), nullable=False)
    dateipfad = db.Column(db.String(500), nullable=False)
    dateityp = db.Column(db.String(20))  # PDF, Bild, Audio
    upload_datum = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    ist_oeffentlich = db.Column(db.Boolean, default=True)

# Einfache Routen für Tests
@app.route("/")
def index():
    """Hauptseite - Weiterleitung zum Klassenbuch"""
    return redirect(url_for('klassenbuch'))

@app.route("/klassenbuch")
def klassenbuch():
    klassen = Klasse.query.all()
    return render_template("virtuelles_klassenbuch.html", klassen=klassen)

@app.route("/test")
def test():
    """Test-Route um zu prüfen ob die Datenbank funktioniert"""
    user_count = User.query.count()
    klasse_count = Klasse.query.count()
    schueler_count = Schueler.query.count()
    
    return f"""
    <h1>🎉 Datenbank Test erfolgreich!</h1>
    <p>Benutzer: {user_count}</p>
    <p>Klassen: {klasse_count}</p>
    <p>Schüler: {schueler_count}</p>
    <p><a href="/klassenbuch">Zum Klassenbuch</a></p>
    """

# Datenbank initialisieren
def init_db():
    """Datenbank initialisieren"""
    try:
        with app.app_context():
            db.create_all()
            print("✅ Datenbank erfolgreich initialisiert!")
            
            # Test-Daten erstellen falls keine vorhanden
            if User.query.count() == 0:
                admin = User(
                    username='admin',
                    email='admin@moschee.de',
                    password_hash='admin123',
                    is_admin=True
                )
                db.session.add(admin)
                db.session.commit()
                print("✅ Test-Admin erstellt (admin/admin123)")
                
            return True
    except Exception as e:
        print(f"❌ Fehler beim Initialisieren der Datenbank: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Starte Klassenbuch-System...")
    
    if init_db():
        print("✅ System bereit!")
        print("📍 Besuchen Sie: http://localhost:5000/test")
        print("📍 Klassenbuch: http://localhost:5000/klassenbuch")
        app.run(debug=True, port=5000)
    else:
        print("❌ System konnte nicht gestartet werden!")