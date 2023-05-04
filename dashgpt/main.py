from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash import dcc
import pandas as pd

from app import *
from home import *
import home
import header

import openai
from dotenv import load_dotenv
import os

load_dotenv()

#definicao da chave da API
openai.api_key = os.getenv("OPENAI_API_KEY")

try:
    df_historico = pd.read_csv('histori.csv', index_col=0)
except:
    df_historico = pd.DataFrame(columns=['role', 'message'])

df_historico = df_historico.to_dict()


app.layout = dbc.Container([
    dcc.Store(id='historical_msg_store', data=df_historico, storage_type='memory'),
    dcc.Location(id="url"),
    dbc.Row([
        dbc.Col([
            dbc.Row([
                dbc.Col([
                    header.layout
                ], className= 'header_layout'),
            ]),
            dbc.Row([
                dbc.Col([
    
                ]),
            ],id="page_content"),
        ])
    ])
], fluid=True)



def gerar_resposta(messages):
    mensagens = []
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", ##
    #model="gpt-3.5-turbo-0301", ## ate 1 junho 2023
    messages=messages,
    max_tokens=1024,
    temperature=1,
    # stream=True
    )
    return response.choices[0].message.content


@app.callback(
    Output('cards_respostas', 'children'),
    State('mensagem', 'value'),
    Input('botao_search', 'n_clicks'),
    prevent_initial_call=True
)

def generateCardsList(mensagem, n):
    cardsList = []
    mensagens = []
    mensagens.append({"role": "user", "content": str(mensagem)})
    resposta = gerar_resposta(mensagens)
    card = generate_card(resposta)
    cardsList.append(card)

    return cardsList


@app.callback(
    Output('page_content', 'children'),
    Input('url', 'pathname'),
)

def render_page(pathname):
    if pathname == '/pesquisa-chatgpt' or pathname == '/':
        return home.layout



if __name__ == "__main__":
    app.run_server(port=8050, debug=True)