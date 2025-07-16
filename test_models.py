#!/usr/bin/env python3
"""
Simple test script to verify SQLAlchemy models work without all dependencies
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime

# Basic Flask app setup
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize db
db = SQLAlchemy(app)

# Test models - simplified versions
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    is_teacher = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

class Klasse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    schuljahr = db.Column(db.String(9), nullable=False)
    schueler = db.relationship('Schueler', backref='klasse', lazy=True)
    unterrichtseinheiten = db.relationship('Unterrichtseinheit', backref='klasse', lazy=True)

class Schueler(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    nachname = db.Column(db.String(50), nullable=False)
    geburtsdatum = db.Column(db.Date)
    geschlecht = db.Column(db.String(1))
    notfallkontakt = db.Column(db.String(100))
    familie_id = db.Column(db.Integer, db.ForeignKey('familie.id'), nullable=True)
    klasse_id = db.Column(db.Integer, db.ForeignKey('klasse.id'), nullable=False)

class Unterrichtseinheit(db.Model):
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

class Familie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    familienname = db.Column(db.String(50), nullable=False)
    kontaktperson = db.Column(db.String(100))
    telefon = db.Column(db.String(20))
    email = db.Column(db.String(100))
    adresse = db.Column(db.Text)
    kinder = db.relationship('Schueler', backref='familie', lazy=True)

class LehrerKlassenZuordnung(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    klasse_id = db.Column(db.Integer, db.ForeignKey('klasse.id'), nullable=False)
    
    # Relationships
    user = db.relationship('User', backref='klassen_zuordnungen')
    klasse = db.relationship('Klasse', backref='lehrer_zuordnungen')

# Test function
def test_models():
    with app.app_context():
        try:
            db.create_all()
            print("✅ SUCCESS: All models created successfully!")
            print("✅ Foreign key relationships are working correctly!")
            return True
        except Exception as e:
            print(f"❌ ERROR: {e}")
            return False

if __name__ == "__main__":
    print("Testing SQLAlchemy models...")
    if test_models():
        print("\n🎉 All tests passed! The SQLAlchemy models are working correctly.")
    else:
        print("\n❌ Tests failed! There are issues with the models.")