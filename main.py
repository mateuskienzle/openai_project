from app import *
from dash import html, dcc, Input, Output, State
import openai
from dotenv import load_dotenv
import os
import plotly.graph_objects as go


load_dotenv()

#definicao da chave da API
openai.api_key = os.getenv("OPENAI_API_KEY")


MAIN_CONFIG = {
    "hovermode": "x unified",
    "legend": {"yanchor":"top", 
                "y":1.0, 
                "xanchor":"left",
                "x":1.0,
                "title": {"text": None},
                },
    "margin": {"l":0, "r":0, "t":10, "b":0},
}

MAIN_CONFIG2 = {
    "hovermode": "x unified",
    "legend": {"yanchor":"top", 
                "y":1.0, 
                "xanchor":"left",
                "x":1.0,
                "title": {"text": None},
                },
    "margin": {"l":50, "r":50, "t":50, "b":50},
}


app.layout = dbc.Container([

    dbc.Row([
        dbc.Col([
            dbc.Input(id="pesquisa")
        ], md=11),
        dbc.Col([
           dbc.Button(id="botao_search") 
        ], md=1),
    ], className='g-2 my-auto'),
    dbc.Row([
        dbc.Col([
            
        ],id='resposta', md=12),
    ], className='g-2 my-auto'),

], fluid=True)

@app.callback(
    Output('resposta', 'children'),
    State('pesquisa', 'value'),
    Input('botao_search', 'n_clicks'),
)

def chatgpt(pesquisa, n):
    response = openai.Completion.create(
        engine="text-davinci-003",
        #campo onde é inserido a requisição para o chatGPT
        prompt=pesquisa,
        #temperature é o atributo que indica o nivel de ousadia na resposta, quanto mais próximo de 1, mais ousado é, e quanto mais proximo de 0, mais conservador é.
        temperature=1,
        max_tokens=2048,
        top_p=1,
        stop=None
    )
    resposta_chatgpt = response['choices'][0]['text'].strip()
    resposta_chatgpt.encode("utf-8").decode()
    return resposta_chatgpt

if __name__ == "__main__":
    app.run_server(port=8050, debug=True)