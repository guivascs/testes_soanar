import os
import subprocess
import pickle
import mysql.connector
from flask import Flask, request, render_template_string

app = Flask(__name__)

# Vulnerabilidade: Credenciais hardcoded
DB_USER = "admin"
DB_PASS = "password123"

@app.route('/')
def index():
    # Vulnerabilidade: Cross-Site Scripting (XSS)
    name = request.args.get('name', 'Guest')
    return render_template_string('<h1>Hello, ' + name + '!</h1>')

@app.route('/exec')
def execute_command():
    # Vulnerabilidade: Execução de comando arbitrário
    cmd = request.args.get('cmd')
    return subprocess.check_output(cmd, shell=True)

@app.route('/read')
def read_file():
    # Vulnerabilidade: Path Traversal
    filename = request.args.get('filename')
    with open(filename, 'r') as f:
        return f.read()

@app.route('/pickle')
def pickle_data():
    # Vulnerabilidade: Desserialização insegura
    data = request.args.get('data')
    return pickle.loads(data)

def connect_db():
    # Vulnerabilidade: SQL Injection
    user_id = request.args.get('user_id')
    query = f"SELECT * FROM users WHERE id = {user_id}"
    conn = mysql.connector.connect(user=DB_USER, password=DB_PASS, database='mydb')
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

@app.route('/login')
def login():
    # Vulnerabilidade: Autenticação fraca
    username = request.args.get('username')
    password = request.args.get('password')
    if username == 'admin' and password == 'admin123':
        return "Login successful"
    return "Login failed"

def insecure_random():
    # Vulnerabilidade: Uso de gerador de números aleatórios inseguro
    import random
    return random.randint(1, 6)

@app.route('/delete/<filename>')
def delete_file(filename):
    # Vulnerabilidade: Remoção insegura de arquivo
    os.remove(filename)
    return f"File {filename} deleted"

@app.route('/eval')
def eval_code():
    # Vulnerabilidade: Execução de código arbitrário
    code = request.args.get('code')
    return str(eval(code))

if __name__ == '__main__':
    # Vulnerabilidade: Debug mode ativado em produção
    app.run(debug=True)

# Outras vulnerabilidades:
# - Falta de validação de entrada
# - Falta de sanitização de saída
# - Uso de funções obsoletas/inseguras
# - Falta de tratamento de exceções
# - Exposição de informações sensíveis em logs
