from datetime import datetime, timedelta
import pandas as pd
import sqlite3
import os

DB_PATH = "./vendas.db"

class Database:

    def __init__(self, db_path=DB_PATH):

        self.db_path = db_path
        self._inicializar()
    
    def _inicializar(self):
        if not os.path.exists(self.db_path):
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("""
            CREATE TABLE vendas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data DATE,
                valor REAL  
            )
             """)
            
            base_date = datetime.today()
            for i in range(90):
                date = base_date - timedelta(days=i)
                valor = 100 + (i % 10) * 20
                cursor.execute("INSERT INTO vendas (data, valor) VALUES (?, ?)", (date.strftime('%y-%m-%d'), valor))
            conn.commit()
            conn.close()
    
    def consultar(self, query : str):

        conn = sqlite3.connect(self.db_path)
        df = pd.read_sql_query(query, conn, parse_dates=['data'] if 'data' in query.lower() else None)
        conn.close()
        return df
    