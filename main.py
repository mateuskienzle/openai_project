import openai
from dotenv import load_dotenv
import os

load_dotenv()

#definicao da chave da API
openai.api_key = os.getenv("OPENAI_API_KEY")

def ler_arquivo(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as file:
        return file.read()
    
def resumo(texto):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Resuma o seguinte texto: {texto}",
        temperature=0.9,
        max_tokens=2048,
        top_p=1,
        frequency_penalty=0,
        presence_pentaly=0.6,
        stop=["\n"]
    )
    return response
