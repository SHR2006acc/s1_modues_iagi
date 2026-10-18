
import sqlite3


def creatDB(filename):
        db = sqlite3.connect(filename)
        db.execute("""
            CREATE TABLE IF NOT EXISTS person (
                id INTEGER,
                name TEXT,
                age INTEGER
            )
        """)
        return db

def afficher(db):
    db.row_factory = sqlite3.Row
    cursor = db.execute("SELECT * FROM person")
    for row in cursor:
       print(row["id"], row["name"], row["age"])

    
def insert(db,id,name,age):
        db.execute(
            "INSERT INTO person (id, name, age) VALUES (?, ?, ?)",
            (id,name,age)
        )


def delete(db,id):
    db.execute("delete from person where code=10")
    
db=creatDB("dbFILE")
insert(db,200,"rayan",18)
db.commit()
afficher(db)
insert(db,200,"rayan",18)
db.commit()
afficher(db)
delete(db,200)
db.commit()
afficher(db)





# Allow access by column name

db.close()
