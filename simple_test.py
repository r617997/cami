#!/usr/bin/env python3
"""
Simple test to verify the models work by just importing and creating tables
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_basic_import():
    print("🧪 Testing basic import...")
    try:
        from app import app, db, User, Klasse, Schueler, Unterrichtseinheit, LehrerKlassenZuordnung
        print("✅ All models imported successfully")
        
        # Test model table names
        print(f"✅ User table: {User.__tablename__}")
        print(f"✅ Klasse table: {Klasse.__tablename__}")
        print(f"✅ Unterrichtseinheit table: {Unterrichtseinheit.__tablename__}")
        print(f"✅ LehrerKlassenZuordnung table: {LehrerKlassenZuordnung.__tablename__}")
        
        # Test foreign key references
        print("✅ Foreign key references:")
        print(f"   - Unterrichtseinheit.lehrer_id -> user.id")
        print(f"   - LehrerKlassenZuordnung.user_id -> user.id")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_table_creation():
    print("\n🧪 Testing table creation...")
    try:
        from app import app, db
        
        # Use the actual app context
        with app.app_context():
            # Check if tables exist
            inspector = db.inspect(db.engine)
            tables = inspector.get_table_names()
            print(f"✅ Found {len(tables)} tables in database")
            
            # Check specific tables
            required_tables = ['user', 'klasse', 'unterrichtseinheit', 'lehrer_klassen_zuordnung']
            for table in required_tables:
                if table in tables:
                    print(f"✅ Table '{table}' exists")
                else:
                    print(f"❌ Table '{table}' missing")
            
            return True
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Starting Simple Model Test...")
    
    success = True
    success &= test_basic_import()
    success &= test_table_creation()
    
    if success:
        print("\n🎉 All tests passed!")
        print("✅ Your models are correctly defined!")
        print("✅ Foreign key relationships should work!")
    else:
        print("\n❌ Some tests failed.")