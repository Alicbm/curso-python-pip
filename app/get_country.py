import csv
import charts

def read_csv(path):
  with open(path, 'r') as csvfile:
    #en delimeter se pone ',' porque los datos estan separados por comas (ojo, no son los puntos decimales)
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data = []
    for row in reader:
      iterable = list(zip(header, row))
      
      country_dict = { key: value for key, value in iterable }
      
      data.append(country_dict)
    
    return data

def find_country(data):
  while True:
    print(' ')
    print('-' * 40)
    print('Write "get out" for cancel the process')
    print('-' * 40)
    print(' ')
    
    country = input('Write a country name => ').capitalize()
    search_country = list(filter(lambda element: element['Country/Territory'] == country, data))

    if country.lower() == 'Get Out'.lower():
      print('Goodbye')
      break
    elif len(search_country) == 0:
      print('Country not available')
      continue
    else:                   
      print('Chart Ready')
    return search_country, country


def country_selected (data):

  search_country, country = find_country(data)
  
  keys = list(search_country[0].keys())[5:13]
  values = list(search_country[0].values())[5:13]
  keys_final = list(map(lambda x: x[0:4], keys))
  values_final = list(map(lambda x: float(x), values))
  
  return keys_final, values_final, country
  

if __name__ == '__main__':
  def response():
    data = read_csv('./data.csv')
    keys_final, values_final, country = country_selected(data)
    charts.generate_bar_chart(country, keys_final, values_final)

  while True:
    response()
    continue