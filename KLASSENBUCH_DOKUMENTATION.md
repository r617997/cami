# Virtuelles Klassenbuch - Moschee

## Übersicht

Das virtuelle Klassenbuch-System für die Moschee ist eine umfassende Lösung zur Verwaltung von Schülern, Unterricht, Noten und allen wichtigen Aspekten des Moscheeschul-Betriebs.

## 🆕 Neue Funktionen

### 1️⃣ Grundfunktionen

#### **Schülerverwaltung**
- ✅ **Erweiterte Schülerdaten**: Name, Nachname, Geburtsdatum, Geschlecht, Notfallkontakt
- ✅ **Klassenzuordnung**: Automatische Zuordnung zu Klassen (Stufe 1, Stufe 2, Jugendliche)
- ✅ **Familienzuordnung**: Verknüpfung mehrerer Geschwister in einem Haushalt
- ✅ **Excel Import/Export**: Massenimport von Schülerlisten und Export für Archivierung

#### **Anwesenheitskontrolle**
- ✅ **Erweiterte Statusoptionen**: Anwesend, Abwesend, Verspätet, Entschuldigt
- ✅ **Verspätungs-Tracking**: Dokumentation von Verspätungen in Minuten
- ✅ **Bemerkungsfeld**: Individuelle Notizen zu Anwesenheitsstatus
- ✅ **Echtzeitstatistiken**: Live-Anzeige der Anwesenheitsquote
- ✅ **Anwesenheitshistorie**: Vollständige Übersicht pro Schüler und Klasse

#### **Notenerfassung mit Checklisten**
- ✅ **Bewertungskategorien**: Koranlesen, Religiöses Wissen, Verhalten
- ✅ **5-Sterne-System**: Intuitive Bewertung von 1-5 Sternen
- ✅ **Checklisten**: Detaillierte Kriterien für jede Kategorie
  - **Koranlesen**: Tajwid, Aussprache, Flüssigkeit, Betonung
  - **Religiöses Wissen**: Grundlagen, Anwendung, Zusatzwissen, Fragenbeantwortung
  - **Verhalten**: Respekt, Aufmerksamkeit, Hilfsbereitschaft, Pünktlichkeit
- ✅ **Bemerkungsfelder**: Individuelle Hinweise zu Schülern
- ✅ **Notenhistorie**: Vollständige Bewertungsverläufe

#### **Unterrichtsdokumentation**
- ✅ **Erweiterte Themen-Dokumentation**: Strukturierte Erfassung von Unterrichtsinhalten
- ✅ **Hausaufgaben-Verwaltung**: Digitale Hausaufgaben-Zuweisung
- ✅ **Material-Upload**: Upload von PDFs, Bildern, Audio-Dateien
- ✅ **Lehrer-Zuordnung**: Zuordnung von Lehrern zu Unterrichtseinheiten

### 2️⃣ Spezielle Funktionen für die Moschee

#### **Familienverwaltung**
- ✅ **Familiäre Zuordnung**: Mehrere Geschwister in einem Haushalt
- ✅ **Kontaktdaten**: Zentrale Verwaltung von Familienkontakten
- ✅ **Familienübersicht**: Übersicht aller Kinder einer Familie

#### **Spendenverwaltung**
- ✅ **Spenden-Tracking**: Dokumentation spendenbasierter Beiträge
- ✅ **Verwendungszweck**: Klassenmaterialien, Bücher, Ausflüge
- ✅ **Familienverknüpfung**: Zuordnung von Spenden zu Familien
- ✅ **Spenden-Statistiken**: Monatsübersichten und Jahresberichte

#### **Wettbewerbe**
- ✅ **Wettbewerb-Verwaltung**: Koran-, Wissens- und Verhaltenswettbewerbe
- ✅ **Anmeldesystem**: Digitale Anmeldung von Schülern
- ✅ **Ergebnis-Dokumentation**: Platzierungen und Punkte
- ✅ **Anmeldeschluss**: Automatische Verwaltung von Anmeldefristen

### 3️⃣ Benutzer- und Rollenmanagement

#### **Rollen-System**
- ✅ **Admin**: Vollzugriff auf alle Funktionen und Benutzerverwaltung
- ✅ **Lehrer**: Klassenverwaltung, Anwesenheit, Noten, Unterrichtsdokumentation
- ✅ **Eltern** (optional): Einsicht in Anwesenheit und Fortschritt ihrer Kinder
- ✅ **Lehrer-Klassen-Zuordnung**: Flexible Zuordnung von Lehrern zu Klassen

### 4️⃣ Technische Anforderungen

#### **Benutzerfreundlichkeit**
- ✅ **Responsive Design**: Optimiert für PC, Tablet und Smartphone
- ✅ **Intuitive Bedienung**: Einfache Navigation für IT-Laien
- ✅ **Moderne UI**: Ansprechende Benutzeroberfläche mit Bootstrap 5
- ✅ **Tastatur-Shortcuts**: Schnelle Bedienung für Power-User

#### **Export-Funktionen**
- ✅ **Excel-Export**: Schülerlisten, Noten, Anwesenheit
- ✅ **PDF-Berichte**: Monats- und Jahresübersichten
- ✅ **Archivierung**: Strukturierte Datenarchivierung

### 5️⃣ Dashboard und Übersichten

#### **Erweitertes Dashboard**
- ✅ **Tagesübersicht**: Heutige Unterrichtseinheiten und Anwesenheit
- ✅ **Statistiken**: Anwesenheitsquoten, Spendensummen, Wettbewerbe
- ✅ **Letzte Aktivitäten**: Chronologische Übersicht der Unterrichtsthemen
- ✅ **Schnellaktionen**: Direktzugriff auf häufige Funktionen

## 🚀 Installation und Setup

### Systemanforderungen
- Python 3.8+
- Flask 2.3+
- SQLite (Standard) oder PostgreSQL/MySQL
- Moderne Browser (Chrome, Firefox, Safari, Edge)

### Installation
```bash
# Repository klonen
git clone <repository-url>
cd virtuelles-klassenbuch

# Virtuelle Umgebung erstellen
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Abhängigkeiten installieren
pip install -r requirements.txt

# Datenbank initialisieren
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

# Standard-Bewertungskategorien erstellen
python -c "from app import app, db; app.app_context().push(); db.create_all()"
```

### Erste Schritte
1. **Anwendung starten**: `python app.py`
2. **Browser öffnen**: `http://localhost:3000`
3. **Setup aufrufen**: `/setup_default_categories` für Standard-Bewertungskategorien
4. **Erste Klasse erstellen**: Dashboard → Neue Klasse
5. **Schüler hinzufügen**: Klassenbuch → Schüler hinzufügen

## 📖 Benutzerhandbuch

### Tägliche Nutzung

#### **1. Anwesenheit erfassen**
1. Dashboard → Heutige Unterrichtseinheiten
2. "Anwesenheit" Button klicken
3. Status für jeden Schüler setzen:
   - ✅ Anwesend
   - ❌ Abwesend  
   - ⏰ Verspätet (+ Minuten)
   - 📄 Entschuldigt
4. Bemerkungen hinzufügen
5. Speichern

#### **2. Noten erfassen**
1. Klassenbuch → Klasse auswählen → Noten erfassen
2. Schüler auswählen
3. Bewertungskategorie wählen
4. Sterne-Bewertung vergeben (1-5)
5. Checkliste ausfüllen
6. Bemerkung hinzufügen
7. Speichern

#### **3. Unterricht dokumentieren**
1. Klassenbuch → Unterrichtseinheit erstellen
2. Thema und Inhalte eingeben
3. Hausaufgaben definieren
4. Materialien hochladen
5. Speichern

### Verwaltungsaufgaben

#### **Familie hinzufügen**
1. Familien → Neue Familie
2. Kontaktdaten eingeben
3. Kinder zuordnen
4. Speichern

#### **Spende erfassen**
1. Spenden → Spende erfassen
2. Familie auswählen
3. Betrag und Zweck eingeben
4. Speichern

#### **Wettbewerb erstellen**
1. Wettbewerbe → Wettbewerb erstellen
2. Details eingeben
3. Anmeldeschluss setzen
4. Schüler anmelden

## 🔧 Technische Details

### Datenbank-Schema

#### **Erweiterte Modelle**
- `Familie`: Familienverwaltung
- `Bewertungskategorie`: Notenkategorien
- `Bewertungskriterium`: Checklisten-Kriterien
- `Note`: Bewertungen mit Checklisten
- `ChecklisteItem`: Einzelne Checklisten-Einträge
- `Spende`: Spendenverwaltung
- `Wettbewerb`: Wettbewerbs-Verwaltung
- `WettbewerbTeilnahme`: Teilnahme-Tracking
- `UnterrichtsMaterial`: Materialien-Upload
- `LehrerKlassenZuordnung`: Rollen-Management

#### **Erweiterte Felder**
- `Schueler`: +notfallkontakt, +familie_id
- `Unterrichtseinheit`: +hausaufgaben, +lehrer_id
- `Anwesenheit`: +status, +verspätung_minuten, +bemerkung

### API-Endpunkte

#### **Neue Routen**
- `/dashboard_erweitert` - Erweitertes Dashboard
- `/familien` - Familienverwaltung
- `/noten_erfassen/<klasse_id>` - Notenerfassung
- `/spenden` - Spendenverwaltung
- `/wettbewerbe` - Wettbewerbs-Verwaltung
- `/anwesenheit_erweitert/<unterrichtseinheit_id>` - Erweiterte Anwesenheit
- `/schueler_import` - Excel-Import
- `/schueler_export/<klasse_id>` - Excel-Export

### Sicherheit

- ✅ **Eingabevalidierung**: Alle Formulare validiert
- ✅ **CSRF-Schutz**: Flask-WTF Integration
- ✅ **SQL-Injection-Schutz**: SQLAlchemy ORM
- ✅ **Datei-Upload-Sicherheit**: Validierte Dateitypen
- ✅ **Backup-Funktionen**: Regelmäßige Datensicherung

## 📊 Berichtswesen

### Verfügbare Berichte

#### **Anwesenheitsberichte**
- Tagesübersicht
- Wochenübersicht
- Monatsübersicht
- Schüler-individuelle Berichte

#### **Leistungsberichte**
- Notenübersicht nach Kategorie
- Schüler-Fortschritt
- Klassen-Vergleiche
- Zeitraum-Analysen

#### **Spenden-Berichte**
- Monatsübersicht
- Familien-Übersicht
- Verwendungszweck-Analyse
- Jahresberichte

#### **Wettbewerbs-Berichte**
- Teilnahme-Übersicht
- Ergebnisse
- Statistiken

## 🎨 Benutzeroberfläche

### Design-Prinzipien
- **Benutzerfreundlich**: Intuitive Navigation
- **Responsive**: Mobile-first Design
- **Barrierefrei**: WCAG-konform
- **Modern**: Moderne UI mit Bootstrap 5

### Farbschema
- **Primär**: Blau-Lila Gradient (#667eea → #764ba2)
- **Erfolg**: Grün (#28a745)
- **Warnung**: Gelb (#ffc107)
- **Gefahr**: Rot (#dc3545)
- **Info**: Cyan (#17a2b8)

### Icons
- **Font Awesome 6**: Konsistente Icon-Sprache
- **Semantische Icons**: Bedeutungsvolle Symbole
- **Responsive Icons**: Skalierbare Vektorgrafiken

## 🚀 Erweiterte Features

### Geplante Funktionen
- [ ] **E-Mail-Benachrichtigungen**: Automatische Benachrichtigungen
- [ ] **SMS-Integration**: Kurznachrichten an Eltern
- [ ] **Kalender-Integration**: Terminverwaltung
- [ ] **Backup-Automatisierung**: Automatische Datensicherung
- [ ] **Multi-Sprach-Support**: Türkisch, Arabisch, Deutsch
- [ ] **Mobile App**: Native Mobile-Anwendung
- [ ] **Offline-Modus**: Offline-Funktionalität
- [ ] **Cloud-Synchronisation**: Multi-Standort-Synchronisation

### Anpassungsmöglichkeiten
- **Bewertungsskalen**: Anpassbare Bewertungssysteme
- **Kategorien**: Eigene Bewertungskategorien
- **Felder**: Zusätzliche Schüler-/Familienfelder
- **Berichte**: Individuelle Berichtsvorlagen
- **Branding**: Anpassbares Logo und Design

## 🔧 Wartung und Support

### Regelmäßige Wartung
- **Datenbank-Backup**: Täglich
- **System-Updates**: Monatlich
- **Sicherheits-Patches**: Bei Bedarf
- **Performance-Optimierung**: Quartalsweise

### Support-Kontakte
- **Technischer Support**: [support@example.com]
- **Benutzer-Schulung**: [training@example.com]
- **Feature-Requests**: [features@example.com]

## 📋 Changelog

### Version 2.0.0 (Aktuell)
- ✅ Erweiterte Schülerverwaltung
- ✅ Familienverwaltung
- ✅ Notenerfassung mit Checklisten
- ✅ Spendenverwaltung
- ✅ Wettbewerbs-System
- ✅ Erweiterte Anwesenheitskontrolle
- ✅ Excel Import/Export
- ✅ Modernes Dashboard
- ✅ Responsive Design
- ✅ Rollenmanagement

### Version 1.0.0 (Basis)
- ✅ Grundlegende Klassenverwaltung
- ✅ Einfache Anwesenheitskontrolle
- ✅ Schüler-Grunddaten
- ✅ Basis-Unterrichtsdokumentation

## 🤝 Beitrag zur Entwicklung

Das System ist Open Source und freut sich über Beiträge:
- **Bug Reports**: GitHub Issues
- **Feature Requests**: GitHub Discussions
- **Code Contributions**: Pull Requests
- **Dokumentation**: Wiki-Beiträge
- **Übersetzungen**: Lokalisierungs-Beiträge

## 📄 Lizenz

MIT License - Frei nutzbar für alle Moscheen und Bildungseinrichtungen.

---

**Möge Allah (swt) dieses System segnen und es zu einem wertvollen Werkzeug für die islamische Bildung machen. Amin.**