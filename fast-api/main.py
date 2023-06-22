from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
  return [1,2,3,4,5]

@app.get('/contact')
def get_list():
  return {
    "name": 'platzi'
  }

@app.get('/html', response_class=HTMLResponse)
def get_list():
  return """
    <h1>Hola Soy el Pepe</h1>
    <p>Este es un parrafo de mera prueba</p>
  """


if __name__ == '__main__':
  get_list()
