from flask import Flask,render_template, request,  redirect, url_for
import mysql.connector


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')



def get_conexao():
    return mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='habitos'
    )


@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    titulo = request.form['nome']
    descricao = request.form['descricao']

    print(f'Recebido: {titulo}, {descricao}')   #Teste

    conn = get_conexao()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO habitos (titulo, descricao) VALUES (%s, %s)', (titulo, descricao))
    conn.commit()
    conn.close()

    return redirect(url_for('home'))





if __name__ == '__main__':
    app.run(debug=True)