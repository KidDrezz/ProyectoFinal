#llamo las librerias 
from dash import dash, html, doc 

app=dash(__name__)



app.layout=html.div([hmtl.H1('canal de noticias de andres'),
                     html.Div('Noticia 1:se araman revuelos en la ciudad por culpa de los que no aceptan el presidente electo noticia2: la policia inicia casos por hurtos en estos tiempos')])


if __name__ == '__main__':
  
  app.run_server(host='0.0.0.0',port=80)
