import csv

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
    
    print('*' * 15)
    return data

def country_selected (country, data):
  search_country = list(filter(lambda element: element['Country/Territory'] == country, data))
  data = {}
  years = []
  
  for year in range(1970, 2023):
    year = str(year)
    years.append(year + ' Population')

  for year in years:
    try:
      data[year] = search_country[0][year]
    except KeyError:
      pass

  keys = list(data.keys())
  value = list(data.values())
  keys_modified = list(map(lambda x: x[0:4], keys))
  values_modified = list(map(lambda x: float(x), value))
  result = dict(zip(keys_modified, values_modified)) 
  return result
  

if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  result = country_selected('Argentina', data)
  print(result)