🤖 Prompt-to-Chart App
Este projeto é uma aplicação baseada em FastAPI que simula uma inteligência artificial capaz de receber prompts em linguagem natural (ex: "me mostre o total de vendas do mês passado") e retornar visualizações de dados em forma de gráficos, extraindo e analisando informações diretamente de um banco de dados.

🚀 Objetivo
Transformar perguntas em linguagem natural em consultas SQL automáticas, gerar gráficos com os dados resultantes e entregar essas visualizações ao usuário final por meio de uma interface web simples. Tudo isso de forma adaptável a diversos contextos de dados: vendas, chamados, atendimento, etc.

🧱 Tecnologias Utilizadas
FastAPI — Framework web moderno e rápido

Jinja2 — Motor de templates para HTML

OpenAI GPT API — Para transformar linguagem natural em SQL

SQLite — Banco de dados local simples para testes

Pandas — Manipulação de dados

Matplotlib / Seaborn — Visualização de gráficos

Uvicorn — Servidor ASGI

🗂️ Estrutura do Projeto

app/
├── chart_generator.py      # Geração de gráficos a partir de DataFrames
├── database.py             # Interface para consultas ao banco de dados
├── gpt_sql.py              # Lógica de conversão de prompts em SQL via OpenAI
├── main.py                 # Aplicação FastAPI com renderização de templates
├── static/                 # Onde os gráficos são salvos
├── templates/
│   └── index.html          # Template HTML principal

⚙️ Instalação
Clone o repositório:

git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio

Crie e ative um ambiente virtual:

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

Instale as dependências:

pip install -r requirements.txt

Exporte sua chave da OpenAI para utilizar no projeto.

Ex. da variável:  OPENAI_API_KEY="sua-chave-aqui"  

Execute o servidor:

uvicorn app.main:app --reload

🧪 Exemplo de Uso
Acesse o navegador: http://127.0.0.1:8000

No campo de entrada, insira um prompt como:

"Qual foi o total de vendas do mês de abril?"

A IA(chatGPT) converterá esse prompt em uma consulta SQL, executará no banco e exibirá o resultado como gráfico.

🧠 Como Funciona?
Entrada do Usuário: Um prompt em linguagem natural é enviado via formulário.

Conversão para SQL: O GPTSQLGenerator usa a API da OpenAI para traduzir o prompt em uma consulta SQL.

Consulta ao Banco: O Database executa a SQL gerada em um banco (atualmente SQLite, sendo transicionado para o PostgreSQL).

Geração do Gráfico: O ChartGenerator decide o tipo de gráfico com base nos dados ou prompt e salva a imagem para exibição ao usuário.

Exibição: O gráfico e a SQL são renderizados em uma página HTML.

📊 ChartGenerator — Lógica de Geração
Se o DataFrame possui 2 colunas → barplot

Se possui mais de 2 colunas → heatmap de correlação

Arquivos gerados são salvos em app/static/ com UUID único

🧪 Testes
Você pode criar testes para cada componente (ex: test_gpt_sql.py, test_database.py, test_chart_generator.py) usando pytest. Exemplo básico para testar o ChartGenerator:

def test_gerar_chart():
    df = pd.DataFrame({'Categoria': ['A', 'B'], 'Valor': [10, 20]})
    chart = ChartGenerator().gerar(df, "Teste")
    assert os.path.exists(chart)

🛠️ Melhorias Futuras

Upload do schema do banco de dados

Suporte a múltiplos tipos de banco (PostgreSQL, MySQL, etc.)

Sugestões automáticas de filtros e parâmetros

Armazenamento de histórico de consultas e gráficos

🤝 Contribuições
Sinta-se à vontade para abrir issues, enviar PRs ou sugerir melhorias!

📄 Licença
MIT License — livre para uso e modificação.