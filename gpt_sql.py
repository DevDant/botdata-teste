from openai import OpenAI
import os


class GPTSQLGenerator:

    def __init__(self):
       self.client = OpenAI(api_key="CHAVE_OPENAI")

    def gerar_sql (self, prompt : str) -> str:
        prompt_instrucao = f"""
        Você é um assistente que converte pedidos em linguagem natural para SQL.
        Gere uma query SQL com base na solicitação: "{prompt}"
        Base de dados: vendas(mes, total), chamadas(data, duracao)
        """

        response = self.client.chat.completions.create(
            model ="gpt-4",
            messages=[
                {"role": "system", "content": "Você é um gerador de SQL"},
                {"role": "user", "content": prompt_instrucao},
            ]
        )

        query = response.choices[0].message.content.strip()
        return query