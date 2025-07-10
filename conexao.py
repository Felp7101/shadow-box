import mysql.connector

#teste conexão MySql

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='habitos'
)

if conn.is_connected():
    print('Conectado ao MySQL com sucesso!')
    conn.close()
else:
    print('Erro ao conectar.')