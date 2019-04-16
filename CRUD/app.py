from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

#CONECCION MYSQL
app.config['MYSQL_HOST'] = 'localhost' 
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'crud'
mysql = MySQL(app)

#CONFIGURACIONES
app.secret_key = 'mysecretkey'

@app.route('/')
 
def home():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacto')
    datos = cur.fetchall()
    return render_template('index.html', contacto = datos)

@app.route('/Anadir_un_contacto', methods=['POST'])
def añadir_un_contacto():
    if request.method == 'POST':
        nombrecompleto = request.form['nombrecompleto']
        phone = request.form['phone']
        ciudad = request.form['ciudad']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO contacto (nombrecompleto, phone, ciudad, email) VALUES (%s, %s, %s, %s)", (nombrecompleto, phone, ciudad, email))
        mysql.connection.commit()
        flash("Se ha añadido sactisfactoriamente.")
        return redirect(url_for('home'))

@app.route('/editar/<id>')
def editar_un_contacto(id):
    curso = mysql.connection.cursor()
    curso.execute('SELECT * FROM contacto WHERE id = %s', (id))
    datoss = curso.fetchall()
    print(datoss)
    return 'recibido'
    
@app.route('/eliminar/<string:id>')
def eliminar_un_contacto(id):
    cursor = mysql.connection.cursor()
    cursor.execute('DELETE FROM contacto WHERE id = {0}'.format(id) )
    mysql.connection.commit()
    flash('El conctaco ha sido removido.')
    return redirect(url_for('home'))


if __name__=="__main__":
    app.run(port = 3006, debug = True)
