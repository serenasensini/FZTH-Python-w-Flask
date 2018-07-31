'''
Modulo per la creazione, gestione e esecuzione di query tramite SQLite3
'''

import sqlite3

# Salva il database in un file chiamato 'database.db', e lo apre in scrittura e lettura
file = open('database.db', 'w+')

# Crea un database in RAM
#db = sqlite3.connect(':memory:')

# Si connette al database nel file con SQLite3 DB
db = sqlite3.connect('database.db')

# Si associa un cursore al database per poter eseguire le query
cursor = db.cursor()

# Si esegue la query tramite il cursore
cursor.execute('''CREATE TABLE users(id INTEGER PRIMARY KEY, firstname TEXT, surname TEXT, email TEXT)''')

# Si effettua il commit per salvare il risultato della precedente operazione
db.commit()

# Creo di dati da inserire e li salvo in delle variabili
username1 = 'Andres'
email1 = 'user@example.com'
name1 = 'John'

# Inserisco un utente con i dati sopra definiti
cursor.execute('''INSERT INTO users(username, email, name)
                  VALUES(?,?,?)''', (username1, email1, name1))
print('First user inserted')

# Eseguo una ricerca sugli utenti
cursor.execute('''SELECT * FROM users''')

# Salvo il risultato della query nella variabile all_rows
all_rows = cursor.fetchall()

#Stampo il risultato della query (il risultato è sempre una tupla)
print(all_rows)
