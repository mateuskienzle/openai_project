import openai
from dotenv import load_dotenv  
import subprocess
import os

load_dotenv()

#definicao da chave da API
openai.api_key = os.getenv("OPENAI_API_KEY")

def comando_prompt(comando):
    response = openai.Completion.create(
        engine="text-davinci-003",
        #campo onde é inserido a requisição para o chatGPT
        prompt=f"Escreva um comando shell que faça o seguinte: {comando}",
        #temperature é o atributo que indica o nivel de ousadia na resposta, quanto mais próximo de 1, mais ousado é, e quanto mais proximo de 0, mais conservador é.
        temperature=0.7,
        max_tokens=2048,
        top_p=1,
        stop=None
    )
    resposta = response['choices'][0]['text'].strip()
    resposta.encode("utf-8").decode()
    return resposta

def executar_comando(comando):
    try:
        resultado = subprocess.run(comando, shell=True, check=True)
        print(resultado)
    except subprocess.CalledProcessError as e:
        print(e)

descricao = input('Digite a descricao: ')
comando = comando_prompt(descricao)
print(f'comando gerado: {comando}')
executar_comando(comando)