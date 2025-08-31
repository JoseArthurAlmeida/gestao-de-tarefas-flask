from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Dicionário para armazenar as tarefas em memória
tarefas = {}
contador_id = 1

@app.route('/')
def index():
    """Página principal - lista todas as tarefas"""
    return render_template('index.html', tarefas=tarefas)

@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar_tarefa():
    """Página para adicionar nova tarefa"""
    global contador_id
    
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        descricao = request.form.get('descricao')
        prioridade = request.form.get('prioridade')
        
        if titulo:
            tarefa = {
                'id': contador_id,
                'titulo': titulo,
                'descricao': descricao,
                'prioridade': prioridade,
                'status': 'pendente',
                'data_criacao': datetime.now().strftime('%d/%m/%Y %H:%M'),
                'data_conclusao': None
            }
            tarefas[contador_id] = tarefa
            contador_id += 1
            return redirect(url_for('index'))
    
    return render_template('adicionar.html')

@app.route('/alterar_status/<int:tarefa_id>')
def alterar_status(tarefa_id):
    """Altera o status de uma tarefa"""
    if tarefa_id in tarefas:
        tarefa = tarefas[tarefa_id]
        if tarefa['status'] == 'pendente':
            tarefa['status'] = 'em_andamento'
        elif tarefa['status'] == 'em_andamento':
            tarefa['status'] = 'concluida'
            tarefa['data_conclusao'] = datetime.now().strftime('%d/%m/%Y %H:%M')
        elif tarefa['status'] == 'concluida':
            tarefa['status'] = 'pendente'
            tarefa['data_conclusao'] = None
    
    return redirect(url_for('index'))

@app.route('/excluir/<int:tarefa_id>')
def excluir_tarefa(tarefa_id):
    """Exclui uma tarefa"""
    if tarefa_id in tarefas:
        del tarefas[tarefa_id]
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
