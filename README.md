# Sistema de Gestão de Tarefas

Um aplicativo Flask para gerenciar tarefas de forma simples e eficiente, com armazenamento em memória e tema dark moderno.

## Funcionalidades

- **Listagem de Tarefas**: Visualize todas as suas tarefas em cards organizados
- **Adicionar Tarefas**: Formulário completo para criar novas atividades
- **Gerenciar Status**: Altere o status das tarefas (Pendente → Em Andamento → Concluída)
- **Excluir Tarefas**: Remova tarefas que não são mais necessárias
- **Prioridades**: Defina níveis de prioridade (Baixa, Média, Alta)
- **Timestamps**: Registro automático de criação e conclusão
- **Interface Responsiva**: Design moderno e adaptável
- **Tema Dark**: Interface escura e moderna para melhor experiência visual

## Estrutura do Projeto

```
gestao_tarefas/
├── app.py              # Aplicativo Flask principal
├── templates/          # Templates HTML
│   ├── index.html     # Página principal (lista de tarefas)
│   └── adicionar.html # Formulário para adicionar tarefas
├── static/            # Arquivos estáticos
│   └── css/
│       └── style.css  # Estilos CSS do tema dark
├── requirements.txt    # Dependências do projeto
├── .gitignore         # Arquivo para ignorar arquivos desnecessários
└── README.md          # Este arquivo
```

## Como Executar

1. **Ativar o ambiente virtual:**
   ```bash
   venv\Scripts\activate
   ```

2. **Instalar as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Executar o aplicativo:**
   ```bash
   python app.py
   ```

4. **Acessar no navegador:**
   Abra http://127.0.0.1:5000 no seu navegador

## Rotas da Aplicação

- **`/`** - Página principal com lista de todas as tarefas
- **`/adicionar`** - Formulário para criar nova tarefa
- **`/alterar_status/<id>`** - Altera o status de uma tarefa específica
- **`/excluir/<id>`** - Remove uma tarefa do sistema

## Estados das Tarefas

1. **Pendente** - Tarefa criada, aguardando início
2. **Em Andamento** - Tarefa sendo executada
3. **Concluída** - Tarefa finalizada com data de conclusão

## Armazenamento

- Os dados são armazenados em memória usando um dicionário Python
- Cada tarefa possui um ID único auto-incrementado
- Os dados são perdidos quando o servidor é reiniciado

## Design e Interface

- **Tema Dark**: Cores escuras e modernas para melhor experiência visual
- **Responsivo**: Adaptável para diferentes tamanhos de tela
- **CSS Separado**: Estilos organizados em arquivo próprio para melhor manutenção
- **Animações**: Transições suaves e efeitos hover
- **Badges Coloridos**: Indicadores visuais para status e prioridades

## Tecnologias Utilizadas

- **Flask** - Framework web Python
- **HTML5** - Estrutura das páginas
- **CSS3** - Estilização moderna com tema dark
- **JavaScript** - Interações básicas (confirmação de exclusão)
