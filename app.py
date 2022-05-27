
from dash import Dash, html, dcc 
import pandas as pd              
import plotly.graph_objs as go


app = Dash(__name__)



def serve_layout():
  df = pd.read_excel('datanoticias.xlsx')
  return html.Div([html.H1(df['Titulo']),
                       html.Div(df['Noticia1']),
                       html.Div(df['Noticia2'])])

app.layout = serve_layout

if __name__ == '__main__':
  
  app.run_server(host='0.0.0.0',port=80)
