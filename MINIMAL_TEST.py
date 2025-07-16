#!/usr/bin/env python3
"""
Minimal Test - Nur SQLAlchemy Models ohne zusätzliche Dependencies
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime

# App erstellen
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_minimal.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Datenbankinstanz initialisieren
db = SQLAlchemy(app)

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
    lehrer_zuordnungen = db.relationship('LehrerKlassenZuordnung', backref='klasse', lazy=True)

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

class LehrerKlassenZuordnung(db.Model):
    """Lehrer-Klassen-Zuordnung-Modell"""
    __tablename__ = 'lehrer_klassen_zuordnung'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    klasse_id = db.Column(db.Integer, db.ForeignKey('klasse.id'), nullable=False)
    
    # Relationships
    user = db.relationship('User', backref='klassen_zuordnungen')

# Test-Routen
@app.route("/")
def index():
    return "<h1>✅ Minimal App läuft!</h1><p><a href='/test'>Test DB</a></p>"

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
    <p><a href="/">Zurück</a></p>
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
                
                # Test-Klasse erstellen
                test_klasse = Klasse(
                    name='Stufe 1',
                    schuljahr='2024/2025'
                )
                db.session.add(test_klasse)
                
                db.session.commit()
                print("✅ Test-Daten erstellt!")
                
            return True
    except Exception as e:
        print(f"❌ Fehler beim Initialisieren der Datenbank: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Starte Minimal Test...")
    
    if init_db():
        print("✅ System bereit!")
        print("📍 Besuchen Sie: http://localhost:5001/")
        print("📍 Test: http://localhost:5001/test")
        app.run(debug=True, port=5001)
    else:
        print("❌ System konnte nicht gestartet werden!")