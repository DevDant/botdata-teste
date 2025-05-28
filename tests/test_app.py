import os
from app.gpt_sql import GPTSQLGenerator
from app.database import Database
from app.chart_generator import ChartGenerator

def test_gerar_sql():
    gpt = GPTSQLGenerator()
    prompt = "Me mostre o total de vendas por mês"
    query = gpt.gerar_sql(prompt)
    print(f"SQL Gerado: {query}")
    assert query.lower().startswith("select")

def test_consulta_database():
    db = Database()
    query = "SELECT mes, total from vendas"
    df = db.consultar(query)
    print(f"Resultado da consulta: {df}")
    assert not df.empty
    assert 'mes' in df.columns and 'total' in df.columns

def test_gerar_grafico():
    db = Database()
    chart = ChartGenerator()
    df = db.consultar("SELECT mes, total from vendas")
    path = chart.generate_chart(df, "Total de Vendas por Mês")
    print(f"Gráfico gerado: {path}")
    assert os.path.exists(path)

if __name__ == "__main__":
    test_gerar_sql()
    test_consulta_database()
    test_gerar_grafico()
    print("Todos os testes passaram com sucesso!")