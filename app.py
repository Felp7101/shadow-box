from flask import Flask,render_template, request, jsonify



app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')



#teste conexão MySql
db_config = {
    'host': 'localhost',
    'user': 'seu_usuario',
    'password': 'sua_senha',
    'database': 'habito'
}






if __name__ == '__main__':
    app.run(debug=True)