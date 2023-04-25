import openai
from dotenv import load_dotenv
import os

load_dotenv()

#definicao da chave da API
openai.api_key = os.getenv("OPENAI_API_KEY")

def ler_arquivo(arquivo):
    with open(arquivo, 'r') as file:
        return file.read()
    
def traducao(texto, idioma_origem, idioma_destino):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Traduza o seguinte texto do idioma {idioma_origem} para o idioma {idioma_destino}: {texto}",
        #temperature é o atributo que indica o nivel de ousadia na resposta, quanto mais próximo de 1, mais ousado é, e quanto mais proximo de 0, mais conservador é.
        temperature=0.4,
        max_tokens=2048,
        top_p=1,
        stop=None
    )
    resposta = response['choices'][0]['text'].strip()
    resposta.encode("utf-8").decode()
    return resposta

arquivo = 'artigo.txt'
texto = ler_arquivo(arquivo)
# print(texto)
print(traducao(texto, "português", "inglês"))