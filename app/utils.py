def get_population():
  keys = ['col', 'bol']
  values = [300, 400]
  return keys, values

def population_by_country(data, country):
  res = list(filter(lambda item: item['country'] == country, data))
  return res