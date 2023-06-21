import utils

data = [
    {
      'country': 'colombia',
      'population': 300
    },
    {
      'country': 'peru',
      'population': 150
    },
    {
      'country': 'brazil',
      'population': 500
    },
    {
      'country': 'china',
      'population': 1000
    },
  ]

def run():
  keys, values = utils.get_population()
  print(keys, values)
  
  country = input('Write a country => ')
  
  specific_country = utils.population_by_country(data, country)
  print(specific_country)

#sirve para: si el archivo /app/main.py es ejecutado desde la terminar va a correr rl codigo de la funcion run(), de esta forma se evita que el archivo corra de forma automatica al importarlo en otro archivo
if __name__ == '__main__':
  run()