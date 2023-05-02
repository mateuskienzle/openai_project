import openai
from dotenv import load_dotenv
import os

load_dotenv()

#definicao da chave da API
openai.api_key = os.getenv("OPENAI_API_KEY")

# def gerar_resposta(messages):
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo", ##
#         #model="gpt-3.5-turbo-0301", ## ateh 1 junho 2023
#         messages=messages,
#         max_tokens=1024,
#         temperature=0.5
#     )
#     return response

# mensagens = [{"role": "system", "content": "Você é um assistente gente boa."}]

# def chatgpt(texto):

#     mensagens.append({"role": "user", "content": str(texto)})
#     answer = gerar_resposta(mensagens)
#     # print("ChatGPT:", answer[0], "\nCusto:\n", answer[1])
#     # mensagens.append({"role": "assistant", "content": answer[0]})
#     return answer

# chatgpt("qual o maior time do mundo?")


# import openai

# # Initialize the API key
# openai.api_key = "sua_key_string"

def gerar_resposta(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", ##
        #model="gpt-3.5-turbo-0301", ## ate 1 junho 2023
        messages=messages,
        max_tokens=1024,
        temperature=1,
        # stream=True
    )
    return [response.choices[0].message.content, response.usage]

mensagens = []

while True:
    # Ask a question
    question = input("Perguntar pro ChatGPT (\"sair\"): ")

    if question == "sair" or question == "":
        print("saindo")
        break
    else:
        mensagens.append({"role": "user", "content": str(question)})

        answer = gerar_resposta(mensagens)
        print("ChatGPT:", answer[0], "\nCusto:\n", answer[1])
        mensagens.append({"role": "assistant", "content": answer[0]})