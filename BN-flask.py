import bottle
import sqlite3 # pour la base de donnée
import sys # pour quitter le programme
import datetime # pour la date et l'heure

app = bottle.Bottle()

@app.route('/')
def index():
    return bottle.template('./templates/index.html')

if __name__ == '__main__':
    app.run(debug=True)


'''
"""
Programme Python qui permet à l’utilisateur de tenir un bloc-notes personnel. 
L’utilisateur peut ajouter des notes, les lire, et les rechercher.
"""

# créez la base de donnée

'''
conn = sqlite3.connect('premiercourspython2023.db') # créez la base de donnée
cursor = conn.cursor() # créez un curseur pour la base de donnée
'''

# créez la table
'''
cursor.execute("""
    CREATE TABLE IF NOT EXISTS notes
       (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        type TEXT,
        titre TEXT,
        note TEXT,
        date TEXT
        )
""")
conn.commit()


"""
Créez une classe Blocnote qui contient une liste de notes et qui permet d’ajouter, afficher, supprimer une ou plusieurs notes.
"""

class Blocnote:
    def __init__(self, nom):
        self.nom = nom
        self.notes = []

    def ajouter(self, note):
        self.notes.append(note)
        cursor.execute("""INSERT INTO notes(type, titre, note, date) VALUES(?, ?, ?, ?)""",
                       (note.type, note.titre, note.note, note.date))
        conn.commit()

        

class Note:
    def __init__(self, note, date):
        self.note = note
        self.date = date

class NoteTexte(Note):
    def __init__(self, titre, note, date, type=None):
        super().__init__(note, date)  # Notez que le titre est passé comme note ici
        self.type = "notesTexte"
        self.titre = titre


class NoteTexte(Note):
    def __init__(self, titre, fichier, date, type=None):
        super().__init__(fichier, date)  # Notez que le titre est passé comme note ici
        self.type = "notesTexte"
        self.titre = titre


blocnote = Blocnote("Bloc-note personnel")

while True:
    print("Bienvenue dans votre bloc-notes personnel !")
    print("/-----------------------------------------/")
    print("1. Ajouter une note")
    print("2. Afficher les notes")
    print("3. Supprimer une note")
    print("4. Quitter")
    choix = input("Entrez votre choix : ")
    match choix :

        case "1":
            print("Entrez le type de la note :")
            print("1. Note texte")
            print("2. Note image")
            choix = input("Entrez votre choix : ")
            match choix :
                case "1":
                    titre = input("Entrez le titre de la note : ")
                    note = input("Entrez la note : ")
                    date = datetime.datetime.now()
                    note = NoteTexte(titre, note, date)
                    blocnote.ajouter(note)
                    print("Votre note à été ajoutée avec succès !")
                case "2":
                    titre = input("Entrez le titre de la note : ")
                    fichier = input("Entrez le nom du fichier : ")
                    date = datetime.datetime.now()
                    note = NoteImage(titre, fichier, date)
                    blocnote.ajouter(note)
                    print("Votre note à été ajoutée avec succès !")
        case "2":
            print("Entrez le type des notes que vous voulez afficher :")
            print("1. Notes texte")
            print("2. Notes image")
            choix = input("Entrez votre choix : ")
            match choix :
                case "1":
                    cursor.execute("""SELECT * FROM notes WHERE type = 'notesTexte'""")
                    notes = cursor.fetchall()
                    print("Voici la liste des notes : ")
                    print("/-----------------------------------------/")
                    for note in notes:
                        print(note)
                    print("/-----------------------------------------/")
                case "2":
                    cursor.execute("""SELECT * FROM notes WHERE type = 'notesFichier'""")
                    notes = cursor.fetchall()
                    print("Voici la liste des notes : ")
                    print("/-----------------------------------------/")
                    for note in notes:
                        print(note)
                    print("/-----------------------------------------/") 

        case "3":
            print("Entrez le type des notes que vous voulez supprimer :")
            print("1. Notes texte")
            print("2. Notes image")
            choix = input("Entrez votre choix : ")
            match choix :
                case "1":
                    cursor.execute("""SELECT * FROM notes WHERE type = 'notesTexte'""")
                    notes = cursor.fetchall()
                    print("Voici la liste des notes : ")
                    print("/-----------------------------------------/")
                    for note in notes:
                        print(note)
                    print("/-----------------------------------------/")
                    id = input("Entrez l'id de la note que vous voulez supprimer : ")
                    print("/-----------------------------------------/")
                    cursor.execute("""DELETE FROM notes WHERE id = ?""", (id,))
                    conn.commit()
                    print("Votre note à été supprimée avec succès !")
                case "2":
                    cursor.execute("""SELECT * FROM notes WHERE type = 'notesFichier'""")
                    notes = cursor.fetchall()
                    print("Voici la liste des notes : ")
                    print("/-----------------------------------------/")
                    for note in notes:
                        print(note)
                    print("/-----------------------------------------/")
                    id = input("Entrez l'id de la note que vous voulez supprimer : ")
                    print("/-----------------------------------------/")
                    cursor.execute("""DELETE FROM notes WHERE id = ?""", (id,))
                    conn.commit()
                    print("Votre note à été supprimée avec succès !")