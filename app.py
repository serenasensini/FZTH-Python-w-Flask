from flask import Flask, render_template, request, redirect, url_for
import sqlite3

# Definisco una nuova applicazione in Flask
app = Flask(__name__)

'''
 "app" = nome dell'applicazione
 "route" = decoratore per catturare una richiesta, definito tra parentesi tonde 
'''

#route verso la pagina principale
#alla action "/" corrisponde la funzione main()
@app.route('/')
def main():

    # Prima creo il database, così che posso salvare gli utenti se successivamente si registrano
    # !Attenzione: ogni volta che avvio l'applicazione, il file database.db viene cancellato

    # Si connette al database nel file con SQLite3 DB
    db = sqlite3.connect('database.db')

    # Si associa un cursore al database per poter eseguire le query
    cursor = db.cursor()

    # Si esegue la query tramite il cursore per creare una tabella per gestire gli utenti
    cursor.execute('''CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, name TEXT, email TEXT, password TEXT)''')

    # Si effettua il commit per salvare il risultato della precedente operazione
    db.commit()

    print("Tabella creata!")

    #restituisce il template index.html
    return render_template('index.html')

#alla action "showSignUp", corrisponde la funzione showSignUp()
@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

#alla action "signUp", corrisponde la funzione signUp, che accetta request di tipo GET e POST
#il tipo GET è il tipo di default
@app.route('/signUp',methods=['POST'])
def signUp():
    try:
        #parametro associato alla request
        #e' fondamentale che il nome del parametro sia UGUALE a quello presente nei campi di input sotto l'attributo "name"
        #esempio: <input type="email" name="EMAIL" id="inputEmail" class="form-control" placeholder="Email address" required autofocus>
        _name = request.form['name']
        _email = request.form['email']
        _password = request.form['password']

        print("Parametri inseriti: ")
        print(_name)
        print(_email)
        print(_password)

        db = sqlite3.connect("database.db")
        cursor = db.cursor()

        # Inserisco un utente con i dati sopra definiti
        cursor.execute('''INSERT INTO users(name, email, password) VALUES(?,?,?)''', (_name, _email, _password))
        db.commit()

        print("Utente inserito!")

    except Exception as e:
        print(e)
    finally:
        # Chiuso il riferimento al puntatore
        cursor.close() 
        # Chiudo la connessione al database
        db.close()
        return redirect(url_for('confirmation'))

@app.route('/confirmation/', methods=['GET'])
def confirmation():
    return render_template("confirmation.html")

# Condizione per far avviare l'applicazione
if __name__ == "__main__":
    app.run(port=5002)
